#importing necessary packages
import pandas as pd
from scipy import stats
import warnings
import seaborn as sns
import matplotlib.pyplot as plt

# Suppress UserWarning and FutureWarning
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)


# Step 1: Load the CSV files into DataFrames

atgl_data = pd.read_csv('ATGL.csv', parse_dates=['Date'])
adani_green_data = pd.read_csv('ADANIGREEN.csv', parse_dates=['Date'])
adani_energy_data = pd.read_csv('ADANIENSOL.csv', parse_dates=['Date'])

# Step 2: Calculate daily returns based on the Close price

for df in [atgl_data, adani_green_data, adani_energy_data]:
    df['Daily Returns'] = df['Close'].pct_change().dropna()
atgl_data['Stock'] = 'Adani Total Gas'
adani_green_data['Stock'] = 'Adani Green'
adani_energy_data['Stock'] = 'Adani Energy Solutions'

# Concatenating all the data into one DataFrame
combined_data = pd.concat([atgl_data[['Date', 'Stock', 'Daily Returns']], 
                           adani_green_data[['Date', 'Stock', 'Daily Returns']], 
                           adani_energy_data[['Date', 'Stock', 'Daily Returns']]], 
                          ignore_index=True)



# Removing rows with missing values
combined_data = combined_data.dropna(subset=['Daily Returns'])



# Performing ANOVA to test if there's a significant difference between the stocks' returns

grouped_data = [combined_data[combined_data['Stock'] == stock]['Daily Returns'] for stock in combined_data['Stock'].unique()]
f_statistic, p_value = stats.f_oneway(*grouped_data)

# Printing ANOVA results
print("\nANOVA Results:")
print("F-statistic:", f_statistic)
print("P-value:", p_value)

if p_value < 0.05:
    print("There is a significant difference in the average returns of the stocks.")
else:
    print("No significant difference in the average returns of the stocks.")

# Violin Plot Visualization

plt.figure(figsize=(10, 6))
sns.violinplot(x="Stock", y="Daily Returns", data=combined_data, palette="Set2", inner="stick", linewidth=1.25)
plt.title("Comparison of Daily Returns (Adani Stocks)", fontsize=16, weight='bold')
plt.ylabel("Daily Returns", fontsize=14)
plt.xlabel("Stocks", fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()



