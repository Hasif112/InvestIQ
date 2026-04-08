from user_profile import collect_user_profile
from budgeting import analyze_budget
from investments import suggest_investments
from forecasting import forecast_goal

def main():
    print("🎯 Welcome to SmartFin – Your AI-Enhanced Finance Advisor\n")

    profile = collect_user_profile()
    savings = analyze_budget(profile)
    suggest_investments(profile)
    forecast_goal(savings)

if __name__ == "__main__":
    main()
