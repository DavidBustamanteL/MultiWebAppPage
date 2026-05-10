# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 14:11:44 2023

@authors: DavidBL

Topic: Annual %-Change Econ. Growth
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
    path = "/econgrw",
    name = "Economic Growth",
    title = "Economic Growth")


# importing the data (Our World in Data)

df_raw = pd.read_csv("gdp-per-capita-growth.csv")
df = df_raw.copy()

# Cleaning

df.rename(
    columns = {"Entity":"Country",
    "Code": "ISO3",
    "GDP per capita growth (annual %)": "GDPpcAn%"},
    inplace = True)

df["Country"] = df["Country"].replace(
    "United States Virgin Islands",
    "British Virgin Islands")

year_order = sorted(df["Year"].unique()) # for problems with years' order

# Getting the ISO2

def get_iso2(country_name):
    try:
        country = pycountry.countries.get(name = country_name)
        return country.alpha_2
    except AttributeError:
        return None

df["ISO2"] = df["Country"].apply(get_iso2)

manual_iso2 = {
    "Bolivia": "BO",
    "Brunei": "BN",
    "Cape Verde": "CV",
    "Cote d'Ivoire": "CI",
    "Curacao": "CW",
    "Democratic Rep of Congo": "CD",
    "East Timor": "TL",
    "Iran": "IR",
    "Kosovo": "XK",
    "Laos": "LA",
    "Micronesia": "FM",
    "Moldova": "MD",
    "Palestine": "PS",
    "Russia": "RU",
    "South Korea": "KR",
    "Syria": "SY",
    "Tanzania": "TZ",
    "British Virgin Islands": "VG",
    "Venezuela": "VE",
    "Vietnam": "VN"}

df.loc[df["Country"].isin(manual_iso2.keys()),
"ISO2"] = df["Country"].map(manual_iso2)

# dropping nan values for econ. groups, etc, and duplicate rows(if needed)

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

layout = html.Div([
    html.H1("Annual Percentage Change in GDP Per Capita betw. 1961 and 2020",
            style = {"textAlign": "left"}),

    dcc.Markdown(
        """
        The data was collected by aggregating information using currency exchange rates.            
        No adjustments for price differences between countries were considered.
        """,
        style = {"textAlign": "left", "fontSize": "18px"}),

    dbc.Row([
        dbc.Col([

            html.Div(
                dcc.Graph(
                    id = "gdp-fig",
                    style = {
                        "width": "100%",
                        "height": "700px"
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

            html.Div(["Source: ",
                html.A(
                    "Our World in Data",
                    href = "https://ourworldindata.org/economic-growth",
                    target = "_blank")],
                style = {
                    "textAlign": "left",
                    "fontSize": "14px",
                    "marginTop": "5px",
                    "color": "darkblue"
                })
        ])
    ])
])

@callback(
    Output("gdp-fig", "figure"),
    Input("gdp-fig", "id"),
    prevent_initial_call = False)


def updated_graph(trigger):
    min_value = -5
    max_value = 5
    year_order = sorted(df["Year"].unique())  # for problems with years' order

    fig = px.choropleth(
        df,
        locations = "ISO3",
        geojson = None,
        color = "GDPpcAn%",
        range_color = [min_value, max_value],
        hover_name = "Country",
        hover_data = ["GDPpcAn%"],
        labels = {"GDPpcAn%":"Annual<br>% Change"},
        color_continuous_scale = "RdBu",
        color_continuous_midpoint = 0,
        animation_frame = "Year",
        category_orders = {"Year": year_order})  # for problems with years' order

    fig.update_layout(
        height = 600,
        width = 1111,
        autosize = False,
        margin=dict(l=0, r=0, t=30, b=0),
        geo = dict(
            landcolor = "lightgray",
            showland = True,
            showcountries = True,
            countrycolor = "gray",
            countrywidth = 0.5,
            showframe = False,
            showcoastlines = False,
            projection_type = "kavrayskiy7"))
    
    return fig







