# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 21:05:24 2020

@author: michal
"""

import json
import numpy as np
import partition.greedy as partition
from random import randint
import time
'''
TODO

- dokonczyc randomowe generowanie jsona z przykladem do rozwiazania
- brute force powinien działać na wszystkich rozwiązaniach 

'''
#def generate_random_example_to_json(numbers, rang):
#    arr_of_nums = np.array(0)
#    for c in range(0, numbers):
#        v = randint(0, rang)
#        arr_of_nums = np.append(arr_of_nums, v)
#    row_json = json.dump(arr_of_nums)
#    return row_json

#print(generate_random_example_to_json(10, 12))
         

def reading_sets_to_partion_from_file():
    with open('jsons/examples.json') as exampleSets:
        dataSets = json.load(exampleSets)
    return dataSets

def generate_example_resolves(sets, k):
    return partition.greedy(sets, 2)


def solutions_from_json(dataSet):
    solution_list = []
    for i in range(1, len(dataSet) + 1):
        solution_list.extend(dataSet['S' + str(i)])
        #solution_list.extend(generate_random_resolving(dataSet['S' + str(i)]))
    return solution_list


def number_of_results(dataSet, nr):
    dict_res = dict()
    c = 0
    while c < nr:
        dict_res[c] = dataSet[c]
        c += 1
    return dict_res

def goal_function(solution):
    return number_of_results(generate_example_resolves(solutions_from_json(reading_sets_to_partion_from_file()), 1), 1).get(solution)

#print(reading_sets_to_partion_from_file())

#print(solutions_from_json(reading_sets_to_partion_from_file()))
#print(generate_example_resolves(solutions_from_json(reading_sets_to_partion_from_file()), 1))
#print(number_of_results(generate_example_resolves(solutions_from_json(reading_sets_to_partion_from_file()), 1), 1))
#print(number_of_results(solutions_from_json(reading_sets_to_partion_from_file()), 3))
#print(goal_function(10))

#lecimy niżej z brute forceeeeeeeeeeeeeem
#aby brute force zadziałał podajemy mu pattern na najlepsze rozwiązania wygenerowane przez nas

def brute_force_met(pattern):
    np_arr = np.array(pattern)
    score = 0
    arr_to_check = np.array(0)
    length_pattern = len(np_arr)
    current_col = 0
    sol = 0
    for i in range(0, length_pattern - 1):
        arr_to_check = np.append(arr_to_check, 0)
    while sol < 10000:
        arr_to_check[current_col] = sol
        #print(sol)
        if np_arr[current_col] == arr_to_check[current_col]:
            if (len(arr_to_check) - 1) == current_col:
                break;
            sol = 0
            current_col += 1
        else:
            sol += 1
            score += 1
        
    print("Iterations in Brute Force: " + str(score))
        
    return arr_to_check


#poniżej hill climb jazdaaaaaaaaaaaaaa
def hill_climb_met(number):
    #number = sum(number)
    ans = set()
    ans.add((number,))
    for x in range(1, number):
        for y in hill_climb_met(number - x):
            ans.add(tuple(sorted((x,) + y)))
    return ans
    

#print(brute_force_met(goal_function(0)))
#print(sum(solutions_from_json(reading_sets_to_partion_from_file())))
#print(hill_climb_met(solutions_from_json(reading_sets_to_partion_from_file())))
#print(hill_climb_met(sum(solutions_from_json(reading_sets_to_partion_from_file()))))

#wykonania ze zliczaniem czasu
#generowanie przykłądowego rozwiazania czas
start_gen = time.time()
generate_example_resolves(solutions_from_json(reading_sets_to_partion_from_file()), 1)
print("--- %s seconds - Example problem resolve generation time" % (time.time() - start_gen))
###############################################################
#brute force zliczanie czasu na znalezienie najlepszego rozwiązania
start_brut = time.time()
brute_force_met(goal_function(0))
print("--- %s seconds - Brute force generation time" % (time.time() - start_brut))
###############################################################
#hillclimb - generowanie wszystkich możliwych rozwiązań zliczanie czasu
start_hill = time.time()
hill_climb_met(sum(solutions_from_json(reading_sets_to_partion_from_file())))
print("--- %s seconds - Hill Climb generation time" % (time.time() - start_hill))
###############################################################










