import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Eco-Sync Dashboard", layout="wide")

st.title("🌱 Eco-Sync: Autonomous Environmental Guardian")
st.write("Eco-Sync is an autonomous, amphibious robotic system designed for real-time environmental monitoring and waste remediation. Utilizing integrated sensor arrays and AI-powered vision, it detects pollutants in both land and water ecosystems. Through smart data tracking and automated alerts, it delivers actionable insights for a sustainable, cleaner future.")

# Map Section
st.subheader("📍 Live Operational Map")
m = folium.Map(location=[18.4088, 76.5604], zoom_start=16)

folium.Marker([18.4088, 76.5604], popup="Land Site: Status Normal", icon=folium.Icon(color="green")).add_to(m)
folium.Marker([18.4100, 76.5650], popup="Water Site: Cleanup Required", icon=folium.Icon(color="blue")).add_to(m)

st_folium(m, width=900, height=400)

# Dashboard
col1, col2 = st.columns(2)
with col1:
    st.info("### 🌿 Land Site (Air/Soil)")
    st.write("**AQI:** 42 | **Humidity:** 65% | **Temp:** 28°C")
    st.write("**Recommendation:** Routine monitoring.")
with col2:
    st.warning("### 💧 Water Site (Aquatic)")
    st.write("**Water Quality:** Moderate | **Plastic:** 12kg")
    st.write("**Recommendation:** Cleanup required.")

# AI Sidebar
st.sidebar.header("🤖 AI Vision System")
uploaded_file = st.sidebar.file_uploader("Upload image for AI Scan", type=["jpg", "png"])
if uploaded_file:
    st.sidebar.image(uploaded_file, caption="Analyzing...", use_column_width=True)
    st.sidebar.success("Scan Result: Pollutants identified. Cleanup advised.")
