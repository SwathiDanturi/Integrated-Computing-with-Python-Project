"""
Analysis of data from NYC OpenData about NYPD Arrest Data (Year to Date).

File: analysis_t1.py
Initial developers: Olivia LaCroix and Swathi Danturi
Date: 11/29/2024
Data source:
https://data.cityofnewyork.us/Public-Safety/NYPD-Arrest-Data-Year-to-Date-/uip8-fykc/about_data
Developer: Olivia LaCroix
"""

import csv


class Analysis:
    """
    Analyze arrest(s) and related crime data from NYC OpenData,
    about arrests completed by New York Police Department.
    """

    def __init__(self, file_path):
        """
        Initialize instance variable `self.arrests` list with dictionary
        objects.
        A dictionary object has:
            keys: strings from the fields in the 1st row of the CSV file
            values: strings with information corresponding to the keys

        :param file_path: str, path of CSV file, relative to `analysis.py`
            module. The file has a heading 1st row, followed by rows that have
            data about arrests completed by New York Police Department that
            was collected and published by NYC OpenData
            https://data.cityofnewyork.us/Public-Safety/NYPD-Arrest-Data-Year-to-Date-/uip8-fykc/about_data:
                one respondent per row and one column per answer.
        :return: Analysis object
        """
        self.arrests = []
        try:
            with open(file_path, mode="r", encoding="utf-8") as csv_file:
                csv_reader = csv.DictReader(
                    csv_file, delimiter=",", quotechar='"'
                )
                self.arrests = list(csv_reader)
        except IOError as err:
            print(err)

    def __str__(self):
        """
        Returns string representation of the list `self.arrests`. The elements
        of the list are dictionaries. Each dictionary corresponds to a row
        in the text file located at `file_path`.
        """
        return self.arrests
