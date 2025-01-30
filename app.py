import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import main

st.metric(label="Accuracy", value="96 %", delta="56 %")
labels = ['Yes', 'No']
values = [np.sum(main.predict_eligibility == 1), np.sum(main.predict_eligibility == 2)]
colors = ['#66b3ff', '#ff9999']
plt.figure(figsize=(6, 6))
plt.pie(values, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title('Eligibility Predictions')
plt.subplot(1,2,1)

labels2 = ['Married', 'Divorced', 'Widowed']
values2 = [np.sum(main.predict_marital == 2), np.sum(main.predict_marital == 1), np.sum(main.predict_marital == 3)]
plt.subplot(1,2,2)

st.pyplot(plt)