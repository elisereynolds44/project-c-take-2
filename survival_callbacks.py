"""
Survival Tab Callbacks
"""

from dash import Input, Output, State, callback_context
import pandas as pd
from data_loader import load_median_income_data, load_cost_of_living_data


def register_survival_callbacks(app):
    # 1st call back to display the latest median income at the top of the tab
    @app.callback(
        Output("survival-income-display", "children"),
        Input("tabs", "active_tab"),
    )
    def display_latest_income(active_tab):
        if active_tab != "survival_tab":
            return ""
        df = load_median_income_data()
        latest = df.sort_values("Date").iloc[-1]
        year = latest["Date"].year
        income = latest["Income"]
        return f"Using {year} median household income: ${income:,.0f}"

    # 2nd callback to calc result
    @app.callback(
        Output("groceries-choice", "value"),
        Output("dining-choice", "value"),
        Output("transportation-choice", "value"),
        Output("childcare-choice", "value"),
        Output("housing-choice", "value"),
        Output("survival-result", "children"),
        Input("calculate-button", "n_clicks"),
        Input("reset-again", "n_clicks"),
        State("groceries-choice", "value"),
        State("dining-choice", "value"),
        State("transportation-choice", "value"),
        State("childcare-choice", "value"),
        State("housing-choice", "value"),
        prevent_initial_call=True,
    )

    def survival_game(calc_clicks, reset_clicks, groceries, dining, transport, childcare, housing):
        ctx = callback_context
        if not ctx.triggered:
            return groceries, dining, transport, childcare, housing

        triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]

        if triggered_id == "reset-button":
            return "basic", "cheap", "transit", "none", "shared", ""


        # load income
        income_df = load_median_income_data()
        cost_df = load_cost_of_living_data()
        latest_income = income_df.sort_values("Date").iloc[-1]["Income"] / 12 # monthly
        cost_row = cost_df.iloc[0] # assume single row for Dallas


        # costs by categories

        # ----- Groceries -------

        groceries_map = {

            "basic": [
                "Milk (regular), (1 liter) (USD)",
                "Eggs (regular) (12) (USD)",
                "Loaf of Fresh White Bread (500g) (USD)",
                "Rice (white), (1kg) (USD)"
            ],

            "protein": [
                "Chicken Fillets (1kg) (USD)",
                "Local Cheese (1kg) (USD)",
                "Beef Round (1kg) (or Equivalent Back Leg Red Meat) (USD)"
            ],

            "full": [
                "Milk (regular), (1 liter) (USD)",
                "Eggs (regular) (12) (USD)",
                "Loaf of Fresh White Bread (500g) (USD)",
                "Rice (white), (1kg) (USD)",
                "Chicken Fillets (1kg) (USD)",
                "Local Cheese (1kg) (USD)",
                "Beef Round (1kg) (or Equivalent Back Leg Red Meat) (USD)",
                "Apples (1kg) (USD)",
                "Banana (1kg) (USD)",
                "Oranges (1kg) (USD)",
                "Tomato (1kg) (USD)",
                "Potato (1kg) (USD)",
                "Onion (1kg) (USD)",
                "Lettuce (1 head) (USD)"
            ]
        }

        groceries_total = sum(cost_row[col] for col in groceries_map[groceries])

        # ----- Dining -------
        dining_map = {
            "cheap": [
                ("McMeal at McDonalds (or Equivalent Combo Meal) (USD)", 1)
            ],
            "moderate": [
                ("McMeal at McDonalds (or Equivalent Combo Meal) (USD)", 2),
                ("Cappuccino (regular, in restaurants) (USD)", 4),
                ("Domestic Beer (0.5 liter draught, in restaurants) (USD)", 1)
            ],
            "expensive": [
                ("Meal for 2 People, Mid-range Restaurant, Three-course (USD)", 1),
                ("Cappuccino (regular, in restaurants) (USD)", 4),
                ("Imported Beer (0.33 liter bottle, in restaurants) (USD)", 2)
            ]
        }

        dining_total = sum(cost_row[item] * qty for item, qty in dining_map[dining])

        # ----- Transportation -------

        if transport == "transit":
            transport_total = cost_row["Monthly Pass (Regular Price) (USD)"]
        elif transport == "gas":
            fuel_price = cost_row["Gasoline (1 liter) (USD)"]
            estimated_liters = 50 # approx 1 tank per week
            transport_total = fuel_price * estimated_liters
        elif transport == "car":
            fuel = cost_row["Gasoline (1 liter) (USD)"] * 50
            insurance = 100 # estimated monthly insurance
            maintenance = 50 # basic maintenance avg
            transport_total = fuel + insurance + maintenance
        else:
            transport_total = 0

        # ----- Childcare -------
        if childcare == "none":
            childcare_total = 0
        elif childcare == "home":
            childcare_total = 783 # (9400 / 12 from dataset)
        elif childcare == "center":
            childcare_total = 866 # (10380 / 12 from dataset)
        else:
            childcare_total = 0

        # ----- Housing -------
        if housing == "shared":
            housing_total = cost_row["Apartment (1 bedroom) Outside of Centre (USD)"] * 0.5
        elif housing == "outside":
            housing_total = cost_row["Apartment (1 bedroom) Outside of Centre (USD)"]
        elif housing == "center":
            housing_total = cost_row["Apartment (1 bedroom) in City Centre (USD)"]
        else:
            housing_total = 0

        # total and result
        total_expenses = groceries_total + dining_total + transport_total + childcare_total + housing_total
        remaining = latest_income - total_expenses

        if remaining < 0:
            msg = f"You're short by ${abs(remaining):,.2f} - you may need to rethink your budget! 💸"
        elif remaining < 300:
            msg = f"You barely make it with only ${remaining:,.2f} left over. 🫣"
        else:
            msg= f"Nice! You have ${remaining:,.2f} left after expenses. 💪"

        breakdown = f"""
        **Monthly Income**: ${latest_income:,.2f}
        
        - Groceries: ${groceries_total:,.2f}
        - Dining: ${dining_total:,.2f}
        - Transport: ${transport_total:,.2f}
        - Childcare: ${childcare_total:,.2f}
        - Housing: ${housing_total:,.2f}
        
        **Total expenses**: ${total_expenses:,.2f}
        **{msg}**
        """

        return groceries, dining, transport, childcare, housing, breakdown




