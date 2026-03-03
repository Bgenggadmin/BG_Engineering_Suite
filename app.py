import streamlit as st
import pandas as pd
import os

# Set page layout
st.set_page_config(page_title="B&G Engineering Suite", layout="wide")

st.title("🏭 B&G Engineering Master Portal")
st.write("Current Status: **Local CSV Database Mode**")

# This code does NOT use st.secrets. 
# It only looks for the file you created in this repository.
if os.path.exists('data_log.csv'):
    st.success("✅ System Ready: data_log.csv is active.")
    df = pd.read_csv('data_log.csv')
    st.write("### Recent Activity Log")
    st.dataframe(df.tail(10))
else:
    st.error("❌ File 'data_log.csv' not found in this repository. Please create it!")

st.sidebar.info("Select a department from the sidebar.")
