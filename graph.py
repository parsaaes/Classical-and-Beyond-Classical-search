from collections import defaultdict
import numpy as np
class GraphClass:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = defaultdict(list)
        self.weights = defaultdict(list)

    def add_edge(self, u, v, cost=0):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u) # make the graph undirected
        self.weights[(u, v)] = cost
        self.weights[(v, u)] = cost

    def cost(self,u,v):
        return self.weights[(u,v)]

    def print_graph(self):
        print(self.adj_list)
        print(self.weights)
        for g in self.adj_list:
            print(self.adj_list.get(g))

    def number_of_edges(self):
        res = 0
        for key in self.adj_list:
            res += len(self.adj_list[key])
        return res


def main():
    romania = GraphClass(20)
    romania.add_edge("Arad", "Zerind",75)
    romania.add_edge("Arad", "Timosora",118)
    romania.print_graph()
    return
if __name__ == "__main__":
        main()