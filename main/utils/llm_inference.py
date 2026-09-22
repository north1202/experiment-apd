import os
import json
import time
import pandas as pd
from openai import OpenAI

# ==================== 阿里云 DashScope 接口配置 ====================
client = OpenAI(
    api_key="sk-849b31ef6a1f46e1b268ae4a9ae18b97",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
MODEL_NAME = "qwen-plus"


# =================================================================

def predict_relevance_qwen_en(title_en, abstract_en):
    """
    直接读取英文文献内容，严格依据纳入与排除标准判定文献相关性，并输出中英双语理由
    """
    if not title_en or str(title_en).strip() == '':
        return 0, "缺失标题 (Missing Title)", "Missing Title"

    # 构造高度结构化的科研文献筛选专家提示词，要求双语输出
    prompt = f"""你是一位精通学术出版规范与科研诚信领域的资深评审专家。
现在需要你对一篇学术文献进行主题相关性筛选。

【研究主题】
分析学术界关于“AI在学术/出版中的伦理与披露（AI Disclosure）”的讨论，以便后续与出版商政策进行对比研究。

【严格的纳入与排除标准】
1. 纳入标准 (Inclusion Criteria) - 必须同时满足以下所有条件：
   - 研究对象明确涉及人工智能技术（如AI, Generative AI, LLM, GPT, ChatGPT等）。
   - 核心议题紧密涉及伦理（Ethics）、学术诚信、出版规范、或AI使用披露（AI Disclosure）。
   - 场景明确限定在学术写作、科学研究、期刊发表、同行评议或学术出版领域。
2. 排除标准 (Exclusion Criteria) - 满足任意一项即判定为不相关（0）：
   - 仅讨论AI算法的技术开发、模型训练、架构或性能优化，不涉及伦理或出版规范。
   - 场景属于医疗伦理（如AI辅助临床诊断伦理）、法律AI、自动驾驶或工业机器人等非学术出版场景。

【待评审文献内容（英文）】
Title: {title_en}
Abstract: {abstract_en}

请审慎评估后，严格按照以下 JSON 格式返回结果。不要包含任何多余的解释、标点或 Markdown 代码块标记（如 ```json 等）：
{{
  "predicted_relevance": 1或0,
  "justification_zh": "必须结合具体的纳入或排除标准，用1句话概述你判定的核心中文理由。",
  "justification_en": "Provide the corresponding core justification in English within 1 sentence."
}}"""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,  # 严格控制随机性，保证评审一致性
            response_format={"type": "json_object"}  # 强化 JSON 约束
        )

        res_content = response.choices[0].message.content
        res_data = json.loads(res_content)

        return (
            res_data.get('predicted_relevance', 0),
            res_data.get('justification_zh', ''),
            res_data.get('justification_en', '')
        )

    except Exception as e:
        print(f"解析异常: {e}")
        return 0, f"Error: {str(e)}", f"Error: {str(e)}"


def run_screening_pipeline(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"错误：找不到输入文件 '{input_file}'，请检查文件名。")
        return

    # 引入多重编码自适应读取机制，解决 UnicodeDecodeError 报错
    try:
        df = pd.read_csv(input_file, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(input_file, encoding='gbk')

    print(f"成功加载原版英文数据集，共计 {len(df)} 条记录。正在启用 {MODEL_NAME} 执行精准伦理主题筛选（双语理由模式）...")

    predictions = []
    justifications_zh = []
    justifications_en = []

    for idx, row in df.iterrows():
        t_en = row.get('Title', '')
        a_en = row.get('Abstract', '')

        print(f"正在分析第 {idx + 1}/{len(df)} 篇文献: {str(t_en)[:30]}...")

        pred, just_zh, just_en = predict_relevance_qwen_en(t_en, a_en)
        predictions.append(pred)
        justifications_zh.append(just_zh)
        justifications_en.append(just_en)

        # 频率窗口控制，防止触发阿里云并发限制
        time.sleep(0.2)

    # 将预测结果、中文理由、英文理由分别写入不同的列
    df['LLM_Prediction'] = predictions
    df['Justification_ZH'] = justifications_zh
    df['Justification_EN'] = justifications_en

    # 导出结果时，显式指定使用 utf-8 编码，防止后续脚本读取时再次报错
    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"\n自动化筛选推理完成！中英双语结果已存入: {output_file}")


if __name__ == '__main__':
    # 阶段一：先对150篇包含原版英文和人工标签的验证集运行推理
    #INPUT_PATH = 'to_be_annotated_150.csv'
    #OUTPUT_PATH = 'test_set_results.csv'

    # 阶段二：当验证集混淆矩阵调校满意后，切换至全量2059篇母表运行（解封下两行）
     INPUT_PATH = 'combined_metadata2.csv'
     OUTPUT_PATH = 'final_screened_ethics_dataset.csv'0

     run_screening_pipeline(INPUT_PATH, OUTPUT_PATH)