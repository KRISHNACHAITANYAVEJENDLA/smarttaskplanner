import streamlit as st
import requests

st.set_page_config(page_title="Smart Task Planner", layout="wide")
st.title("🧠 Smart Task Planner")
st.markdown("### Break your goal into actionable tasks using AI reasoning.")

goal = st.text_input("🎯 Enter your goal:", placeholder="e.g., Launch a product in 2 weeks")

API_URL = "https://smarttaskplanner-85vq.onrender.com/plan/"

if st.button("Generate Plan"):
    if goal.strip():
        with st.spinner("⏳ Generating plan... Please wait."):
            try:
                res = requests.get(API_URL, params={"goal": goal}, timeout=90)
                if res.status_code == 200:
                    try:
                        data = res.json()
                        if "plan" in data:
                            st.success("✅ Plan Generated Successfully!")
                            st.markdown("### 📋 Suggested Plan")
                            st.markdown(data["plan"])
                        else:
                            st.warning("⚠️ Unexpected response format from backend.")
                            st.text(res.text)
                    except ValueError:
                        st.error("⚠️ Backend returned invalid JSON response.")
                        st.text(res.text)
                else:
                    st.error(f"❌ API Error: {res.status_code}")
                    st.text(res.text)
            except requests.exceptions.ConnectionError:
                st.error("⚠️ Could not connect to backend. Please ensure the API is live on Render.")
            except requests.exceptions.Timeout:
                st.error("⏰ The request timed out. Please try again later.")
    else:
        st.warning("Please enter a goal before generating.")

st.markdown("---")
st.caption("🌐 Powered by FastAPI + Streamlit | Developed by Krishna Chaitanya Vejendla")
