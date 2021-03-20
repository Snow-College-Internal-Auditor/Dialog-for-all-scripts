stops = [1,2,3,4]  
students_per_stop = [2,5,10,3]  
time_between_stops = [10,5,2] 
start_index =  0
final_result = 0
last_stop = None
explored = [False] * len(stops)

def get_time_traveld(start_index, time_between_stops, next_stop_index):
    total_time_traveld_between_two_stops = 0
    if start_index > next_stop_index:
        start_index , next_stop_index = next_stop_index, start_index
    for i in range(start_index, next_stop_index):
        total_time_traveld_between_two_stops += time_between_stops[i]
    return total_time_traveld_between_two_stops


def next_right(stops, start_index):
    sub_explored = [False] * len(stops)
    sub_explored[start_index] = True
    for i in range(1, len(stops)):
        try:
            if sub_explored[start_index + i] == False:
                go_right = stops[start_index + i]
                next_stop = 0
                for i in stops:
                    if go_right == i:
                        go_right = next_stop
                        break
                    next_stop += 1
                return go_right
        except:
            return None
    return None

def next_left(stops, start_index):
    sub_explored = [False] * len(stops)
    sub_explored[start_index] = True
    for i in range(1, len(stops)):
        if sub_explored[start_index - i] == False:
            go_left = stops[start_index - i]
            next_stop = 0
            for i in stops:
                if go_left == i:
                    go_left = next_stop
                    break
                next_stop += 1
            return go_left
    return None


def soda_bus(stops, students_per_stop, time_between_stops, start_index, final_result, last_stop, explored):
    final_result = 0
    explored[start_index] = True
    if last_stop != None:
        total_time_traveld_between_two_stops = get_time_traveld(last_stop, time_between_stops, start_index)
        for kids in students_per_stop:
                final_result += total_time_traveld_between_two_stops * kids
    
    students_per_stop[start_index] = 0
    if sum(students_per_stop) == 0:
        return final_result

    if start_index == 0 or explored[start_index - 1] == True:
        go_left = None
    else:
        go_left = next_left(stops, start_index)
        if go_left != None:
            final_result += soda_bus(stops, students_per_stop, time_between_stops, go_left, final_result, start_index, explored)

    go_right = next_right(stops, start_index)
    if go_right != None and explored[go_right] == False:
        final_result += soda_bus(stops, students_per_stop, time_between_stops, go_right, final_result, start_index, explored)


    
    return final_result




def test_total_soda_drank_for_1_stop():
    explored = [False] * 1
    assert soda_bus([1], [10], [0], 0, 0, None, explored) == 0

def test_total_soda_drank_for_2_stops():
    explored = [False] * 2
    assert soda_bus([1,2], [5, 10], [10], 0, 0, None, explored) == 100
    explored = [False] * 2
    assert soda_bus([1,2], [5, 10], [10], 1, 0, None, explored) == 50

def test_total_soda_drank_for_3_stops():
    explored = [False] * 3
    assert soda_bus([1,2,3], [2,5,10], [10,5], 0, 0, None, explored) == 200
    explored = [False] * 3
    assert soda_bus([1,2,3], [2,5,10], [10,5], 1, 0, None, explored) == 90
    explored = [False] * 3
    assert soda_bus([1,2,3], [2,5,10], [10,5], 2, 0, None, explored) == 55
test_total_soda_drank_for_3_stops()

def test_total_soda_drank_for_4_stops():
    explored = [False] * 4
    assert soda_bus([1,2,3,4], [2,5,10,3], [10,5,2], 0, 0, None, explored) == 251

# soda_bus(stops, students_per_stop, time_between_stops, start_index, final_result)
