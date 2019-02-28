import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

# Data to read in with pandas; do it here, don't load each time
df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/'
    'datasets/master/gapminderDataFiveYear.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Create space for a graph (that we'll specify in a callback)
app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    # Create the input component
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()}
    )
])


@app.callback(
# Specify where the reactive output will go and where the input is coming from
## Note: we never alter the global dataframe, we just make copies
    dash.dependencies.Output('graph-with-slider', 'figure'),
    [dash.dependencies.Input('year-slider', 'value')])
    
# Grab the year 
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year] # Filter for just that year
    traces = [] # Create a place to append scatter plots
    for i in filtered_df.continent.unique(): # Make a plot for each continent
        df_by_continent = filtered_df[filtered_df['continent'] == i]
        traces.append(go.Scatter(
            x=df_by_continent['gdpPercap'],
            y=df_by_continent['lifeExp'],
            text=df_by_continent['country'], # Put the country name in the pop-up text
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i # Name each plot (I think)
        ))

    return { # Return a dictionary with plots and layout info (plotly stuff)
        'data': traces, 
        'layout': go.Layout(
            xaxis={'type': 'log', 'title': 'GDP Per Capita'},
            yaxis={'title': 'Life Expectancy', 'range': [20, 90]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server()