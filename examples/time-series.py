import dash
from dash import dcc, html;
from dash.dependencies import Input, Output
# import plotly.graph_objects as go
import plotly.express as px
from components.Generate import gen_table, gen_dropDown


df = px.data.stocks()

app = dash.Dash(__name__)


app.layout = html.Div([
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


@app.callback(
    Output("time-series-chart", "figure"), 
    [Input("ticker", "value")])
def display_time_series(ticker):
    fig = px.line(df, x='date', y=ticker)
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
