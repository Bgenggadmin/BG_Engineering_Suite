
import streamlit as st
from supabase import create_client, Client

# 1. Page Configuration
st.set_page_config(
    page_title="B&G Engineering Suite",
    page_icon="🏭",
    layout="wide"
)

# 2. Connection Test (The "Heartbeat")
def init_connection():
    try:
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
        return create_client(url, key)
    except Exception as e:
        st.error(f"❌ Connection Error: {e}")
        return None

supabase = init_connection()

# 3. Sidebar Navigation Info
st.sidebar.success("Select a Department above to start logging.")
st.sidebar.info("B&G Engineering - Production v1.0")

# 4. Main Welcome Screen
st.title("🏭 B&G Engineering Master Portal")
st.markdown("---")

if supabase:
    st.success("✅ System Online: Connected to Central Database")
    
    # Dashboard Layout
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Production Status", value="Active", delta="On Track")
        if st.button("Go to Shop Floor"):
            st.switch_page("pages/1_Production.py")

    with col2:
        st.metric(label="QC Queue", value="Pending", delta="-2 Jobs")
        if st.button("Go to Quality"):
            st.switch_page("pages/2_Quality.py")

    with col3:
        st.metric(label="System Alerts", value="0", delta="Normal")
        if st.button("Report Maintenance"):
            st.switch_page("pages/3_Maintenance.py")

st.markdown("---")
st.write("### 📢 Daily Instructions")
st.info("Log all entries before 6:00 PM. Contact the Admin if you face sync issues.")
