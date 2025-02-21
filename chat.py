import streamlit as st
import uuid
from datetime import datetime
from auth import logout 

def setup_sidebar():
    with st.sidebar:
        st.markdown('<div class="header">🗨 Chat Sessions Log</div>', unsafe_allow_html=True)

        if st.button("🌼 Start a New Session", use_container_width=True):
            create_new_chat()
            st.rerun()

        for chat_id, chat_data in st.session_state.chat_history.items():
            col1, col2 = st.columns([0.85, 0.15])

            with col1:
                if st.button(chat_data["title"], key=f"select_{chat_id}"):
                    st.session_state.selected_chat = chat_id
                    st.rerun()

            with col2:
                if st.button("🗑", key=f"delete_{chat_id}", help="Delete this chat"):
                    delete_chat(chat_id)
                    st.rerun()

        if st.button("🚪 Log Out", use_container_width=True):
            logout()

        if st.button("📺 Display Video", use_container_width=True):
            video_page_url = "ChatBoot\ChatBoot\DisplayVid.py"
            st.markdown(f'<a href="{video_page_url}" target="_blank">عرض الفيديو</a>', unsafe_allow_html=True)


        if st.button("💬 Quotes", use_container_width=True):
            st.session_state.page = "quotes"
            st.query_params["ChatBoot\ChatBoot\quote.py"] = "quotes"
            st.markdown('<a href="ChatBoot\ChatBoot\quote.py" target="_blank">Quotes</a>', unsafe_allow_html=True)
            st.rerun()



def display_chat():
    if "selected_chat" in st.session_state and st.session_state.selected_chat:
        chat_data = st.session_state.chat_history.get(st.session_state.selected_chat, {"messages": []})
        messages = chat_data["messages"]

        st.markdown('<div class="header">🌺 Companion - Your Current Chat</div>', unsafe_allow_html=True)

        for msg in messages:
            if msg["role"] == "user":
                st.markdown(f"""
                <div class="user-message">
                    <strong>You:</strong><br>
                    {msg["content"]}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="assistant-message">
                    <strong>Companion:</strong><br>
                    {msg["content"]}
                </div>
                """, unsafe_allow_html=True)

def create_new_chat():
    new_chat_id = str(uuid.uuid4())
    st.session_state.chat_history[new_chat_id] = {
        "messages": [],
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "title": "New Session"
    }
    st.session_state.selected_chat = new_chat_id

def delete_chat(chat_id):
    if chat_id in st.session_state.chat_history:
        del st.session_state.chat_history[chat_id]
        if st.session_state.selected_chat == chat_id:
            st.session_state.selected_chat = None