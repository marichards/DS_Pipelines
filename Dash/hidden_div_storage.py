# Example for how to cache data for given user's session

# Create global data frame
global_df = pd.read_csv('...')

app.layout = html.Div([
    dcc.Graph(id='graph'), # Spot for graph
    html.Table(id='table'), # Spot for table
    dcc.Dropdown(id='dropdown'), # Dropdown selector

    # Hidden div inside the app that stores the intermediate value
    html.Div(id='intermediate-value', style={'display': 'none'}) # The display:none keeps it hidden
])

# Only update the value
@app.callback(Output('intermediate-value', 'children'), [Input('dropdown', 'value')])
def clean_data(value):
     # some expensive clean data step
     cleaned_df = your_expensive_clean_or_compute_step(value)

     # more generally, this line would be
     # json.dumps(cleaned_df)
     return cleaned_df.to_json(date_format='iso', orient='split') # Now it's a JSON; it's serialized!

     # Take the hidden value and use it to make a figure
@app.callback(Output('graph', 'figure'), [Input('intermediate-value', 'children')])
def update_graph(jsonified_cleaned_data):

    # more generally, this line would be
    # json.loads(jsonified_cleaned_data)
    dff = pd.read_json(jsonified_cleaned_data, orient='split')

    figure = create_figure(dff)
    return figure

    # Take the hidden value and use it to make a table
@app.callback(Output('table', 'children'), [Input('intermediate-value', 'children')])
def update_table(jsonified_cleaned_data):
    dff = pd.read_json(jsonified_cleaned_data, orient='split')
    table = create_table(dff)
    return table