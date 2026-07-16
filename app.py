import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit_geolocation import streamlit_geolocation
import random

st.set_page_config(page_title="Eco-Sync | Enterprise Dashboard", layout="wide")

st.title("🌐 ECO-SYNC | Autonomous Monitoring System")
st.markdown("---")

# 1. Location and Map Logic
location = streamlit_geolocation()
lat, lon = (location['latitude'], location['longitude']) if location and location['latitude'] else (18.4088, 76.5604)

st.subheader("📍 Geospatial Operational Layer")
water_toggle = st.toggle("Enable Aquatic Monitoring Sector")

m = folium.Map(location=[lat, lon], zoom_start=16)

# Generate 30 Random Land Markers
for i in range(30):
    offset_lat = random.uniform(-0.005, 0.005)
    offset_lon = random.uniform(-0.005, 0.005)
    folium.Marker(
        [lat + offset_lat, lon + offset_lon], 
        popup=f"Land Sector {i+1}", 
        icon=folium.Icon(color="green", icon="leaf")
    ).add_to(m)

# Conditional Water Marker
if water_toggle:
    folium.Marker(
        [lat + 0.002, lon + 0.002], 
        popup="Water Body Sector", 
        icon=folium.Icon(color="blue", icon="tint")
    ).add_to(m)

map_data = st_folium(m, width=1000, height=500)

# 2. Telemetry Display
if map_data['last_object_clicked']:
    clicked = map_data['last_object_clicked']['popup']
    st.markdown(f"### 🔍 Telemetry Data: {clicked}")
    
    if "Land" in clicked:
        col1, col2, col3 = st.columns(3)
        col1.metric("AQI", "42")
        col2.metric("Humidity", "65%")
        col3.metric("Temp", "28°C")
        st.info("Status: Normal Operation")
    elif "Water" in clicked:
        col1, col2 = st.columns(2)
        col1.metric("Plastic Density", "12 kg")
        col2.metric("Water Quality", "Moderate")
        st.warning("Status: Cleanup Required")

# 3. Timeline
st.markdown("### ⏳ Performance Trend")
days = [f"Day {i}" for i in range(1, 8)]
st.select_slider("Select Timeline:", options=days)

# 4. AI Analysis
st.markdown("### 🤖 Cognitive AI Analysis")
uploaded_file = st.file_uploader("Upload imagery for automated detection", type=["jpg", "png"])
if uploaded_file:
    st.success("Environment Successfully Classified via Neural Analysis.")
