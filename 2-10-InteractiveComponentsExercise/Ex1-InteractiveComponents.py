#######
# Objective: Create a dashboard that takes in two or more
# input values and returns their product as the output.
######

# Perform imports here:
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

# Launch the application:
app = dash.Dash()

# Create a Dash layout that contains input components
# and at least one output. Assign IDs to each component:
app.layout = html.Div([
    html.Div([
        html.H4('Enter 1st value'),
        dcc.Input(id='first_val', value='0', type='text')],
        style={'width': '48%', 'display': 'inline-block'}
    ),
    html.Div([
        html.H4('Enter 2nd value'),
        dcc.Input(id='second_val', value='0', type='text')],
        style = {'width': '48%', 'float':'right', 'display': 'inline-block'}
    ),
    html.Hr(),
    html.H4('1st value * 2nd value is:'),
    html.Div(id='result')
])

# Create a Dash callback:
@app.callback(
    Output(component_id='result', component_property='children'),
    [
        Input(component_id='first_val', component_property='value'),
        Input(component_id='second_val', component_property='value')
    ]
)
def multiply(num1, num2):
    return float(num1) * float(num2)

# Add the server clause:
if __name__ == '__main__':
    app.run_server()















