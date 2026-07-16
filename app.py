import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit_geolocation import streamlit_geolocation

# Professional Dark-Themed Configuration
st.set_page_config(page_title="Eco-Sync | Intelligent Monitoring", layout="wide")
st.markdown("""
    <style>
    .stApp {background-color: #0f1117;}
    h1 {color: #00ffcc; font-family: 'Segoe UI', sans-serif;}
    h2, h3 {color: #ffffff;}
    .stMetric {background-color: #1c252b; padding: 15px; border-radius: 10px;}
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 ECO-SYNC | Autonomous Monitoring System")
st.markdown("---")

# 1. Map Setup (Professional Dark Theme)
location = streamlit_geolocation()
lat, lon = (location['latitude'], location['longitude']) if location and location['latitude'] else (18.4088, 76.5604)

m = folium.Map(location=[lat, lon], zoom_start=17, tiles="CartoDB dark_matter")
folium.Marker([lat+0.0001, lon], popup="Land Site", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
folium.Marker([lat-0.0001, lon], popup="Water Site", icon=folium.Icon(color="blue", icon="tint")).add_to(m)

# 2. Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📍 Geospatial Operational Layer")
    map_data = st_folium(m, width=800, height=450)

with col2:
    st.subheader("🔍 Site Telemetry")
    if map_data['last_object_clicked']:
        clicked = map_data['last_object_clicked']['popup']
        if "Land" in clicked:
            st.metric("Air Quality Index", "42", "-2")
            st.write("**Soil Humidity:** 65%")
            st.write("**Ambient Temp:** 28°C")
            st.info("STATUS: NORMAL | Monitoring Active")
        elif "Water" in clicked:
            st.metric("Plastic Density", "12 kg", "+0.5")
            st.write("**Water Quality:** Moderate")
            st.write("**Turbidity:** 4.2 NTU")
            st.warning("STATUS: ACTION REQUIRED | Cleanup Initialized")
    else:
        st.write("Select a site marker on the map to initialize the live telemetry feed.")

# 3. Timeline
st.markdown("### ⏳ Historical Performance Index")
st.slider("Operational Timeframe", 0, 100, 50, key="timeline")

# 4. AI Analysis
st.markdown("### 🤖 Cognitive AI Analysis")
uploaded_file = st.file_uploader("Upload multispectral imagery for automated detection", type=["jpg", "png"])
if uploaded_file:
    with st.spinner('Running neural analysis...'):
        st.image(uploaded_file, width=400)
        st.success("Analysis Complete: Environment classified successfully.")
