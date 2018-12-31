from collections import deque
from graph import GraphClass
from node import Node
from romania_problem import RomaniaProblem
import problem_generator as pg

def child_node(problem, node, action):
    return Node(problem.transition(node.state,action),action,node)


def GraphBFS(problem):
    node = Node(problem.initial_state,None,None)
    print(node)
    if problem.goal_test(node.state):
        return node
    frontier = deque([node])
    explored = set()
    while True:
       if len(frontier) == 0:
           return None
       node = frontier.pop()
       explored.add(node.state)
       for action in problem.actions(node.state):
           child = child_node(problem, node, action)
           if (child.state not in explored):
               if(child not in frontier):
                   print(child.state + " <- " + child.parent.state)
                   if problem.goal_test(child.state):
                       return child
                   frontier.appendleft(child)


def main():
    romania_graph = pg.get_romania_graph()
    romania_prob = RomaniaProblem("Arad","Bucharest", romania_graph)
    node = GraphBFS(romania_prob)
    if node is not None:
        node.print_path()
    return
if __name__ == "__main__":
        main()