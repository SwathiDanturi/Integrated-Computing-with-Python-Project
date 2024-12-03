## Design Document of Analysis class of analysis_t2
- File name: DESIGN_t2.md
- Developer: Swathi Danturi
- Date: 12/01/2024

### Design of crime_most_committed_agegroup() method
- define a new method in `analysis_t2.py` called `crime_most_committed_agegroup`.
- `self` is the current instance of the class.
- `self.arrests` is the instance variable of the class.
    - the elements of the list are dictionaries.
    - each dictionary corresponds to a row in the text file.
- `crime_type` is passed as an argument, to find the age group that has committed it the most.
- declare an accumulator `age_group_crime_count` and initialize it to an empty dictionary, to store the crime count of the age groups.
- declare one more accumulator `gender`, to hold the crime count by gender and intialize the values of keys `M` and `F` of it to `0`.
- using `for` loop iterate through each `arrest` record of `self.arrests` and at each iteration:
    - check whether `crime_type` is in `arrest['PD_DESC']` using `if`
        - now, `if` `arrest['AGE_GROUP']` is `not in` the dictionary `age_group_crime_count`, then:
            - intialize the value of `age_group_crime_count` for the key `arrest['AGE_GROUP']` to zero.
        - increment the value of `age_group_crime_count` for the key `arrest['AGE_GROUP']` by 1.
        - also increase the count of the value `gender` for the key `arrest[PERP_SEX]` by 1.
- assign the max value from the `age_group_crime_count` to the variable `highest_crime_count` using `max()' function with default value as zero.
- `highest_crime_count` holds the maximum count of crime committed.
- to the list `highest_count_age_groups` assign all the `keys` of `age_group_crime_count` whose count equals `highest_crime_count` using `.items()`.
- `highest_count_age_groups` list has the list of age groups which has committed the crime most.
- assign the ratio of `gender['M'] : gender['F']` obtained using string concatenation to `ratio`.
- return the tuple `(highest_count_age_groups, highest_crime_count, ratio)`.
