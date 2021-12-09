import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

df = px.data.gapminder()
countries = (
    df.country.drop_duplicates()
    .sample(n=10, random_state=42)
)
df = df[df.country.isin(countries)]

app = dash.Dash(__name__)
app.layout = html.Div([
    html.P("Select y-axis"),
    dcc.Dropdown(
        id='y-axis',
        options=[
            {'label': x, 'value': x} 
            for x in ['lifeExp', 'pop', 'gdpPercap']],
        value='pop'
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"), 
    [Input("y-axis", "value")])
def display_area(y):
    fig = px.area(
        df, x="year", y=y,
        color="continent", line_group="country")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
