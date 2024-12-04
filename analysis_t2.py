"""
Analysis of data from NYC OpenData about NYPD Arrest Data (Year to Date).

File: analysis_t2.py
Initial developers: Swathi Danturi
Date: 11/29/2024
Data source:
https://data.cityofnewyork.us/Public-Safety/NYPD-Arrest-Data-Year-to-Date-/uip8-fykc/about_data
"""

import csv


class AnalysisT2:
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

        :param file_path: str, path of CSV file, relative to `analysis_t2.py`
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

    def crime_most_committed_agegroup(self, crime_type):
        """
        For a given crime type, finding the age group of the perpetrator
        that has committed the most number of crimes and also find the ratio
        of the crime count between Male and Female
        Returns a tuple with the following elements:
        - age group(s) that has committed the most number of crimes
        - count of crimes committed by the age group(s)
        - ratio of crime count between `Male` and `Female`
        """
        age_group_crime_count = {}
        gender = {"M": 0, "F": 0}
        for arrest in self.arrests:
            if crime_type in arrest["PD_DESC"]:
                if arrest["AGE_GROUP"] not in age_group_crime_count:
                    age_group_crime_count[arrest["AGE_GROUP"]] = 0
                age_group_crime_count[arrest["AGE_GROUP"]] += 1
                gender[arrest["PERP_SEX"]] += 1
        highest_crime_count = max(age_group_crime_count.values(), default=0)
        highest_count_age_groups = [
            age_group
            for age_group, count in age_group_crime_count.items()
            if count == highest_crime_count
        ]
        ratio = str(gender["M"]) + ":" + str(gender["F"])
        result_string = f"""
The age group(s) that has committed the most number of crimes,
for the crime type '{crime_type}' is/are
{highest_count_age_groups}, with a count of '{highest_crime_count}'.
Ratio of crime count between Male and Female is
'{ratio}'.
"""
        print(result_string)
        return (highest_count_age_groups, highest_crime_count, ratio)
