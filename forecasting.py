from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_goal(savings_per_month):
    try:
        goal = float(input("\n🎯 Enter your savings goal amount (e.g., 10000): "))
    except ValueError:
        print("❌ Invalid number.")
        return

    # Simulate savings over 12 months
    months = np.array(range(1, 13)).reshape(-1, 1)
    savings = savings_per_month * months

    model = LinearRegression()
    model.fit(months, savings)

    estimated_months = goal / savings_per_month
    print(f"📈 Estimated months to reach goal: {estimated_months:.1f}")
