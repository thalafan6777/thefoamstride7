import streamlit as st
import firebase_admin
from firebase_admin import credentials, db

# Firebase Initialization
cred = credentials.Certificate("thefoamstride-firebase-adminsdk-fbsvc-3da2d80166.json")  # Replace with your actual path
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://thefoamstride-default-rtdb.firebaseio.com'  # Replace with your Firebase DB URL
})

# Function to fetch data from Firebase "calendar" node
def get_calendar_data():
    ref = db.reference('/calendar')  # Fetching data from "calendar"
    data = ref.get()
    return data

# Streamlit App
st.title("📅 Firebase Calendar Data Viewer")

calendar_data = get_calendar_data()

# Check if data is available
if calendar_data:
    for date, info in calendar_data.items():
        st.subheader(f"📅 {date}")
        st.write(info)  # Displaying data
else:
    st.warning("No calendar data found.")

# Run the app with: streamlit run app.py
