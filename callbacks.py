"""
CALLBACKSS !
"""

from dash import Input, Output
import plotly.graph_objects as go
from data_loader import load_housing_index_data, load_cost_of_living_data, load_median_income_data
from components.charts import make_bar_chart, make_line_chart
import pandas as pd

def register_callbacks(app):
    # Callback #1: Update the housing price index line chart
    @app.callback(
        Output("line-chart", "figure"),
        Input("housing-source-dropdown", "value"),
    )

    def update_line_chart(source):
        if source == "fred":
            df = load_median_income_data()
            title = "Median Household Income Over Time (Dallas County)"
            y_axis = "Income"
        else:
            df = load_housing_index_data()
            title = "Housing Price Index Over Time"
            y_axis = "Index"

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df["Date"],
            y=df[y_axis],
            mode="lines+markers",
            marker_color="indianred",
            name=y_axis,
        ))
        fig.update_layout(
            title_text=title,
            xaxis_title="Date",
            yaxis_title=y_axis,
            height=400
        )
        return fig

    # Callback #2: Update the cost breakdown bar chart and table based on selected cateogry and year
    @app.callback(
        Output("bar-chart", "figure"),
        Output("cost-table", "data"),
        Input("category-dropdown", "value"),
    )
    def update_bar_and_table(category):
        df = load_cost_of_living_data()

        category_map = {
            "housing": [
                "Apartment (1 bedroom) in City Centre (USD)",
                "Apartment (1 bedroom) Outside of Centre (USD)",
                "Apartment (3 bedrooms) in City Centre (USD)",
                "Apartment (3 bedrooms) Outside of Centre (USD)",
                "Price per Square Meter to Buy Apartment in City Centre (USD)",
                "Price per Square Meter to Buy Apartment Outside of Centre (USD)",
                "Mortgage Interest Rate in Percentages (%), Yearly, for 20 Years Fixed-Rate"
            ],
            "childcare": [
                "Preschool (or Kindergarten), Full Day, Private, Monthly for 1 Child (USD)",
                "International Primary School, Yearly for 1 Child (USD)"
            ],
            "groceries": [
                "Milk (regular), (1 liter) (USD)",
                "Loaf of Fresh White Bread (500g) (USD)",
                "Rice (white), (1kg) (USD)",
                "Eggs (regular) (12) (USD)",
                "Local Cheese (1kg) (USD)",
                "Chicken Fillets (1kg) (USD)",
                "Beef Round (1kg) (or Equivalent Back Leg Red Meat) (USD)",
                "Apples (1kg) (USD)",
                "Banana (1kg) (USD)",
                "Oranges (1kg) (USD)",
                "Tomato (1kg) (USD)",
                "Potato (1kg) (USD)",
                "Onion (1kg) (USD)",
                "Lettuce (1 head) (USD)",
                "Water (1.5 liter bottle, at the market) (USD)",
                "Bottle of Wine (Mid-Range, at the market) (USD)",
                "Domestic Beer (0.5 liter bottle, at the market) (USD)",
                "Imported Beer (0.33 liter bottle, at the market) (USD)"
            ],
            "dining": [
                "Meal, Inexpensive Restaurant (USD)",
                "Meal for 2 People, Mid-range Restaurant, Three-course (USD)",
                "McMeal at McDonalds (or Equivalent Combo Meal) (USD)",
                "Domestic Beer (0.5 liter draught, in restaurants) (USD)",
                "Imported Beer (0.33 liter bottle, in restaurants) (USD)",
                "Cappuccino (regular, in restaurants) (USD)",
                "Coke/Pepsi (0.33 liter bottle, in restaurants) (USD)",
                "Water (0.33 liter bottle, in restaurants) (USD)"
            ],
            "utilities": [
                "Basic (Electricity, Heating, Cooling, Water, Garbage) for 85m2 Apartment (USD)",
                "Internet (60 Mbps or More, Unlimited Data, Cable/ADSL) (USD)",
                "1 min. of Prepaid Mobile Tariff Local (No Discounts or Plans) (USD)"
            ],
            "transportation": [
                "One-way Ticket (Local Transport) (USD)",
                "Monthly Pass (Regular Price) (USD)",
                "Taxi Start (Normal Tariff) (USD)",
                "Taxi 1km (Normal Tariff) (USD)",
                "Taxi 1hour Waiting (Normal Tariff) (USD)",
                "Gasoline (1 liter) (USD)",
                "Volkswagen Golf 1.4 90 KW Trendline (Or Equivalent New Car) (USD)",
                "Toyota Corolla Sedan 1.6l 97kW Comfort (Or Equivalent New Car) (USD)"
            ],
            "lifestyle": [
                "Fitness Club, Monthly Fee for 1 Adult (USD)",
                "Tennis Court Rent (1 Hour on Weekend) (USD)",
                "Cinema, International Release, 1 Seat (USD)",
                "1 Pair of Jeans (Levis 501 Or Similar) (USD)",
                "1 Summer Dress in a Chain Store (Zara, H&M, …) (USD)",
                "1 Pair of Nike Running Shoes (Mid-Range) (USD)",
                "1 Pair of Men Leather Business Shoes (USD)"
            ],
            "income": [
                "Average Monthly Net Salary (After Tax) (USD)"
            ]
        }

        cols = category_map.get(category, [])
        selected = df[cols].iloc[0]

        # format
        table_data = [{"Category": col, "Cost": selected[col]} for col in selected.index]
        return make_bar_chart(list(selected.index), list(selected.values)), table_data
