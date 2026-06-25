import streamlit as st
import pandas as pd

# Page Setup
st.set_page_config(
    page_title="Ferry Capacity Analytics",
    layout="wide"
)

st.title("🚢 Ferry Capacity Utilization Analytics")

# Load Data
df = pd.read_csv(
    "data/Toronto Island Ferry Tickets.csv"
)

# Convert Timestamp
df["Timestamp"] = pd.to_datetime(
    df["Timestamp"]
)

# Sidebar Filter
st.sidebar.header("Filters")

selected_year = st.sidebar.selectbox(
    "Select Year",
    sorted(df["Timestamp"].dt.year.unique())
)

# Apply Year Filter
df = df[
    df["Timestamp"].dt.year == selected_year
]

# Create Total Activity Load
df["Total Activity Load"] = (
    df["Sales Count"] +
    df["Redemption Count"]
)

# KPI Calculations
avg_load = round(
    df["Total Activity Load"].mean(),
    2
)

max_load = df["Total Activity Load"].max()

capacity_ratio = round(
    (avg_load / max_load) * 100,
    2
)

congestion = round(
    (
        df["Total Activity Load"]
        >
        df["Total Activity Load"].quantile(0.80)
    ).mean() * 100,
    2
)

idle = round(
    (
        df["Total Activity Load"]
        <
        df["Total Activity Load"].quantile(0.20)
    ).mean() * 100,
    2
)

# KPI Cards
c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Capacity Utilization %",
    capacity_ratio
)

c2.metric(
    "Congestion %",
    congestion
)

c3.metric(
    "Idle Capacity %",
    idle
)

c4.metric(
    "Average Activity",
    avg_load
)

st.divider()
c4.metric(
    "Average Activity",
    avg_load
)

st.divider()

# Monthly Analysis
df["Month"] = df["Timestamp"].dt.month

monthly = (
    df.groupby("Month")["Total Activity Load"]
    .mean()
)

st.subheader(
    "Monthly Activity Trend"
)

st.bar_chart(monthly)

# Season Analysis

def get_season(month):
    if month in [6, 7, 8]:
        return "Summer"
    elif month in [12, 1, 2]:
        return "Winter"
    else:
        return "Other"

df["Season"] = df["Month"].apply(get_season)
# Season Filter

selected_season = st.sidebar.selectbox(
    "Select Season",
    ["All", "Summer", "Winter", "Other"]
)

if selected_season != "All":
    df = df[
        df["Season"] == selected_season
    ]

seasonal = (
    df.groupby("Season")["Total Activity Load"]
    .mean()
)

st.subheader(
    "Seasonal Activity Comparison"
)

st.bar_chart(seasonal)