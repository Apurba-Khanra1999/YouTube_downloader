import streamlit as st

st.set_page_config(
    page_title="YTools",
    page_icon="⚙️",
    layout="wide",
)

st.title("⬇️ YouTube Multi Downloader ⬇️")
st.markdown("<p style='text-align: left;'>This is a simple YouTube tools where you can download videos, playlists, audios, thumbnails of any resolution just by selecting from the given options.</p>", unsafe_allow_html=True)
st.markdown("     -- User friendly UX/UI")
st.markdown("     -- Download audios,videos, thumbnails, playlists")
st.markdown("     -- High quality content available")
st.markdown(" -----------------------------------------------------------------------------------------------------------------")

st.markdown(" Please feel free to suggest an edit 📝")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}

            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)