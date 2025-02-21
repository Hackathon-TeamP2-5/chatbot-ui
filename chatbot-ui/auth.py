import streamlit as st
from pymongo import MongoClient
from urllib.parse import quote_plus
import hashlib
import time
from utils import initialize_session_state

username = quote_plus("aliaburas")  
password = quote_plus("Ali@2005")  
MONGO_URI = f"mongodb+srv://{username}:{password}@cluster1.6i9tf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"
client = MongoClient(MONGO_URI)
db = client["sample_mflix"]
users_collection = db["users"]

def login(email, password):
    user = users_collection.find_one({"email": email, "password": hashlib.sha256(password.encode()).hexdigest()})
    if user:
        st.session_state.logged_in = True
        st.session_state.user_email = email
        st.success("✅ Successfully logged in! Redirecting to the main page...")
        time.sleep(2)
        st.query_params["page"] = "app"
        st.rerun()
    else:
        st.error("❌ Incorrect email or password")

def signup(email, password, confirm_password):
    if password == confirm_password:
        existing_user = users_collection.find_one({"email": email})
        if existing_user:
            st.error("⚠ This email is already in use")
        else:
            users_collection.insert_one({"email": email, "password": hashlib.sha256(password.encode()).hexdigest()})
            st.success("✅ Account created successfully! You can now log in.")
    else:
        st.error("❌ Passwords do not match!")

def logout():
    st.session_state.logged_in = False
    st.session_state.user_email = ""
    st.session_state.chat_history = {}
    st.session_state.selected_chat = None
    st.success("✅ Successfully logged out! Redirecting to the login page...")
    time.sleep(2)
    st.query_params["page"] = "auth"
    st.rerun()