"""
Functions to create charts (line and bar) for dashboard visualizations.
"""

import plotly.graph_objects as go
from packaging import markers


def make_line_chart(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["Date"],
        y=df["Index"],
        mode="lines+markers",
        name="Housing Price Index",
    line=dict(color="royalblue"),
        ))
    fig.update_layout(
        title="Housing Price Index Over Time",
        xaxis_title="Date",
        yaxis_title="Index Value",
        height=400
    )
    return fig

def make_bar_chart(categories, values, title="Cost Breakdown"):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=categories,
        y=values,
        marker_color="indianred",
        text=[f"${v:,.2f}" for v in values],
        textposition="auto",
    ))
    fig.update_layout(title=title, xaxis_title="Category", yaxis_title="Cost (USD)")
    return fig