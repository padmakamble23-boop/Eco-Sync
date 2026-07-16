import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit_geolocation import streamlit_geolocation
import random

st.set_page_config(page_title="Eco-Sync | Enterprise", layout="wide")

# 1. Initialize stable state
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    # Get location once
    loc = streamlit_geolocation()
    lat, lon = (loc['latitude'], loc['longitude']) if loc and loc['latitude'] else (18.4088, 76.5604)
    
    # Build Map once
    m = folium.Map(location=[lat, lon], zoom_start=16)
    for i in range(30):
        folium.Marker(
            [lat + random.uniform(-0.005, 0.005), lon + random.uniform(-0.005, 0.005)], 
            popup=f"Land Sector {i+1}", 
            icon=folium.Icon(color="green", icon="leaf")
        ).add_to(m)
    st.session_state.map_obj = m

st.title("🌐 ECO-SYNC | Autonomous Monitoring System")

# 2. Controls
water_toggle = st.toggle("Enable Aquatic Monitoring Sector")

# 3. Display Map
st.subheader("📍 Geospatial Operational Layer")
# We use 'returned_objects' to handle interaction without refreshing the whole map object
map_data = st_folium(st.session_state.map_obj, width=1000, height=500, returned_objects=['last_object_clicked'])

# 4. Telemetry Logic (Outside the map definition)
if map_data['last_object_clicked']:
    clicked = map_data['last_object_clicked']['popup']
    st.markdown(f"### 🔍 Telemetry: {clicked}")
    if "Land" in clicked:
        col1, col2, col3 = st.columns(3)
        col1.metric("AQI", "42")
        col2.metric("Humidity", "65%")
        col3.metric("Temp", "28°C")
    elif "Water" in clicked:
        st.warning("Aquatic data active")

# 5. Bottom UI (No refresh-heavy elements)
st.markdown("### ⏳ Performance Trend")
st.select_slider("Select Timeline:", options=[f"Day {i}" for i in range(1, 8)])
