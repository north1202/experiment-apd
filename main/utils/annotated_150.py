import os
import pandas as pd


def generate_annotation_sample(input_file, sample_file, sample_size=150):
    """
    从合并后的母表中按平台分层随机抽取指定数量的文献，生成用于人工标注的验证集。
    """
    if not os.path.exists(input_file):
        print(f"错误：找不到母表文件 '{input_file}'，请先运行第一步的合并代码。")
        return

    # 1. 读取合并后的母表
    df = pd.read_csv(input_file, index_col='ID')

    # 2. 计算每个平台应当抽取的数量（分层抽样，确保各占一半）
    half_size = sample_size // 2

    # 3. 按数据源分别进行随机抽样
    scopus_pool = df[df['Source'] == 'Scopus']
    wos_pool = df[df['Source'] == 'WoS']

    if len(scopus_pool) < half_size or len(wos_pool) < half_size:
        print("警告：某一平台的文献数量不足以进行对等分层抽样，将切换为全局随机抽样。")
        df_sample = df.sample(n=sample_size, random_state=42)
    else:
        # random_state=42 确保每次运行代码抽取的样本一致，方便可重复性研究
        scopus_sample = scopus_pool.sample(n=half_size, random_state=42)
        wos_sample = wos_pool.sample(n=half_size, random_state=42)
        # 合并两部分的抽样结果
        df_sample = pd.concat([scopus_sample, wos_sample])

    # 4. 新增两列用于后续的人工标注与记录
    # Ground_Truth: 供您人工填写 1（相关）或 0（不相关）
    # Annotated: 标记该行是否已经看齐，方便多人在 Excel 中协同或分批标注
    df_sample['Ground_Truth'] = ''
    df_sample['Annotated'] = 'No'

    # 5. 重新打乱样本顺序，防止 Excel 中前 75 篇全是一个平台，后 75 篇全是一个平台
    df_sample = df_sample.sample(frac=1, random_state=42)

    # 6. 保存为独立的标注工作表
    df_sample.to_csv(sample_file, index=True)

    print("\n" + "=" * 30)
    print(" 验证集抽样任务完成 ")
    print("=" * 30)
    print(f"成功抽取文献总数: {len(df_sample)} 篇")
    print("抽样样本的平台分布:")
    print(df_sample['Source'].value_counts())
    print(f"已生成待标注工作表: {sample_file}")
    print("提示：请用 Excel 打开该文件，阅读 Title 和 Abstract，并在 'Ground_Truth' 列中填入 1 或 0。")
    print("=" * 30)


if __name__ == '__main__':
    # 输入与输出文件名定义
    INPUT_METADATA = 'combined_metadata2.csv'
    OUTPUT_SAMPLE = 'to_be_annotated_150.csv'

    generate_annotation_sample(INPUT_METADATA, OUTPUT_SAMPLE, sample_size=150)