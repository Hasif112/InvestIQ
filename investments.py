import pandas as pd

def suggest_investments(profile, file_path='data/stock_data.csv'):
    print("\n📊 Investment Suggestions Based on Your Risk Tolerance:")

    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print("❌ Investment data not found.")
        return

    risk = profile['risk_tolerance']

    if risk == "conservative":
        suggestions = df[df['risk'] == 'low']
    elif risk == "moderate":
        suggestions = df[df['risk'].isin(['low', 'moderate'])]
    else:
        suggestions = df  # aggressive

    print(suggestions[['name', 'type', 'average_return']].to_string(index=False))
