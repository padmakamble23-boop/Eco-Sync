import streamlit as st
import folium
from streamlit_folium import st_folium
import random

st.set_page_config(layout="wide")

# 1. Initialize Map once
if 'm' not in st.session_state:
    m = folium.Map(location=[18.4088, 76.5604], zoom_start=15)
    for i in range(20):
        folium.Marker(
            [18.4088 + random.uniform(-0.005, 0.005), 76.5604 + random.uniform(-0.005, 0.005)],
            popup=f"Sector_{i+1}",
            icon=folium.Icon(color="green" if i < 17 else "blue")
        ).add_to(m)
    st.session_state.m = m
    st.session_state.last_clicked = None

st.title("🌐 ECO-SYNC | Dashboard")

# 2. Layout
col1, col2 = st.columns([2, 1])

with col1:
    # Key='map' prevents re-rendering
    map_data = st_folium(st.session_state.m, width=700, height=500, key="map")
    
    # Capture the click
    if map_data['last_object_clicked']:
        st.session_state.last_clicked = map_data['last_object_clicked']['popup']

with col2:
    st.subheader("📊 Telemetry")
    if st.session_state.last_clicked:
        clicked = st.session_state.last_clicked
        st.write(f"**Target:** {clicked}")
        
        # Timeline Slider
        day = st.select_slider("Select Day", options=[1, 2, 3, 4, 5, 6, 7])
        
        # Telemetry Content
        if "Sector" in clicked:
            st.metric("AQI", 40 + day)
            st.write(f"**Status:** Normal")
            st.warning("AI Recommendation: Routine check")
    else:
        st.info("Click a map marker to view data.")

# 3. AI Upload at the bottom
st.divider()
uploaded_file = st.file_uploader("Upload Image")
if uploaded_file:
    st.success("Analysis Complete.")
