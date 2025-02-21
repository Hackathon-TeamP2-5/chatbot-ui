import streamlit as st

st.set_page_config(page_title="📺 Psychotherapy Videos & GIFs", layout="wide")

st.title("🌿 Psychotherapy & Mental Health")

st.write("Explore a collection of videos and GIFs related to psychotherapy and mental health.")
st.image("https://static.vecteezy.com/system/resources/previews/016/181/668/original/therapy-session-semi-flat-color-characters-editable-figures-full-body-people-on-white-professional-psychological-help-simple-cartoon-style-illustration-for-web-graphic-design-and-animation-vector.jpg", use_container_width=True)

st.markdown("""
## 🧠 What is Psychotherapy?
Psychotherapy is a method used to help individuals cope with mental and emotional issues.  
It aims to improve mental health through conversation and psychological support.
""")

st.header("🎥 Psychotherapy Videos")

col1, col2 = st.columns(2)

with col1:
    st.video("https://www.youtube.com/watch?v=fRWhmVie0GU")  # Psychotherapy for Depression
    st.video("https://www.youtube.com/watch?v=db3K8b3ftaY")  # Understanding Anxiety  

with col2:
    st.video("https://www.youtube.com/watch?v=ZdyOwZ4_RnI")  # Cognitive Behavioral Therapy (CBT)
    st.video("https://www.youtube.com/watch?v=TOfU6nnQiAU")  # How Psychotherapy Helps Mental Health  

st.write("💡 Have a video suggestion? Submit it below!")

st.header("🎞 Relaxing GIFs")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://media3.giphy.com/media/xThuWbKwgGz1EGNF28/giphy.gif", caption="Relaxation", use_container_width=True)

with col2:
    st.image("https://media1.giphy.com/media/BivM2hUHpgEHuIC4ug/giphy.gif", caption="Emotional Control", use_container_width=True)

with col3:
    st.image("https://media3.giphy.com/media/Rol6kVQRMOWVLR3vFG/giphy.gif", caption="Mindfulness & Calmness", use_container_width=True)

st.write("💡 Suggest a video to add to our collection!")

with st.form("video_suggestion"):
    name = st.text_input("Your Name")
    video_url = st.text_input("YouTube Video URL")

    submitted = st.form_submit_button("Submit Suggestion")

    if submitted:
        if video_url.startswith("https://www.youtube.com"):
            st.success("✅ Thank you! Your suggestion will be reviewed.")
        else:
            st.error("❌ Please enter a valid YouTube URL.")

st.markdown("---")
