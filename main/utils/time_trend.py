import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================================================================
# 1. Global Font & Style Configuration (Pure English)
# ==============================================================================
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

# Load dataset
df = pd.read_excel("Updated_content_场景与多利益主体全量矩阵.xlsx")

# Extract 4-digit publication year
df['Year'] = df['文献名称'].astype(str).str.extract(r'(\b(?:19|20)\d{2}\b)')[0]
years_order = ['2023', '2024', '2025', '2026']
class_order = [f"class{i}" for i in range(12)]
df_year = df[df['Year'].isin(years_order)].copy()

# ==============================================================================
# 2. Chart 1: Temporal Evolution of Social Harms Types (2023–2026)
# ==============================================================================
ct_year_harms = pd.crosstab(df_year['Year'], df_year['社会系统伤害类型'])
ct_year_harms_pct = ct_year_harms.div(ct_year_harms.sum(axis=1), axis=0) * 100

harms_col_map = {
    '人际伤害 (Interpersonal Harms)': 'Interpersonal Harms',
    '分配伤害 (Allocative Harms)': 'Allocative Harms',
    '服务质量伤害 (Quality-of-Service Harms)': 'Quality-of-Service Harms',
    '社会系统伤害 (Social System Harms)': 'Social System Harms',
    '表征伤害 (Representational Harms)': 'Representational Harms'
}
ct_year_harms_pct = ct_year_harms_pct.rename(columns=harms_col_map)
harms_order = [
    'Interpersonal Harms', 'Allocative Harms',
    'Quality-of-Service Harms', 'Social System Harms', 'Representational Harms'
]
ct_year_harms_pct = ct_year_harms_pct[harms_order]

fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)
palette = sns.color_palette("tab10", len(harms_order))

for idx, col in enumerate(harms_order):
    ax.plot(
        ct_year_harms_pct.index,
        ct_year_harms_pct[col],
        marker='o',
        linewidth=2.2,
        markersize=7,
        label=col,
        color=palette[idx]
    )
    for x, y in zip(ct_year_harms_pct.index, ct_year_harms_pct[col]):
        ax.annotate(
            f"{y:.1f}%",
            (x, y),
            textcoords="offset points",
            xytext=(0, 6),
            ha='center',
            fontsize=8.5,
            weight='bold'
        )

ax.set_title("Temporal Evolution of Social Harms Types (2023–2026)", fontsize=13, pad=15, weight='bold')
ax.set_xlabel("Publication Year", fontsize=11, weight='bold', labelpad=10)
ax.set_ylabel("Proportion within Year (%)", fontsize=11, weight='bold', labelpad=10)
ax.set_ylim(0, 45)
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.legend(title="Social Harms Type", bbox_to_anchor=(1.02, 1), loc='upper left', fontsize=9.5)
plt.tight_layout()
plt.savefig("Temporal_Evolution_Social_Harms.png")
plt.close()

# ==============================================================================
# 3. Chart 2: Temporal Dynamics of Governance Scenarios and Stakeholders
# ==============================================================================
scen_cols = ['场景_1. 作者投稿与披露', '场景_2. 编辑技术预审', '场景_3. 专家同行评议', '场景_4. 宏观评价与体制']
scen_names = ['1. Submission', '2. Screening', '3. Peer Review', '4. Macro Policy']
year_counts = df_year['Year'].value_counts()

ct_year_scen_pct = df_year.groupby('Year')[scen_cols].sum().div(year_counts, axis=0) * 100
ct_year_scen_pct.columns = scen_names

stake_cols = ['主体_作者与科研人员', '主体_期刊编辑部与出版商', '主体_同行评议专家', '主体_高校与科研院所', '主体_AI技术开发商']
stake_names = ['Authors', 'Publishers', 'Reviewers', 'Institutions', 'AI Developers']
ct_year_stake_pct = df_year.groupby('Year')[stake_cols].sum().div(year_counts, axis=0) * 100
ct_year_stake_pct.columns = stake_names

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 5.5), dpi=300)

# Subplot A: Governance Scenarios
ct_year_scen_pct.plot(kind='bar', ax=ax1, width=0.75, colormap='Purples')
ax1.set_title("(A) Governance Scenarios Engagement Rate over Time", fontsize=12, pad=12, weight='bold')
ax1.set_xlabel("Publication Year", fontsize=10.5, weight='bold')
ax1.set_ylabel("Coverage within Year (%)", fontsize=10.5, weight='bold')
ax1.set_xticklabels(years_order, rotation=0)
ax1.set_ylim(0, 100)
ax1.grid(axis='y', linestyle='--', alpha=0.5)
ax1.legend(title="Governance Scenario", fontsize=9, loc='upper left')

# Subplot B: Stakeholders
ct_year_stake_pct.plot(kind='bar', ax=ax2, width=0.8, colormap='Greens')
ax2.set_title("(B) Stakeholders Responsibility Rate over Time", fontsize=12, pad=12, weight='bold')
ax2.set_xlabel("Publication Year", fontsize=10.5, weight='bold')
ax2.set_ylabel("Coverage within Year (%)", fontsize=10.5, weight='bold')
ax2.set_xticklabels(years_order, rotation=0)
ax2.set_ylim(0, 110)
ax2.grid(axis='y', linestyle='--', alpha=0.5)
ax2.legend(title="Stakeholder", fontsize=9, loc='upper left')

plt.suptitle("Temporal Dynamics of Governance Scenarios and Stakeholders (2023–2026)", fontsize=14, weight='bold', y=0.98)
plt.tight_layout()
plt.savefig("Temporal_Dynamics_Scenarios_and_Stakeholders.png")
plt.close()

# ==============================================================================
# 4. Chart 3: BERTopic Clusters Temporal Emergence Heatmap
# ==============================================================================
ct_year_class = pd.crosstab(df_year['BERTopic聚类'], df_year['Year']).reindex(class_order).fillna(0)
ct_year_class_pct = ct_year_class.div(ct_year_class.sum(axis=1), axis=0) * 100

plt.figure(figsize=(9, 7), dpi=300)
sns.heatmap(
    ct_year_class_pct,
    annot=True,
    fmt=".1f",
    cmap="YlGnBu",
    cbar_kws={'label': 'Class-Wise Temporal Distribution (%)'},
    annot_kws={"size": 10, "weight": "bold"}
)
plt.title("BERTopic Clusters Temporal Emergence and Evolution Heatmap (%)", fontsize=13, pad=15, weight='bold')
plt.xlabel("Publication Year", fontsize=11, labelpad=10, weight='bold')
plt.ylabel("BERTopic Cluster (Class)", fontsize=11, labelpad=10, weight='bold')
plt.tight_layout()
plt.savefig("BERTopic_Clusters_Temporal_Heatmap.png")
plt.close()

print("All pure English temporal charts successfully exported!")