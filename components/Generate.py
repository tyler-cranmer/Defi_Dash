#!/usr/bin/python3
import dash;
from dash import dcc, dash_table;
from dash import html;
from dash.dependencies import Input, Output;
import plotly.express as px;
import pandas as pd;
import os;
from collections import OrderedDict


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
])


def gen_table(dataframe):

    data = OrderedDict(dataframe)
    df = pd.DataFrame(
    OrderedDict([(name, col_data * 10) for (name, col_data) in data.items()])
)

    return html.Div([
    html.H4(children='Data Frame'),
    dash_table.DataTable(
    columns=[{"name": i, "id": i} for i in dataframe.columns],
    data=dataframe.to_dict('records'),
    page_size=10
)
    ])


def gen_stack(df):
    tokens = (df.Name.drop_duplicates().sample(n=5, random_state=5))
    df = df[df.Name.isin(tokens)]

    return html.Div([
    html.P("Select y-axis"),
    dcc.Dropdown(
        id='y-axis',
        options=[
            {'label': x, 'value': x} 
            for x in ['Total Volume', 'Market Cap', 'oPrice']],
        value='Market Cap'
    ),
    dcc.Graph(id="graph")

])