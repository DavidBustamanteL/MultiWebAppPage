# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 14:11:44 2023

@authors: DavidBL

Topic: Cover page
"""

import dash
from dash import dcc, html


# Dash register

dash.register_page(
    __name__,
    path = "/",  # represents the url text, / alone is for home(1st page)
    name = "HOME",  # name of page, commonly used as name of link
    title = "Home")  # represents the title of browser's tab

# The layout

layout = html.Div(
    [html.Img(
        src = "assets/logo_schriftzug.jpg", # Official JGU logo
        style = {"position": "fixed",
                "bottom": "20px",
                "right": "20px",
                "width": "300px"}),
        
        dcc.Markdown("# Introduction to Computational Statistics and Data Analysis in Python"),  # Title
        html.Br(),  # Add a line break
        html.P("Topic:",
        style = {
            "font-weight": "bold",
            "color": "darkblue"}),
        html.Div([
            html.P(
                "Data Management & Visualization")]),
        html.Br(),
        html.P("Approach:",
        style = {"font-weight": "bold",
                "color": "darkblue"}),
        html.Div([
            html.P(
                "Application using a Multipage Web App with Dash by Plotly")]),
        html.Br(),
        html.P("Research Question:",
        style = {"font-weight": "bold",
                "color": "darkblue"}),
        html.Div([
            html.P("As countries grow, does so their social expenditure?")]),
        html.Br(),
        html.Br(),
        html.Br(),
        html.P("Group members:",
        style = {"font-weight": "bold",
                "color": "darkblue"}),
        html.Div([
            html.P("Bustamante, David - Mat-nr. XXX")])])
