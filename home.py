from dash import Dash, html, dcc, Output, Input
from plotly import express as px
import pandas as pd
import dash_bootstrap_components as dbc


app = Dash(__name__, title='Dash', suppress_callback_exceptions=True,
           external_stylesheets=[dbc.themes.BOOTSTRAP])


tab_style = {





}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'border-bottom': '5px solid #119DFF',


    'fontWeight': 'bold',
}

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"


def navbar(title): return dbc.Navbar(
    dbc.Container(
        children=[
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(
                            html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand(
                            title, className="ms-2")),

                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://plotly.com",
                style={"textDecoration": "none"},
            ),


        ]
    ),
    color="dark",
    dark=True,
)


app.layout = html.Div(

    children=[

        navbar('Dash'),
        dcc.Tabs(className="mx-0 mx-md-5 mt-1 ", id="tabs-input", value='tab-1', children=[
            dcc.Tab(label='Labour Force by Age Group State Malaysia',
                    value='tab-1', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Electricity Consumption, Malaysia (Monthly)',
                    value='tab-2', style=tab_style, selected_style=tab_selected_style),
        ]),

        html.Div(id='tabs-content'),
    ]
)


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


@app.callback(
    Output('Month_vs_Consumption', 'figure'),
    Input('dropdown_consumption', 'value'),
)
def electricity_consumption(consumption):
    df = pd.read_csv('Electricity Consumption, Malaysia (Monthly).csv')
    fig = px.line(df, x="Month", y=consumption, color='Year', text=consumption)
    fig.update_traces(textposition="bottom right")

    return fig


@app.callback(Output('tabs-content', 'children'),
              Input('tabs-input', 'value'))
def render_content(tab):

    tab_1 = html.Div(className="mx-0 mx-md-5 mt-4  ",
                     children=[
                         # html.H1(children='Labour Force by Age Group State Malaysia'),

                         html.Div(className="text-center ",
                                  children='''
        Year 1982 - Year 2021
    '''),

                         # Dropdown
                         html.Div(className="mx-0 mx-md-5 mt-4 d-flex justify-content-center  ",
                                  children=[
                                      dcc.Checklist(className=" w-75  ",
                                                    id="malaysia_state",
                                                    options=['Malaysia', 'Johor', 'Kedah', 'Kelantan', 'Melaka', 'Negeri Sembilan', 'Pahang', 'Pulau Pinang', 'Perak',
                                                             'Perlis', 'Selangor', 'Terengganu', 'Sabah', 'Sarawak', 'W.P. Kuala Lumpur', 'W.P. Labuan', 'W.P. Putrajaya'],
                                                    value=["Malaysia",
                                                           "Terengganu"],
                                                    inline=True,
                                                    inputStyle={"margin-left": "15px",
                                                                "margin-right": "5px"}
                                                    ),
                                  ]
                                  ),

                         # GRAPH SECTION
                         html.Div(
                             children=[
                                 dcc.Graph(id='labour_vs_age'),
                             ]
                         ),
                     ]
                     )

    tab_2 = html.Div(className="mx-1 mx-md-5 mt-4 ",

                     children=[
                         #  html.H1(
                         #      children='Electricity Consumption, Malaysia (Monthly)'),

                         html.Div(className="text-center ", children='''
        Year 2018 - Year 2022
    '''),

                         # Dropdown
                         html.Div(className="mt-4 mx-auto justify-content-center w-75", style={'margin': 'auto', },
                                  children=[
                                      dcc.Dropdown(className=" text-center",

                                                   options=['Local consumption-Industrial, commercial and mining (Million kilowatt-hours)', 'Local consumption- Domestic and public lighting (Million kilowatt-hours)',
                                                            'Exports (Million kilowatt-hours)', 'Losses (Million kilowatt-hours)'],
                                                   value='Local consumption-Industrial, commercial and mining (Million kilowatt-hours)',
                                                   id='dropdown_consumption',

                                                   ),

                         ]
                         ),

                         # GRAPH SECTION
                         html.Div(className="mt-4  ",
                                  children=[
                                      dcc.Graph(id='Month_vs_Consumption'),
                                  ]
                                  ),
                     ])

    if tab == 'tab-1':
        return tab_1
    elif tab == 'tab-2':
        return tab_2


app.run_server(debug=True)
