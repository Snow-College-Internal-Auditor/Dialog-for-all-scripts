from functools import lru_cache
from typing import final


cached = lru_cache(maxsize=None)
cached_2 = lru_cache(maxsize=None)

def soda_bus(stops_visited: list, students_per_stop: list, time_between_stops: list, start_index: int):
    students_per_stop[start_index] = 0
    sum_of_students_left = sum(students_per_stop)
    sum_of_students_left -= students_per_stop[start_index]
    sub_total = []
    final_results = []

    """At every stop we ask are selves in this algorithm what is the cost if i know go right and what is the cost if I know go left.
    When then break up the problem by going right and finding that cost, line 41, and going left and finding that cost, also line 41. The process continuies 
    unilt we have either dropped off all the students, so visited all the stops, or we can no longer go left or right. If we have 
    visited all the stops we return the total of all the decisions up to this point. If we try to go to a stop that is not there. So, 
    go out of bounds, then we return an arbitray big number. Once we can no longer go left or right we append the losest cost to a final_result
    clear are sub paths and start back from the first valid choice. Once we have explored all possible routes we then return the lowest cost. 
    That part that we cache it that subproblem of the cost of going left or right. I also cashed the part that totals the time to trival from
    point a to b. 
    subproblems/divide: Cost of going left vs cost of going right. I divide the problem by going left and determing the cost and going right 
    from the same starting point and determing the cost
    re-combine:Once we have gone through all possible stops we return the cost of all associated subproblems. 
    """
    @cached
    def sub_soda_bus(current_exit: int, right_index: int, lef_index: int, last_stop: int, sum_of_students_left: int):
        if sum_of_students_left <= 0:
            return sum(sub_total)

        if current_exit >= len(stops_visited):
            return float('inf')

        if current_exit < 0:
            return float('inf')
            

        time_between_two_stops = get_time_traveld(last_stop, tuple(time_between_stops), current_exit)
        total_soda_drank = time_between_two_stops * sum_of_students_left
        sum_of_students_left -= students_per_stop[current_exit]
        sub_total.append(total_soda_drank)

        go_right = sub_soda_bus(right_index + 1, right_index + 1, lef_index, current_exit, sum_of_students_left)
        go_left = sub_soda_bus(lef_index - 1, right_index, lef_index - 1, current_exit, sum_of_students_left)
        final_results.append(min(go_right, go_left))
        sub_total.clear()

        return min(final_results)
    


    return sub_soda_bus(start_index, start_index, start_index, start_index, sum_of_students_left)

@cached_2
def get_time_traveld(start_index, time_between_stops, next_stop_index):
    total_time_traveld_between_two_stops = 0
    if start_index > next_stop_index:
        start_index , next_stop_index = next_stop_index, start_index
    for i in range(start_index, next_stop_index):
        total_time_traveld_between_two_stops += time_between_stops[i]
    return total_time_traveld_between_two_stops


def test_total_soda_drank_for_1_stop():
    assert soda_bus([1], [10], [0], 0) == 0

def test_total_soda_drank_for_2_stops():
    assert soda_bus([1,2], [5, 10], [10], 0) == 100
    assert soda_bus([1,2], [5, 10], [10], 1) == 50


def test_total_soda_drank_for_3_stops():
    assert soda_bus([1,2,3], [2,5,10], [10,5], 0) == 200
    assert soda_bus([1,2,3], [2,5,10], [10,5], 1) == 90
    assert soda_bus([1,2,3], [2,5,10], [10,5], 2) == 55

def test_total_soda_drank_for_4_stops():
    assert soda_bus([1,2,3,4], [2,5,10,3], [10,5,2], 0) == 251
    assert soda_bus([1,2,3,4], [2,5,10,3], [10,5,2], 1) == 119
test_total_soda_drank_for_4_stops()




