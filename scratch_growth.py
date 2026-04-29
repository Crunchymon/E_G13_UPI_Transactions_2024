import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data and prep just like notebook
df = pd.read_csv('/Users/aditr/Desktop/dvaproject/E_G13_UPI_Transactions_2024/data/processed/cleaned_upi_transactions_2024.csv')
df = df.dropna(subset=['sender_age_group', 'sender_state', 'transaction_type', 'amount_inr'])
df = df.drop_duplicates()
df['amount_inr'] = pd.to_numeric(df['amount_inr'], errors='coerce')
df = df.dropna(subset=['amount_inr'])
df['sender_age_group'] = df['sender_age_group'].str.strip().str.title()

age_group_analysis = df.groupby('sender_age_group').agg(
    total_transactions=('amount_inr', 'count'),
    total_value=('amount_inr', 'sum'),
    avg_value=('amount_inr', 'mean')
).reset_index()

# Task 2: Growth segmentation logic
median_txns = age_group_analysis['total_transactions'].median()
median_avg_val = age_group_analysis['avg_value'].median()

def get_segment(row):
    if row['total_transactions'] >= median_txns and row['avg_value'] >= median_avg_val:
        return 'Core'
    elif row['total_transactions'] < median_txns and row['avg_value'] >= median_avg_val:
        return 'Growth Opportunity'
    elif row['total_transactions'] >= median_txns and row['avg_value'] < median_avg_val:
        return 'Upsell Opportunity'
    else:
        return 'Low Priority'

age_group_analysis['segment'] = age_group_analysis.apply(get_segment, axis=1)

print("--- TABLE ---")
print(age_group_analysis.to_markdown())

# Plotting to save
plt.figure(figsize=(12, 8))
sns.scatterplot(
    data=age_group_analysis, 
    x='total_transactions', 
    y='avg_value', 
    size='total_value', 
    sizes=(200, 3000), 
    hue='segment', 
    palette={'Core': '#2ca02c', 'Growth Opportunity': '#1f77b4', 'Upsell Opportunity': '#ff7f0e', 'Low Priority': '#d62728'}, 
    alpha=0.7, 
    edgecolor='black'
)

# Median lines
plt.axvline(median_txns, color='gray', linestyle='--', alpha=0.7, label='Median Transactions')
plt.axhline(median_avg_val, color='gray', linestyle='--', alpha=0.7, label='Median Avg Value')

# Labels
for i in range(len(age_group_analysis)):
    plt.text(age_group_analysis['total_transactions'][i] * 1.02, 
             age_group_analysis['avg_value'][i], 
             age_group_analysis['sender_age_group'][i], 
             fontsize=10)

plt.title("Growth Opportunity Matrix by Age Group", fontsize=14, pad=15)
plt.xlabel("Total Transactions (Engagement)", fontsize=12)
plt.ylabel("Avg Transaction Value (Monetization)", fontsize=12)

# Adjust legend
handles, labels = plt.gca().get_legend_handles_labels()
# sns scatterplot creates legend items for both hue and size, let's keep only hue and median lines
# Typically, first few are segments, then sizes
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', frameon=True)
plt.tight_layout()
plt.savefig('growth_matrix.png', dpi=300, bbox_inches='tight')

