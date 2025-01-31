import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import main
import seaborn as sns

st.header("Dashboard")
col1, col2, col3,col4,col5 = st.columns(5)
col1.metric(label="Accuracy", value="91.68 %")
col3.metric(label="Recall Score", value=np.round( main.sklearn_recall * 100, 2))
col5.metric(label="Precision Score", value=np.round(main.sklearn_precision * 100,2))

labels = ['Yes', 'No']
values = [np.sum(main.predict_eligibility == 1), np.sum(main.predict_eligibility == 2)]
colors = ['#66b3ff', '#ff9999', '#99ff99']

labels2 = ['Married', 'Divorced', 'Widowed']
values2 = [np.sum(main.test_df['Marital Status'] == 2), np.sum(main.test_df['Marital Status'] == 1), np.sum(main.test_df['Marital Status'] == 3)]

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].pie(values, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
axes[0].set_title('Eligibility Predictions')

axes[1].pie(values2, labels=labels2, autopct='%1.1f%%', colors=colors, startangle=140)
axes[1].set_title('Marital Status')

st.pyplot(fig)

plt.figure(figsize=(6, 6))
sns.heatmap(main.sklearn_cm, annot=True, fmt='d', cmap='Blues', linewidths=0.5)

# Labels and title
plt.xlabel("Predicted Labels")
plt.ylabel("Actual Labels")
plt.title("Confusion Matrix Heatmap")

# Show the plot
st.pyplot(plt)