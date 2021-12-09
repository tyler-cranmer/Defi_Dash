import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from components.Generate import gen_table, gen_dropDown;

# df = px.data.gapminder()
df = pd.read_csv('/Users/tylercranmer/Dev/DeFi_Dash/allData/stack.csv')

countries = (
    df.Name.drop_duplicates()
    .sample(n=5, random_state=42)
)
df = df[df.Name.isin(countries)]

app = dash.Dash(__name__)
app.layout = html.Div([
    html.P("Select y-axis"),
    dcc.Dropdown(
        id='y-axis',
        options=[
            {'label': x, 'value': x} 
            for x in ['Volume', 'Market Cap', 'Open']],
        value='Volume'
    ),
    dcc.Graph(id="graph"),

    html.Div([
    html.H4(children='stock data'),
    gen_table(df)]),

])


@app.callback(
    Output("graph", "figure"), 
    [Input("y-axis", "value")])
def display_area(y):
    fig = px.area(
        df, x="Date", y=y,
        color="Name", line_group="Name")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
