import os
import json
import time
import pandas as pd
from pypdf import PdfReader
from openai import OpenAI
from tqdm import tqdm

# ==========================================
# 1. 基础路径与客户端配置
# ==========================================
BERTOPIC_DIR = "other"  # 存放 class0.csv 到 class11.csv 的文件夹
PAPERS_DIR = "papers_folder"  # 存放 258 篇文献 PDF 全文的文件夹
OUTPUT_EXCEL = "学术出版AI伦理_LLM交叉验证与幻觉审计矩阵_补充.xlsx"

# 初始化独立的外部审计客户端（以 GPT-4o 为例）
audit_client = OpenAI(
    api_key="sk-xxx",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


# ==========================================
# 2. 构建严谨的交叉审计提示词（提示词工程控制）
# ==========================================
def build_cross_audit_prompt(filename, article_text, current_row_json):
    prompt = f"""你是一位专注于科学计量学、学术出版规制（基于 COPE 声明）的首席数据质量审计专家。
现有另一名编码员（初筛模型）针对文献【{filename}】全文本进行了解构，并提取了一项关于 AI 伦理伤害的观测记录。
你的任务是：对照提供的【文献原文全文本】，对这项已有记录进行严格的真值校验与幻觉审计。

# 初筛编码员提交的待审计记录：
{current_row_json}

# 文献原文全文本（前32000字截断）：
{article_text}

# 审计与打分硬性标准（针对四大核心断言）：
请逐一审查并对以下四个维度评定“忠实度得分”（必须为 1.0、0.5 或 0.0）：
1. 伤害定类得分 (harm_class_score)：[具体表现]是否准确对齐其[伤害类型分类]？（1.0=完美对齐; 0.5=勉强说得通; 0.0=完全张冠李戴）
2. 表现忠实得分 (manifestation_score)：[具体表现]在原文中是否有直接的语义线索支持？（1.0=完全忠实; 0.5=存在部分微调/推导偏误; 0.0=纯属无中生有的输入驱动型幻觉）
3. 理由溯源得分 (reason_score)：[判断的理由]里提及的章节和观点在原文中是否真实存在？（1.0=精准存在; 0.0=虚构章节或伪造文本线索）
4. 对策合规得分 (mitigation_score)：[消除/缓解措施]是否确实由原文作者在文中提出？（1.0=完全由作者提出; 0.5=属于模型常识过拟合、硬性嫁接的通用治理套话; 0.0=原文完全无对策且模型虚构了对策）

# 返回格式要求：
必须直接返回一个满足下述结构的简纯 JSON 对象，不要包含任何 Markdown 标记或多余解释：
{{
  "harm_class_score": 1.0,
  "harm_class_reason": "简短的审计理由",
  "manifestation_score": 1.0,
  "manifestation_reason": "简短的审计理由",
  "reason_score": 1.0,
  "reason_reason": "简短的审计理由",
  "mitigation_score": 0.5,
  "mitigation_reason": "指出是否属于常识过拟合与对策嫁接"
}}
"""
    return prompt


# ==========================================
# 3. 循环遍历各类别并执行双轨审计
# ==========================================
all_audit_records = []
csv_files = [f for f in os.listdir(BERTOPIC_DIR) if f.endswith('.csv')]

print(f"📂 成功扫描到 {len(csv_files)} 个聚类文件。启动外部模型交叉验证流程...\n")

for file in csv_files:
    file_path = os.path.join(BERTOPIC_DIR, file)
    class_name = file.replace('.csv', '')

    try:
        df = pd.read_csv(file_path, encoding='utf-8')
    except:
        df = pd.read_csv(file_path, encoding='gbk')

    tqdm.write(f"\n⏳ 开始审计类别 [{class_name}] ... 共计 {len(df)} 条记录")

    for index, row in tqdm(df.iterrows(), total=len(df), desc=f"正在审计 {class_name}"):
        paper_title = row.get('文献名称', '')
        if not paper_title:
            continue

        # 读取对应的 PDF 全文本
        pdf_path = os.path.join(PAPERS_DIR, paper_title)
        article_text = ""
        if os.path.exists(pdf_path):
            try:
                reader = PdfReader(pdf_path)
                for page in reader.pages:
                    t = page.extract_text()
                    if t: article_text += t
            except Exception as e:
                article_text = "文本提取失败"

        if len(article_text) > 32000:
            article_text = article_text[:32000]

        if article_text == "文本提取失败" or pd.isna(row.get('对应具体表现', '')):
            continue

        # 将当前行的数据结构化
        current_row_json = row.to_json(force_ascii=False)
        current_prompt = build_cross_audit_prompt(paper_title, article_text, current_row_json)

        try:
            response = audit_client.chat.completions.create(
                model='qwen-plus',  # 选用高推理独立审计模型
                messages=[{"role": "user", "content": current_prompt}],
                response_format={"type": "json_object"},
                temperature=0.0  # 硬性锁定随机性，保证审计结果极度客观一致
            )

            audit_res = json.loads(response.choices[0].message.content)

            # 整合原纪录与审计得分
            combined_record = {
                "文献名称": paper_title,
                "BERTopic聚类": class_name,
                "原提取_伤害类型": row.get('社会系统伤害类型分类'),
                "原提取_具体表现": row.get('对应具体表现'),
                "原提取_对策措施": row.get('消除/缓解这个伤害的具体措施'),
                "审计_伤害分类得分": audit_res.get("harm_class_score"),
                "审计_伤害分类理由": audit_res.get("harm_class_reason"),
                "审计_表现忠实得分": audit_res.get("manifestation_score"),
                "审计_表现忠实理由": audit_res.get("manifestation_reason"),
                "审计_对策合规得分": audit_res.get("mitigation_score"),
                "审计_对策合规理由": audit_res.get("mitigation_reason")
            }
            all_audit_records.append(combined_record)

        except Exception as e:
            tqdm.write(f"❌ 审计 Row {index} 失败: {e}")
            continue

        time.sleep(1)

# ==========================================
# 4. 持久化保存
# ==========================================
df_output = pd.DataFrame(all_audit_records)
df_output.to_excel(OUTPUT_EXCEL, index=False)
print(f"\n🎉 交叉验证流全部结束！审计矩阵已写入: '{OUTPUT_EXCEL}'")