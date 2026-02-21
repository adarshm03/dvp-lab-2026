import pandas as pd
import plotly.graph_objects as go

# Create sample time-series data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'Value': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
}

df = pd.DataFrame(data)

# Create time series plot
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=df['Date'],
        y=df['Value'],
        mode='lines+markers',
        name='Value Trend'
    )
)

fig.update_layout(
    title='Time Series Plot',
    xaxis_title='Date',
    yaxis_title='Value'
)

fig.show()