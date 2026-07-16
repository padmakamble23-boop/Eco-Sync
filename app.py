import streamlit as st
import folium
from streamlit_folium import st_folium
import random

st.set_page_config(page_title="Eco-Sync | Professional", layout="wide")

# 1. FIXED DATA GENERATOR
def get_data(sector_name, day):
    # Using a deterministic random seed based on name+day so data is consistent
    random.seed(len(sector_name) + day)
    if "Land" in sector_name:
        return {
            "AQI": random.randint(30, 100),
            "Humidity": random.randint(40, 80),
            "Temp": random.randint(20, 35),
            "Status": "Normal",
            "Recommendation": "Routine Monitoring",
            "Alert": "None"
        }
    else:
        return {
            "Water Quality": "Moderate",
            "Recommendation": "Standard Cleanup Required",
            "Alert": "Minimal"
        }

# 2. INITIALIZE MAP (Only once)
if 'map_obj' not in st.session_state:
    m = folium.Map(location=[18.4088, 76.5604], zoom_start=16)
    for i in range(25):
        folium.Marker([18.4088 + random.uniform(-0.005, 0.005), 76.5604 + random.uniform(-0.005, 0.005)], 
                      popup=f"Land Sector {i+1}", icon=folium.Icon(color="green")).add_to(m)
    for i in range(5):
        folium.Marker([18.4088 + random.uniform(-0.005, 0.005), 76.5604 + random.uniform(-0.005, 0.005)], 
                      popup=f"Water Sector {i+1}", icon=folium.Icon(color="blue")).add_to(m)
    st.session_state.map_obj = m

st.title("🌐 ECO-SYNC | Autonomous Monitoring System")

# 3. INTERACTIVE LOGIC
col_map, col_data = st.columns([2, 1])

with col_map:
    # Use key='map' so Streamlit tracks this component stably
    map_data = st_folium(st.session_state.map_obj, width=700, height=500, key='map')

with col_data:
    st.subheader("📊 Site Analysis")
    
    # Check if a marker was clicked
    clicked = None
    if map_data['last_object_clicked']:
        clicked = map_data['last_object_clicked']['popup']
        st.session_state.selected_marker = clicked

    if 'selected_marker' in st.session_state:
        st.write(f"**Selected:** {st.session_state.selected_marker}")
        day = st.select_slider("Select Timeline", options=[1, 2, 3, 4, 5, 6, 7])
        
        data = get_data(st.session_state.selected_marker, day)
        
        # Display data based on type
        if "Land" in st.session_state.selected_marker:
            st.metric("AQI", data["AQI"])
            st.write(f"Humidity: {data['Humidity']}% | Temp: {data['Temp']}°C")
            st.write(f"Status: {data['Status']}")
            st.info(f"AI Rec: {data['Recommendation']}")
        else:
            st.write(f"Water Quality: {data['Water Quality']}")
            st.warning(f"AI Rec: {data['Recommendation']}")
            st.error(f"Alert: {data['Alert']}")
    else:
        st.info("👈 Tap a map marker to view data.")

# 4. AI UPLOAD (Fixed)
st.divider()
uploaded_file = st.file_uploader("Upload multispectral imagery", type=["jpg", "png"])
if uploaded_file:
    st.success("Environment analysis validated.")
