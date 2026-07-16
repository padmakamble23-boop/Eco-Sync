import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit_geolocation import streamlit_geolocation

st.set_page_config(page_title="Eco-Sync AI", layout="wide")

st.title("🌱 Eco-Sync: Intelligent Guardian")

# 1. Live Location Tracking
st.subheader("📍 Live Tracker")
location = streamlit_geolocation()

if location and location['latitude']:
    lat, lon = location['latitude'], location['longitude']
    m = folium.Map(location=[lat, lon], zoom_start=18)
    folium.Marker([lat, lon], popup="Your Location", icon=folium.Icon(color="red")).add_to(m)
    st_folium(m, width=900, height=300)
    
    # Logic: Detect if near water (Simple distance check)
    # In a real app, you would use a water-body map database
    is_water = st.toggle("Simulate: I am at a Water Body") 
else:
    st.write("Please enable location access to see the map.")
    is_water = False

# 2. Dynamic Dashboard
st.subheader("📊 Site Data")
if is_water:
    st.warning("### 💧 Aquatic Analysis")
    st.write("Water Quality: Moderate")
    st.write("Plastic Collected: 12kg")
    st.write("Status: Contaminated")
    st.write("Recommendation: Cleanup required")
    st.write("Alert: Action needed")
else:
    st.info("### 🌿 Land Analysis")
    st.write("AQI: 42")
    st.write("Humidity: 65%")
    st.write("Temperature: 28°C")
    st.write("Status: Normal")
    st.write("Recommendation: Routine monitoring")
    st.write("Alert: None")

# 3. Timeline Slider
st.subheader("⏳ Historical Timeline")
time_val = st.slider("Select Time Period:", 0, 100, 50)
st.write(f"Displaying data for index: {time_val}")

# 4. AI Vision Logic
st.sidebar.header("🤖 AI Analysis")
uploaded_file = st.sidebar.file_uploader("Upload Image", type=["jpg", "png"])

if uploaded_file:
    st.sidebar.image(uploaded_file, caption="Processing...", use_column_width=True)
    # Simple AI Logic Mockup
    if "water" in uploaded_file.name.lower():
        st.sidebar.success("AI: Water body detected. Displaying aquatic data.")
    else:
        st.sidebar.success("AI: Land surface detected. Displaying air quality data.")
