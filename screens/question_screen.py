"""
Questions screen.
"""

import streamlit as st

class QuestionScreen:
    """
    Displays quiz questions to user.
    """

    def __init__(self, quiz):
        """
        Stores quiz instance.
        """

        self.quiz = quiz

    def render(self):
        """
        Render current question.
        """

        current_index = st.session_state.current_question

        question = self.quiz.questions[current_index]

        st.subheader(
            f"Question {current_index + 1}"
        )

        st.write(question.question_text)

        user_answer = st.radio(
            "Select your answer:",
            [
                ("A", question.answer_a),
                ("B", question.answer_b),
                ("C", question.answer_c),
                ("D", question.answer_d)
            ],
            format_func=lambda x: f"{x[0]}. {x[1]}",

            key=f"question_{current_index}"
        )

        if st.button("Next"):

            selected_letter = user_answer[0]

            st.session_state.user_answers.append(
                selected_letter
            )

            if selected_letter == question.correct_answer:
                st.session_state.score += 1
            else:
                st.session_state.incorrect_questions.append(
                    {
                        "question": question.question_text,
                        "correct_answer": question.correct_answer
                    }
                )

            st.session_state.current_question += 1

            if (
                st.session_state.current_question
                >= len(self.quiz.questions)
            ):
                st.session_state.screen = "results"


            st.rerun()