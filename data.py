import pandas as pd
import random

# Define ministries and some example schemes
ministries_schemes = {
    "Ministry Of Agriculture and Farmers Welfare": ["PM-Kisan", "RKVY"],
    "Ministry Of Chemicals And Fertilizers": ["Fertilizer Subsidy", "Nutrient-Based Subsidy"],
}

# Generate dummy data
def generate_dummy_data(num_records):
    data = []
    for _ in range(num_records):
        name = f"Person_{random.randint(1, 1000)}"
        adhaar_no = f"{random.randint(100000000000, 999999999999)}"
        pan_number = f"ABCDE{random.randint(1000, 9999)}F"
        number_of_dependents = random.randint(0, 5)
        medical_expenses = random.randint(5000, 100000)
        loan_status = random.choice(["Yes", "No"])
        no_of_schemes_availed = random.randint(0, 2)
        annual_income = random.randint(25000, 300000)
        if annual_income > 150000:
            bank_balance = random.randint(100000, 400000)
        else:
            bank_balance = random.randint(20000, 150000)
        employment_status = random.choice(["Employed", "Unemployed", "Self-Employed", "Employed", "Employed"])
        age = random.randint(18, 75)
        real_estate_status = random.choice(["Own", "Rent", "No Property"])
        ministry = random.choice(list(ministries_schemes.keys()))
        scheme = random.choice(ministries_schemes[ministry])
        marital_status = random.choice(["Widowed", "Married", "Married", "Married", "Married", "Divorced", "Married"])
        
        data.append({
            "Name": name,
            "Adhaar No.": adhaar_no,
            "PAN Number": pan_number,
            "Number of Dependents": number_of_dependents,
            "Medical Expenses": medical_expenses,
            "Loan Status": loan_status,
            "No. of Schemes Availed": no_of_schemes_availed,
            "Annual Income": annual_income,
            "Employment Status": employment_status,
            "Age": age,
            "Real Estate Status": real_estate_status,
            "Bank Balance": bank_balance,
            "Ministry": ministry,
            "Scheme": scheme,
            "Marital Status": marital_status
        })
    
    return pd.DataFrame(data)

# Generate 50 dummy records
dummy_data = generate_dummy_data(1000)

# Display the first 10 rows of the dataset
print(dummy_data.head(10))

# Save the dataset to a CSV file
dummy_data.to_csv("data2.csv", index=False)

print("Dummy data has been saved to 'dummy_data.csv'.")
