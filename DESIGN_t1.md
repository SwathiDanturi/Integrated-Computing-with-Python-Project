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