import copy
import random
from collections import defaultdict
from math import floor

import problem_generator as pg
from coloring_problem import ColoringProblem

def fitness_func(problem,state):
    value = 0
    for key in problem.graph.adj_list:
        for neigh in problem.graph.adj_list[key]:
            if state[problem.char_to_int(key)] != state[problem.char_to_int(neigh)]:
                value += 1
    return value/(2 * problem.graph.number_of_edges())

def init_population(population_size, constraint, length):
    population = list()
    for i in range(population_size):
        child = list()
        for j in range(length):
            child.append(random.choice(constraint))
        population.append(child)

    return population


def crossover(first, second):
    n = len(first)
    x = random.randrange(0, n)
    return first[:x] + second[x:]


def mutate(original, constraints, rate=0.2):
    if not prob(rate):
        return original
    print("I'm being mutated!")
    c = random.randrange(0, len(original))
    return original[:c] + [random.choice(constraints)] + original[c+1:]





def prob(probability):
    return random.random() < probability

def genetic_algoirthm(problem, populationSize, tournamentSize, numberOfGenerations, mutationRate=0.1):
    initial_population = init_population(populationSize,problem.constraints,len(problem.graph.adj_list))
    population = list()
    for g in range(0,numberOfGenerations):
        parents = run_tournament(initial_population, problem, tournamentSize)
        new_gen = list()
        for i in range(0, floor(len(parents) / 2)):
            new_gen.append(crossover(parents[2*i],parents[2*i + 1]))
        if len(parents) % 2 == 1:
            new_gen.append(parents[len(parents) - 1])

        population = list()
        population.extend(parents)
        population.extend(new_gen)

        for i in range(0, floor(len(initial_population) * problem.graph.V * mutationRate)):
            mutate(random.choice(population),problem.constraints,0.3)

        initial_population = population
        find_worst(population,problem)
        find_best(population,problem)

    return population


def find_best(population, problem):
    best = None
    best_score = 0
    for individual in population:
        score = fitness_func(problem, individual)
        if (score > best_score):
            best_score = score
            best = individual
    print("best is " + str(best_score))

def find_worst(population, problem):
    worst = None
    worst_score = 1
    for individual in population:
        score = fitness_func(problem, individual)
        if (score < worst_score):
            worst_score = score
            worst = individual
    print("worst is " + str(worst_score))


def run_tournament(initial_population, problem, tournamentSize):
    parents = list()
    for i in range(0, tournamentSize):
        tournament = list()
        for j in range(0, tournamentSize):
            tournament.append(random.choice(initial_population))
        # choose the winner
        best = None
        best_score = 0
        for individual in tournament:
            score = fitness_func(problem, individual)
            print(str(individual) + ":" + str(score))
            if (score > best_score):
                best_score = score
                best = individual
        #print(str(best_score) + " wins!")
        parents.append(best)
    return parents


def random_init_state(keys,values):
    result = defaultdict()
    for key in keys:
        result[key] = random.choice(values)
    return result

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
    # print(init_population(3,problem.constraints,len(problem.graph.adj_list)))
    #print(['G', 'B', 'R', 'R', 'R', 'B', 'B', 'G', 'G', 'G', 'G'])
    #print(mutate(['G', 'B', 'R', 'R', 'R', 'B', 'B', 'G', 'G', 'G', 'G'],problem.constraints))
    # run_tournament(init_population(3,problem.constraints,len(problem.graph.adj_list)),problem,3)
    population = genetic_algoirthm(problem,30,5,10)
    return
if __name__ == "__main__":
        main()
