#######
# Objective: Create a scatterplot of 1000 random data points.
# x-axis values should come from a normal distribution using
# np.random.randn(1000)
# y-axis values should come from a uniform distribution over [0,1) using
# np.random.rand(1000)
######

# Perform imports here:
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# Define a data variable
random_x = np.random.randn(10000) # normal distribution
random_y = np.random.rand(10000)  # uniform distribution
data = [
    go.Scatter(x=random_x,
               y=random_y,
               mode='markers',
               marker=dict(
               size=5,
               color='red',
               symbol='circle',
               line=dict(
               width=0
               )
               ))
]
# Define the layout
layout = go.Layout(title='Scatter Plot',
                   xaxis={'title': 'normal distribution'},
                   yaxis=dict(title='uniform distribution'),
                   hovermode='closest')

# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='scatter.html')
