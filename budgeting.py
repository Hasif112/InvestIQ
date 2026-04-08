def analyze_budget(profile):
    income = profile['income']
    expenses = profile['expenses']
    currency = profile['currency']
    savings = income - expenses
    savings_rate = (savings / income) * 100

    print("\n💰 Budget Analysis:")
    print(f"- Income: {currency} {income}")
    print(f"- Expenses: {currency} {expenses}")
    print(f"- Monthly Savings: {currency} {savings}")
    print(f"- Savings Rate: {savings_rate:.2f}%")

    if savings_rate < 10:
        print("⚠️  Try to reduce spending. Aim to save at least 10%.")
    elif savings_rate < 20:
        print("👍 Decent savings. Push towards 20%+ if possible.")
    else:
        print("🎉 Great job! You're saving efficiently!")

    return savings
