from bokeh.plotting import figure, show, output_file
from bokeh.layouts import gridplot
import random
import numpy as np

# Sample data
x = list(range(1, 11))
y1 = [random.randint(1, 10) for _ in x]
y2 = [random.randint(1, 10) for _ in x]

# Line Plot
p1 = figure(title="Line Plot", width=400, height=300)
p1.line(x, y1, line_width=2, color="blue")

# Scatter Plot
p2 = figure(title="Scatter Plot", width=400, height=300)
p2.scatter(x, y2, size=10, color="red")

# Bar Plot
p3 = figure(title="Bar Plot", width=400, height=300)
p3.vbar(x=x, top=y1, width=0.5, color="green")

# Histogram
hist, edges = np.histogram(y1, bins=5)

p4 = figure(title="Histogram", width=400, height=300)
p4.quad(
    top=hist,
    bottom=0,
    left=edges[:-1],
    right=edges[1:],
    fill_color="purple",
    line_color="black"
)

# Arrange plots in grid
grid = gridplot([[p1, p2], [p3, p4]])

# Output
output_file("bokeh_multiple_plots.html")
show(grid)  