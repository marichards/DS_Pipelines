# Basic idea: Use Input/Output 

import dash
import dash_core_components as dcc
import dash_html_components as html
# This is different from dcc.Input, which is a component (not a callback)
# These are only for callback purposes
from dash.dependencies import Input, Output 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Establish Input...
## There's some initial value (value) with a component ID (id)
app.layout = html.Div([
# This is the dcc input, NOT the callback input (it's a text box)
    dcc.Input(id='my-id', value='initial value', type='text'),
    html.Div(id='my-div') # Output will go here; notice there's no value here; callback fills it in
])


# Happens when an input value changes
## Note: there's only 2 properties for each and they're always in this order; don't have to name them
@app.callback(
    Output(component_id='my-div', component_property='children'), # Output is children property of my-div
    [Input(component_id='my-id', component_property='value')] # Input is the value property of my-id
)


def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)


if __name__ == '__main__':
    app.run_server()