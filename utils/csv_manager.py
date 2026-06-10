"""
Handles the reading and writing of quiz results.
"""

import csv
from datetime import datetime

class ResultManager:
    """
    Manages quiz result storage.
    """

    def __init__(self, file_path):
        """
        Stores the CSV file path.
        """

        self.file_path = file_path

    def save_result(
        self,
        name,
        score,
        percentage,
        result
    ):
        """
        Saving one quiz's result to CSV.
        """

        try:
            with open(self.file_path, mode="a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)

                writer.writerow(
                    [
                        name,
                        score,
                        percentage,
                        result,
                        datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S"
                        )
                    ]
                )

        except Exception as error:
            print(
                f"Error saving result: {error}"
            )

    def load_results(self):
        """
        Loads all saved results.
        """

        results = []

        try:
            with open(
                self.file_path,
                mode="r",
                encoding="utf-8"
            ) as file:
                reader = csv.DictReader(file)

                for row in reader:
                    results.append(row)

        except Exception as error:
            print(
                f"Error loading results: {error}"
            )

        return results
    