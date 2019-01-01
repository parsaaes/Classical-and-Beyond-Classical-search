from collections import deque
from graph import GraphClass
from node import Node
from romania_problem import RomaniaProblem
import problem_generator as pg

def child_node(problem, node, action):
    return Node(problem.transition(node.state,action),action,node)


def TreeBFS(problem):
    visited = 0
    expanded_nodes = 0
    maximum_memory = 0

    node = Node(problem.initial_state,None,None)
    if problem.goal_test(node.state):
        return (node, (visited,expanded_nodes,maximum_memory,node.cost))
    frontier = deque([node])
    while True:
       if len(frontier) == 0:
           return (None,None)
       node = frontier.pop()
       visited += 1
       for action in problem.actions(node.state):
           child = node.child_node(problem, action,node.cost + 1)
           if(child.state not in frontier):
                   print(child.state + " <- " + child.parent.state)
                   if problem.goal_test(child.state):
                       return (child, (visited,expanded_nodes,maximum_memory,child.cost))
                   frontier.appendleft(child)
                   expanded_nodes += 1
                   maximum_memory = max(maximum_memory,len(frontier))


def main():
    romania_graph = pg.get_romania_graph()
    romania_prob = RomaniaProblem("Arad","Bucharest", romania_graph)
    node, details = TreeBFS(romania_prob)
    if node is not None:
        node.print_path()
        print(details)
    return

if __name__ == "__main__":
    print("Tree BFS: ")
    main()