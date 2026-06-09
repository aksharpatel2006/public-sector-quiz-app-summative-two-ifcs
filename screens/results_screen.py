"""
Results screen.
"""

import streamlit as st
import pandas as pd

class ResultsScreen:
    """
    Displays quiz results.
    """

    def render(self):
        """
        Renders results screen.
        """
        
        score = st.session_state.score
        total_questions = 10

        percentage = int(
            (score/total_questions)*100
        )
        passed = score >= 7

        st.title("Results")

        st.subheader(
            f"You scored {score}/{total_questions} ({percentage}%)"
        )

        if passed:
            st.success("PASS")
        else:
            st.error("FAIL")

        st.divider()

        st.subheader(
            "Questions you got wrong + correct answers:"
        )

        if len(st.session_state.incorrect_questions) > 0:
            for item in st.session_state.incorrect_questions:
                st.write(
                    f"**{item['question']}**"
                )
                st.write(
                    f"Correct Answer: {item['correct_answer']}"
                )
                st.write("---")

        st.divider()

        chart_data = pd.DataFrame({"Result": ["Correct", "Incorrect"], "Count":[score, total_questions-score]})
        
        st.subheader("Performance")

        st.bar_chart(
            chart_data.set_index("Result")
        )

        st.divider()

        if not passed:
            if st.button("Retry"):
                self.reset_quiz()
                st.rerun()
        else:
            st.success(
                "Congratulations! You passed."
            )

    def reset_quiz(self):
        """
        Reset quiz session.
        """

        st.session_state.screen = "welcome"
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.user_answers = []
        st.session_state.incorrect_questions = []