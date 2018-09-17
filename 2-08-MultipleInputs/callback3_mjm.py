#######
# Here we'll use the mpg.csv dataset to demonstrate
# how multiple inputs can affect the same graph.
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv('../data/mpg.csv')

features = df.columns

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(id='xaxis',
                     options=[{'label': i, 'value': i} for i in features], value='displacement')
    ], style=dict(
        width='45%',
        display='inline-block')),
    html.Div([
        dcc.Dropdown(id='yaxis',
                     options=[{'label': i, 'value': i} for i in features], value='mpg')
    ], style=dict(
        width='45%',
        display='inline-block',
        float='right')),
    dcc.Graph(id='feature-graphics')
], style={'padding': 10})


@app.callback(Output('feature-graphics', 'figure'),
              [Input('xaxis', 'value'),
               Input('yaxis', 'value')])
def update_graph(xaxis_name, yaxis_name):
    data = [go.Scatter(
        x=df[xaxis_name],
        y=df[yaxis_name],
        text=df['name'],
        mode='markers',
        marker=dict(
            size=15,
            opacity=0.5,
            line=dict(
                width=0.5, color='white'
            )
        )
    )]

    layout = go.Layout(
        xaxis={'title': xaxis_name},
        yaxis={'title': yaxis_name},
        margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
        hovermode='closest')
    return dict(data=data, layout=layout)


if __name__ == '__main__':
    app.run_server()
