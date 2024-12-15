## Project: New York City's Crime Data in 2024
### Developers: 
- T1: Olivia LaCroix
- T2: Swathi Danturi

## Project Overview
This project analyzes data from NYC OpenData about NYPD Arrest Data (Year to Date). The analysis includes identifying patterns in arrests, such as the most common crimes, the demographics of perpetrators, and the time differences between arrests.

## Data Source
- Name: NYPD Arrest Data (Year to Date)
- Link: [NYPD Arrest Data (Year to Date)](https://data.cityofnewyork.us/Public-Safety/NYPD-Arrest-Data-Year-to-Date-/uip8-fykc/about_data)
- Catalog: [Catalog of the dataset](https://catalog.data.gov/dataset/nypd-arrest-data-year-to-date)

## Client Overview 
- Demo the functionality of the methods implemented in AnalysisT1 and
    AnalysisT2. 
- To run this module, in Terminal, select bash and change directory to <name> directory.
- Then, either use the arrow in upper-right corner, or, in the Terminal, run: python client.py

## Analysis Overview
Analysis_t1
- `most_arrests_day_most_common_race()`: Identifies the day with the highest number of arrests and the most common race of the perpetrators on that day.
- `highest_felony_offense_in_borough()`: Determines which borough has the highest number of felony arrests and the most common felony offense in that borough.

Analysis_t2
- `crime_most_committed_agegroup(crime_type)`: Finds the age group that has committed the most number of crimes for a given crime type and the ratio of crime count between Male and Female.
- `avg_time_diff_between_arrests(crime_type)`: Calculates the average time difference in days between arrests for a given crime type, according to the age group of the perpetrator.

## Testing Overview
- Each method has 1 testing file, named as follows, each with 3 testing function, with the name `testing_file_name_#` where `#` defines the number of the records in the file used for testing
  - `test_most_arrests_day_most_common_race.py` for Analysis_t1
  - `test_highest_felony_offense_in_borough.py` for Analysis_t1
  - `test_crime_most_committed_agegroup.py` for Analysis_t2
  - `test_avg_time_diff_between_arrests.py` for Analysis_t2
- To run test files, either use the arrow in upper-right corner, or, in the Terminal, run: pytest test_file_name.py
  
## Data Documentation
- For detailed information about the dataset, refer to `PROPOSAL.md` file.
- For detailed information about how to run the program, refer to `HOWTO.md` file.
- For installing the packages required to run this program, install - `requirements.txt`
- For detailed information about the dataset, the questions, solution and testing refer to `REPORT.md`.

## Design Documents
- Design Document for Analysis_t1 - DESIGN_t1.md
- Design Document for Analysis_t2 - DESIGN_t2.md

## License
This dataset is licensed under the MIT License.
