# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 12:59:52 2023

@authors: DavidBL, TatianaT, YevheniiaO, CesarV

Topic: QR-Code
"""

import dash
from dash import html

# Dash register

dash.register_page(
    __name__,
    path = "/sharing-is-caring",  # represents the url text, / is for home(1st page)
    name = "Sharing is Caring",  # name of page, commonly used as name of link
    title = "QR-Code")  # represents the title of browser's tab

# Layout

layout = html.Div(
    children = ["Thank you!",
                html.Div(style = {
                    "display": "flex",
                    "flexDirection": "column",
                    "alignItems": "center",
                    "justifyContent": "center",
                    "height": "70vh"},
    children = [html.Img(
        src = "assets/qr-code.png",  # Our QR-code
        style = {"width": "500px"}),
                html.Div(
                    "QR-Code valid until the end of today at 11:59pm",
                    style = {"textAlign": "left",
                            "fontSize": "14px",
                            "marginTop": "5px",
                            "color": "darkblue"})])],
    style = {
        "textAlign": "center",
        "fontSize": "32px",
        "marginTop": "20px",
        "color": "darkblue"})




