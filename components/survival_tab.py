"""
Survival Tab would u survive interactive game like scenario
"""

from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

def build_survival_tab():
    return dbc.Container([
        html.H4("Would You Survive In Dallas?", className="text-center mt-4 mb-3"),

        html.Div(id="survival-income-display", className="text-center mb-3"),

        html.Div("Based on the most recent median household income, select one option from each category to simulate your monthly budget. "),

        html.Hr(),

        dbc.Label("Groceries (Monthly):"),
        dcc.Dropdown(
            id="groceries-choice",
            options=[
                {"label": "Basic Staples - Milk, Eggs, Bread, Rice", "value": "basic"},
                {"label": "Protein-Packed - Chicken, Cheese, Beef", "value": "protein"},
                {"label": "Full Grocery Mix - All of the Above + Fruits + Veggies", "value": "full"},
            ],
            value="basic",
        ),

        html.Br(),
        dbc.Label("Dining Out (Monthly):"),
        dcc.Dropdown(
            id="dining-choice",
            options=[
                {"label": "Cheap - 1 McMeal from McDonald's", "value": "cheap"},
                {"label": "Moderate - 2 McMeals, 4 Coffees, 1 Beer", "value": "moderate"},
                {"label": "Expensive - Fancy dinner, 4 coffees, 2 beers", "value": "expensive"},
            ],
            value="cheap",
        ),

        html.Br(),
        dbc.Label("Transportation (Monthly):"),
        dcc.Dropdown(
            id="transportation-choice",
            options=[
                {"label": "Public Transit Pass", "value": "transit"},
                {"label": "Gasoline (commuter car)", "value": "gas"},
                {"label": "Car Ownership (gas + insurance est.)", "value": "car"},
            ],
            value="transit",
        ),

        html.Br(),
        dbc.Label("Childcare (Monthly):"),
        dcc.Dropdown(
            id="childcare-choice",
            options=[
                {"label": "None", "value": "none"},
                {"label": "Home-Based (avg infant/toddler rate)", "value": "home"},
                {"label": "Center-Based (avg infant/toddler rate", "value": "center"},
            ],
            value="none",
        ),

        html.Br(),
        dbc.Label("Housing (Monthly Rent):"),
        dcc.Dropdown(
            id="housing-choice",
            options=[
                {"label": "1BR Outside Center", "value": "outside"},
                {"label": "1BR In City Center", "value": "center"},
                {"label": "Shared Roomate Situation", "value": "shared"},
            ],
            value="shared",
        ),

        html.Hr(),

        dbc.Button("Calculate Budget Survival", id="calculate-button", color="primary", className="mb-3"),
        html.Div(id="survival-result", className="mt-3"),
        dbc.Button("Play Again", id="reset-again", color="secondary", className="mt-2"),
        ], className="p-4")