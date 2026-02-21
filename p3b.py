# import the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing data.
cars_data = pd.read_csv("Cars.csv")

# Create scatter plot using two variables, Age and Price.
plt.scatter(cars_data['Age'],cars_data['Price'],c='blue')

#To set the title
plt.title('Scatter plot of Price vs Age of the Cars')

#To set the x and y axis labels.
plt.xlabel('Age (months)')
plt.ylabel('Price (Euros)')

#To show the scatter plot
plt.show()