"""
defines the main layout, and includes tab nav and containers
for each page (Learn, Play, Results, History)
"""

import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table
from components.markdown import learn_markdown, data_sources
from components.inputs import input_controls
from components.tables import cost_table
from components.survival_tab import build_survival_tab

layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                [html.H2("Dallas Cost of Living Dashboard", className="text-center bg-primary text-white p-2"),
                html.H4("Elise Reynolds - CS 150 Community Action Computing", className = "text-center"),
                    ])
        ),
        dbc.Row([
            dbc.Tabs([
                dbc.Tab(learn_markdown, label="Learn", tab_id="learn_tab"),

                dbc.Tab([
                    input_controls,
                    dcc.Graph(id="bar-chart"),
                    dcc.Graph(id="line-chart"),
                    ], label="Play", tab_id="play_tab"),

                dbc.Tab([
                    cost_table,
                    html.Div(data_sources, className="mt-3"),
                ], label="Results", tab_id="result_tab"),

                dbc.Tab(build_survival_tab(), label="Would You Survive", tab_id="survival_tab"),
            ], id="tabs", active_tab="play_tab", style={"marginBottom": "20px"})
        ])
        ],
    fluid=True,)