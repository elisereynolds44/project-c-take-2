from webbrowser import register

from dash import Dash
import dash_bootstrap_components as dbc
from layout import layout
from callbacks import register_callbacks
from survival_callbacks import register_survival_callbacks

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.SUPERHERO],
)
app.title = "Dallas Cost of Living Dashboard"

register_callbacks(app)
register_survival_callbacks(app)
app.layout = layout

if __name__ == '__main__':
    app.run_server(debug=True)