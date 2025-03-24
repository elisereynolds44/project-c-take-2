"""
Reusable input components (dropdowns, sliders, radios) for the Play Tab
"""

import dash_bootstrap_components as dbc
from dash import dcc, html

input_controls = dbc.Card([
    dbc.CardBody([
        html.H5("Explore Cost of Living Variables", className="card-title"),

        dbc.Label("Select Housing Index Source:"),
        dcc.Dropdown(
            id="housing-source-dropdown",
            options=[
                {"label": "Original Source", "value": "default"},
                {"label": "FRED Index", "value": "fred"},
            ],
            value="default",
            clearable=False,
            className="mb-3",
        ),

        dbc.Label("Select Expense Category:"),
        dcc.Dropdown(
            id="category-dropdown",
            options=[
                {"label": "Housing", "value": "housing"},
                {"label": "Childcare", "value": "childcare"},
                {"label": "Groceries", "value": "groceries"},
                {"label": "Dining Out", "value": "dining"},
                {"label": "Utilities", "value": "utilities"},
                {"label": "Transportation", "value": "transportation"},
            ],
            value="housing",
            clearable=False,
        ),
    ])
])