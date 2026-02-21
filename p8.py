import numpy as np
import plotly.graph_objects as go

# Create data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

# Create meshgrid
x, y = np.meshgrid(x, y)

# Create Z values
z = np.sin(np.sqrt(x**2 + y**2))

# Create 3D surface plot
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])

# Update layout
fig.update_layout(
    title='3D Surface Plot Example',
    scene=dict(
        xaxis_title='X Axis',
        yaxis_title='Y Axis',
        zaxis_title='Z Axis'
    )
)

# Show plot
fig.show()