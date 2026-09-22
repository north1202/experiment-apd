import os
import json
import time
import pandas as pd
from pypdf import PdfReader
from openai import OpenAI
from tqdm import tqdm  # 引入可视化进度条模块

# ==========================================
# 1. 配置路径与变量
# ==========================================
PAPERS_DIR = "E:\work\experiment\Academic publishing dataset\main\input\full_md"
OUTPUT_EXCEL = "AI伦理文献全文社会伤害与对策提取矩阵.xlsx"

client = OpenAI(
    api_key="sk-xx",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# ==========================================
# 2. 硬编码嵌入完整的 4 种真实伤害治理对策作为 Few-shot 示例
# ==========================================
example_context = """【示例文献名称】：ChatGPT and the rise of generative AI: Threat to academic integrity?
【示例全文核心议题】：探讨以 ChatGPT 为代表的生成式 AI 对学术诚信的系统性威胁、对宏观教学和科学评价机制的冲击，并提出多方协同的风险治理策略。

【演绎得到的社会伤害分类】：分配伤害 (Allocative Harms)
【对应具体表现与演绎理由】：低收入地区因技术壁垒和检测成本加剧学术不公。文中指出 Turnitin 等防作弊技术工具的整合需要高昂的资金成本，许多中低收入国家（LMICs）的机构无力承担。这导致 ChatGPT 的滥用会进一步恶化这些地区原本就存在的作弊问题，加剧了全球学术资源与评价体系的非均衡受损。
【文中消除或缓解该伤害的具体措施】：① 低成本技术供给：需要多利益相关者共同创造一种更便宜、安全、可持续且负责任的全球通用解决方案。② 包容性国际合作：呼吁 OpenAI 等技术开发方将与教育界的互动合作，从目前的美国扩大到全球其他地区，尤其是中低收入国家的学术利益相关者。
----------------------------------------
【演绎得到的社会伤害分类】：服务质量伤害 (Quality-of-Service Harms)
【对应具体表现与演绎理由】：AI 算法缺陷与幻觉造成的学术质量劣化。文中引用了 OpenAI 官方的系统免责声明，即 ChatGPT 偶尔会生成错误信息、有害指令或带偏见的内容，且其知识受限于训练数据。这种技术自身的性能局限直接对学术诚信与研究产出的最终质量构成威胁。
【文中消除或缓解该伤害的具体措施】：① 提升信息透明度：学术机构和出版商必须在政策中明确界定使用 AI 生成文本且不加承认属于学术不端行为，并向全行业明示这种技术对科学真实性底线的侵害。② 全员能力建设：在高校内部广泛开展针对教职员工和学生的学术能力培训，引导其了解 LLM 的局限性与正确、合规的使用边界。
----------------------------------------
【演绎得到的社会伤害分类】：人际伤害 (Interpersonal Harms)
【对应具体表现与演绎理由】：学术互信与智力能动性向算法的盲目让渡。文中指出，由于 ChatGPT 能够流畅地回答本科生和研究生的考试与代码问题，导致教授们极度担忧未来的论文评估将失效；学生极易盲目让渡自身智力能动性，使传统教学的人际互信关系异化为人类对算法的依赖。
【文中消除或缓解该伤害的具体措施】：① 重构学术考核范式：建议学术机构彻底改变现有的评估方法，从评估“最终完成的论文短篇”转向评估“论文写作过程中的批判性思维”。② 强制性引入口试（Oral Exams）：在论文或代码技术评估中，将口试/面试由辅助手段提升为“主要考核部分”，以此直接测试并确保学生真正理解了知识，修复人际间的授信纽带。
----------------------------------------
【演绎得到的社会伤害分类】：社会系统伤害 (Social System Harms)
【对应具体表现与演绎理由】：传统科学信用与归责机制的体制性坍塌。文中提及已有研究将 ChatGPT 列为合著者。对此，作者重申了 Nature 和 Science 杂志的严正立场——LLM 绝不能被接受为期刊的署名作者，因为 AI 的滥用正试图颠覆传统的学术管理制度 and 责任承担机制。
【文中消除或缓解该伤害的具体措施】：① 顶层政策重修：学术机构必须紧急审查并修订其学术诚信政策，将未经披露的 AI 文本使用明确定义为违规。② 协同共创引用规范：学术机构需要与期刊编辑、出版商等行业相关方紧密合作，共同制定出有效、统一的 AI 工具披露与引用标准（如记录生成日期、提示词、限制直引篇幅等）。③ 技术开发方联合归责：开发商（如 OpenAI）不能仅推出“不完美分类器”了事，必须深度参与学术界全球治理，共同 co-create 出具有低成本且高可信度的防作弊和可追溯工具。
----------------------------------------
"""


# ==========================================
# 3. 构建单篇文献【全文本】深度挖掘提示词
# ==========================================
def build_prompt(filename, article_text):
    prompt = f"""你是一位专注于科学计量学、学术出版规制以及社会技术伤害（Sociotechnical Harms）分类的资深研究员。

# 任务目标
请仔细研读我提供的一篇【文献原文全文本】，对其进行系统性的文本内容分析（Content Analysis）。请识别出文章中讨论的、由生成式AI（如ChatGPT、LLM）对“学术伦理”和“出版伦理”场景造成的社会技术伤害（Sociotechnical Harms）。对于识别出的每种伤害，不仅要提炼出其具体表现，还必须深挖**文章作者在文中提出的消除、缓解、或应对该伤害的具体治理策略与建议**。

# 社会技术伤害分类基准与学术出版场景映射（完全基于 COPE 声明与指南的规制边界）
1. 分配伤害 (Allocative Harms)：指AI系统的应用或技术壁垒，直接或间接导致学术个体在发表机会、研究资助或学术声誉等资源的分配上面临算法不公。
2. 表征伤害 (Representational Harms)：指AI基于底层训练数据的偏见，在语言、文化、地域或学科视角的生成与评审中，对特定学术群体或知识体系造成抹杀、同质化或边缘化。
3. 服务质量伤害 (Quality-of-Service Harms)：指AI系统自身的算法缺陷（如幻觉）或不合规使用，直接降低了学术出版内容本身的最终效能、真实性与科学质量。
4. 人际伤害 (Interpersonal Harms)：指AI的介入消解、破坏或异化了学术共同体内部长期建立的、基于人类智力的互信、保密和协作纽带。
5. 社会系统伤害 (Social System Harms)：指AI在学术界的滥用，对宏观的学术管理制度、出版评价体系以及科学整体公信力造成的广泛性、制度性冲击。

# 【核心约束——长文本精读铁律】
1. 完全基于给定的【文献原文全文本】内容进行提取和演绎，【绝对禁止任何主观杜撰、凭空编造】。
2. 提取出的社会伤害分类，必须在“判断理由”中指明是基于文章中哪些核心章节或作者论点推理得出。
3. 如果五类伤害中，某些类别在本文中【完全没有被提及】，请【直接忽略】，不要勉强凑数。若整篇文献全文本未提及任何一种伤害，则 findings 字段返回空列表。
4. 对于“消除/缓解措施”，如果文章中【确实没有提及任何对策】，请在此字段填写“（该文献未提及具体缓解措施）”，保持客观真实。

# 【参考演绎案例（Few-Shot Examples - 像素级模仿此处的推理深度与对策提炼方式）】
以下是人类专家对一篇典型全文进行分析后得到的标准完整范例：
{example_context}

# 【当前待分析文献名称】: {filename}

# 【待分析文献原文全文本】
{article_text}

# 返回格式要求
请必须返回一个满足下述结构的 JSON 对象，不要包含任何多余的解释。
{{
  "paper_title": "{filename}",
  "findings": [
    {{
      "harm_type": "发现的社会伤害类型分类（如：人际伤害）",
      "manifestation": "文献原文中对应的学术/出版场景具体表现",
      "reason": "这样判断的理由（必须紧扣原文的文本线索或作者核心观点描述）",
      "mitigation_strategy": "文中提到的如何消除或缓解该伤害的具体策略、建议或解决方案（若文章未提及，请填写：该文献未提及具体缓解措施）"
    }}
  ]
}}
"""
    return prompt


# ==========================================
# 4. 自动化读取 PDF 全文本并单篇提交大模型（引入 tqdm 可视化）
# ==========================================
if not os.path.exists(PAPERS_DIR):
    print(f"错误：未找到名为 '{PAPERS_DIR}' 的文件夹，请创建该文件夹并放入文献 PDF。")
    exit()

pdf_files = [f for f in os.listdir(PAPERS_DIR) if f.lower().endswith('.pdf')]
print(f"📁 成功在文件夹中扫描到 {len(pdf_files)} 篇 PDF 全文文献。准备开始精读分析...\n")

results_accumulator = []

# 使用 tqdm 包装循环，desc 设置进度条左侧的前缀文字，unit 设置单位
progress_bar = tqdm(pdf_files, desc="🚀 正在精读文献", unit="篇")

for filename in progress_bar:
    pdf_path = os.path.join(PAPERS_DIR, filename)

    # 动态更新进度条的后缀显示信息，提示当前正在处理的文件名
    progress_bar.set_postfix_str(f"当前: {filename[:20]}...")

    # 提取单篇 PDF 的完整文本
    article_text = ""
    try:
        reader = PdfReader(pdf_path)
        for page_num, page in enumerate(reader.pages):
            page_text = page.extract_text()
            if page_text:
                article_text += f"\n[PAGE {page_num + 1}]\n{page_text}"
    except Exception as e:
        # 使用 tqdm.write 替代普通的 print，防止破坏进度条的渲染结构
        tqdm.write(f"⚠️ 提取 {filename} 的文本失败: {e}，跳过此篇。")
        continue

    # 防止单篇文献内容极端过长进行安全截断（保留前 35000 个字符）
    if len(article_text) > 35000:
        article_text = article_text[:35000] + "\n\n[内容过长，脚本进行了安全截断]"

    # 动态组装针对该篇全文的专属提示词
    current_prompt = build_prompt(filename, article_text)

    try:
        response = client.chat.completions.create(
            model='qwen3.7-max',
            messages=[
                {"role": "user", "content": current_prompt}
            ],
            response_format={"type": "json_object"}
        )

        raw_content = response.choices[0].message.content
        paper_data = json.loads(raw_content)
        results_accumulator.append(paper_data)

        # 统计当前文献成功提取出了几种伤害类型
        harm_count = len(paper_data.get("findings", []))
        tqdm.write(f"✅ {filename} 分析成功，提取到 {harm_count} 种伤害。")

    except Exception as e:
        tqdm.write(f"❌ {filename} 调用大模型失败: {e}")
        results_accumulator.append({"paper_title": filename, "findings": [], "error": str(e)})

    # 遵守频率限制规避
    time.sleep(3)

# 关闭进度条
progress_bar.close()

# ==========================================
# 5. 全文多维数据扁平化并持久化导出
# ==========================================
print("\n📊 所有文献全文深度剖析完毕，正在生成最终的 Excel 矩阵...")
final_results = []

for paper_analysis in results_accumulator:
    title = paper_analysis.get("paper_title", "未知文献")
    findings = paper_analysis.get("findings", [])

    if not findings:
        error_msg = "（该文献全文本中未涉及任何符合 COPE 基准的社会伤害类型或对策）" if "error" not in paper_analysis else f"分析失败，错误原因: {paper_analysis['error']}"
        final_results.append({
            "文献名称": title,
            "社会伤害类型分类": "（无对应伤害类型）",
            "对应具体表现": error_msg,
            "这样判断的理由": "依据包含/排除铁律自动排除",
            "消除/缓解这个伤害的具体措施": "（无）"
        })
    else:
        for find in findings:
            final_results.append({
                "文献名称": title,
                "社会伤害类型分类": find.get("harm_type"),
                "对应具体表现": find.get("manifestation"),
                "这样判断的理由": find.get("reason"),
                "消除/缓解这个伤害的具体措施": find.get("mitigation_strategy")
            })

df_output = pd.DataFrame(final_results)
df_output.to_excel(OUTPUT_EXCEL, index=False)
print(f"\n🎉 任务全部结束！200+篇全文本分析矩阵已成功写入: '{OUTPUT_EXCEL}'")