import streamlit as st
import random

quotes = [
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn’t just find you. You have to go out and get it."
]

def get_random_quote():
    return random.choice(quotes)

# Set page title
st.set_page_config(page_title="💬 Motivational Quotes", layout="wide")

st.title("💬 Motivational Quotes")

# Display a random quote
st.markdown(f"### ✨ {get_random_quote()}")

# Button to get a new quote
if st.button("🔄 Get Another Quote"):
    st.rerun()
