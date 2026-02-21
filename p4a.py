import pandas as pd
import matplotlib.pyplot as plt

# Importing data
cars_data = pd.read_csv("Cars.csv")

# Plotting Histogram
# Use 'KM' (Kilometers) as the variable for the histogram
plt.hist(cars_data['KM'], color='green', edgecolor='white', bins=5)

# Setting labels and title
plt.title('Histogram of Kilometers')
plt.xlabel('Kilometers')
plt.ylabel('Frequency')

# Display the plot
plt.show()