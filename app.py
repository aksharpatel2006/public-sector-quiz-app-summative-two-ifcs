"""
Main Entry Point for Application
"""

import streamlit as st
from screens.welcome_screen import WelcomeScreen
from screens.info_screen import InfoScreen
from screens.question_screen import QuestionScreen
from models.quiz import Quiz

st.set_page_config(
     page_title="Public Sector Quiz",
     layout="centered"
)

quiz = Quiz("/Users/aksharpatel/Library/Application Support/Coding/quiz_app_ifcs_two/public-sector-quiz-app-summative-two-ifcs/data/questions.csv")

if "screen" not in st.session_state:
    st.session_state.screen = "welcome"

if st.session_state.screen == "welcome":
    WelcomeScreen().render()

elif st.session_state.screen == "info":
    InfoScreen().render()

elif st.session_state.screen == "quiz":
    QuestionScreen(quiz).render()

elif st.session_state.screen == "results":
    st.title("Results Screen Coming In Commit 4")