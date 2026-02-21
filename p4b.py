import matplotlib.pyplot as plt
import pandas as pd

# Creating dataset from CSV
cars_data = pd.read_csv("Cars_Barplot.csv")
cars = cars_data["Car"]
data = cars_data["Sales"]

# Creating plot
fig = plt.figure(figsize=(10, 7))
plt.pie(data, labels=cars, autopct='%1.1f%%')

# Show plot
plt.show()