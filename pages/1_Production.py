import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.title("🏗️ Production Unit")

# Simple form that saves to the CSV file in this repo
with st.form("prod_form", clear_on_submit=True):
    job = st.text_input("Job Code (e.g., BG-001)")
    op = st.text_input("Operator Name")
    rem = st.text_area("Remarks/Work Done")
    submit = st.form_submit_button("Submit to Logs")

    if submit:
        new_entry = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Department": "Production",
            "Job_Code": job,
            "Operator": op,
            "Status": "Completed",
            "Remarks": rem
        }
        
        # Add to the CSV file
        file_path = 'data_log.csv'
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
            df.to_csv(file_path, index=False)
            st.success(f"✅ Job {job} recorded in data_log.csv!")
        else:
            st.error("❌ Cannot find data_log.csv. Please create it in the main repository.")
