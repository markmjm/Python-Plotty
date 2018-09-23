#######
# First Milestone Project: Develop a Stock Ticker
# dashboard that either allows the user to enter
# a ticker symbol into an input box, or to select
# item(s) from a dropdown list, and uses pandas_datareader
# to look up and display stock data on a graph.
######

# ADD A SUBMIT BUTTON TO TAKE ADVANTAGE OF DASH STATE
import dash
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas_datareader.data as web  # requires v0.6.0 or later
from datetime import datetime
import pandas as pd

app = dash.Dash()

data = [dict(x=[1, 2],
             y=[3, 1])]

nsdq = pd.read_csv('../data/NASDAQcompanylist.csv')
nsdq.set_index('Symbol', inplace=True)

layout = dict(title='Default Title')
fig = go.Figure(data=data, layout=layout)
options=[]
for tic in nsdq.index:
    aDict = dict()
    aDict = dict(
        label = str(nsdq.loc[tic]['Name']) + ' ' + tic,
        value = tic
    )
    options.append(aDict)

app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.Div([
        html.H3('enter a stock symbol:', style=dict(paddingRight='30')),
        dcc.Dropdown(
            id='stock_picker',
            options = options,
            value=['TSLA'],
            multi = True
        )
    ], style=dict(display='inline-block', verticalAlign='top', width = '30%')),
    html.Div([
        html.H3('Select start and end date (must be within 5 years)'),
        dcc.DatePickerRange(id='date_picker',
                            min_date_allowed=datetime(2010, 1, 1),
                            max_date_allowed=datetime.today(),
                            start_date=datetime(2018, 1, 1),
                            end_date=datetime.today()
                            )
    ], style=dict(display='inline-block')),
    html.Div([
        html.Button(id='submit-button',
                    n_clicks=0,
                    children='Submit',
                    style=dict(
                        fontSize=24, marginLeft='30px'
                    ))
    ], style=dict(display='inline-block')),
    dcc.Graph(id='stock_graph',
              figure=fig
              )
])


@app.callback(
    Output('stock_graph', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [
        State('stock_picker', 'value'),
        State('date_picker', 'start_date'),
        State('date_picker', 'end_date')
    ]
)
def update_graph(n_clicks,stock_picker, start_date, end_date):
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')

    traces = []
    for tic in stock_picker:
        df = web.DataReader(tic, 'iex', start, end)
        traces.append(dict(
            x=df.index,
            y=df['close'],
            name=tic
        ))

    data = traces
    layout = dict(title=stock_picker)
    if data:
        return go.Figure(data=data, layout=layout)
    else:
        return go.Figure(data=[dict(x=[0],
             y=[0])], layout=dict(title=''))


if __name__ == '__main__':
    app.run_server()
