from collections import deque
from graph import GraphClass
from node import Node
from romania_problem import RomaniaProblem
import problem_generator as pg

def child_node(problem, node, action):
    return Node(problem.transition(node.state,action),action,node)


def GraphDFS(problem):
    node = Node(problem.initial_state,None,None)
    frontier = deque([node])
    explored = set()
    while True:
       if len(frontier) == 0:
           return None
       node = frontier.pop()
       if problem.goal_test(node.state):
           return node
       explored.add(node.state)
       for action in problem.actions(node.state):
           child = node.child_node(problem, action)
           if child.state not in explored and child not in frontier:
               frontier.append(child)
    return None


def main():
    romania_graph = pg.get_romania_graph()
    romania_prob = RomaniaProblem("Arad","Bucharest", romania_graph)
    node = GraphDFS(romania_prob)
    if node is not None:
        node.print_path()
    return

if __name__ == "__main__":
    print("Graph DFS: ")
    main()