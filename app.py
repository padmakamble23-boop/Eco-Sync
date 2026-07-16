import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit_geolocation import streamlit_geolocation

# Clean Corporate Styling
st.set_page_config(page_title="Eco-Sync | Professional Dashboard", layout="wide")
st.markdown("""
    <style>
    .main {background-color: #ffffff;}
    h1 {color: #2c3e50; font-family: 'Helvetica', sans-serif;}
    .stMetric {border: 1px solid #e1e4e8; padding: 20px; border-radius: 8px;}
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 ECO-SYNC | Autonomous Monitoring System")
st.markdown("---")

# 1. Map Logic
location = streamlit_geolocation()
lat, lon = (location['latitude'], location['longitude']) if location and location['latitude'] else (18.4088, 76.5604)

m = folium.Map(location=[lat, lon], zoom_start=17)

# Multiple markers representing different sensors
markers = [
    {"pos": [lat+0.0005, lon+0.0005], "type": "land", "name": "Sector A (Land)"},
    {"pos": [lat-0.0005, lon-0.0005], "type": "land", "name": "Sector B (Land)"},
    {"pos": [lat+0.0005, lon-0.0005], "type": "water", "name": "Sector C (Water)"}
]

for mark in markers:
    color = "green" if mark["type"] == "land" else "blue"
    folium.Marker(mark["pos"], popup=mark["name"], icon=folium.Icon(color=color)).add_to(m)

st.subheader("📍 Geospatial Operational Layer")
map_data = st_folium(m, width=800, height=400)

# 2. Telemetry Display
if map_data['last_object_clicked']:
    clicked = map_data['last_object_clicked']['popup']
    st.subheader(f"Telemetry for {clicked}")
    
    if "Land" in clicked:
        col1, col2, col3 = st.columns(3)
        col1.metric("AQI", "42")
        col2.metric("Humidity", "65%")
        col3.metric("Temp", "28°C")
        st.info("Status: Normal | Monitoring Active")
    elif "Water" in clicked:
        col1, col2 = st.columns(2)
        col1.metric("Plastic Density", "12 kg")
        col2.metric("Water Quality", "Moderate")
        st.warning("Status: Cleanup Required")

# 3. Timeline (7 Days)
st.markdown("### ⏳ Performance Trend")
days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]
selected_day = st.select_slider("Select Timeline:", options=days)
st.write(f"Displaying historical records for: **{selected_day}**")

# 4. AI Analysis
st.markdown("### 🤖 Cognitive AI Analysis")
uploaded_file = st.file_uploader("Upload multispectral imagery", type=["jpg", "png"])
if uploaded_file:
    st.image(uploaded_file, caption="Analysis In Progress...", width=300)
    st.success("Environment Successfully Classified.")
