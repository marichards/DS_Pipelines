# Import dashboard packages
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc # Graphs, dropdowns, markdown blocks, tables, input types, etc
import dash_html_components as html # Library of components for each HTML tag (e.g. html.H1 is an <h1> tag)

# Import numerical/data packages
import pandas as pd
import numpy as np
import scipy as sp

#############

## Load stylesheet from online
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Create the Dash app using the specified stylesheet
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Customize colors of background and text
colors = {
    'background': '#111111', # Black background
    'text': '#7FDBFF' # Text is light blue
}

# Creation of layout tree
# Children: contains string, component, or list of components; always first component 
# This makes a bucket where we add a header
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={ # Note that styles are in a dictionary and properties are camelCased 
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    # Centered subtitle text
    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph( # From the "core components", add a graph
        id='example-graph-2',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ], # Create 2 bar graphs
            'layout': {
                'plot_bgcolor': colors['background'], # Make plot background black
                'paper_bgcolor': colors['background'], # Make surrounding background black
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)