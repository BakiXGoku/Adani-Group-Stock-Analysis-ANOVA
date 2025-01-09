import yfinance as yf
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Step 1: Define stock tickers
tickers = {
    "Adani Total Gas": "ATGL.NS",
    "Adani Green": "ADANIGREEN.NS",
    "Adani Energy Solutions": "ADANIENSOL.NS"
}

# Step 2: Download stock data for the past 12 months
data = {}
for name, ticker in tickers.items():
    stock_data = yf.download(ticker, period="1y", interval="1d")
    data[name] = stock_data['Close'].pct_change().dropna()  # Daily returns

# Step 3: Perform ANOVA
returns = list(data.values())
f_stat, p_value = stats.f_oneway(*returns)


# Step 4: Display ANOVA results
print("ANOVA Results:")
print(f"F-statistic: {f_stat}")
print(f"P-value: {p_value}")

if p_value < 0.05:
    print("There is a significant difference in the average returns of the stocks.")
else:
    print("No significant difference in the average returns of the stocks.")

# Step 3: Combine data into a single DataFrame for seaborn
combined_data = pd.concat(data, names=['Stock']).reset_index()
combined_data.columns = ['Stock', 'Date', 'Daily Returns']

plt.figure(figsize=(10, 6))
sns.violinplot(x="Stock", y="Daily Returns", data=combined_data, palette="muted", inner="quartile")
plt.title("Comparison of Daily Returns (Adani Stocks)", fontsize=14)
plt.ylabel("Daily Returns", fontsize=12)
plt.xlabel("Stocks", fontsize=12)
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()
