import streamlit as st
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Make a GET request to your Flask API to fetch data
api_url = "http://app:5000/"
response = requests.get(api_url)
data = response.json()

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
