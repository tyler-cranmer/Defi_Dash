import dash
from dash import dcc, html;
from dash.dependencies import Input, Output
import plotly.graph_objects as go

import pandas as pd
from datetime import datetime

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
df = pd.read_csv('/Users/tylercranmer/Dev/DeFi_Dash/newData/Maker_(MKR).csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Checklist(
        id='toggle-rangeslider',
        options=[{'label': 'Include Rangeslider', 
                  'value': 'slider'}],
        value=['slider']
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"), 
    [Input("toggle-rangeslider", "value")])
def display_candlestick(value):
    fig = go.Figure(go.Candlestick(
        x=df['Date'],
        open=df['AAPL.Open'],
        high=df['AAPL.High'],
        low=df['AAPL.Low'],
        close=df['AAPL.Close']
    ))
    
    fig.update_layout(
        xaxis_rangeslider_visible='slider' in value
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
