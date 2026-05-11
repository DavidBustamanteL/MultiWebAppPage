# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 18:07:16 2023

@authors: DavidBL

Topic: Health
"""

import dash
from dash import dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import pycountry
import pycountry_convert as pc


dash.register_page(
    __name__,
    path = "/healthcare",
    name = "Public Healthcare Spending",
    title = "Healthcare")


# Importing the data (Our World in Data)

df_raw = pd.read_csv("public-health-expenditure-share-GDP-OWID.csv")
df = df_raw.copy()

# Some cleaning

df.rename(
    columns = {"Entity":"Country",
    "Code": "ISO3",
    "public_health_expenditure_pc_gdp": "HealthExpend"},
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
    "South Korea": "KR"}

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

# Figure

fig = px.line(
    df,
    x = "Year",
    y = "HealthExpend",
    color = "Continent",
    color_discrete_map = color_map,
    line_group = "Country",
    hover_name = "Country",
    line_shape = "spline",
    render_mode = "svg",
    labels = {
        "HealthExpend": "% of GDP",
        "Year": "Years"
    }
)

fig.update_layout(
    height = 555,
    width = 1111,
    autosize = False,
    margin = dict(l = 20, r = 20, t = 40, b = 80)
    #plot_bgcolor = "white"
)


# Layout

layout = html.Div([
    html.H1(
        "Public Healthcare Expenditure as Share of GDP",
        style = {"textAlign": "left"}),
    dcc.Markdown(
        """
        Historical data for Healthcare expenditure in the public sector.
        """,
        style = {
            "textAlign": "left",
            "fontSize": "18px"}),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Div(
                dcc.Graph(
                    id = "lines",
                    figure = fig,
                    style = {
                        "height": "700px",
                        "width": "100%"},
                    config = {
                        "responsive": False,
                        "displayModeBar": True),
                style = {
                    "height": "700px",
                    "maxHeight": "700px",
                    "overflow": "hidden",
                    "width": "100%"}),
            html.Div(
                [
                    "Source: ",
                    html.A(
                        "Our World in Data",
                        href = "https://ourworldindata.org/financing-healthcare",
                        target = "_blank")],
                style = {
                    "textAlign": "left",
                    "fontSize": "14px",
                    "marginTop": "5px",
                    "color": "darkblue"}
            )

        ])
    ])

])
