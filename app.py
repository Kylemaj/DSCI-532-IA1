import altair as alt
from dash import Dash, dcc, html, Input, Output
import pandas as pd

sales = pd.read_csv("vgsales.csv")

def plot_altair(xcol):
    chart = alt.Chart(sales.sample(4900)).mark_circle().encode(
        x=xcol, 
        y='Genre',
        size='count()',
        color='count()').interactive()
    return chart.to_html()

app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server

app.layout = html.Div([
        dcc.Dropdown(
            id='xcol', value='Platform',
            options=[
                {'label': 'Platform', 'value': 'Platform'},
                {'label': 'Publisher', 'value': 'Publisher'}]),
        html.Iframe(
            id='scatter',
            style={'border-width': '0', 'width': '100%', 'height': '400px'},
            srcDoc=plot_altair(xcol='Platform'))])

@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xcol', 'value'))
def update_output(xcol):
    return plot_altair(xcol)

if __name__ == '__main__':
    app.run_server(debug=True)
