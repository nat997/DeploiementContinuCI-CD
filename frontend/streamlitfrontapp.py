import streamlit as st
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def fetch_data(api_url):
    response = requests.get(api_url)
    return response.json()

# Split the process_data function into two to handle degree and timestamp data separately
def process_degree_data(data):
    degree_data = pd.DataFrame(data, columns=["Degree ID", "Degree Value"])
    return degree_data

def process_timestamp_data(data):
    timestamp_data = pd.DataFrame(data, columns=["Timestamp ID", "Timestamp"])
    timestamp_data["Timestamp"] = pd.to_datetime(timestamp_data["Timestamp"])
    return timestamp_data

# Define API URLs for degree and timestamp data
api_url_degree = "http://app:5000/degree"
api_url_timestamp = "http://app:5000/timestamp"

# Fetch and process degree data
degree_data_json = fetch_data(api_url_degree)
degree_data = process_degree_data(degree_data_json["Degree Data"])

# Fetch and process timestamp data
timestamp_data_json = fetch_data(api_url_timestamp)
timestamp_data = process_timestamp_data(timestamp_data_json["Timestamp Data"])

# Ensure that the length of both datasets is the same for plotting (or handle discrepancies appropriately)
min_length = min(len(degree_data), len(timestamp_data))
degree_values = degree_data["Degree Value"].values[:min_length]
timestamps = timestamp_data["Timestamp"].values[:min_length]

# Create a Streamlit chart using Matplotlib
st.title("Degree vs Timestamp Chart")
fig, ax = plt.subplots()
ax.plot(timestamps, degree_values, marker='o')  # Added marker for better visualization
ax.set_xlabel("Timestamp")
ax.set_ylabel("Degree Value")
ax.set_title("Degree vs Timestamp")

# Rotate date labels for better readability
plt.xticks(rotation=45)
plt.tight_layout()

# Display the chart in Streamlit
st.pyplot(fig)
