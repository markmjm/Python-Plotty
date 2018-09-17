import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='my_id', value ='Inital_value', type='text'),
    html.Div(id='my_dev', style=dict(
        border='2px blue solid'
    ))
])


# @app.callback is function update_output_div decorator
@app.callback(
    Output(component_id='my_dev', component_property='children'),
    [Input(component_id='my_id', component_property='value')]
)
def update_output_div(user_input):
    return f'You\'ve entered {user_input}'

if __name__ == '__main__':
    app.run_server()