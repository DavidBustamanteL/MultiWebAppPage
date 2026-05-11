# Economic Growth and Government Spending  
### A Multipage Dash Web App for Interactive Data Visualization

An interactive multipage web application built with Python, Dash, and Plotly to explore the relationship between economic growth and social spending across countries. The project focuses on **data cleaning, interactive storytelling, and visualization techniques** for students learning data science and web-based analytics. :contentReference[oaicite:0]{index=0}

---

# Project Overview

This project was developed as part of an academic course on computational statistics and data analysis in Python. The main goal is to demonstrate how interactive visualizations can improve storytelling and exploratory data analysis. :contentReference[oaicite:1]{index=1}

The application explores questions such as:

- Do countries increase social spending as they become wealthier?
- How does GDP per capita relate to government expenditure?
- How do education and healthcare spending vary across continents?

Instead of static graphs, the project uses a **multipage Dash application** that allows users to interact with the data through sliders, dropdown menus, animations, and hover effects. :contentReference[oaicite:2]{index=2}

---

# Features

## Interactive Dash Web App
- Multipage layout
- Sidebar navigation menu
- Interactive charts and animations
- Dynamic updates using callbacks
- Responsive visual storytelling

## Visualizations Included
- Animated choropleth world map
- Bubble chart with population scaling
- Histograms with dropdown filtering
- Interactive noodle graph (time series)

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

## Concepts Covered
- Data cleaning
- Data wrangling
- Interactive visualization
- Web app structure
- Dashboard development
- Storytelling with data

---

# Project Structure

The project follows the recommended Dash multipage folder structure described in the paper. :contentReference[oaicite:3]{index=3}

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
│       └── government.csv
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name
```

---

## 2. Create a Virtual Environment (Recommended)

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Required Packages

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install dash plotly pandas dash-bootstrap-components pycountry pycountry-convert
```

---

# Running the App

Navigate to the `src` folder and run:

```bash
python app.py
```

Dash will start a local server. Open the browser link shown in the terminal, usually:

```text
http://127.0.0.1:8050/
```

---

# Data Sources

The datasets were obtained from **Our World in Data**, allowing consistent and reliable data collection across multiple indicators. :contentReference[oaicite:4]{index=4}

Datasets include:
- GDP per capita
- Government spending
- Education spending
- Healthcare spending
- Population statistics

Sources:
- https://ourworldindata.org/
- https://ourworldindata.org/economic-growth
- https://ourworldindata.org/government-spending
- https://ourworldindata.org/financing-education
- https://ourworldindata.org/financing-healthcare

---

# Visualizations Explained

## 1. GDP per Capita Growth Map

An animated choropleth map displaying annual percentage changes in GDP per capita from 1961–2020. Users can explore yearly changes using an interactive slider. :contentReference[oaicite:5]{index=5}

### Skills Demonstrated
- Geospatial visualization
- Animation with Plotly
- Slider interactivity
- Color scaling

---

## 2. Government Spending vs GDP

A bubble chart comparing GDP per capita and government spending, where bubble size represents population. Facets separate continents for easier comparison. :contentReference[oaicite:6]{index=6}

### Skills Demonstrated
- Bubble charts
- Faceting
- Log transformations
- Interactive filtering

---

## 3. Education Spending Dashboard

Histogram visualizations showing education spending as a percentage of government expenditure. Dropdown menus allow continent-specific filtering. :contentReference[oaicite:7]{index=7}

### Skills Demonstrated
- Dropdown callbacks
- Histograms
- Aggregation
- Interactive filtering

---

## 4. Healthcare Spending Trends

A noodle graph visualizing public healthcare spending over time across countries and continents. :contentReference[oaicite:8]{index=8}

### Skills Demonstrated
- Time-series visualization
- Multi-line plots
- Interactive legends
- Trend analysis

---

# Data Cleaning Process

The project includes several important data preparation steps using Pandas. :contentReference[oaicite:9]{index=9}

## Cleaning Tasks
- Renaming columns
- Sorting years chronologically
- Removing duplicates
- Handling missing ISO country codes
- Filtering out continent-level aggregates
- Preparing datasets for merging and visualization

This makes the repository especially useful for beginners learning **real-world data preparation**.

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

Many beginner projects focus only on static plots or basic scripts. This repository demonstrates how to combine:

- Data cleaning
- Interactive visualization
- Web development
- Storytelling
- Reproducible project structure

into a single coherent application. :contentReference[oaicite:10]{index=10}

---

# Future Improvements

Possible extensions include:

- Adding econometric analysis
- Deploying the app online
- Adding user-uploaded datasets
- Including machine learning models
- Improving responsiveness for mobile devices
- Adding downloadable reports




Please provide proper attribution when appropriate.
````
