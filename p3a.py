import matplotlib.pyplot as plt
import pandas as pd

# Initialize the lists for X and Y
data = pd.read_csv("Cars_Barplot.csv")
df = pd.DataFrame(data)

X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])

# Plot the data using bar() method
plt.bar(X, Y, color='g')
plt.title("Used Car Sales")
plt.xlabel("Car")
plt.ylabel("Number Sold")

# Show the plot
plt.show()