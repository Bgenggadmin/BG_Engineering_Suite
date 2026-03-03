import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Simple Page Setup
st.set_page_config(page_title="B&G Engineering", layout="centered")

st.title("🏗️ B&G Engineering Log")
st.write("Direct GitHub Interface (No Database Required)")

# 1. The File Check
file_path = 'data_log.csv'

# 2. The Input Form
with st.form("entry_form", clear_on_submit=True):
    st.subheader("New Entry")
    job = st.text_input("Job Number")
    operator = st.text_input("Operator")
    status = st.selectbox("Status", ["In Progress", "Completed", "Pending"])
    submit = st.form_submit_button("Save to GitHub")

    if submit:
        new_data = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Job": job,
            "Operator": operator,
            "Status": status
        }
        
        # Save Logic
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            df.to_csv(file_path, index=False)
            st.success(f"✅ Job {job} recorded successfully!")
        else:
            st.error("❌ Error: data_log.csv not found. Please create it first.")

# 3. View the Data
if os.path.exists(file_path):
    st.divider()
    st.subheader("Recent Logs")
    data = pd.read_csv(file_path)
    st.dataframe(data.tail(10), use_container_width=True)
