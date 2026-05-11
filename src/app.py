# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 10:26:37 2023

@authors: DavidBL

Topic: Multipage webapp
"""

# Packages
import dash
from dash import html
import dash_bootstrap_components as dbc
import webbrowser
import os

# Packages to have installed for the entire project
"""
pip install numpy
pip install pandas
pip install dash
pip install dash_bootstrap_components
pip install plotly
pip install pycountry
pip install pycountry_convert
"""

# WD if needed
#os.chdir("")

# App

# For Spyder
"""
app = dash.Dash(__name__, use_pages = True,
                external_stylesheets = [dbc.themes.SPACELAB])
"""

# Other Editors
app = dash.Dash(
    "app",
    use_pages = True,
    external_stylesheets = [dbc.themes.SPACELAB]
)

# Menu
sidebar = dbc.Nav([dbc.NavLink([
    html.Div(page["name"], className = "ms-2")],
    href = page["path"], active = "exact")
    for page in dash.page_registry.values()],
    vertical = True,
    pills = True,
    className = "bg-light")

# Layout

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div(
            "Economic Growth and Government Spending",
            style = {
                "fontSize": 50,
                "textAlign": "center",
                "color": "darkblue"
            }
        ))
    ]),

    html.Hr(),

    dbc.Row([
        dbc.Col(
            [sidebar],
            xs = 4, sm = 4, md = 2, lg = 2, xl = 2, xxl = 2
        ),

        dbc.Col(
            html.Div(
                dash.page_container,
                style = {
                    "height": "auto",
                    "minHeight": "0",
                    "overflow": "hidden"
                }
            ),
            xs = 8, sm = 8, md = 10, lg = 10, xl = 10, xxl = 10
        )
    ])
], fluid = True)


if __name__ == "__main__":
    port = 8050  # Predefined port
    app.run(jupyter_mode = "external", debug = False, port = port)
    
    url = f"http://127.0.0.1:{port}/"
    
    # Open URL in default web browser
    webbrowser.open(url)

