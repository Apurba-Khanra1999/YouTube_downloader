import streamlit as st
from pytube import YouTube

st.set_page_config(
    page_title="Utube Audio",
    page_icon="⚙️",
    layout="wide",
)

st.markdown("<h1 style='text-align: center;'>⏬ Download Audio ⏬</h1>", unsafe_allow_html=True)

savePath = "D:/Youtube/Audios"
link = st.text_input(label="Youtube Videos Link",placeholder="Paste url")

if st.button(label="Download Audio ⬇️"):
    uTube = YouTube(link)
    st.subheader(uTube.title)
    streamList = uTube.streams.filter(only_audio=True)
    videosList = list(enumerate(streamList))
    for i in videosList:
        st.write(i)
    download=streamList[0].download(savePath)
    st.success(f"Downloaded successfully\n {streamList[0].title} to {savePath}")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


