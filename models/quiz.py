"""
Quiz Model
"""

import csv
from models.question import Question


def calculate_percentage(score, total_questions):
        """
        Pure function - calculates quiz percentage.
        """

        return int((score/ total_questions) * 100)

class Quiz:
    """
    Class to handle quiz functionality.
    """

    def __init__(self, csv_file):
        """
        Loads quiz questions
        """

        self.questions = self.load_questions(csv_file)


    def load_questions(self, csv_file):
        """
        Read questions from the CSV file.
        """

        questions = []
        

        try:
            file = open(csv_file, "r", newline="", encoding="utf-8")
            reader = csv.DictReader(file)
            for row in reader:
                question = Question(
                    row["Number"],
                    row["Question"],
                    row["Answer A"],
                    row["Answer B"],
                    row["Answer C"],
                    row["Answer D"],
                    row["Correct Answer"]
                )
                questions.append(question)

        except FileNotFoundError:
            print(f"Questions file not found: {csv_file}")

        return questions