"""
compare_ocr_metrics.py

This script generates comparison bar charts for OCR performance metrics
of Tesseract and EasyOCR on Bengali text recognition.

It uses matplotlib and seaborn to visualize Character-Level Accuracy (CLA),
Word-Level Accuracy (WLA), Character Error Rate (CER), and Word Error Rate (WER)
for both raw and preprocessed image configurations.

Run this script in a Python environment with the required packages installed:
- matplotlib
- seaborn
- pandas
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set seaborn style
sns.set(style="whitegrid")

# Define the data from Table 6.1
data = {
    "Configuration": [
        "Tesseract-Raw", "Tesseract-Preprocessed",
        "EasyOCR-Raw", "EasyOCR-Preprocessed"
    ],
    "CLA (%)": [56.88, 18.40, 69.99, 52.70],
    "WLA (%)": [45.61, 51.35, 50.99, 29.98],
    "CER (%)": [35.18, 81.60, 30.01, 47.30],
    "WER (%)": [54.39, 48.65, 49.01, 70.02]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Melt for grouped bar chart
df_melted = df.melt(id_vars="Configuration", var_name="Metric", value_name="Value")

# Define colors for different metrics
metric_palette = {
    "CLA (%)": "#4CAF50",    # Green
    "WLA (%)": "#2196F3",    # Blue
    "CER (%)": "#FF9800",    # Orange
    "WER (%)": "#F44336"     # Red
}

# Function to add data labels on bars
def add_data_labels(ax):
    for p in ax.patches:
        height = p.get_height()
        ax.annotate(f'{height:.2f}',
                    (p.get_x() + p.get_width() / 2., height),
                    ha='center', va='bottom',
                    fontsize=9, xytext=(0, 3),
                    textcoords='offset points')

# 1. Grouped Bar Chart (All Metrics in One Chart)
plt.figure(figsize=(12, 6))
ax = sns.barplot(data=df_melted, x="Configuration", y="Value", hue="Metric", palette=metric_palette)

plt.title("Average OCR Performance Across All Configurations", fontsize=14)
plt.ylabel("Value (%)")
plt.xticks(rotation=20)
plt.legend(title="Metric", bbox_to_anchor=(1.05, 1), loc='upper left')

add_data_labels(ax)  # Add labels to grouped bar chart

plt.tight_layout()
plt.savefig('grouped_bar_chart_accuracyVserror_rates.jpg')  # Save plot
plt.show()

# 2. Clustered Charts: Accuracy vs Error Metrics Separately
# Accuracy metrics only
accuracy_metrics = ["CLA (%)", "WLA (%)"]
df_accuracy = df[["Configuration"] + accuracy_metrics].melt(id_vars="Configuration", var_name="Metric", value_name="Value")

plt.figure(figsize=(10, 5))
ax2 = sns.barplot(data=df_accuracy, x="Configuration", y="Value", hue="Metric", palette=metric_palette)

plt.title("Character and Word Level Accuracy", fontsize=14)
plt.ylabel("Accuracy (%)")
plt.xticks(rotation=20)
plt.legend(title="Metric")

add_data_labels(ax2)  # Add labels to clustered chart

plt.tight_layout()
plt.savefig('clustered_chart_accuracy_rates.jpg')  # Save plot
plt.show()
