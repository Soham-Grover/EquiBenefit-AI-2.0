import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.impute import SimpleImputer  # For handling missing values

# -----SETTING UP OUR DATA-----

# Reading our dummy data csv file
df = pd.read_csv("dummy2.csv")

# Encoding Employment status to numbers
emp_encode = {'Employment Status': {'Employed': 1, 'Unemployed': 2, 'Self-Employed': 3}}
df.replace(emp_encode, inplace=True)

# Encoding Marital Status
m_encode = {'Marital Status': {'Divorced': 1, 'Married': 2, "Widowed": 3}}
df.replace(m_encode, inplace=True)

# Encoding Owns Property
own_encode = {'Real Estate Status': {'Own': 1, 'Rent': 2, 'No Property': 3}}
df.replace(own_encode, inplace=True)

# Encoding Loan status
loan_encode = {'Loan Status': {"Yes": 1, "No": 2}}
df.replace(loan_encode, inplace=True)

# Encoding Eligibility
eli_encode = {'ELIGIBILITY CRITERIA': {'YES': 1, 'NO': 2}}
df.replace(eli_encode, inplace=True)

# Option 2: Impute missing values (uncomment the following lines if you want to impute instead of dropping)
# imputer = SimpleImputer(stra  tegy='mean')  # Use 'mean', 'median', or 'most_frequent'
# df[['Number of Dependents', 'Medical Expenses', 'No. of Schemes Availed', 'Annual Income', 'Age', 'Bank Balance']] = imputer.fit_transform(df[['Number of Dependents', 'Medical Expenses', 'No. of Schemes Availed', 'Annual Income', 'Age', 'Bank Balance']])

# TRAINING
KNN = KNeighborsClassifier()

x = df[['Number of Dependents',
        'Medical Expenses',
        'Loan Status',
        'No. of Schemes Availed',
        'Annual Income',
        'Employment Status',
        'Age',
        'Real Estate Status',
        "Bank Balance",
        "Marital Status"]]

y = df['ELIGIBILITY CRITERIA']

KNN.fit(x, y)

# TESTING
test_df = pd.read_csv('test_2.csv')

test_df.replace(emp_encode, inplace=True)
test_df.replace(m_encode, inplace=True)
test_df.replace(own_encode, inplace=True)
test_df.replace(loan_encode, inplace=True)
test_df.replace(eli_encode, inplace=True)


# Option 2: Impute missing values (uncomment the following lines if you want to impute instead of dropping)
# test_df[['Number of Dependents', 'Medical Expenses', 'No. of Schemes Availed', 'Annual Income', 'Age', 'Bank Balance']] = imputer.transform(test_df[['Number of Dependents', 'Medical Expenses', 'No. of Schemes Availed', 'Annual Income', 'Age', 'Bank Balance']])

x_test = test_df[['Number of Dependents',
                  'Medical Expenses',
                  'Loan Status',
                  'No. of Schemes Availed',
                  'Annual Income',
                  'Employment Status',
                  'Age',
                  'Real Estate Status',
                  "Bank Balance",
                  "Marital Status"]]

y_test = test_df["ELIGIBILITY CRITERIA"]

print(df.head())
print(test_df.head())

predict_eligibility = KNN.predict(x_test)

for prediction in predict_eligibility:
        if prediction == 1:
            print("Yes")
        elif prediction == 2:
              print("No")

# ------ Model Done -------

sklearn_cm = confusion_matrix(y_test, predict_eligibility)
print(sklearn_cm)