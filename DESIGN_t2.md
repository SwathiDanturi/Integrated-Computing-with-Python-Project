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

### Design of avg_time_diff_between_arrests() method
- define a new method in `analysis_t2.py` called `crime_most_committed_agegroup`.
- `self` is the current instance of the class.
- `self.arrests` is the instance variable of the class.
    - the elements of the list are dictionaries.
    - each dictionary corresponds to a row in the text file.
- `crime_type` is passed as an argument, to calculate the average time difference of arrests of that `crime_type` for each `BOROUGH` and each `AGE_GROUP`.
- define an accumulator `time_diff`and initialize it to a empty dictionary.
- `time_diff` is used to store the time differences between all the consecutive arrest dates.
- define one more empty dictionary `arrest_days`, an accumulator to store the arrest dates of each borough according to age groups.
- using `for` loop, iterate through each `arrest` record of `self.arrests` and at each iteration:
    - check whether `crime_type` is in `arrest['LAW_CAT_CD']` using `if`:
        - if yes, then assign the value of borough available at `arrest["ARREST_BORO"]` to the variable `boro`.
        - and also assign the value of age group available at `arrest["AGE_GROUP"]` to the varibale `age_group`.
        - now, split the arrest date with `"/"` as delimiter at `arrest["ARREST_DATE"]` uaing `split()` method.
        - convert the result of above step to a tuple of intergers using `map()` and then packing them into a tuple.
        - assgin this tuple to a local variable called `arrest_date`.
        - check `if` `boro` is in `arrest_days`:
            - if no, initialize the value of `arrest_days` for the key `boro` to an empty dictionary.
        - check `if` `age_group` is in `arrest_days[boro]`:
            - if no, initialize the value of `arrest_days[boro]` for the key `age_group` to an empty list.
        - append the `arrest_date` to the list `arrest_days[boro][age_group]`.
- iterate through `arrest_days.items` with `boro, age_groups` as iterators and at each iteration:
    - `if` `boro` is not in `time_diff`, then initialize `time_diff[boro]` to an empty dictionary.
    - using `for` loop, iterate through the items of `age_groups.items` with `age_groups, dates` as iterators and at each iteration:
        - assign the sorted list of `dates` obtained using `sorted()` function to a variable called `dates`.
        - define an empty list called `diffs` to store the list of differences of each consecutive arrest dates.
        - now iterate through `dates` using `range()` function on `length-1` of `dates` with `i` as iterator.
            - call the `date_diff` instance method by passing `dates[i] and dates[i+1]` as arguments.
            - append the `return` value of the above method to `diffs`.
        - if the list `diffs` is not empty then:
            - find the average time difference by dividing the sum of `diffs` by length of `diffs` obtained using `sum()` and `len()` respectively.
            - typecast the average value to float and assign it to a local variable called `avg_time_diff`.
            - round off the average to 2 decimal value using `round()` and assign it to `time_diff[boro]` at the key `age_group`.
        - else,
            - assign `zero` to `time_diff[boro]` at the key `age_group`.
- declare an empty dictionary called `result` to store average time difference of `crime_type` for each `AGE_GROUP` of each `ARREST_BORO` in a readable format.
- iterate through `time_diff.items()` using the iterators `boro, age_group`:
    - initialize `result[boro]` to an empty dictionary.
    - iterate through `age_group.items()` using the iterators `age, time`:
        - at `result[boro][age]` store the value of `time`
- return the dictionary `result`.

### Design of date_diff() instance method
### used to calculate the difference between dates and is called from avg_time_diff_between_arrests() method
- define a new method in `analysis_t2.py` called `date_diff`.
- `self` is the current instance of the class.
- `date1`, `date2` are the two parameters of type tuple for the method whose difference needs to be calculated.
- unpack the tuple `date1` into varibales `m1`, `d1`, `y1`.
- unpack the tuple `date2` into varibales `m2`, `d2`, `y2`.
- calculate number of days in `date1` type casted to float, using the calculation `y1 * 365 + m1 * 30 + d1` and assign it to `days1`.
- calculate number of days in `date2` type casted to float, using the calculation `y2 * 365 + m2 * 30 + d2` and assign it to `days2`.
- return the difference `days2 - days1`.