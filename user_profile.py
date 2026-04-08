import json
import os

def collect_user_profile():
    print("👤 Enter your financial profile:")

    name = input("Name: ")
    age = int(input("Age: "))
    occupation = input("Occupation: ")
    income = float(input("Monthly Income: "))
    expenses = float(input("Monthly Expenses: "))
    location = input("Location: ")
    currency = input("Currency (e.g., USD, EUR): ")
    risk_tolerance = input("Risk Tolerance (conservative / moderate / aggressive): ").lower()

    profile = {
        "name": name,
        "age": age,
        "occupation": occupation,
        "income": income,
        "expenses": expenses,
        "location": location,
        "currency": currency,
        "risk_tolerance": risk_tolerance
    }

    save_user_profile(profile)
    return profile

def save_user_profile(profile, file_path="data/user_data.json"):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        json.dump(profile, f, indent=4)
