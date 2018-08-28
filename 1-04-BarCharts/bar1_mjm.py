import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.offline as pyo

df  = pd.read_csv(('../Data/2018WinterOlympics.csv'))

trace1 = go.Bar(
    x=df['NOC'],
    y=df['Gold'],
    marker=dict(
        color='FFD700'
    )
)
trace2 = go.Bar(
    x=df['NOC'],
    y=df['Silver'],
    marker=dict(
        color='#9EAA0A1'
    )

)

trace3 = go.Bar(
    x=df['NOC'],
    y=df['Bronze'],
    marker=dict(
        color='#CD7F32'
    )
)


data = [trace1, trace2, trace3]


layout = go.Layout(title='Medals', barmode='stack')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)