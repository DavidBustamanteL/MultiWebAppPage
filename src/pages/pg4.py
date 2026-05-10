# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 18:07:16 2023

@authors: DavidBL

Topic: Education
"""

import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import pycountry
import pycountry_convert as pc


# Dash register

dash.register_page(
    __name__,
    path = "/edu",
    name = "Education Spending",
    title = "Education")


# Importing the data (Our World in Data)

df = pd.read_csv("share-of-education-in-government-expenditure.csv")

# Cleaning

df.rename(
    columns = {
        "Entity":"Country",
        "Code": "ISO3",
        "Government expenditure on education, total (% of government expenditure)": "EduExpend"},
        inplace = True)

# Getting the ISO2

def get_iso2(country_name):
    try:
        country = pycountry.countries.get(name = country_name)
        return country.alpha_2
    except AttributeError:
        return None

df["ISO2"] = df["Country"].apply(get_iso2)

manual_iso2 = {
    "British Virgin Islands": "VG",
    "Brunei": "BN",
    "Cape Verde": "CV",
    "Cote d'Ivoire": "CI",
    "Democratic Rep. of Congo": "CD",
    "East Timor": "TL",
    "Iran": "IR",
    "Laos": "LA",
    "Micronesia": "FM",
    "Moldova": "MD",
    "Palestine": "PS",
    "Russia": "RU",
    "Syria": "SY",
    "Tanzania": "TZ",
    "Vietnam": "VN"}

df.loc[df["Country"].isin(manual_iso2.keys()),
"ISO2"] = df["Country"].map(manual_iso2)

# dropping nan values for econ. groups, etc

df = df.dropna()
df = df.drop_duplicates(keep = "first")

# Getting the continents

def get_continent(iso2_code):
    try:
        continent_code = pc.country_alpha2_to_continent_code(iso2_code)
        continent_name = pc.convert_continent_code_to_continent_name(continent_code)
        return continent_name
    except KeyError:
        return None

df["Continent"] = df["ISO2"].apply(get_continent)


# Layout

color_map = {
    "Europe": "#66b3ff",         # Bright Blue
    "Asia": "#ffff00",           # Yellow
    "Africa": "#2ca02c",         # Green
    "Oceania": "#ff7f00",        # Orange
    "North America": "#9467bd",  # Purple
    "South America": "#ff0000"}  # Bright Red

layout = html.Div([
    html.H1(
        "Average Education Budget across the Globle",
        style = {"textAlign": "left"}
    ),

    dcc.Markdown(
        """
        Education Expenditure as % of Total Gov. Expenditure.  
        Averages are calculated from the available years in the dataset.
        """,
        style = {
            "textAlign": "left",
            "fontSize": "18px"
        }
    ),

    html.Br(),

    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                options = (
                    [{"label": "World", "value": "World"}] +
                    [{"label": continent, "value": continent}
                     for continent in df.Continent.unique()]
                ),
                id = "cont-choice",
                value = "World"
            )
        ],
        xs = 10, sm = 10, md = 8, lg = 4, xl = 4, xxl = 4)
    ]),

    dbc.Row([
        dbc.Col([

            html.Div(
                dcc.Graph(
                    id = "line-fig",
                    style = {
                        "height": "700px",
                        "width": "100%"
                    },
                    config = {
                        "responsive": False,
                        "displayModeBar": True
                    }
                ),
                style = {
                    "height": "700px",
                    "maxHeight": "700px",
                    "overflow": "hidden",
                    "width": "100%"
                }
            ),

            html.Div(
                [
                    "Source: ",
                    html.A(
                        "Our World in Data",
                        href = "https://ourworldindata.org/financing-education",
                        target = "_blank"
                    )
                ],
                style = {
                    "textAlign": "left",
                    "fontSize": "14px",
                    "marginTop": "5px",
                    "color": "darkblue"
                }
            )

        ],
        width = 12)
    ])

])

@callback(
    Output("line-fig", "figure"),
    Input("cont-choice", "value"))


def update_graph(value):
    if value == "World":
        fig = px.histogram(
            df, x = "Continent",
            y = "EduExpend", histfunc = "avg",
            color = "Continent",
            color_discrete_map = color_map)
        fig.update_layout(
            xaxis_title = None,
            yaxis_title = "% of Total Gov. Expenditure")
        fig.update_layout(plot_bgcolor = "white") 
        fig.update_xaxes(
            mirror = False,
            ticks = "outside",
            showline = False,
            linecolor = "lightgrey",
            gridcolor = "lightgrey")
        fig.update_yaxes(
            mirror = False,
            ticks = "outside",
            showline = False,
            linecolor = "lightgrey",
            gridcolor = "lightgrey")
    else:
        dff = df[df.Continent == value]
        fig = px.histogram(
            dff, x = "Country", y = "EduExpend", histfunc = "avg",
            color = "Continent", color_discrete_map = color_map)
        fig.update_layout(
            xaxis_title = "Countries",
            yaxis_title = "% of their Total Gov. Expenditure")
        fig.update_xaxes(
            mirror = False,
            ticks = "outside",
            showline = False,
            linecolor = "lightgrey",
            gridcolor = "lightgrey")
        fig.update_yaxes(
            mirror = False,
            ticks = "outside",
            showline = False,
            linecolor = "lightgrey",
            gridcolor = "lightgrey")
        if value == "Asia":
            fig.update_xaxes(tickangle = 270)
        if value == "Europe":
            fig.update_xaxes(tickangle = 270)
        if value == "Africa":
            fig.update_xaxes(tickangle = 270)
    fig.update_layout(
        height = 600,
        width = 1111,
        autosize = False,
        margin = dict(l = 20, r = 20, t = 40, b = 80),
        plot_bgcolor = "white"
    )

    return fig