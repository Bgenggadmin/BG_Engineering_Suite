import streamlit as st

# DIAGNOSTIC: This will show you exactly what keys are detected
st.write("### 🔍 System Diagnosis")
if not st.secrets:
    st.error("The entire Secrets storage is empty. The Dashboard Save failed.")
else:
    st.write("Detected Keys in Dashboard:", list(st.secrets.keys()))

# Attempt Connection only if keys exist
if "SUPABASE_URL" in st.secrets and "SUPABASE_KEY" in st.secrets:
    from supabase import create_client, Client
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    supabase: Client = create_client(url, key)
    st.success("✅ Connection Confirmed!")
else:
    st.warning("⚠️ One or more keys are still missing from the Dashboard.")
