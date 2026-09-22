import re
import pandas as pd


def clean_and_combine_datasets(scopus_file, wos_file, output_file):
    """
    对齐 Scopus 与 Web of Science 数据集字段，执行多阶段去重并合并。
    """
    # 1. 动态兼容编码读取原始数据
    try:
        df_scopus = pd.read_csv(scopus_file, encoding='utf-8')
    except UnicodeDecodeError:
        df_scopus = pd.read_csv(scopus_file, encoding='gbk')

    try:
        df_wos = pd.read_csv(wos_file, encoding='utf-8')
    except UnicodeDecodeError:
        df_wos = pd.read_csv(wos_file, encoding='gbk')

    print(f"原始数据读取成功：Scopus 包含 {len(df_scopus)} 条记录，WoS 包含 {len(df_wos)} 条记录。")

    # 2. 提取并标准化对齐 Scopus 的核心字段
    scopus_clean = pd.DataFrame({
        'Title': df_scopus['Title'].fillna('').astype(str).str.strip(),
        'Abstract': df_scopus['Abstract'].fillna('').astype(str).str.strip(),
        'DOI': df_scopus['DOI'].fillna('').astype(str).str.strip(),
        'Source': 'Scopus'
    })

    # 3. 提取并标准化对齐 WoS 的核心字段（修正关键字段映射）
    wos_clean = pd.DataFrame({
        'Title': df_wos['Article Title'].fillna('').astype(str).str.strip(),
        'Abstract': df_wos['Abstract'].fillna('').astype(str).str.strip(),
        'DOI': df_wos['DOI'].fillna('').astype(str).str.strip(),
        'Source': 'WoS'
    })

    # 4. 初步合并，并剔除无效空值行
    df_combined = pd.concat([scopus_clean, wos_clean], ignore_index=True)
    df_combined = df_combined[(df_combined['Title'] != '') & (df_combined['Abstract'] != '')]
    print(f"剔除空文本后的合并总数（去重前）：{len(df_combined)}")

    # 5. 构建文本规范化字段（移除标点、特殊符号并转为全小写），用于模糊重合比对
    df_combined['Title_Norm'] = df_combined['Title'].str.lower().str.replace(r'[^a-z0-9]', '', regex=True)

    # 6. 多阶段精确去重策略
    # 拆分为“含有效DOI群组”与“空DOI群组”分别处理，避免因DOI为空导致误删
    has_doi = df_combined[df_combined['DOI'] != '']
    no_doi = df_combined[df_combined['DOI'] == '']

    # 针对含第一标识符(DOI)的数据集进行双重过滤
    has_doi = has_doi.drop_duplicates(subset=['DOI'], keep='first')
    has_doi = has_doi.drop_duplicates(subset=['Title_Norm'], keep='first')

    # 合并回流，并针对无DOI或跨平台拼写微调的记录进行全局标题去重
    final_df = pd.concat([has_doi, no_doi], ignore_index=True)
    final_df = final_df.drop_duplicates(subset=['Title_Norm'], keep='first')

    # 7. 移除中间辅助计算列，规范化索引
    final_df = final_df.drop(columns=['Title_Norm'])
    final_df.index.name = 'ID'

    # 8. 持久化存储与统计输出
    final_df.to_csv(output_file, index=True)

    print("\n" + "=" * 30)
    print(" 数据清洗与无损融合任务完成 ")
    print("=" * 30)
    print(f"最终有效非冗余文献总数: {len(final_df)} 篇")
    print("各数据源平台文献分布:")
    print(final_df['Source'].value_counts())
    print(f"结构化母表已成功写入: {output_file}")
    print("=" * 30)


if __name__ == '__main__':
    # 请根据您的真实存放路径修改以下文件名称
    SCOPUS_INPUT = 'scopus数据集.csv'
    WOS_INPUT = 'wos数据集.csv'
    OUTPUT_METADATA = 'combined_metadata2.csv'

    clean_and_combine_datasets(SCOPUS_INPUT, WOS_INPUT, OUTPUT_METADATA)