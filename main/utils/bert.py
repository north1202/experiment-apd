import pandas as pd
import multiprocessing
from bertopic import BERTopic
from umap import UMAP
from hdbscan import HDBSCAN
from sklearn.feature_extraction.text import CountVectorizer
from sentence_transformers import SentenceTransformer

def generate_final_results_k12():
    # ==========================================
    # 1. 数据读取与预处理
    # ==========================================
    file_path = "core_dataset.csv"
    try:
        df = pd.read_csv(file_path, encoding='gbk')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='utf-8', encoding_errors='ignore')

    abstracts = df['Abstract'].dropna().astype(str).tolist()
    print(f"成功提取摘要数量: {len(abstracts)} 篇\n")

    # ==========================================
    # 2. 核心模型初始化与训练 (应用最优参数 K=12)
    # ==========================================
    print("正在加载句向量模型并执行最终聚类...")
    embedding_model = SentenceTransformer("allenai/specter2_base")
    # 预计算 embeddings 以加速拟合过程
    embeddings = embedding_model.encode(abstracts, show_progress_bar=True)

    # 保持与网格搜索高度一致的底层算法配置
    umap_model = UMAP(n_neighbors=5, n_components=5, min_dist=0.0, metric='cosine', random_state=42)
    hdbscan_model = HDBSCAN(min_cluster_size=5, min_samples=2, metric='euclidean', cluster_selection_method='eom', prediction_data=True)
    vectorizer_model = CountVectorizer(stop_words="english")

    topic_model = BERTopic(
        embedding_model=embedding_model,
        umap_model=umap_model,
        hdbscan_model=hdbscan_model,
        vectorizer_model=vectorizer_model,
        language="english",
        nr_topics=13,  # 强制收敛至经统计检验最优的 12 个主题以及 1 个垃圾类
        calculate_probabilities=False,
        verbose=True
    )

    # 执行拟合
    topics, _ = topic_model.fit_transform(abstracts, embeddings)

    # ==========================================
    # 3. 提取特征词并固化分类结果至磁盘
    # ==========================================
    print("\n正在生成特征词清单与 CSV 数据文件...")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_colwidth', None)

    topic_info = topic_model.get_topic_info()
    print("\n=== 最优分类 (K=12) 主题概览 ===")
    print(topic_info[['Topic', 'Count', 'Name']])

    # 将分类标签写入 DataFrame 并保存
    df['Topic'] = topic_model.topics_
    df.to_csv("core_dataset_final_13.csv", index=False, encoding='utf-8-sig')

    # 输出特征词至独立文本文件备用
    with open("Topic_Keywords_13.txt", "w", encoding="utf-8") as f:
        f.write("=== 12个最优主题核心特征词清单 ===\n")
        for t_id in range(len(topic_info) - 1): # 排除 Topic -1
            words = [word for word, _ in topic_model.get_topic(t_id)[:10]]
            line = f"Topic {t_id}: {', '.join(words)}\n"
            f.write(line)
            print(line.strip())

    # ==========================================
    # 4. 生成学术可视化图表 (离线 HTML 格式)
    # ==========================================
    print("\n正在渲染交互式分析图表...")
    # 配置跨平台的无衬线中文字体体系
    font_style = dict(family="Microsoft YaHei, SimHei, sans-serif", size=14)

    fig1 = topic_model.visualize_barchart(top_n_topics=13)
    fig1.update_layout(title="学术主题特征词与 c-TF-IDF 权重分布 (K=12)", font=font_style, width=1400, height=800)
    fig1.write_html("1_barchart_13.html")

    fig2 = topic_model.visualize_heatmap()
    fig2.update_layout(title="学术主题语义相似度映射矩阵 (K=12)", font=font_style, width=1000, height=1000)
    fig2.write_html("2_heatmap_13.html")

    fig3 = topic_model.visualize_topics()
    fig3.update_layout(title="文献数据集二维语义空间投影 (K=12)", font=font_style, width=1200, height=800)
    fig3.write_html("3_topic_map_13.html")

    fig4 = topic_model.visualize_hierarchy(top_n_topics=13)
    fig4.update_layout(title="文献主题层次合并结构树 (K=12)", font=font_style, width=1200, height=800)
    fig4.write_html("4_hierarchy_13.html")

    print("\n=======================================================")
    print("分析流水线执行完毕。产出成果如下：")
    print("1. 完整数据表: core_dataset_final_13.csv")
    print("2. 特征词清单: Topic_Keywords_13.txt")
    print("3. 分析图表: 1_barchart_13.html 至 4_hierarchy_13.html")
    print("=======================================================")

if __name__ == '__main__':
    multiprocessing.freeze_support()
    generate_final_results_k12()