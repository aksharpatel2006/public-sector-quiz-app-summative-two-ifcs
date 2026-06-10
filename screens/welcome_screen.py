"""
Welcome screen for the quiz application.
"""

import streamlit as st
from utils.validation import validate_name_input

class WelcomeScreen:
    """
    Handles the rendering of app's welcome page.
    """

    def render(self):
        """
        Renders the welcome page.
        """

        st.title("Welcome")

        st.write(
            """
            Welcome to the Public Sector Quiz.
            """
        )

        name = st.text_input(
            "Please enter your name:"
        )

        name = name.capitalize()
        
        if st.button("OK"):
            valid, message = validate_name_input(name)

            if not valid:
                st.error(message)
            else:
                st.session_state.name = name
                st.session_state.screen = "info"
                st.rerun()