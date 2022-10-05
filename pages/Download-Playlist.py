import streamlit as st
from pytube import Playlist

st.set_page_config(
    page_title="Utube Playlist",
    page_icon="⚙️",
    layout="wide",
)

st.title("⏬ 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗬𝗼𝘂𝗧𝘂𝗯𝗲 𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁⏬")
fetchPlayList = st.text_input(label="Playlist URL",placeholder="Paste link")
resolutions = st.selectbox("Select resolution",("144p","240p","360p","480p","720p","1080p"))
savePath = "D:/Youtube/Playlists"
playList = Playlist(fetchPlayList)

if st.button(label="Download Playlist ⬇️"):
    st.header(playList.title)
    for i in playList.videos:
        st.subheader(f'Downloading.. {i.title}')
        #i.streams.first().download()
        i.streams.filter(res=resolutions).first().download(savePath)
        st.success(f"Successfully downloaded {i.title}")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}

            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)