import streamlit as st
import folium
from streamlit_folium import st_folium
import random

st.set_page_config(page_title="Eco-Sync | Professional", layout="wide")

# 1. HARD-CODED LOCATION (Prevents GPS-induced flickering)
LAT, LON = 18.4088, 76.5604 

# 2. Build Map ONLY if it doesn't exist
if 'map_obj' not in st.session_state:
    m = folium.Map(location=[LAT, LON], zoom_start=16)
    for i in range(30):
        folium.Marker(
            [LAT + random.uniform(-0.005, 0.005), LON + random.uniform(-0.005, 0.005)], 
            popup=f"Sector_{i+1}", 
            icon=folium.Icon(color="green", icon="leaf")
        ).add_to(m)
    st.session_state.map_obj = m

st.title("🌐 ECO-SYNC | Autonomous Monitoring System")

# 3. Static Map Display
st.subheader("📍 Geospatial Operational Layer")
map_data = st_folium(st.session_state.map_obj, width=800, height=400, returned_objects=['last_object_clicked'])

# 4. Info Box (Appears only on click)
if map_data and map_data.get('last_object_clicked'):
    clicked = map_data['last_object_clicked']['popup']
    st.markdown("---")
    st.subheader(f"🔍 Telemetry Report: {clicked}")
    
    # Simple display
    col1, col2 = st.columns(2)
    col1.metric("Air Quality Index", "42")
    col2.metric("Sensor Status", "Active")
    st.success("Data stream stable.")
else:
    st.info("Tap a marker on the map to view site data.")

# 5. Fixed UI Elements
st.markdown("---")
st.markdown("### ⏳ Performance Trend")
st.select_slider("Timeframe", options=["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"])

st.markdown("### 🤖 Cognitive AI Analysis")
uploaded_file = st.file_uploader("Upload site imagery", type=["jpg", "png"])
if uploaded_file:
    st.success("Neural analysis complete.")
