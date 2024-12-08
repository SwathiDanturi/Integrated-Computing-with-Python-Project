"""
Test the functionality of the methods implemented in
analysis_t1.py and analysis_t2.py.

File: client.py
Date: 12/04/2024
Developers: Olivia LaCroix, Swathi Danturi
"""

from analysis_t1 import AnalysisT1
from analysis_t2 import AnalysisT2


def main():
    """
    Demo the functionality of the methods implemented in AnalysisT1 and
    AnalysisT2.
    To run this module, in Terminal,
    select bash and change directory to PROJECT directory.
    Then, either use the arrow in upper-right corner, or,
    in the Terminal, run: python client.py
    """
    # Analysis1
    analysis1 = AnalysisT1("./data/NYPD_Arrest_Data_50_T1.csv")
    result = analysis1.most_arrests_day_most_common_race()
    print(result)

    # Analysis2
    analysis2 = AnalysisT2("./data/NYPD_Arrest_Data_50_T2.csv")
    result = analysis2.crime_most_committed_agegroup("DRIVING")
    print(result)
    result = analysis2.avg_time_diff_between_arrests("V")
    print(result)


main()
