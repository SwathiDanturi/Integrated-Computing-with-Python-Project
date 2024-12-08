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
        :return: AnalysisT2 object
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
'{ratio}'."""
        print(result_string)
        return (highest_count_age_groups, highest_crime_count, ratio)

    def date_diff(self, date1, date2):
        """
        calculates the difference in days between two dates
        called by the method avg_time_diff_between_arrests()
        """
        m1, d1, y1 = date1
        m2, d2, y2 = date2
        days1 = float(y1 * 365 + m1 * 30 + d1)
        days2 = float(y2 * 365 + m2 * 30 + d2)
        return days2 - days1

    def avg_time_diff_between_arrests(self, crime_type):
        """
        For each borough, finding the average time difference in days
        between the arrests for the crime type passed as an argument,
        according to the age group of the perpetrator
        """
        time_diff = {}
        arrest_days = {}
        for arrest in self.arrests:
            if arrest["LAW_CAT_CD"] == crime_type:
                boro = arrest["ARREST_BORO"]
                age_group = arrest["AGE_GROUP"]
                arrest_date = tuple(map(int, arrest["ARREST_DATE"].split("/")))
                if boro not in arrest_days:
                    arrest_days[boro] = {}
                if age_group not in arrest_days[boro]:
                    arrest_days[boro][age_group] = []
                arrest_days[boro][age_group].append(arrest_date)
        for boro, age_groups in arrest_days.items():
            if boro not in time_diff:
                time_diff[boro] = {}
                for age_group, dates in age_groups.items():
                    dates = sorted(dates)
                    diffs = [
                        self.date_diff(dates[i], dates[i + 1])
                        for i in range(len(dates) - 1)
                    ]
                    if diffs:
                        avg_time_diff = float(sum(diffs) / len(diffs))
                        time_diff[boro][age_group] = round(avg_time_diff, 2)
                    else:
                        time_diff[boro][age_group] = 0
        result = {}
        for boro, age_group in time_diff.items():
            result[boro] = {}
            for age, time in age_group.items():
                result[boro][age] = time
        print(
            "The Average time difference between arrests for each borough, "
            "for each age group is of crime type",
            crime_type,
            "is:",
        )
        return result
