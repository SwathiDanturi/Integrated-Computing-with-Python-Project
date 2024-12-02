"""
Test crime_most_committed_agegroup function of analysis_t2.py

File: test_crime_most_committed_agegroup.py
Developer: Swathi Danturi
Date: 12/01/2024
"""

import pytest
from analysis_t2 import Analysis


def test_crime_most_committed_agegroup_10():
    """
    Test crime_most_committed_agegroup function of analysis_t2.py
    with NYPD_Arrest_Data_10_T2.csv
    for the crime type 'Intoxicated & Impaired Driving'
    """
    analysis = Analysis("./data/NYPD_Arrest_Data_10_T2.csv")
    expected = (['25-44', '18-24'], 2, '3:1')
    actual = analysis.crime_most_committed_agegroup('DRIVING')
    assert actual == expected


def test_crime_most_committed_agegroup_50():
    """
    Test crime_most_committed_agegroup function of analysis_t2.py
    with NYPD_Arrest_Data_50_T2.csv
    for the crime type 'Intoxicated & Impaired Driving'
    """
    analysis = Analysis("./data/NYPD_Arrest_Data_50_T2.csv")
    expected = (['25-44', '<18', '65+'], 3, '9:4')
    actual = analysis.crime_most_committed_agegroup('DRIVING')
    assert actual == expected


def test_crime_most_committed_agegroup_100():
    """
    Test crime_most_committed_agegroup function of analysis_t2.py
    with NYPD_Arrest_Data_100_T2.csv
    for the crime type 'Intoxicated & Impaired Driving'
    """
    analysis = Analysis("./data/NYPD_Arrest_Data_100_T2.csv")
    expected = (['65+', '25-44'], 7, '22:3')
    actual = analysis.crime_most_committed_agegroup('DRIVING')
    assert actual == expected


pytest.main()
