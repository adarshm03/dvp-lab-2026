import matplotlib.pyplot as plt

def linear_plot():
    # Sample data
    x = [1, 2, 3, 4, 5]
    y = [3, 7, 9, 11, 14]

    # Plot the data
    plt.plot(x, y, marker='o', linestyle='-', label='Linear Plot')

    # Labels and Title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Linear Plot Example')

    # Show legend
    plt.legend()

    # Show plot
    plt.grid(True)
    plt.show()

# Call function
linear_plot()