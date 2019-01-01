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
    best = state
    best_score = problem.evaluation(state)
    for key in state:
        last_value = state[key]
        for action in problem.actions(last_value):
            state[key] = action
            if problem.evaluation(state) > best_score:
                best = copy.deepcopy(state)
                best_score = problem.evaluation(state)
            state[key] = last_value
    return best

def random_neigh(problem, state):
    res = list()
    init_score = problem.evaluation(state)
    for key in state:
        last_value = state[key]
        for action in problem.actions(last_value):
            state[key] = action
            if problem.evaluation(state) > init_score:
                good = copy.deepcopy(state)
                res.append(good)
            state[key] = last_value
    if len(res) == 0:
        return None
    return random.choice(res)

def first_neigh(problem, state):
    best_score = problem.evaluation(state)
    for key in state:
        last_value = state[key]
        for action in problem.actions(last_value):
            state[key] = action
            if problem.evaluation(state) > best_score:
                return state
            state[key] = last_value
    return None

def hb(problem, init_state):
    current = init_state
    while True:
        neigh = best_neigh(problem,current)
        if problem.evaluation(neigh) > problem.evaluation(current):
            current = neigh
        else:
            return (current, str(str(problem.evaluation(current)) + " from " + str(problem.best_score -2)))

def stochstic_hb(problem, init_state):
    current = init_state
    while True:
        neigh = random_neigh(problem,current)
        if neigh != None and problem.evaluation(neigh) > problem.evaluation(current):
            current = neigh
        else:
            return (current, str(str(problem.evaluation(current)) + " from " + str(problem.best_score -2)))

def first_hb(problem, init_state):
    current = init_state
    while True:
        neigh = first_neigh(problem,current)
        if neigh != None and problem.evaluation(neigh) > problem.evaluation(current):
            current = neigh
        else:
            return (current, str(str(problem.evaluation(current)) + " from " + str(problem.best_score -2)))

def random_restart_hb(problem):
    keys = problem.vertices()
    init_state = random_init_state(keys, problem.constraints)
    current = init_state
    while True:
        neigh = best_neigh(problem,current)
        if problem.evaluation(neigh) > problem.evaluation(current):
            current = neigh
            print(problem.evaluation(neigh))
        else:
            if problem.evaluation(current) >= problem.best_score - 2 :
                return (current, str(str(problem.evaluation(current)) + " from " + str(problem.best_score -2)))
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
