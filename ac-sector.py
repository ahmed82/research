# Re-import necessary libraries and recreate the chart

import matplotlib.pyplot as plt
import numpy as np

# blockchain market in the supply chain sector
start_value_supply_chain = 3  # billion
end_value_supply_chain = 15  # billion
years_supply_chain = np.arange(2023, 2029)  # From 2023 to 2028

# Calculate CAGR for this scenario based on the starting and ending values
CAGR_supply_chain = ((end_value_supply_chain / start_value_supply_chain) ** (1 / (2028 - 2023)) - 1) * 100

# Generate projected values using CAGR
values_supply_chain = start_value_supply_chain * (1 + CAGR_supply_chain / 100) ** (years_supply_chain - 2023)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(years_supply_chain, values_supply_chain, marker='o', linestyle='-', color='g')

# Adding titles and labels
plt.title('Projected Blockchain Market Growth in the Supply Chain Sector (2023-2028)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Market Size (Billion $)', fontsize=12)

# Display the chart
plt.grid(True)
plt.xticks(years_supply_chain)
plt.show()
