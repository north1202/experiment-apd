import os
import json
import time
import pandas as pd
from openai import OpenAI
from tqdm import tqdm

# ==========================================
# 1. 基础配置与客户端初始化
# ==========================================
INPUT_CSV = "Updated_content.csv"
OUTPUT_EXCEL = "Updated_content_场景与多利益主体全量矩阵_修改版.xlsx"

client = OpenAI(
    api_key="sk-xxx",  #
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


# ==========================================
# 2. 构建 Prompt（基于 4 大场景[多选] 与 5 大主体[多选]）
# ==========================================
def build_classification_prompt(manifestation, mitigation):
    prompt = f"""您是一位专注于科学计量学与学术出版规制（基于 COPE 指南）的首席研究员。
我将提供两段提取的文本：【映射场景具体表现】与【解决/缓解该对策的措施】。请对其进行严谨的分类标注。

【映射场景具体表现】: {manifestation}
【解决/缓解该对策的措施】: {mitigation}

# 任务 1：将【映射场景具体表现】归入以下 4 大治理场景之一（支持多选，若涉及多方请全部列出）：
可选流程列表：
- "1. 作者投稿与披露" (论文撰写、数据生成、AI辅助润色、作者声明与透明披露等)
- "2. 编辑技术预审" (编辑部查重、AI检测拦截、撤稿处理、期刊投稿政策等)
- "3. 专家同行评议" (审稿保密泄露、审稿人使用AI代写审稿意见、同行评议可重复性等)
- "4. 宏观评价与体制" ("唯论文"绩效考核、高校学术诚信政策、数字鸿沟、科研资助与顶层法规等)

# 任务 2：分析【解决/缓解该对策的措施】，识别出涉及的所有利益主体（支持多选，若涉及多方请全部列出）：
可选主体列表：
- "作者与科研人员" (学者自我规范、诚信内化、透明披露、提升AI素养)
- "期刊编辑部与出版商" (期刊更新投稿指南、部署检测工具、把控出版质量、保密审查)
- "同行评议专家" (审稿保密履职、坚持人工把关证据链、拒绝AI生成审稿意见)
- "高校与科研院所" (考核体制改革、科研诚信培训、机构支持政策、项目基金监管)
- "AI技术开发商" (算法偏见修复、嵌入可溯源数字水印、技术工具普惠)

# 输出格式要求：
必须直接返回一个简纯 JSON 对象，`governance_scenario`以及`stakeholders` 必须是一个列表（Array）：
{{
  "governance_scenario": ["1. 作者投稿与披露", "2. 编辑技术预审"],
  "stakeholders": ["作者与科研人员", "期刊编辑部与出版商"]
}}
"""
    return prompt


# ==========================================
# 3. 读取 CSV 并遍历标注
# ==========================================
try:
    df = pd.read_csv(INPUT_CSV, encoding='gbk')
except Exception:
    df = pd.read_csv(INPUT_CSV, encoding='utf-8')

print(f"📊 成功载入 Updated_content.csv，共 {len(df)} 条记录。开始二次标注...\n")

scenario_lists = []
stakeholder_lists = []

for index, row in tqdm(df.iterrows(), total=len(df), desc="🏷️ 正在分类标注"):
    manifestation = str(row.get('映射场景具体表现', ''))
    mitigation = str(row.get('解决/缓解该对策的措施', ''))

    if pd.isna(manifestation) or manifestation.strip() == '':
        scenario_lists.append([])
        stakeholder_lists.append([])
        continue

    prompt = build_classification_prompt(manifestation, mitigation)

    try:
        response = client.chat.completions.create(
            model='qwen3.7-max',
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            temperature=0.0  # 锁定随机性，保证分类的一致性
        )

        res_json = json.loads(response.choices[0].message.content)

        # 1. 解析场景列表 (支持字符串和列表类型容错)
        scen_list = res_json.get("governance_scenario", [])
        if isinstance(scen_list, str): scen_list = [scen_list]
        scenario_lists.append(scen_list)

        # 2. 解析利益主体列表
        s_list = res_json.get("stakeholders", [])
        if isinstance(s_list, str): s_list = [s_list]
        stakeholder_lists.append(s_list)

    except Exception as e:
        tqdm.write(f"❌ 行 {index} 标注异常: {e}")
        scenario_lists.append([])
        stakeholder_lists.append([])

    time.sleep(0.5)

# ==========================================
# 4. 独热编码 (One-Hot Encoding) 展开与导出
# ==========================================

# 存储原始多选列表文本
df['映射治理场景_原始列表'] = [", ".join(l) for l in scenario_lists]
df['对策利益主体_原始列表'] = [", ".join(l) for l in stakeholder_lists]

# 展开 4 个治理场景维度为独立 0/1 列
all_scenarios = [
    "1. 作者投稿与披露",
    "2. 编辑技术预审",
    "3. 专家同行评议",
    "4. 宏观评价与体制"
]

for scen_name in all_scenarios:
    df[f"场景_{scen_name}"] = [1 if any(scen_name in item for item in curr_list) else 0 for curr_list in scenario_lists]

# 展开 5 个利益主体维度为独立 0/1 列
all_stakeholders = [
    "作者与科研人员",
    "期刊编辑部与出版商",
    "同行评议专家",
    "高校与科研院所",
    "AI技术开发商"
]

for s_name in all_stakeholders:
    df[f"主体_{s_name}"] = [1 if any(s_name in item for item in curr_list) else 0 for curr_list in stakeholder_lists]

df.to_excel(OUTPUT_EXCEL, index=False)
print(f"\n🎉 {len(df)} 条记录处理完成！场景与主体独热矩阵已写入: '{OUTPUT_EXCEL}'")