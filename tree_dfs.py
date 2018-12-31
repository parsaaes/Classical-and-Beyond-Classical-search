from collections import deque
from graph import GraphClass
from node import Node
from romania_problem import RomaniaProblem
import problem_generator as pg

def child_node(problem, node, action):
    return Node(problem.transition(node.state,action),action,node)


def TreeDFS(problem):
    node = Node(problem.initial_state,None,None)
    frontier = deque([node])
    while True:
       if len(frontier) == 0:
           return None
       node = frontier.pop()
       if problem.goal_test(node.state):
           return node
       for action in problem.actions(node.state):
           frontier.append(node.child_node(problem, action))
    return None


def main():
    romania_graph = pg.get_romania_graph()
    romania_prob = RomaniaProblem("Arad","Bucharest", romania_graph)
    node = TreeDFS(romania_prob)
    if node is not None:
        node.print_path()
    return

if __name__ == "__main__":
    print("Tree DFS: ")
    main()