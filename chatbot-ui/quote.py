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

def workout_website():
    url = "https://suar.me/6Adx" 
    st.markdown(f'<meta http-equiv="refresh" content="0;>')