import streamlit as st
import requests

st.set_page_config(page_title="Smart Task Planner", layout="wide")
st.title("🧠 Smart Task Planner")
st.markdown("### Break your goal into actionable tasks using AI reasoning.")

goal = st.text_input("🎯 Enter your goal:", placeholder="e.g., Launch a product in 2 weeks")

API_URL = "https://smarttaskplanner-85vq.onrender.com/plan/"  # ✅ Corrected backend URL

if st.button("Generate Plan"):
    if goal.strip():
        with st.spinner("⏳ Generating plan... Please wait."):
            try:
                res = requests.get(API_URL, params={"goal": goal}, timeout=60)
                if res.status_code == 200:
                    st.success("✅ Plan Generated Successfully!")
                    st.markdown("### 📋 Suggested Plan")
                    st.markdown(res.json()["plan"])
                else:
                    st.error(f"❌ API Error: {res.status_code}")
            except requests.exceptions.ConnectionError:
                st.error("⚠️ Could not connect to backend. Please make sure FastAPI is running.")
            except requests.exceptions.Timeout:
                st.error("⏰ Request timed out. Try again after a few seconds.")
    else:
        st.warning("Please enter a goal before generating.")
