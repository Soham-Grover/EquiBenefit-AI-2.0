import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# -----SETTING UP OUR DATA-----

# Reading our dummy data csv file
df = pd.read_csv("Updated_Govt_Schemes_Data.csv")

# Encoding Employment status to numbers

print(df["Employment Status"][:5])

emp_encode = {'Employment Status': {'Employed': 1, 'Unemployed': 2, 'Self-employed': 3, 'Retired': 4}}
df.replace(emp_encode, inplace=True)

# Encoding education level
df['Education Level'].fillna('None', inplace=True)

edulevel_encode = {'Education Level': {'Secondary': 2, 'Primary': 1, 'Higher': 3, 'Graduate': 4, 'None': 5}}
df.replace(edulevel_encode, inplace=True)

# Encoding Region

region_encode = {'Region': {'Urban': 1, 'Rural': 2, 'Suburban': 3}}
df.replace(region_encode, inplace=True)

# Encoding Owns Property

own_encode = {'Owns Property': {'Yes': 1, 'No': 0}}
df.replace(own_encode, inplace=True)
# print(df['Owns Property'].value_counts())

# Encoding Loan status
loan_encode = {'Loan Status': {'No Loan': 0, 'Pending': 1, 'Defaulted': 2, 'Paid': 3}}
df.replace(loan_encode, inplace=True)

# Encoding Eligibilty

eli_encode = {'Eligibility': {'Yes': 1, 'No': 0}}
df.replace(eli_encode, inplace=True)


print(df["Employment Status"][:5])

# TRAINING

KNN = KNeighborsClassifier()

x = df[['Income',
        'Number of Dependents',
        'Employment Status',
        'Age',
        'Education Level',
        'Region',
        'Owns Property',
        'Bank Balance',
        'Loan Status',
        'Medical Expenses']]

y = df['Eligibility']


KNN = KNN.fit(x,y)

test = pd.DataFrame()

# TESTING

# Reading our dummy test file

test_df = pd.read_csv('test_data.csv')

test_df.replace(emp_encode, inplace=True)
test_df['Education Level'].fillna('None', inplace=True)
test_df.replace(edulevel_encode, inplace=True)
test_df.replace(region_encode, inplace=True)
test_df.replace(own_encode, inplace=True)
test_df.replace(loan_encode, inplace=True)
test_df.replace(eli_encode, inplace=True)


x_test = test_df[['Income',
                  'Number of Dependents',
                  'Employment Status',
                  'Age',
                  'Education Level',
                  'Region',
                  'Owns Property',
                  'Bank Balance',
                  'Loan Status',
                  'Medical Expenses']]

y_test = test_df["Eligibility"]

predict_eligibilty = KNN.predict(x_test)

for prediction in predict_eligibilty:
    if prediction == 1:
        print('Yes')
    else:
        print('No')

# ------ Model Done -------

# ------- Representation of our model ----------

yes_count = np.sum(predict_eligibilty == 1)
no_count = np.sum(predict_eligibilty == 0)

# Prepare the data for the bar plot
labels = ['Yes', 'No']
counts = [yes_count, no_count]

# Create the bar plot
plt.bar(labels, counts, color=['green', 'red'])
plt.xlabel('Eligibility')
plt.ylabel('Number of Predictions')
plt.title('Number of Yes and No Predictions')
plt.show()

print(confusion_matrix(y_test, predict_eligibilty))