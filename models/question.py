"""
Question Model
"""

class Question:
    """
    Class for modelling a single quiz question.
    """

    def __init__(self, question_number, question_text, answer_a, answer_b, answer_c, answer_d, correct_answer):
        """
        Creates the Question object and initialises its values.
        """

        self.question_number = question_number
        self.question_text = question_text
        self.answer_a = answer_a
        self.answer_b = answer_b
        self.answer_c = answer_c
        self.answer_d = answer_d
        self.correct_answer = correct_answer
        