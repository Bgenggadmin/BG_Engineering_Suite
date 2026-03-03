import streamlit as st
from supabase import create_client, Client

# SAFETY CHECK: Ensure Secrets are loaded before running
try:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    supabase: Client = create_client(url, key)
except KeyError:
    st.error("❌ Secrets not found! Please check Streamlit Cloud Settings.")
    st.stop()
