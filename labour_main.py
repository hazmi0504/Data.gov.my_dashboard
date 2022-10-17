from dash import Dash, html, dcc, Output, Input
from plotly import express as px
import pandas as pd

app = Dash(__name__, title='Labour Force by Age Group State Malaysia')

app.layout = html.Div(

    children=[
        html.H1(children='Labour Force by Age Group State Malaysia'),

        html.Div(children='''
        Year 1982 - Year 2021
    '''),

        # Dropdown
        html.Div(
            children=[
                dcc.Checklist(
                    id="malaysia_state",
                    options=['Malaysia', 'Johor', 'Kedah', 'Kelantan', 'Melaka', 'Negeri Sembilan', 'Pahang', 'Pulau Pinang', 'Perak',
                             'Perlis', 'Selangor', 'Terengganu', 'Sabah', 'Sarawak', 'W.P. Kuala Lumpur', 'W.P. Labuan', 'W.P. Putrajaya'],
                    value=["Malaysia", "Terengganu"],
                    inline=True),
            ]
        ),

        # GRAPH SECTION
        html.Div(
            children=[
                dcc.Graph(id='labour_vs_age'),
            ]
        ),
    ])


@app.callback(
    Output('labour_vs_age', 'figure'),
    [Input('malaysia_state', 'value'), ]
)
def electricity_consumption(state):
    df = pd.read_csv(
        'labour_force_by_age_group_state_malaysia_1982_2021_dataset.csv')
    mask = df.State.isin(state)
    fig = px.line(df[mask], x='Year', y='Total', color='Age')

    return fig


app.run_server(debug=True)
