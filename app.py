import streamlit as st
from supabase import create_client, Client

# Use the EXACT names from the Secrets box
try:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    supabase: Client = create_client(url, key)
except Exception as e:
    st.error("⚠️ Secrets missing! Check Streamlit Cloud Settings.")
    st.stop()
