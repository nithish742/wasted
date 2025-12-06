import pandas as pd
import matplotlib.pyplot as plt

# Quarterly data
data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'InventoryTurnover': [5.53, 1.53, 6.58, 7.15]
}

df = pd.DataFrame(data)
average_itr = df['InventoryTurnover'].mean()
industry_target = 8

print(f"Average Inventory Turnover Ratio: {average_itr:.2f}")

# Plotting
plt.figure(figsize=(8,5))
plt.plot(df['Quarter'], df['InventoryTurnover'], marker='o', label='Company ITR')
plt.axhline(industry_target, color='red', linestyle='--', label='Industry Target')
plt.title('Quarterly Inventory Turnover Ratio')
plt.ylabel('Inventory Turnover Ratio')
plt.xlabel('Quarter')
plt.legend()
plt.grid(True)
plt.savefig('inventory_turnover_trend.png', dpi=300)
plt.show()
