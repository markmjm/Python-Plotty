#######
# This shows the mpg.csv dataset as a spread out scatter plot
# without any callbacks.
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from numpy import random

app = dash.Dash()

df = pd.read_csv('../data/mpg.csv')
# Add a random "jitter" to model_year to spread out the plot
df['year'] = random.randint(-4, 5, len(df)) * 0.10 + df['model_year']

#######################
# Left side figure
#######################
data_l = [go.Scatter(
    x=df['year'] + 1900,
    y=df['mpg'],
    text=df['name'],
    hoverinfo='text' + 'x' + 'y',  # see doc
    mode='markers'
)]
layout_l = go.Layout(
    title='-mpg.csv dataset-',
    xaxis=dict(title='model year'),
    yaxis=dict(title='miles per gallon'),
    hovermode='closest'
)
fig_l = go.Figure(data=data_l, layout=layout_l)

#######################
# Left side figure
#######################
data_r = [go.Scatter(
    x=[0, 1],
    y=[0, 1],
    mode='lines'
)]
layout_r = go.Layout(
    title='Accelaration',
    margin={'l': 0}
)
fig_r = go.Figure(data=data_r, layout=layout_r)

app.layout = html.Div([
    html.Div([dcc.Graph(id='mpg_scatter',
                        figure=fig_l)],
             style=dict(
                 width='50%',
                 display='inline-block'
             )),
    html.Div([dcc.Graph(id='mpg_line',
                        figure=fig_r)],
             style=dict(
                 width='20%',
                 height='50%',
                 display='inline-block'
             ))
])


@app.callback(
    Output('mpg_line', 'figure'),
    [Input('mpg_scatter', 'hoverData')])
def callback_graph(hoverData):
    if hoverData:
        v_index = hoverData['points'][0]['pointIndex']  # vehical index ... point selected
        data = [go.Scatter(
            x=[0, 1],
            y=[0, 60 / df.iloc[v_index]['acceleration']],
            mode='lines',
            line={'width': 2 * df.iloc[v_index]['cylinders']}
        )]
        layout = go.Layout(
            title=df.iloc[v_index]['name'],
            xaxis={'visible': False},
            yaxis={'visible': False, 'range': [0, 60 / df['acceleration'].min()]},
            margin={'l': 0},
            height=300
        )
        fig = go.Figure(data=data, layout=layout)
        return fig


if __name__ == '__main__':
    app.run_server()
