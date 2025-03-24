"""
Dash DashTable set up for displaying filtered cost data in Results Tab.
"""

from dash import dash_table
import pandas as pd

cost_table = dash_table.DataTable(
    id="cost-table",
    columns=[
        {"name": "Category", "id": "Category"},
        {"name": "Cost (USD)", "id": "Cost"}
    ],
    data=[], # come back to
    style_table={"overflowX": "auto"},
    style_cell={"textAlign": "left", "padding": "5px"},
    style_header={"backgroundColor": "#1e1e1e", "color": "white"},
    page_size=10,
)
