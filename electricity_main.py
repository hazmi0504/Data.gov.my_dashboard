from dash import Dash, html, dcc, Output, Input
from plotly import express as px
import pandas as pd

app = Dash(__name__, title='Electricity Consumption, Malaysia (Monthly)')

app.layout = html.Div(

    children=[
    html.H1(children='Electricity Consumption, Malaysia (Monthly)'),

    html.Div(children='''
        Year 2018 - Year 2022
    '''),

    # Dropdown
    html.Div(
        children=[
            dcc.Dropdown(
            ['Local consumption-Industrial, commercial and mining (Million kilowatt-hours)','Local consumption- Domestic and public lighting (Million kilowatt-hours)','Exports (Million kilowatt-hours)','Losses (Million kilowatt-hours)'],
            value='Local consumption-Industrial, commercial and mining (Million kilowatt-hours)',
            id='dropdown_consumption'),
        ]
    ),

    # GRAPH SECTION
    html.Div(
        children=[
        dcc.Graph(id='Month_vs_Consumption'),
        ]
    ),
])

@app.callback(
    Output('Month_vs_Consumption','figure'),
    Input('dropdown_consumption', 'value'),
    )
def electricity_consumption(consumption):
    df = pd.read_csv('Electricity Consumption, Malaysia (Monthly).csv')
    fig = px.line(df, x="Month", y=consumption, color='Year', text=consumption)
    fig.update_traces(textposition="bottom right")

    return fig

app.run_server(debug=True)