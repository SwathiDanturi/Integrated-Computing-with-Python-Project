"""
Test the method to determine which borough has the highest number of felony
arrests and the most common felony offense in that borough.

File: test_highest_felony_offense_in_borough.py
Developer: Olivia LaCroix
Date: 11/30/2024
"""

import pytest
from analysis_t1 import AnalysisT1


def test_highest_felony_offense_in_borough_10_t1():
    """Use NYPD_Arrest_Data_10.csv to test highest_felony_offense_in_borough.
    """
    arrest_file = "./data/NYPD_Arrest_Data_10_T1.csv"
    analysis_obj = AnalysisT1(arrest_file)
    actual = analysis_obj.highest_felony_offense_in_borough()
    expected = ("M", "LARCENY,GRAND FROM OPEN AREAS, UNATTENDED", 2)
    assert actual == expected


def test_highest_felony_offense_in_borough_50_t1():
    """Use NYPD_Arrest_Data_50.csv to test highest_felony_offense_in_borough.
    """
    arrest_file = "./data/NYPD_Arrest_Data_50_T1.csv"
    analysis_obj = AnalysisT1(arrest_file)
    actual = analysis_obj.highest_felony_offense_in_borough()
    expected = ("K", "ASSAULT 2,1,UNCLASSIFIED", 2)
    assert actual == expected


def test_highest_felony_offense_in_borough_100_t1():
    """Use NYPD_Arrest_Data_100.csv to test highest_felony_offense_in_borough.
    """
    arrest_file = "./data/NYPD_Arrest_Data_100_T1.csv"
    analysis_obj = AnalysisT1(arrest_file)
    actual = analysis_obj.highest_felony_offense_in_borough()
    expected = ("K", "ROBBERY,OPEN AREA UNCLASSIFIED", 4)
    assert actual == expected


pytest.main()
