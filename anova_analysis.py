import numpy as np
from scipy import stats

# Example data: Stock returns of three groups
group1 = [2.5, 3.0, 3.5, 3.8]
group2 = [3.0, 3.5, 4.0, 4.2]
group3 = [4.0, 4.5, 5.0, 5.5]

# Perform one-way ANOVA
f_stat, p_value = stats.f_oneway(group1, group2, group3)

# Output results
print(f"F-statistic: {f_stat}")
print(f"P-value: {p_value}")

# Interpretation
if p_value < 0.05:
    print("There is a significant difference between the groups.")
else:
    print("No significant difference between the groups.")
