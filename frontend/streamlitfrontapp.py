import streamlit as st
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def fetch_data(api_url):
    response = requests.get(api_url)
    return response.json()

def process_data(data):
    degree_data = pd.DataFrame(data["Degree Data"], columns=["Degree ID", "Degree Value"])
    timestamp_data = pd.DataFrame(data["Timestamp Data"], columns=["Timestamp ID", "Timestamp"])
    timestamp_data["Timestamp"] = pd.to_datetime(timestamp_data["Timestamp"])
    return degree_data, timestamp_data

# Main Streamlit app logic
api_url = "http://app:5000/"
data = fetch_data(api_url)
degree_data, timestamp_data = process_data(data)

# Create a DataFrame from the degree and timestamp data
degree_data = pd.DataFrame(data["Degree Data"], columns=["Degree ID", "Degree Value"])
timestamp_data = pd.DataFrame(data["Timestamp Data"], columns=["Timestamp ID", "Timestamp"])

# Convert Timestamp column to datetime
timestamp_data["Timestamp"] = pd.to_datetime(timestamp_data["Timestamp"])

# Extract data as numpy arrays for plotting
timestamps = timestamp_data["Timestamp"].values
degree_values = degree_data["Degree Value"].values

# Create a Streamlit chart using Matplotlib
st.title("Degree vs Timestamp Chart")
fig, ax = plt.subplots()
ax.plot(timestamps, degree_values)
ax.set_xlabel("Timestamp")
ax.set_ylabel("Degree Value")
ax.set_title("Degree vs Timestamp")

# Display the chart in Streamlit
st.pyplot(fig)
