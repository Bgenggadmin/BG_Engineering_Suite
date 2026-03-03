
import streamlit as st
from supabase import create_client, Client

# Connection
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(url, key)

st.title("🏗️ Production Entry")

with st.form("production_form"):
    job = st.text_input("Enter Job Code (e.g., BG-101)")
    name = st.text_input("Operator Name")
    note = st.text_area("Work Details")
    submit = st.form_submit_with_button("Submit to Quality")

    if submit:
        data = {
            "job_code": job,
            "operator_name": name,
            "remarks": note,
            "status": "Completed",
            "department": "Production"
        }
        supabase.table("reports").insert(data).execute()
        st.success(f"Job {job} sent to Quality Control!")
