import streamlit as st
from auth import login, signup
from chat import setup_sidebar, display_chat
from utils import initialize_session_state, get_ai_response

def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Companion - Psychological Support", layout="wide")
    load_css()  
    initialize_session_state()

    query_params = st.query_params
    current_page = query_params.get("page", "auth")

    if current_page == "auth":
        if st.session_state.logged_in:
            st.query_params["page"] = "app"
            st.rerun()
        else:
            st.title("🔐 Login / Create a New Account")
            menu = ["login", "Create a New Account"]
            choice = st.radio("Select Action: ", menu, horizontal=True)

            with st.container():
                col1, col2, col3 = st.columns([1, 1, 1]) 
                with col2:
                    if choice == "login":
                        st.markdown("### login")
                        email = st.text_input("📧 Email", key="login_email")
                        password = st.text_input("🔑 Password", type="password", key="login_password")
                        if st.button("🔓 login", key="login_button"):
                            login(email, password)

                    elif choice == "Create":
                        st.markdown("### Create a New Account")
                        email = st.text_input("📧 Email", key="signup_email")
                        password = st.text_input("🔑 Password", type="password", key="signup_password")
                        confirm_password = st.text_input("🔑 Confirm Password", type="password", key="signup_confirm_password")
                        if st.button("📝 Create a New Account", key="signup_button"):
                            signup(email, password, confirm_password)

    elif st.session_state.logged_in:
        st.title("Welcome to Rafeeq – Psychological Support")
        setup_sidebar()
        display_chat()

        user_input = st.text_input("Type your message here...", key="user_input")
        if st.button("Send", key="send_button"):
            if st.session_state.selected_chat is None:
                st.warning("⚠ Please select a chat session or create a new one.")
            else:
                st.session_state.chat_history[st.session_state.selected_chat]["messages"].append(
                    {"role": "user", "content": user_input}
                )
                ai_response = get_ai_response(user_input)
                st.session_state.chat_history[st.session_state.selected_chat]["messages"].append(
                    {"role": "assistant", "content": ai_response}
                )
                st.rerun()

    else:
        st.query_params["page"] = "auth"
        st.rerun()

def display_video_page():
    st.set_page_config(page_title="📺 Display Video", layout="wide")
    
    st.title("📺 Watch Psychotherapy Videos")

    st.write("Explore informative psychotherapy videos curated for mental health support.")

    st.video("https://www.youtube.com/watch?v=fRWhmVie0GU")  # Example video

    st.markdown("---")

    if st.button("🔙 Back to Home"):
        st.session_state.page = "app"
        st.query_params["page"] = "app"
        st.rerun()

if __name__ == "__main__":
    main()