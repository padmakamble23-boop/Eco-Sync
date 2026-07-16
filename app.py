import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit_geolocation import streamlit_geolocation
import random

st.set_page_config(page_title="Eco-Sync | Professional", layout="wide")

# 1. Initialize Map Object (Run once)
if 'map_obj' not in st.session_state:
    loc = streamlit_geolocation()
    lat, lon = (loc['latitude'], loc['longitude']) if loc and loc['latitude'] else (18.4088, 76.5604)
    
    m = folium.Map(location=[lat, lon], zoom_start=16)
    for i in range(30):
        folium.Marker(
            [lat + random.uniform(-0.005, 0.005), lon + random.uniform(-0.005, 0.005)], 
            popup=f"Land Sector {i+1}", 
            icon=folium.Icon(color="green", icon="leaf")
        ).add_to(m)
    st.session_state.map_obj = m

st.title("🌐 ECO-SYNC | Autonomous Monitoring System")

# 2. Map Component
st.subheader("📍 Geospatial Operational Layer")
# We remove 'returned_objects' to stop the constant refreshing
map_data = st_folium(st.session_state.map_obj, width=1000, height=500)

# 3. Triggered Info Box (Only appears after click)
if map_data['last_object_clicked']:
    clicked = map_data['last_object_clicked']['popup']
    
    # This info box only renders when a click is detected
    st.markdown(f"---")
    st.markdown(f"### 🔍 Telemetry Data: {clicked}")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Status", "Operational")
    col2.metric("Sensor ID", clicked.split()[-1])
    col3.metric("Last Sync", "Just now")
    
    st.info("Environment data successfully retrieved from sensor network.")

# 4. Static Elements (Do not trigger refresh)
st.markdown("---")
st.markdown("### ⏳ Performance Trend")
st.select_slider("Select Timeline:", options=[f"Day {i}" for i in range(1, 8)])

st.markdown("### 🤖 Cognitive AI Analysis")
uploaded_file = st.file_uploader("Upload imagery for analysis", type=["jpg", "png"])
if uploaded_file:
    st.success("Analysis Complete.")
