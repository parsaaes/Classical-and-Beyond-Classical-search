import copy
import random
from collections import defaultdict

import problem_generator as pg
from coloring_problem import ColoringProblem

def random_init_state(keys,values):
    result = defaultdict()
    for key in keys:
        result[key] = random.choice(values)
    return result

def best_neigh(problem, state):
    expanded = 0
    best = state
    best_score = problem.evaluation(state)
    for key in state:
        last_value = state[key]
        for action in problem.actions(last_value):
            state[key] = action
            expanded += 1
            if problem.evaluation(state) > best_score:
                best = copy.deepcopy(state)
                best_score = problem.evaluation(state)
            state[key] = last_value
    return (best, expanded)

def random_neigh(problem, state):
    expanded = 0;
    res = list()
    init_score = problem.evaluation(state)
    for key in state:
        last_value = state[key]
        for action in problem.actions(last_value):
            state[key] = action
            expanded += 1
            if problem.evaluation(state) > init_score:
                good = copy.deepcopy(state)
                res.append(good)
            state[key] = last_value
    if len(res) == 0:
        return (None,None)
    return (random.choice(res),expanded)

def first_neigh(problem, state):
    expanded = 0
    best_score = problem.evaluation(state)
    for key in state:
        last_value = state[key]
        for action in problem.actions(last_value):
            state[key] = action
            expanded += 1
            if problem.evaluation(state) > best_score:
                result = copy.deepcopy(state)
                state[key] = last_value
                return (result, expanded)
            state[key] = last_value
    return (None,None)

def hb(problem, init_state):
    visited = 0
    expanded = 0
    current = init_state
    while True:
        neigh, e = best_neigh(problem,current)
        if problem.evaluation(neigh) > problem.evaluation(current):
            current = neigh
            visited += 1
            expanded += e
        else:
            return (current, str(str(problem.evaluation(current)) + " from " + str(problem.best_score -2)), visited, expanded)

def stochstic_hb(problem, init_state):
    visited = 0
    expanded = 0

    current = init_state
    while True:
        neigh, e = random_neigh(problem,current)
        if neigh != None and problem.evaluation(neigh) > problem.evaluation(current):
            current = neigh
            visited += 1
            expanded += e
        else:
            return (current, str(str(problem.evaluation(current)) + " from " + str(problem.best_score -2)), visited, expanded)

def first_hb(problem, init_state):
    visited = 0
    expanded = 0

    current = init_state
    while True:
        neigh, e = first_neigh(problem,current)
        if neigh != None and problem.evaluation(neigh) > problem.evaluation(current):
            current = neigh
            visited += 1
            expanded += e
        else:
            return (current, str(str(problem.evaluation(current)) + " from " + str(problem.best_score -2)),visited,expanded)

def random_restart_hb(problem):
    visited = 0
    expanded = 0

    keys = problem.vertices()
    init_state = random_init_state(keys, problem.constraints)
    current = init_state
    while True:
        neigh, e = best_neigh(problem,current)
        if problem.evaluation(neigh) > problem.evaluation(current):
            current = neigh
            print(problem.evaluation(neigh))
            visited += 1
            expanded += e
        else:
            if problem.evaluation(current) >= problem.best_score - 2 :
                return (current, str(str(problem.evaluation(current)) + " from " + str(problem.best_score -2)), visited, expanded)
            else:
                current = random_init_state(keys, problem.constraints)

def main():
    coloring = pg.get_coloring_graph()
    init = defaultdict()
    init["A"] = "R"
    init["B"] = "R"
    init["C"] = "R"
    init["D"] = "R"
    init["E"] = "R"
    init["F"] = "R"
    init["G"] = "R"
    init["H"] = "R"
    init["I"] = "R"
    init["J"] = "R"
    init["K"] = "R"
    problem = ColoringProblem(init,None,coloring)
    #print(hb(problem, init))
    #print(stochstic_hb(problem, init))
    #print(first_hb(problem, init))
    print(random_restart_hb(problem))

    return
if __name__ == "__main__":
        main()
