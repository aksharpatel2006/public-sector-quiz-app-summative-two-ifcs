"""
Information screen displayed before the quiz begins.
"""

import streamlit as st

class InfoScreen:
    """
    Displays quiz information and instructions.
    """

    def render(self):
        """
        Renders information screen.
        """

        st.title("Public Sector Quiz")

        st.write(
            f"Hi {st.session_state.name}, welcome to the public sector quiz!"
        )

        st.write(
            """
            This quiz will test your knowledge on the public sector, covering key aspects like security, data sensitivity, and ways of working.
            There are 10 multiple choice questions in this quiz. The pass mark is 70%.
            Once you select an answer, press the “Next” button to move on.
            If you fail, you will have to retake the quiz.
            
            When you're ready to take the quiz, press the ready button below.
            """
        )
        
        col1, col2, col3 = st.columns([1, 1, 1])

        with col2:
            if st.button("Ready", use_container_width=True):
                # initialising values of quiz.
                st.session_state.current_question = 0
                st.session_state.score = 0
                st.session_state.user_answers = []
                st.session_state.incorrect_questions = []
                st.session_state.screen = "quiz"
                st.rerun()