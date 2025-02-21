import hashlib
import streamlit as st

def initialize_session_state():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "user_email" not in st.session_state:
        st.session_state.user_email = ""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = {}
    if "selected_chat" not in st.session_state:
        st.session_state.selected_chat = None

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def get_ai_response(user_input):
    from transformers import pipeline
    chatbot_pipeline = pipeline("text-generation", model="distilgpt2")
    response = chatbot_pipeline(user_input, max_length=100, do_sample=True, temperature=0.7)
    return response[0]['generated_text']