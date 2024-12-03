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
                csv_reader = csv.DictReader(csv_file, delimiter=",", quotechar='"')
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

    def most_arrests_day_most_common_race(self):
        """This method identifies the day with the highest number of arrests.
        The method then identifies which perpetrator by race was arrested the
        most on that day. The method returns a tuple with the date and the
        race of the perpetrator who were arrested the most on that day.
        """

        arrests_per_day = {}
        arrests_by_race_on_max_day = {}

        for arrest in self.arrests:
            arrest_date = arrest["ARREST_DATE"]

            if arrest_date in arrests_per_day:
                arrests_per_day[arrest_date] += 1
            else:
                arrests_per_day[arrest_date] = 1

        max_arrests_per_day = max(arrests_per_day, key=arrests_per_day.get)

        for arrest in self.arrests:
            if arrest["ARREST_DATE"] == max_arrests_per_day:
                perp_race = arrest["PERP_RACE"]

                if perp_race in arrests_by_race_on_max_day:
                    arrests_by_race_on_max_day[perp_race] += 1
                else:
                    arrests_by_race_on_max_day[perp_race] = 1

        most_common_race = max(
            arrests_by_race_on_max_day, key=arrests_by_race_on_max_day.get
        )
        print(
            f"The day with the most arrests was: {max_arrests_per_day}, "
            f"the most common perpetrator race on that day was: "
            f"{most_common_race}"
        )
        return max_arrests_per_day, most_common_race
