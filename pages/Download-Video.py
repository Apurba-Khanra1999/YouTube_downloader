import streamlit as st
from pytube import YouTube

st.set_page_config(
    page_title="Utube video",
    page_icon="⚙️",
    layout="wide",
)

st.title("⏬ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐯𝐢𝐝𝐞𝐨𝐬⏬")

savePath = "D:/Youtube/Videos"
link = st.text_input(label="Youtube Videos Link",placeholder="Paste url")
res = st.selectbox("Select resolution",("144p","240p","360p","480p","720p","1080p"))


if st.button(label="Download Video ⬇️"):
    uTube = YouTube(link)
    st.subheader(uTube.title)

    #streamList = uTube.streams.all()

    streamList = uTube.streams.filter(resolution=res,progressive=True)
    videosList = list(enumerate(streamList))
    for i in videosList:
        st.subheader("Downloading . . . ")
    streamList[0].download(savePath)
    st.success(f"Downloaded successfully\n {streamList[0].title} to {savePath}")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}

            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

