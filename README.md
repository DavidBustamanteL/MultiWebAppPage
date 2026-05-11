# Economic Growth and Government Spending  
### A Multipage Dash Web App for Interactive Data Visualization

An interactive multipage web application built with Python, Dash, and Plotly to explore the relationship between economic growth and social spending across countries.

The project focuses on:

- Data cleaning
- Interactive storytelling
- Dashboard development
- Data visualization with Plotly
- Web applications in Python

This repository is especially useful for students learning data science, data manipulation, and interactive visualization for the first time.

---

# Project Overview

This project was developed as part of an academic course on computational statistics and data analysis in Python.

The application explores questions such as:

- Do countries increase social spending as they become wealthier?
- How does GDP per capita relate to government expenditure?
- How do education and healthcare spending vary across continents?

Instead of static graphs, the project uses a **multipage Dash application** that allows users to interact with the data through:

- Sliders
- Dropdown menus
- Animations
- Hover effects
- Interactive legends
- Dynamic callbacks

The goal is to demonstrate how interactive visualizations improve storytelling and exploratory data analysis.

---

# Features

## Interactive Dash Web App

- Multipage layout
- Sidebar navigation menu
- Interactive charts and animations
- Dynamic updates using callbacks
- Responsive visual storytelling

---

## Visualizations Included

- Animated choropleth world map
- Bubble chart with population scaling
- Histograms with dropdown filtering
- Interactive noodle graph (time series)

---

## Data Processing

- Data cleaning with Pandas
- ISO country code handling
- Country filtering and standardization
- Missing value treatment
- Dataset merging and preparation

---

# Technologies Used

## Python Libraries

- `dash`
- `plotly`
- `pandas`
- `dash_bootstrap_components`
- `pycountry`
- `pycountry_convert`

---

## Concepts Covered

- Data cleaning
- Data wrangling
- Interactive visualization
- Web app structure
- Dashboard development
- Storytelling with data

---

# Project Structure

The project follows the recommended Dash multipage folder structure.

```text
project-folder/
│
├── src/
│   ├── app.py
│   │
│   ├── pages/
│   │   ├── page1.py
│   │   ├── page2.py
│   │   ├── page3.py
│   │   └── ...
│   │
│   ├── assets/
│       ├── gdp.csv
│       ├── education.csv
│       ├── healthcare.csv
│       ├── government.csv
│       └── any images added to the web page
│
├── README.md
└── .gitignore
```

# Data Sources

The datasets were obtained from **Our World in Data**, allowing consistent and reliable data collection across multiple indicators.

Datasets include:

- GDP per capita
- Government spending
- Education spending
- Healthcare spending
- Population statistics

Useful sources:

- https://ourworldindata.org/
- https://ourworldindata.org/economic-growth
- https://ourworldindata.org/government-spending
- https://ourworldindata.org/financing-education
- https://ourworldindata.org/financing-healthcare

---

# Visualizations Explained

## 1. GDP per Capita Growth Map

An animated choropleth map displaying annual percentage changes in GDP per capita from 1961–2020.

Users can explore yearly changes using an interactive slider.

### Skills Demonstrated

- Geospatial visualization
- Animation with Plotly
- Slider interactivity
- Color scaling
- Hover information

---

## 2. Government Spending vs GDP

A bubble chart comparing GDP per capita and government spending, where bubble size represents population.

Facets separate continents for easier comparison.

### Skills Demonstrated

- Bubble charts
- Faceting
- Log transformations
- Interactive filtering
- Population scaling

---

## 3. Education Spending Dashboard

Histogram visualizations showing education spending as a percentage of government expenditure.

Dropdown menus allow continent-specific filtering.

### Skills Demonstrated

- Dropdown callbacks
- Histograms
- Aggregation
- Interactive filtering
- Dynamic updates

---

## 4. Healthcare Spending Trends

A noodle graph visualizing public healthcare spending over time across countries and continents.

### Skills Demonstrated

- Time-series visualization
- Multi-line plots
- Interactive legends
- Trend analysis

---

# Data Cleaning Process

The project includes several important data preparation steps using Pandas.

## Cleaning Tasks

- Renaming columns
- Sorting years chronologically
- Removing duplicates
- Handling missing ISO country codes
- Filtering continent-level aggregates
- Preparing datasets for merging and visualization

This repository is especially useful for beginners learning real-world data preparation workflows.

---

# Learning Goals

This repository is ideal for students learning:

- Python for data science
- Interactive dashboards
- Data visualization
- Data storytelling
- Dash and Plotly
- Pandas data manipulation
- Web app organization
- GitHub project structure

---

# Why This Project Matters

Many beginner projects focus only on static plots or simple scripts.

This repository demonstrates how to combine:

- Data cleaning
- Interactive visualization
- Web development
- Storytelling
- Reproducible project structure

into a single coherent application.

---

# Future Improvements

Possible extensions include:

- Adding econometric analysis
- Deploying the app online
- Adding user-uploaded datasets
- Including machine learning models
- Improving responsiveness for mobile devices
- Adding downloadable reports
