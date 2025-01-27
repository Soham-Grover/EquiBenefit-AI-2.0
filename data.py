import pandas as pd
import random

# Generate dummy data
data = []
for i in range(50):
    name = f"Person_{random.randint(1, 1000)}"
    aadhaar_no = random.randint(100000000000, 999999999999)
    pan_number = f"ABCDE{random.randint(1000, 9999)}F"
    num_dependents = random.randint(0, 5)
    medical_expenses = random.randint(5000, 100000)
    loan_status = random.choice(["Yes", "No"])
    schemes_availed = random.randint(0, 2)
    annual_income = random.randint(50000, 1000000)
    employment_status = random.choice(["Employed", "Unemployed", "Self-Employed"])
    age = random.randint(18, 75)
    real_estate_status = random.choice(["Own", "Rent", "None"])
    bank_balance = random.randint(10000, 500000)
    ministry = random.choice([
        "Ministry Of Agriculture and Farmers Welfare",
        "Ministry Of Chemicals And Fertilizers"
    ])
    scheme = (
        "PM-Kisan" if ministry == "Ministry Of Agriculture and Farmers Welfare" else
        random.choice(["Nutrient-Based Subsidy", "Fertilizer Subsidy"])
    )
    data.append([
        name, aadhaar_no, pan_number, num_dependents, medical_expenses,
        loan_status, schemes_availed, annual_income, employment_status,
        age, real_estate_status, bank_balance, ministry, scheme
    ])

# Create a DataFrame
columns = [
    "Name", "Adhaar No.", "PAN Number", "Number of Dependents",
    "Medical Expenses", "Loan Status", "No. of Schemes Availed",
    "Annual Income", "Employment Status", "Age", "Real Estate Status",
    "Bank Balance", "Ministry", "Scheme"
]
df = pd.DataFrame(data, columns=columns)

# Save to a CSV file or print
df.to_csv("dummy_data.csv", index=False)
print(df)
