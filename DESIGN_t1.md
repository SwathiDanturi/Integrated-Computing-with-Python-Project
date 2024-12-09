## Analysis Class Design Document
- Developer: Olivia LaCroix
- Date: 11/30/2024

### most_arrests_day_most_common_race() method
1. Initialize an empty dictionary `{}` called `arrests_per_day` to store the arrests on each day.
2. Initialize another empty dictionary `{}` called `arrests_by_race_on_max_day` to hold the number of arrests by a race on the day with the highest number of arrests. 
3. Create a for loop with the loop variable `arrests` and iterate over the `self.arrests` list which each item represents an arrest record. 
    - store the `"ARREST DATE"` column information in the variable `arrest_date`
    - if the `arrest_date` exists in the dictionary `arrests_per_day` then increase that key in the `arrests_per_day` dictionary by `1`
    - else, add the `arrest_date` to the dictionary by adding `1`
4. Find the day with the highest number of arrests by using the `max()` built-in function with `.get` on `arrests_per_day` which gets the key arrest date with the highest number of arrests. Store it in `max_arrests_per_day`.
5. Create another for loop for `arrests` in `self.arrests`
    - if the `arrest_date` is equal to `==` the `max_arrests_per_day`, store it in `perp_race`
    - if `perp_race` is in `arrests_by_race_on_max_day` dictionary, then increase the value by `1`
    - else, add the `perp_race` to the dictionary and initialize the count to `1`.
6. Use the `max()` built-in function again to find the arrest counts by race on the highest arrest day with `.get` on `arrests_by_race_on_max_day`
7. For this method, use the print statements to give a clear result;
print `f"The day with the most arrests was: {max_arrests_per_day}, "`
            `f"the most common perpetrator race on that day was: "`
8. Then `return` a tuple containing `max_arrests_per_day, most_common_race`

### highest_felony_offense_in_borough() method
1. Initialize an empty dictionary `{}` called `borough_dict` which stores data from each borough with the key being the felony offense and the value being the frequency. 
2. Create a for loop to iterate over `self.arrests` which contains a list of arrest records data using the loop variable `arrest`. 
    - at each step check if the arrest category called `LAW_CAT_CD` is a felony offense by seeing if it is equal to `'F'` in order to filter by felony offenses
        - assign the borough from `"ARREST_BORO"` in the arrest dictonary to `borough` 
        - assign the offense from `"PD_DESC"` in the arrest dictionary to `offense` 
        - check if the `borough` is already in `borough_dict` 
            - if it is not, add the borough by initializing a dictionary with the keys. Since it is not in the dictionary yet, set the `"arrest_count"` to `0` and `"offenses"` to an empty dictonary `{}` to account for the different felony offenses.
        - Then, increase the `"arrest_count"` by `1` in the specific borough every time the type of felony arrest is found. 
        - to count the offenses, check if the `offense` is already in borough `"offenses"` dictionary, and if it is, increase that offense type by `1`.
        - otherwise, if the `offense` is not yet counted, create the `offense` and add to the `"offenses"` dictionary by initializing it with `1`.
3. Create a variable called `most_felony_arrests_borough` to track the names of the boroughs with the most arrests and set it to `None`.
4. Create a variable called `max_arrest_count` to store the borough with the highest number felony arrests and set it to `0`. 
5. Create a for loop with two loop variables called `borough` and `data` to iterate through `borough_dict` using the `.items()` method. This will loop through both loop variables at the same time in the dictionary. 
    - if the `"arrest_count"` for the borough is greater than `>` the `max_arrest_count` then update the following:
        - update `most_felony_arrests_borough` with the new `borough` 
        - update `max_arrest_count` with the borough with the most felony arrests using `data['arrest_count']`
6. Initialize a new variable to track the `most_committed_offense` in the borough with the most felony offenses and set it to `None`
7. Intialize another new variable to track the `max_offense_count` to track how many times that offense occurred and set it to `0`.
8. Create a for loop with two loop variables called `offense` and `count` to iterate over the `most_felony_arrests_borough` using `items()` method in the `borough_dict` which is a dictionary where the borough is the key. The `.items()` method will return a tuple which contains the `offense` which is the name of the felony offense and `count` which is the number of times that offense was committed in the borough with the most arrests.
    - if the `count` is greater `>` than the `max_offense_count`
        - update the `most_committed_offense` with the new most committed `offense`
        - update the `max_offense_count` with the offense most committed by `count` 
9. For this method, use the print statements to give a clear result; print 
        `f"The borough with the highest number of felony arrests was: "{most_felony_arrests_borough}."` and `f"The most committed felony offense being " {most_committed_offense} with {max_offense_count} occurrence(s)."`
10. Then `return` a tuple containing `most_felony_arrests_borough,      most_committed_offense, max_offense_count`
