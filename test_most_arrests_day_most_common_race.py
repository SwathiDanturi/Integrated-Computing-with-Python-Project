"""
Test the method to determine the day with the most arrests and the most common
race of the perpetrator on that day.

File: test_most_arrests_day_most_common_race.py
Developer: Olivia LaCroix
Date: 11/29/2024
"""

from analysis_t1 import Analysis


def test_most_arrests_day_most_common_race_10_t1():
    """Use NYPD_Arrest_Data_10.csv to test most_arrests_day_most_common_race.
    """
    arrest_file = "./data/NYPD_Arrest_Data_10_T1.csv"
    analysis_obj = Analysis(arrest_file)
    actual = analysis_obj.most_arrests_day_most_common_race()
    expected = ("1/1/2024", "BLACK")
    assert actual == expected


def test_most_arrests_day_most_common_race_50_t1():
    """Use NYPD_Arrest_Data_50.csv to test most_arrests_day_most_common_race.
    """
    arrest_file = "./data/NYPD_Arrest_Data_50_T1.csv"
    analysis_obj = Analysis(arrest_file)
    actual = analysis_obj.most_arrests_day_most_common_race()
    expected = ("1/1/2024", "BLACK")
    assert actual == expected


def test_most_arrests_day_most_common_race_100_t1():
    """Use NYPD_Arrest_Data_100.csv to test most_arrests_day_most_common_race.
    """
    arrest_file = "./data/NYPD_Arrest_Data_100_T1.csv"
    analysis_obj = Analysis(arrest_file)
    actual = analysis_obj.most_arrests_day_most_common_race()
    expected = ("3/1/2024", "BLACK")
    assert actual == expected
