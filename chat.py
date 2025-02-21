import streamlit as st
import requests
import uuid
from datetime import datetime
from auth import logout

CHATBOT_API_URL = "http://localhost:3000/api/chatbot/message/"

# Ensure get_bot_response is defined first
def get_bot_response(user_message):
    """Fetch AI response from backend API"""
    try:
        response = requests.post(CHATBOT_API_URL, json={"message": user_message})
        
        if response.status_code == 200:
            return response.json().get("response", "I'm not sure how to respond to that. 🤖")
        else:
            return f"❌ Error: {response.status_code} - {response.text}"
    
    except requests.exceptions.ConnectionError:
        return "⚠️ Error: Unable to connect to chatbot server. Is it running?"
    except Exception as e:
        return f"⚠️ Unexpected Error: {str(e)}"

def display_chat():
    """Display chat messages from the selected session and handle user input."""
    st.subheader("💬 Companion - Your Current Chat")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = {}

    if "selected_chat" not in st.session_state or not st.session_state.selected_chat:
        st.info("Start a new session to begin chatting.")
        return

    chat_id = st.session_state.selected_chat
    if chat_id not in st.session_state.chat_history:
        st.session_state.chat_history[chat_id] = {"messages": []}

    chat_messages = st.session_state.chat_history[chat_id]["messages"]

    # Display previous messages
    for message in chat_messages:
        with st.chat_message("assistant" if message["role"] == "bot" else "user"):
            st.write(message["content"])

    # User input box
    user_input = st.chat_input("Type your message here...")
    if user_input:
        chat_messages.append({"role": "user", "content": user_input})

        # Show spinner while waiting for the response
        with st.spinner("💬 Thinking..."):
            bot_response = get_bot_response(user_input)

        chat_messages.append({"role": "bot", "content": bot_response})

        st.session_state.chat_history[chat_id]["messages"] = chat_messages
        st.rerun()  # Refresh UI
        
    
def setup_sidebar():
    """Setup sidebar for chat sessions and user actions."""
    with st.sidebar:
        st.markdown('<div class="header">🗨 Chat Sessions Log</div>', unsafe_allow_html=True)

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = {}

        if st.button("🌼 Start a New Session", use_container_width=True):
            create_new_chat()

        for chat_id, chat_data in st.session_state.chat_history.items():
            col1, col2 = st.columns([0.85, 0.15])

            with col1:
                if st.button(chat_data["title"], key=f"select_{chat_id}"):
                    st.session_state.selected_chat = chat_id

            with col2:
                if st.button("🗑", key=f"delete_{chat_id}", help="Delete this chat"):
                    delete_chat(chat_id)
                    st.rerun()  # Refresh after deleting a chat

        if st.button("🚪 Log Out", use_container_width=True):
            logout()


def create_new_chat():
    """Create a new chat session."""
    new_chat_id = str(uuid.uuid4())
    st.session_state.chat_history[new_chat_id] = {
        "messages": [],
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "title": f"Session {len(st.session_state.chat_history) + 1}"
    }
    st.session_state.selected_chat = new_chat_id
    st.rerun()  # Refresh UI to reflect new chat session

def delete_chat(chat_id):
    """Delete a chat session."""
    if chat_id in st.session_state.chat_history:
        del st.session_state.chat_history[chat_id]
        if st.session_state.selected_chat == chat_id:
            st.session_state.selected_chat = None
