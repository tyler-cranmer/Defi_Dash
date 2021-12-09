#!/usr/bin/python3
import dash;
from dash import dcc, html;
from dash.dependencies import Input, Output;
import plotly.express as px;
import pandas as pd;
import os;
from components.Generate import gen_table, gen_time_series, gen_stack

stack_df = pd.read_csv('/Users/tylercranmer/Dev/DeFi_Dash/allData/stack.csv')
price_df = pd.read_csv('/Users/tylercranmer/Dev/DeFi_Dash/allData/price.csv')
market_sing_df = pd.read_csv('/Users/tylercranmer/Dev/DeFi_Dash/allData/mk_cap_single.csv')
market_df = pd.read_csv('/Users/tylercranmer/Dev/DeFi_Dash/allData/market_cap.csv')
vol_sing_df = pd.read_csv('/Users/tylercranmer/Dev/DeFi_Dash/allData/total_vol_single.csv')
volume_df = pd.read_csv('/Users/tylercranmer/Dev/DeFi_Dash/allData/total_volume.csv')
bubble_df = pd.read_csv('/Users/tylercranmer/Dev/DeFi_Dash/allData/bubble_noBTC.csv')
df1 = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/tesla-stock-price.csv')

app = dash.Dash(__name__)

fig = px.scatter(bubble_df, x="total volume", y="price",
                 size="market cap", color="name", hover_name="abv",
                 log_x=True, size_max=60)

app.layout = html.Div([
    html.Div([
    html.H1(children=' DeFi Data Dashboard', style={'textAlign': 'center'}),
    html.H4(children='1 Year Token Price Data', style={'textAlign': 'center'}),
    gen_time_series(price_df)]),
    gen_table(price_df),

    html.H2(children='Total Volume x Price', style={'textAlign': 'center'}),
    html.H4(children='Defi Tokens Price, Total Volume and Total Market Cap', style={'textAlign': 'center'}),
    dcc.Graph(
        id='bubble',
        figure=fig
    ),

    html.Div([
    gen_table(bubble_df)]),

    html.Div([
    html.H2(children='Area Stacked Chart', style={'textAlign': 'center'}),
    html.H4(children= "Token's Market Cap, Total Volume, Price Data", style={'textAlign': 'center'}),
    gen_stack(stack_df)]),
    gen_table(stack_df)

])


@app.callback(
    Output("time-series-chart", "figure"), 
    [Input("ticker", "value")])

def display_time_series(ticker):
    fig = px.line(price_df, x='Date', y=ticker)
    return fig

@app.callback(
    Output("graph", "figure"), 
    [Input("y-axis", "value")])
def display_area(y):
    fig = px.area(
        stack_df, x="Date", y=y,
        color="Name", line_group="Name")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)