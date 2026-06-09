"""
Main Entry Point for Application
"""

import streamlit as st
from screens.welcome_screen import WelcomeScreen
from screens.info_screen import InfoScreen

st.set_page_config(
     page_title="Public Sector Quiz",
     layout="centered"
)

if "screen" not in st.session_state:
    st.session_state.screen = "welcome"

if st.session_state.screen == "welcome":
    WelcomeScreen().render()

elif st.session_state.screen == "info":
    InfoScreen().render()

elif st.session_state.screen == "quiz":
    st.title("Quiz Screen Coming soon..")