# utils/visualization.py

import plotly.express as px
import pandas as pd

def plot_threats(threats):
    """Visualize the threat data using a bar chart."""
    fig = px.bar(threats, x='Threat Type', color='Severity', title='Threat Overview')
    import streamlit as st
    st.plotly_chart(fig)

def plot_sample_bar_chart():
    """Create and display a sample bar chart."""
    # Sample data
    data = {
        "Category": ["A", "B", "C"],
        "Values": [10, 15, 7]
    }
    df = pd.DataFrame(data)

    # Create a bar chart
    fig = px.bar(df, x='Category', y='Values', title='Sample Bar Chart')
    fig.show()