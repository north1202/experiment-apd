import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt


def evaluate_screening_quality(result_file):
    # ==================== 核心修正区域 ====================
    # 优先使用 utf-8 读取，如果失败则自动切换为 gbk 编码读取
    try:
        df = pd.read_csv(result_file, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(result_file, encoding='gbk')
    # =====================================================

    # 强制转换类型，确保统计维度对齐
    df['Ground_Truth'] = pd.to_numeric(df['Ground_Truth'], errors='coerce')
    df['LLM_Prediction'] = pd.to_numeric(df['LLM_Prediction'], errors='coerce')

    # 剔除未完成人工标注的无效行
    df_clean = df.dropna(subset=['Ground_Truth', 'LLM_Prediction'])

    y_true = df_clean['Ground_Truth'].astype(int)
    y_pred = df_clean['LLM_Prediction'].astype(int)

    print(f"参与混淆矩阵评估的有效验证样本数: {len(df_clean)} 篇\n")

    # 2. 生成学术规范标准的二分类混淆矩阵 (1=相关, 0=不相关)
    # 调整labels顺序为 [1, 0]，使矩阵左上角聚焦于核心的“真正例(TP)”
    cm = confusion_matrix(y_true, y_pred, labels=[1, 0])

    # 3. 打印精细的分类统计学报告（包含 Precision, Recall, F1-score）
    report = classification_report(y_true, y_pred, target_names=['Excluded (0)', 'Included (1)'])
    print("=" * 25 + " 核心评价指标报告 " + "=" * 25)
    print(report)
    print("=" * 68)

    # 4. 利用 Seaborn 绘制高质量热力图
    plt.figure(figsize=(7, 5.5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', linewidths=1, linecolor='gray',
                xticklabels=['Predict Included (1)', 'Predict Excluded (0)'],
                yticklabels=['Actual Included (1)', 'Actual Excluded (0)'],
                annot_kws={"size": 14, "weight": "bold"})

    plt.ylabel('Actual Label (Human Gold Standard)', fontsize=12, labelpad=10)
    plt.xlabel('Predicted Label (Qwen-Plus Decision)', fontsize=12, labelpad=10)
    plt.title('AI Disclosure Research Topic Screening \nConfusion Matrix Verification', fontsize=14, pad=20,
              weight='bold')
    plt.tight_layout()

    # 保存可视化图片
    plt.savefig('screening_confusion_matrix.png', dpi=300)
    plt.show()


if __name__ == '__main__':
    RESULT_FILE = 'test_set_results.csv'
    evaluate_screening_quality(RESULT_FILE)