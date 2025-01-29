# Reload the CSV file
file_path = 'data2.csv'
import pandas as pd

# Load the dataset
data = pd.read_csv(file_path)

# Define the criteria for economic stability
def determine_eligibility(row):
    # Example criteria: annual income > 300,000 or bank balance > 200,000 or owns real estate
    if row['Annual Income'] > 200000 or row['Bank Balance'] > 200000 and row['Real Estate Status'] == 'Own':
        return "NO"
    elif row['Marital Status'] == "Widowed" or row["Marital Status"] == "Divorced" and row["Annual Income"] < 200000:
        return "YES"
    elif row["Age"] >= 60 and row["Annual Income"] < 250000:
        return "YES"
    elif row["Medical Expenses"] > 75000:
        return "YES"
    elif row["Number of Dependents"] > 2 and row["Annual Income"] < 150000:
        return "YES"
    elif row["Employment Status"] == "Unemployed" and row["Bank Balance"] < 200000:
        return "YES"
    else:
        return "NO"

# Apply the criteria and add a new column
data['ELIGIBILITY CRITERIA'] = data.apply(determine_eligibility, axis=1)

# Save the updated dataset
updated_file_path = 'dummy2.csv'
data.to_csv(updated_file_path, index=False)

