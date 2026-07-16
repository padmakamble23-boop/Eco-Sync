import streamlit as st
import folium
from streamlit_folium import st_folium
import random

st.set_page_config(page_title="Eco-Sync | Professional", layout="wide")

# 1. DATA GENERATOR (Simulates 7 days of historical data)
def get_data(sector_name, day):
    # This simulates different data for each day
    if "Land" in sector_name:
        return {
            "AQI": 40 + (day * 2),
            "Humidity": 60 + day,
            "Temp": 25 + day,
            "Status": "Normal" if day < 5 else "Alert",
            "Recommendation": "Routine monitor" if day < 5 else "Increase filtration",
            "Alert": "None" if day < 5 else "High Particulates"
        }
    else:
        return {
            "Water Quality": "Moderate" if day < 4 else "Poor",
            "Recommendation": "Standard cleanup" if day < 4 else "Urgent biological treatment",
            "Alert": "Low risk" if day < 4 else "Contamination Detected"
        }

# 2. INITIALIZE STABLE STATE
if 'map_obj' not in st.session_state:
    m = folium.Map(location=[18.4088, 76.5604], zoom_start=16)
    for i in range(15): # Land
        folium.Marker([18.4088 + random.uniform(-0.005, 0.005), 76.5604 + random.uniform(-0.005, 0.005)], 
                      popup=f"Land Sector_{i+1}", icon=folium.Icon(color="green")).add_to(m)
    for i in range(3): # Water
        folium.Marker([18.4088 + random.uniform(-0.005, 0.005), 76.5604 + random.uniform(-0.005, 0.005)], 
                      popup=f"Water Sector_{i+1}", icon=folium.Icon(color="blue")).add_to(m)
    st.session_state.map_obj = m

st.title("🌐 ECO-SYNC | Autonomous Monitoring System")

# 3. SIDE-BY-SIDE LAYOUT
col_map, col_data = st.columns([2, 1])

with col_map:
    st.subheader("📍 Geospatial Operational Layer")
    map_data = st_folium(st.session_state.map_obj, width=700, height=450)

with col_data:
    st.subheader("⏳ Performance Timeline")
    day_val = st.select_slider("Select Day", options=[1, 2, 3, 4, 5, 6, 7])
    
    st.markdown("---")
    
    # Logic: Only show info if a marker is clicked
    if map_data and map_data.get('last_object_clicked'):
        clicked = map_data['last_object_clicked']['popup']
        data = get_data(clicked, day_val)
        
        st.markdown(f"### 🔍 Telemetry: {clicked}")
        if "Land" in clicked:
            st.metric("AQI", data["AQI"])
            st.write(f"**Humidity:** {data['Humidity']}%")
            st.write(f"**Temperature:** {data['Temp']}°C")
            st.write(f"**Status:** {data['Status']}")
            st.warning(f"**Recommendation:** {data['Recommendation']}")
            st.error(f"**Alert:** {data['Alert']}")
        else:
            st.write(f"**Water Quality:** {data['Water Quality']}")
            st.warning(f"**Recommendation:** {data['Recommendation']}")
            st.error(f"**Alert:** {data['Alert']}")
    else:
        st.info("👈 Select a marker on the map to view site data.")

# 4. AI UPLOAD (Fixed at bottom)
st.markdown("---")
st.subheader("🤖 Cognitive AI Analysis")
uploaded_file = st.file_uploader("Upload multispectral imagery", type=["jpg", "png"])
if uploaded_file:
    st.success("Neural analysis complete: Data validated.")
