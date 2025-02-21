import streamlit as st
import requests
from auth import login, signup
from chat import setup_sidebar, display_chat
from utils import initialize_session_state

def load_css(theme):
    """
    Dynamically load CSS based on the selected theme and hide Streamlit's header/footer.
    """
    css_file = f"{theme}.css"
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Hide Streamlit's built-in header, footer, and toolbar
    st.markdown(
        """
        <style>
            /* Hide Streamlit header, footer, and toolbar */
            header {visibility: hidden;}
            .css-18e3th9 {display: none !important;} /* Hides Streamlit toolbar */
            footer {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True
    )

def toggle_theme():
    """
    Toggle between light and dark themes and trigger a page rerun.
    """
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"
    st.rerun()

def main():
    st.set_page_config(page_title="Rafeeq - Psychological Support", layout="wide")

    if "theme" not in st.session_state:
        st.session_state.theme = "light"  # Default theme

    load_css(st.session_state.theme)
    initialize_session_state()

    # Header with title and a single toggle button
    col1, col2 = st.columns([5, 1])
    with col1:
        st.markdown("<span style='font-size:26px;font-weight:bold;'>🧠 Rafeeq - Mental Health Chatbot</span>", unsafe_allow_html=True)
    
    with col2:
        if st.button("Toggle Theme", key="theme_toggle"):
            toggle_theme()

    # Show chat if logged in
    if st.session_state.get("logged_in", False):
        setup_sidebar()
        display_chat()
    else:
        st.title("🔐 Login / Create a New Account")
        menu = ["Login", "Create a New Account"]
        choice = st.radio("Select Action: ", menu, horizontal=True)

        with st.container():
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                st.markdown('<div class="stForm">', unsafe_allow_html=True)
                if choice == "Login":
                    email = st.text_input("📧 Email", key="login_email")
                    password = st.text_input("🔑 Password", type="password", key="login_password")
                    if st.button("🔓 Login", key="login_button"):
                        login(email, password)
                else:
                    email = st.text_input("📧 Email", key="signup_email")
                    password = st.text_input("🔑 Password", type="password", key="signup_password")
                    confirm_password = st.text_input("🔑 Confirm Password", type="password", key="signup_confirm_password")
                    if st.button("📝 Sign Up", key="signup_button"):
                        signup(email, password, confirm_password)
                st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
