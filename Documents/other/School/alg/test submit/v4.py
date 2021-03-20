import math
from functools import lru_cache
stops_visited = [1,2,3,4]
students_per_stop = [2,5,10,3]
time_between_stops = [10,5,2]
start_index = 1
total_soda_drank = 0
# assert soda_bus([1,2,3,4], [2,5,10,3], [10,5,2], 0, 0, None, explored) == 251

cached = lru_cache(maxsize=None)
def soda_bus(stops_visited: list, students_per_stop: list, time_between_stops: list, start_index: int, total_soda_drank: int):
    sum_of_students_left = sum(students_per_stop)

    @cached
    def sub_soda_bus(current_exit: int, right_index: int, lef_index: int, last_stop: int, sum_of_students_left: int):

        if current_exit >= len(stops_visited):
            return 0

        if current_exit < 0:
            return 0
            
        if sum_of_students_left <= 0:
            return 0


        sub_total = []
        time_between_two_stops = 0
        if current_exit != last_stop:
            time_between_two_stops = time_between_stops[current_exit-1]
        total_soda_drank = time_between_two_stops * sum_of_students_left
        sum_of_students_left -= students_per_stop[current_exit]
        go_right = sub_soda_bus(right_index + 1, right_index + 1, lef_index, current_exit, sum_of_students_left)
        go_left = sub_soda_bus(lef_index - 1, right_index, lef_index - 1, current_exit, sum_of_students_left)
        sub_total.append(total_soda_drank + min(go_right, go_left))
        return min(sub_total)
    


    return sub_soda_bus(start_index, start_index, start_index, start_index, sum_of_students_left)


def test_total_soda_drank_for_1_stop():
    assert soda_bus([1], [10], [0], 0, 0) == (0)

def test_total_soda_drank_for_2_stops():
     assert soda_bus([1,2], [5, 10], [10], 0, 0) == (100)
     assert soda_bus([1,2], [5, 10], [10], 1, 0) == (50)
test_total_soda_drank_for_2_stops()


print(soda_bus(stops_visited, students_per_stop, time_between_stops, start_index, total_soda_drank))