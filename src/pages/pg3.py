# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 22:09:46 2023

@authors: DavidBL

Topic: Gov. Expenditure vs GDP 
"""

import dash
from dash import dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import pycountry
import pycountry_convert as pc


# Dash register

dash.register_page(
    __name__,
    path="/gobspendvsinc",
    name="Gov. Expenditure vs GDP",
    title="Expenditure vs GDP"
)


# Importing the data

df_raw = pd.read_csv("country-level-government-spending-vs-income.csv")
df = df_raw.copy()


# Cleaning

df = df.drop(df.index[0])

df.rename(
    columns={
        "Entity": "Country",
        "Code": "ISO3",
        "Government Expenditure (IMF based on Mauro et al. (2015))": "GovExpend",
        "GDP per capita, PPP (constant 2017 international $)": "GDPpc",
        "Population (historical estimates)": "Population"
    },
    inplace=True
)

del df["Continent"]

year_order = sorted(df["Year"].unique())


# Getting ISO2

def get_iso2(country_name):
    try:
        country = pycountry.countries.get(name=country_name)
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
    "Vietnam": "VN"
}

df.loc[df["Country"].isin(manual_iso2.keys()), "ISO2"] = df["Country"].map(manual_iso2)


# Dropping missing values and duplicates

df = df.dropna()
df = df.drop_duplicates(keep="first")


# Getting continents

def get_continent(iso2_code):
    try:
        continent_code = pc.country_alpha2_to_continent_code(iso2_code)
        continent_name = pc.convert_continent_code_to_continent_name(continent_code)
        return continent_name
    except KeyError:
        return None


df["Continent"] = df["ISO2"].apply(get_continent)


# Colors

color_map = {
    "Europe": "#66b3ff",
    "Asia": "#ffff00",
    "Africa": "#2ca02c",
    "Oceania": "#ff7f00",
    "North America": "#9467bd",
    "South America": "#ff0000"
}


# Figure

fig = px.scatter(
    df,
    x = "GDPpc",
    y = "GovExpend",
    animation_frame = "Year",
    category_orders = {"Year": year_order},
    animation_group = "Country",
    size = "Population",
    color = "Continent",
    hover_name = "Country",
    facet_col = "Continent",
    color_discrete_map = color_map,
    log_x = True,
    size_max = 45,
    range_x = [100, 200000],
    range_y = [-10, 100],
    labels = {
        "GovExpend": "Government Expenditure in %",
        "GDPpc": "GDP per capita"
    }
)

fig.update_layout(
    height = 600,
    width = 1111,
    autosize = False,
    transition_duration = 800,
    margin = dict(l=20, r=20, t=40, b=40)
)


# Layout

layout = html.Div([

    html.H1(
        "Government Expenditure vs GDP per capita 1990 - 2011",
        style={"textAlign": "left"}
    ),

    dcc.Markdown(
        """
        Governments' Expenditure Data based on Mauro et al. (2015).          
        GDP per capita in PPP (constant 2017 international USD) logarithmically transformed.
        """,
        style={
            "textAlign": "left",
            "fontSize": "18px"
        }
    ),

    html.Br(),

    dbc.Row([
        dbc.Col([

            html.Div(
                dcc.Graph(
                    id="graph",
                    figure=fig,
                    style={
                        "height": "700px",
                        "width": "100%"
                    },
                    config={
                        "responsive": False,
                        "displayModeBar": True
                    }
                ),
                style={
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
                        href="https://ourworldindata.org/government-spending",
                        target="_blank"
                    )
                ],
                style={
                    "textAlign": "left",
                    "fontSize": "14px",
                    "marginTop": "5px",
                    "color": "darkblue"
                }
            )

        ])
    ])
])