from graph import *
import problem_generator as pg
class RomaniaProblem():
    def __init__(self, initial_state, goal_state, graph):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.graph = graph

    def actions(self, state):
        return self.graph.adj_list[state]

    def transition(self, state, action):
        return action

    def path_cost(self,u ,v):
        return self.graph.cost(u,v)

    def goal_test(self,state):
        if state == self.goal_state:
            print(self.goal_state + " is a goal!")
            return True
        return False



def main():
    romania = GraphClass(20)
    romania.add_edge("Oradea","Zerind",71)
    romania.add_edge("Oradea","Sibiu",151)
    romania.add_edge("Zerin","Arad",75)
    romania.add_edge("Arad","Sibiu",140)
    romania.add_edge("Arad","Timisoara",118)
    romania.add_edge("Timisoara","Lugoj",111)
    romania.add_edge("Lugoj","Mehadia",70)
    romania.add_edge("Mehadia","Dobreta",75)
    romania.add_edge("Dobreta","Craiova",120)
    romania.add_edge("Craiova","Rimnicu Vilcea",146)
    romania.add_edge("Rimnicu Vilcea","Sibiu",80)
    romania.add_edge("Rimnicu Vilcea","Pitesti",97)
    romania.add_edge("Craiova","Pitesti",138)
    romania.add_edge("Sibiu","Fagaras",99)
    romania.add_edge("Bucharest","Fagaras",211)
    romania.add_edge("Bucharest","Pitesti",101)
    romania.add_edge("Bucharest","Giurgiu",90)
    romania.add_edge("Bucharest","Urziceni",85)
    romania.add_edge("Hirsova","Urziceni",98)
    romania.add_edge("Hirsova","Eforie",86)
    romania.add_edge("Vaslui","Urziceni",142)
    romania.add_edge("Vaslui","Iasi",92)
    romania.add_edge("Neamt","Iasi",87)

    romania = pg.get_romania_graph()
    print(romania.adj_list)
    romania.print_graph()
    print(romania.weights.get(("A","B")))
    return
if __name__ == "__main__":
        main()