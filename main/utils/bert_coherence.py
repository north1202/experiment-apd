import pandas as pd
import matplotlib.pyplot as plt
import multiprocessing
from bertopic import BERTopic
from umap import UMAP
from hdbscan import HDBSCAN
from sklearn.feature_extraction.text import CountVectorizer
from sentence_transformers import SentenceTransformer
from gensim.corpora import Dictionary
from gensim.models import CoherenceModel


def run_optimized_grid_search():
    # ==========================================
    # 1. 数据准备
    # ==========================================
    file_path = "core_dataset.csv"
    try:
        df = pd.read_csv(file_path, encoding='gbk')
    except:
        df = pd.read_csv(file_path, encoding='utf-8', encoding_errors='ignore')
    abstracts = df['Abstract'].dropna().astype(str).tolist()

    # ==========================================
    # 2. 核心计算模型 (独立重拟合模式)
    # ==========================================
    embedding_model = SentenceTransformer("allenai/specter2_base")
    embeddings = embedding_model.encode(abstracts, show_progress_bar=True)

    vectorizer_model = CountVectorizer(stop_words="english")
    analyzer = vectorizer_model.build_analyzer()
    tokenized_docs = [analyzer(doc) for doc in abstracts]
    dictionary = Dictionary(tokenized_docs)
    corpus = [dictionary.doc2bow(text) for text in tokenized_docs]

    # ==========================================
    # 3. 网格搜索：5 到 15
    # ==========================================
    target_k_range = range(5, 16)
    coherence_scores = []

    print("\n=== 开始网格搜索 (独立重拟合模式) ===")
    for k in target_k_range:
        # 每次循环都重新定义 HDBSCAN 目标簇数
        hdbscan_model = HDBSCAN(
            min_cluster_size=5,
            min_samples=2,
            metric='euclidean',
            cluster_selection_method='eom'
        )

        # 实例化模型
        topic_model = BERTopic(
            embedding_model=embedding_model,
            hdbscan_model=hdbscan_model,
            vectorizer_model=vectorizer_model,
            nr_topics=k  # 直接在模型内设定目标簇数
        )

        topic_model.fit_transform(abstracts, embeddings)

        # 计算连贯性
        topics_words = []
        info = topic_model.get_topic_info()
        actual_k = len(info) - 1  # 排除离群簇

        for t_id in range(actual_k):
            words = [word for word, _ in topic_model.get_topic(t_id)[:10]]
            topics_words.append(words)

        coherence_model = CoherenceModel(
            topics=topics_words, texts=tokenized_docs, corpus=corpus,
            dictionary=dictionary, coherence='c_v'
        )
        score = coherence_model.get_coherence()
        coherence_scores.append(score)

        print(f"K={k} (实际生成簇数: {actual_k}) -> C_v: {score:.4f}")

    # ==========================================
    # 4. 可视化与保存
    # ==========================================
    plt.figure(figsize=(9, 5))
    plt.plot(list(target_k_range), coherence_scores, marker='o', color='b')
    plt.title("Coherence Score Trend (5-15)")
    plt.grid(True)
    plt.savefig("optimized_coherence_trend.png")
    print("\n搜索完毕，趋势图已保存至 'optimized_coherence_trend.png'")


if __name__ == '__main__':
    multiprocessing.freeze_support()
    run_optimized_grid_search()