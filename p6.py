import seaborn as sns
import matplotlib.pyplot as plt

# Load built-in dataset
tips = sns.load_dataset("tips")

# Set overall theme
sns.set_theme(style="whitegrid")

# Set color palette
sns.set_palette("Set2")

# Create figure
plt.figure(figsize=(8, 6))

# Create scatter plot
sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="day",          # Color grouping
    style="time",       # Marker style
    size="size"         # Point size
)

# Remove top and right borders
sns.despine()

# Labels and title
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.title("Seaborn Customized Scatter Plot")

# Show plot
plt.show()