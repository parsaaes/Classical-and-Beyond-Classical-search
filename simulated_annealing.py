import copy
import random
from collections import defaultdict

import problem_generator as pg
from coloring_problem import ColoringProblem

def prob(probability):
    return random.random() < probability

def random_init_state(keys,values):
    result = defaultdict()
    for key in keys:
        result[key] = random.choice(values)
    return result

def next_neigh(problem, state):
    expanded = 0
    result = list()
    for key in state:
        last_value = state[key]
        for action in problem.actions(last_value):
            state[key] = action
            expanded += 1
            neigh = copy.deepcopy(state)
            result.append(neigh)
            state[key] = last_value
    return (random.choice(result), expanded)



def simulated_annealing(problem, init_state, inf):
    visited = 0
    expanded = 0
    t = 0
    current = init_state
    for i in range(0 , inf):
        neigh, e = next_neigh(problem,current)
        expanded += e

        if problem.evaluation(neigh) > problem.evaluation(current):
            current = neigh
            visited += 1
        else:
            delta_e = problem.evaluation(current) - problem.evaluation(neigh)
            if prob(delta_e/i):
                current = neigh
                visited += 1
        t += 1
    return (current, str(str(problem.evaluation(current)) + " from " + str(problem.best_score - 2)), visited, expanded)


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
    print(simulated_annealing(problem,init,50))

    return
if __name__ == "__main__":
        main()
