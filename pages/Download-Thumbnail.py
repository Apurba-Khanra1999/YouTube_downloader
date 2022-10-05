import streamlit as st
from pytube import YouTube

st.set_page_config(
    page_title="Utube thumb",
    page_icon="⚙️",
    layout="wide",
)
st.title("⏬ Download Thumbnail ⏬")

savePath = "D:/Youtube/Thumbnails"
link = st.text_input(label="Youtube Videos Link",placeholder="Paste url")

uTube = YouTube(link)

if st.button("Download Thumbnails ⬇️"):
    st.subheader(uTube.title)
    thumbnail = st.image(uTube.thumbnail_url)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}

            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)