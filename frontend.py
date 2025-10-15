import streamlit as st
import requests

st.set_page_config(page_title="Smart Task Planner", layout="wide")
st.title("🧠 Smart Task Planner")
st.markdown("### Break your goal into actionable tasks using AI-like reasoning.")

goal = st.text_input("🎯 Enter your goal:", placeholder="e.g., Launch a product in 2 weeks")

API_URL = "https://smarttaskplanner-backend.onrender.com/plan/"  # Replace with your backend URL

if st.button("Generate Plan"):
    if goal.strip():
        with st.spinner("⏳ Generating plan... Please wait."):
            try:
                res = requests.get(API_URL, params={"goal": goal}, timeout=60)
                if res.status_code == 200:
                    data = res.json()
                    st.success("✅ Plan Generated Successfully!")
                    st.markdown("### 📋 Suggested Plan")
                    st.markdown(data["plan"])
                else:
                    st.error(f"❌ API Error: {res.status_code}")
                    st.text(res.text)
            except requests.exceptions.RequestException as e:
                st.error(f"⚠️ Connection Error: {e}")
    else:
        st.warning("Please enter a goal before generating.")

st.markdown("---")
st.caption("🌐 Powered by FastAPI + Streamlit | Developed by Krishna Chaitanya Vejendla")
