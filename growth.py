
import matplotlib.pyplot as plt
import numpy as np

# Years from 2021 to 2030
years = np.arange(2021, 2031)

# Starting value in 2021 and estimated value in 2030
start_value = 4.9  # billion
end_value = 50  # billion

# Calculate the values for each year using the CAGR formula
CAGR = 33.6 / 100
values = start_value * (1 + CAGR) ** (years - 2021)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(years, values, marker='o', linestyle='-', color='b')

# Adding titles and labels
plt.title('Projected Growth of Market from 2021 to 2030', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Market Size (Billion $)', fontsize=12)

# Display the chart
plt.grid(True)
plt.xticks(years)
plt.show()
