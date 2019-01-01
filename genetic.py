import copy
import random
from collections import defaultdict
from math import floor
from math import ceil
import matplotlib.pyplot as plt

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

def custom_crossover(gens):
    offset = 0
    result = []
    borders = list()
    for gen in gens:
        x = random.randrange(0,len(gen))
        borders.append(x)
    borders = sorted(borders)
    # print(borders)
    for i in range(0,len(borders) - 1):
        result.extend(gens[i][offset:borders[i]])
        offset = borders[i]
    result.extend(gens[len(gens)-1][offset:])
    return result


def mutate(original, constraints, rate=0.2):
    if not prob(rate):
        return original
    print("I'm being mutated!")
    c = random.randrange(0, len(original))
    return original[:c] + [random.choice(constraints)] + original[c+1:]





def prob(probability):
    return random.random() < probability


def plot_datas(plot_data_best, plot_data_mean, plot_data_worst,x_axis):
    plt.plot(plot_data_best)
    plt.ylabel('best')
    plt.axis([0,x_axis,0.5,1])
    plt.show()
    plt.plot(plot_data_mean)
    plt.ylabel('mean')
    plt.axis([0,x_axis,0.5,1])
    plt.show()
    plt.plot(plot_data_worst)
    plt.ylabel('worst')
    plt.axis([0,x_axis,0.5,1])
    plt.show()


def genetic_algoirthm(problem, populationSize, tournamentSize, numberOfGenerations, mutationRate=0.1):
    plot_data_best = list()
    plot_data_worst = list()
    plot_data_mean = list()

    initial_population = init_population(populationSize,problem.constraints,len(problem.graph.adj_list))
    population = list()
    for g in range(0,numberOfGenerations):
        parents = run_tournament(initial_population, problem, tournamentSize)
        new_gen = list()
        for i in range(0, floor(len(parents) / 2)):
            new_gen.append(crossover(random.choice(parents),random.choice(parents)))
        if len(parents) % 2 == 1:
            new_gen.append(random.choice(parents))

        population = list()
        population.extend(parents)
        population.extend(new_gen)

        for i in range(0, floor(len(initial_population) * problem.graph.V * mutationRate)):
            mutate(random.choice(population),problem.constraints,0.3)

        initial_population = population
        plot_data_worst.append(find_worst(population,problem))
        plot_data_best.append(find_best(population,problem))
        plot_data_mean.append(find_mean(population,problem))

    plot_datas(plot_data_best,plot_data_mean,plot_data_worst,numberOfGenerations)
    return population

def genetic_algoirthm_custom_crossover(problem, populationSize, tournamentSize, numberOfGenerations, mutationRate=0.1, crossover_times=2):
    plot_data_best = list()
    plot_data_worst = list()
    plot_data_mean = list()

    initial_population = init_population(populationSize,problem.constraints,len(problem.graph.adj_list))
    population = list()
    for g in range(0,numberOfGenerations):
        parents = run_tournament(initial_population, problem, tournamentSize)
        new_gen = list()

        for i in range(0, ceil(len(parents)/crossover_times)):
            gens = list()
            for ct in range(0, crossover_times):
                gens.append(random.choice(parents))
            new_gen.append(custom_crossover(gens))

        population = list()
        population.extend(parents)
        population.extend(new_gen)

        for i in range(0, floor(len(initial_population) * problem.graph.V * mutationRate)):
            mutate(random.choice(population),problem.constraints,0.3)

        initial_population = population
        plot_data_worst.append(find_worst(population,problem))
        plot_data_best.append(find_best(population,problem))
        plot_data_mean.append(find_mean(population,problem))

    plot_datas(plot_data_best,plot_data_mean,plot_data_worst,numberOfGenerations)
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
    return best_score

def find_mean(population, problem):
    best = None
    total_score = 0
    for individual in population:
        score = fitness_func(problem, individual)
        total_score += score
    return total_score/len(population)

def find_worst(population, problem):
    worst = None
    worst_score = 1
    for individual in population:
        score = fitness_func(problem, individual)
        if (score < worst_score):
            worst_score = score
            worst = individual
    print("worst is " + str(worst_score))
    return worst_score


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
    # print(custom_crossover([['A','B','C'],['A','B','B'],['C','C','C']]))
    # population = genetic_algoirthm_custom_crossover(problem,100,5,100,0.01,10)
    population = genetic_algoirthm(problem,100,5,100,0.01)


    return
if __name__ == "__main__":
        main()
