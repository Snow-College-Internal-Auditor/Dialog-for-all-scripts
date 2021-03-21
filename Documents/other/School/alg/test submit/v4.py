import math
from functools import lru_cache
stops_visited = [1,2,3,4]
students_per_stop = [2,5,10,3]
time_between_stops = [10,5,2]
start_index = 1
total_soda_drank = 0
# assert soda_bus([1,2,3,4], [2,5,10,3], [10,5,2], 0, 0, None, explored) == 251

cached = lru_cache(maxsize=None)
def soda_bus(stops_visited: list, students_per_stop: list, time_between_stops: list, start_index: int):
    students_per_stop[start_index] = 0
    sum_of_students_left = sum(students_per_stop)
    sum_of_students_left -= students_per_stop[start_index]
    sub_total = []

    # this method will evaluate the cost of going left or right at a given stop. If a stop has already been visited 
    # we will go to the next no visited stop. If we get to the last stop on the right or left side we will check if we can 
    # go the other way and if we cant we will return a aributray big number. Once we get to the end we will return the min 
    # cost for the choices we made go left or going right
    @cached
    def sub_soda_bus(current_exit: int, right_index: int, lef_index: int, last_stop: int, sum_of_students_left: int):
        if sum_of_students_left <= 0:
            return sum(sub_total)

        if current_exit >= len(stops_visited):
            return float('inf')

        if current_exit < 0:
            return float('inf')
            

        time_between_two_stops = get_time_traveld(last_stop, time_between_stops, current_exit)
        total_soda_drank = time_between_two_stops * sum_of_students_left
        sum_of_students_left -= students_per_stop[current_exit]
        sub_total.append(total_soda_drank)
        go_right = sub_soda_bus(right_index + 1, right_index + 1, lef_index, current_exit, sum_of_students_left)
        go_left = sub_soda_bus(lef_index - 1, right_index, lef_index - 1, current_exit, sum_of_students_left)
        return min(go_right, go_left)
    


    return sub_soda_bus(start_index, start_index, start_index, start_index, sum_of_students_left)

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




