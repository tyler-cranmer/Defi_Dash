#!/usr/bin/python3
import dash;
from dash import dcc;
from dash import html;
from dash.dependencies import Input, Output;
import plotly.express as px;
import pandas as pd;
import os;


def gen_time_series(df):
    return html.Div([
    dcc.Dropdown(
        id="ticker",
        options=[{"label": x, "value": x} 
                 for x in df.columns[1:]],
        value=df.columns[1],
        clearable=False,
    ),
    dcc.Graph(id="time-series-chart"),

    html.Div([
    html.H4(children='stock data'),
    gen_table(df)]),
])

def gen_table(dataframe, max_rows=20):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


def gen_dropDown():
    return html.Div([  
        html.Label("Choose Crypto Coin"),  
        dcc.Dropdown(
        id = 'coin dropdown',
        options = [
            {'label' : 'Maker', 'value': 'MKR'},
            {'label' : '0x', 'value': 'ZRX'},
            {'label' : '1inch', 'value': '1INCH'},
            {'label' : 'Aave', 'value': 'AAVE'},
            {'label' : 'Alpha Finance', 'value': 'ALPHA'},
            {'label' : 'Amp', 'value': 'AMP'},
            {'label' : 'Bancor Network Token', 'value': 'BNT'},
            {'label' : 'cDAI', 'value': 'CDAI'},
        ],
        value='MKR'
    )])