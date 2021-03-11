import random

stops = [1,2,3]
students_per_stop = [2,5,10]
time_between_stops = [10,5]




start_index = 0
final_result = 0
explored = [False] * len(stops)

def total_soda_drank(stops, students_per_stop, time_between_stops, start_index, final_result, explored):
    for i in range(0,len(stops)):
        students_per_stop[start_index] = 0
        explored[start_index] = True
        j = random.randint(0, len(stops)-1)
        if j != start_index and explored[j] == False:
            total_time_traveld_between_two_stops = get_time_traveld(start_index, time_between_stops, j)
            for kids in students_per_stop:
                final_result += total_time_traveld_between_two_stops * kids
        if j > len(time_between_stops):
            start_index = j - 1
        else:
            start_index = j

next_stop_index = 1
def get_time_traveld(start_index, time_between_stops, next_stop_index):
    total_time_traveld_between_two_stops = 0
    if start_index > next_stop_index:
        start_index , next_stop_index = next_stop_index, start_index
    for i in range(start_index, next_stop_index):
        total_time_traveld_between_two_stops += time_between_stops[i]
    return total_time_traveld_between_two_stops

total_soda_drank(stops, students_per_stop, time_between_stops, start_index, final_result, explored)




