# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 11:52:48 2023

@authors: DavidBL

Topic: Conclusions
"""

import dash
from dash import dcc, html

# Dash register

dash.register_page(
    __name__,
    path = "/conclusion",  # represents the url text, / is for home(1st page)
    name = "Conclusions",  # name of page, commonly used as name of link
    title = "Conclusion")  # represents the title of browser's tab

# Layout

layout = html.Div(
    [html.Img(
        src="assets/logo_schriftzug.jpg", # Official JGU logo
        style = {"position": "fixed",
                "bottom": "20px",
                "right": "20px",
                "width": "300px"}),
        
        dcc.Markdown("# Conclusions:"),  # Title
        html.Br(),  # Add a line break
        html.P("Answering the RQ:", style = {"font-weight": "bold", "color": "darkblue"}),
        html.Div([
            html.P("Further econometric analysis needed"),
            html.P("Visualizations alone yield mixed results due to the diverse range of countries in the datasets"),
            html.P("Government size, effectiveness, and institutions play a major role in achieving economic growth through proper utilization of public spending")]),
        html.Br(),
        html.P("On the approach:", style = {"font-weight": "bold", "color": "darkblue"}),
        html.Div([
            html.P("Using a multipage web app with Dash by Plotly provided a high level of interactivity in the visualizations"),
            html.P("Which is very useful for the storytelling process, data visualization greatly benefits from")]),
        html.Br(),
        html.P("OVERALL:", style = {"font-weight": "bold", "color": "darkblue"}),
        html.Div([
            html.P("Econometric analysis combined with the hyper-interactive capabilities of Dash can be a major tool for future academic research"),
            html.P("Leveraging the capabilities of Python, a general-purpose software, yields results that other statistically focused options cannot match")])])
        