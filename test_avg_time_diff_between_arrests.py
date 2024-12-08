"""
Test avg_time_diff_between_arrests function of analysist2.py

File: test_avg_time_diff_between_arrests.py
Developer: Swathi Danturi
Date: 12/07/2024
"""

import pytest
from analysis_t2 import AnalysisT2


def test_avg_time_diff_between_arrests_10():
    """
    Test avg_time_diff_between_arrests function of analysist2.py
    with NYPD_Arrest_Data_10_T2.csv for the crime type 'V', Violence
    """
    analysis = AnalysisT2("./data/NYPD_Arrest_Data_10_T2.csv")
    expected = {"K": {"25-44": 0}, "S": {"25-44": 121.0, "18-24": 0}}
    actual = analysis.avg_time_diff_between_arrests("V")
    assert actual == expected


def test_avg_time_diff_between_arrests_50():
    """
    Test avg_time_diff_between_arrests function of analysist2.py
    with NYPD_Arrest_Data_50_T2.csv for the crime type 'V', Violence
    """
    analysis = AnalysisT2("./data/NYPD_Arrest_Data_50_T2.csv")
    expected = {
        "Q": {"25-44": 4.0, "18-24": 17.0, "65+": 33.0},
        "M": {"25-44": 1.0, "18-24": 0.0, "65+": 20.0},
        "K": {"25-44": 0.0, "18-24": 7.0, "45-64": 2.0, "65+": 111.0},
        "B": {"25-44": 6.0, "18-24": 7.0, "45-64": 5.0, "65+": 108.0},
        "S": {"18-24": 78.0, "65+": 0},
    }
    actual = analysis.avg_time_diff_between_arrests("V")
    assert actual == expected


def test_avg_time_diff_between_arrests_100():
    """
    Test avg_time_diff_between_arrests function of analysist2.py
    with NYPD_Arrest_Data_100_T2.csv for the crime type 'V', Violence
    """
    analysis = AnalysisT2("./data/NYPD_Arrest_Data_100_T2.csv")
    expected = {
        "Q": {"45-64": 171.0, "25-44": 74.0, "18-24": 0, "65+": 33.0},
        "K": {"18-24": 34.0, "45-64": 51.0, "25-44": 14.0, "65+": 111.0},
        "M": {
            "18-24": 58.75,
            "65+": 59.0,
            "25-44": 0,
            "45-64": 38.8,
            "<18": 0,
        },
        "B": {"25-44": 59.0, "45-64": 43.67, "18-24": 42.0, "65+": 108.0},
        "S": {"65+": 0},
    }
    actual = analysis.avg_time_diff_between_arrests("V")
    assert actual == expected


pytest.main()
