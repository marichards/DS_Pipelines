import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.plotly as py
import plotly.figure_factory as ff

df = pd.read_csv('Nutrition__Physical_Activity__and_Obesity_-_Policy_and_Environmental_Data.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Create the plotly table
raw_table = ff.create_table(df)

# Simply display as a table
app.layout = html.Div([

    dcc.Graph(go.Scatter(py.iplot(raw_table))
             ])
          
          
          
if __name__ == '__main__':
    app.run_server()