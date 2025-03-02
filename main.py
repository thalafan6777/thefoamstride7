import streamlit as st
import firebase_admin
from firebase_admin import credentials, db
import os

# 🔹 Path to Firebase Credentials (Change This)
JSON_PATH = "thefoamstride-firebase-adminsdk-fbsvc-7199bcbd97.json"  # <-- UPDATE THIS

# 🔹 Firebase Database URL (Change This)
DATABASE_URL = "https://thefoamstride-default-rtdb.firebaseio.com"  # <-- UPDATE THIS

# ✅ Ensure JSON file exists
if not os.path.exists(JSON_PATH):
    st.error(f"❌ ERROR: Firebase credentials file not found: {JSON_PATH}")
    st.stop()

# ✅ Initialize Firebase (Only if not already initialized)
if not firebase_admin._apps:
    try:
        cred = credentials.Certificate(JSON_PATH)
        firebase_admin.initialize_app(cred, {"databaseURL": DATABASE_URL})
    except Exception as e:
        st.error(f"❌ ERROR: Firebase initialization failed: {str(e)}")
        st.stop()

# ✅ Fetch Data from Firebase
try:
    ref = db.reference("/calendar")  # <-- Ensure 'calendar' exists in your database
    data = ref.get()
    
    if data:
        st.success("✅ Data retrieved successfully!")
    else:
        st.warning("⚠️ No data found in Firebase.")

except Exception as e:
    st.error(f"❌ ERROR: Failed to fetch data: {str(e)}")
    st.stop()

# ✅ Display Data in Streamlit
st.title("📅 Firebase Calendar Data")

if data:
    st.json(data)  # Displays data in JSON format
else:
    st.write("No data available.")
