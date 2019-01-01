from graph import *
import problem_generator as pg
import copy

class ColoringProblem():
    def __init__(self, initial_state, goal_state, graph):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.graph = graph
        self.best_score = 42
        self.constraints = ["R","G","B"]

    def evaluation(self, state):
        value = self.best_score
        for key in self.graph.adj_list:
            for neigh in self.graph.adj_list[key]:
                if state[key] == state[neigh]:
                    value -= 1
        #print("score: " + str(value))
        return value

    def highest_value_neigh(self, state):
        best = state
        best_score = self.evaluation(state)
        for key in state:
            last_value = state[key]
            for action in self.actions(last_value):
                state[key] = action
                if self.evaluation(state) > best_score:
                    best = copy.deepcopy(state)
                    best_score = self.evaluation(state)
                state[key] = last_value
        return best
        #     state[key] = "R"
        #     if self.evaluation(state) > best_score:
        #         best = copy.deepcopy(state)
        #         best_score = self.evaluation(state)
        #     state[key] = last_value
        #
        #     state[key] = "G"
        #     if self.evaluation(state) > best_score:
        #         best = copy.deepcopy(state)
        #         best_score = self.evaluation(state)
        #     state[key] = last_value
        #
        #     state[key] = "B"
        #     if self.evaluation(state) > best_score:
        #         best = copy.deepcopy(state)
        #         best_score = self.evaluation(state)
        #     state[key] = last_value
        # #print(best)
        # return best



    def actions(self, state):
        result = ["R","G","B"]
        result.remove(state)
        return result

    def transition(self, state, action):
        return None

    def path_cost(self,u ,v):
        return self.graph.cost(u,v)

    def goal_test(self,state):
        return None

    def vertices(self):
        result = list()
        for g in self.graph.adj_list:
            result.append(g)
        return result

    def char_to_int(self,char):
        map = defaultdict()
        map["A"] = 0
        map["B"] = 1
        map["C"] = 2
        map["D"] = 3
        map["E"] = 4
        map["F"] = 5
        map["G"] = 6
        map["H"] = 7
        map["I"] = 8
        map["J"] = 9
        map["K"] = 10
        return map[char]


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
    test = ColoringProblem(init,None,coloring)
    test.highest_value_neigh(init)
    print(coloring.adj_list)
    coloring.print_graph()
    print(test.vertices())
    return
if __name__ == "__main__":
        main()