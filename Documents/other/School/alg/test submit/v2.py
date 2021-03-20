import random
from functools import lru_cache

"""English (subproblems, how they divided, how they combine)
    so this salution is not recursive so this might be writen out a little different then you think. So this does not work well
    past three stops. What i did though is in my first function, total_soda_drank, trys every possible second stop. It is given
    a starting stop and then at random picks the next stop. Once it does this is passes it to my second function inner_workings. 
    At this point it goes from the second stop to the next, then the next after that. As it is doing this it calculates the amount
    of soda drank from one stop to the next. It then returns the final amount of soda drank to the main function which stores the 
    result and path that got that result. It then repeats until it has gone done every possible second path (i.e for list = [1,2,3] 
    (1-2) or (1-3)). Then once I have visted all of the possible second paths it takes the min time and returns that time and its
    path. My thought was to put the chaching on the second function, inner_workings, but I could not figuer out how to get the list
    to be a tuple for the cashing.
    In short:
        subproblems/how they divide: I calculate the result from each alternative second stop
        how they combine: I store result of each subproblem in a list and take the smallest
    """


def total_soda_drank(stops, students_per_stop, time_between_stops, start_index, final_result):

    explored_top = [False] * len(stops)
    default_explored_inner = [False] * len(stops)
    main_start = start_index
    results = []
    explored_top[start_index] = True
    all_explored = seen_it_all(explored_top)
    default_explored_inner[start_index] = True
    
    while all_explored != True:
        students_per_stop[start_index] = 0
        next_stop = random.randint(0, len(stops)-1)
        if next_stop != start_index and explored_top[next_stop] == False:
            results.append(inner_workings(stops, main_start, time_between_stops, next_stop, students_per_stop, default_explored_inner))
            default_explored_inner = [False] * len(stops)
            default_explored_inner[start_index] = True

            explored_top[next_stop] = True
            all_explored = seen_it_all(explored_top)

    if len(results) == 0:
        return (0, [start_index])

    time_results = []
    paths = []
    for i in results:
        time_results.append(i[0])
        paths.append(i[1])
    
    lowest_time_index = time_results.index(min(time_results))
    final_result = ()
    final_result = final_result + (min(time_results),)
    final_result = final_result + (paths[lowest_time_index],)

    return final_result

def inner_workings(stops, start_index, time_between_stops, next_stop, students_per_stop, explored_inner):
    sub_student_list = []
    sub_tree = []
    result_tuple = ()
    for i in students_per_stop:
        sub_student_list.append(i)

    final_result = 0
    sub_tree.append(start_index)
    sub_tree.append(next_stop)
    total_time_traveld_between_two_stops = get_time_traveld(start_index, time_between_stops, next_stop)
    for kids in sub_student_list:
        final_result += total_time_traveld_between_two_stops * kids

    explored_inner[next_stop] = True
    all_explored = seen_it_all(explored_inner)
    sub_student_list[next_stop] = 0
    start_index = next_stop

    while all_explored != True:
        next_stop = random.randint(0, len(stops)-1)
        if next_stop != start_index and explored_inner[next_stop] == False:
            total_time_traveld_between_two_stops = get_time_traveld(start_index, time_between_stops, next_stop)
            for kids in sub_student_list:
                final_result += total_time_traveld_between_two_stops * kids
            sub_tree.append(next_stop)
            if next_stop > len(time_between_stops):
                start_index = next_stop - 1
            else:
                start_index = next_stop
            explored_inner[next_stop] = True
            sub_student_list[next_stop] = 0
            all_explored = seen_it_all(explored_inner)
    
    return final_result, sub_tree

def seen_it_all(explored):
    number_true = 0
    for i in range(0, len(explored)):
        if explored[i]:
            number_true += 1
    if number_true == len(explored):
        return True
    else:
        return False


def get_time_traveld(start_index, time_between_stops, next_stop_index):
    total_time_traveld_between_two_stops = 0
    if start_index > next_stop_index:
        start_index , next_stop_index = next_stop_index, start_index
    for i in range(start_index, next_stop_index):
        total_time_traveld_between_two_stops += time_between_stops[i]
    return total_time_traveld_between_two_stops

#total_soda_drank(stops, students_per_stop, time_between_stops, start_index, final_result):
def test_total_soda_drank_for_1_stop():
    assert total_soda_drank([1], [10], [0], 0, 0) == (0, [0])


def test_total_soda_drank_for_2_stops():
     assert total_soda_drank([1,2], [5, 10], [10], 0, 0) == (100, [0, 1])
     assert total_soda_drank([1,2], [5, 10], [10], 1, 0) == (50, [1, 0])



def test_total_soda_drank_for_3_stops():
    assert total_soda_drank([1,2,3], [2,5,10], [10,5], 0, 0) == (200, [0, 1, 2])
    assert total_soda_drank([1,2,3], [2,5,10], [10,5], 1, 0) == (90, [1, 2, 0])
    assert total_soda_drank([1,2,3], [2,5,10], [10,5], 2, 0) == (55, [2, 1, 0])


def test_total_soda_drank_for_4_stops():
    assert total_soda_drank([1,2,3,4], [2,5,10,3], [10,5,2], 0, 0) == (251, [0,1,2,3])






