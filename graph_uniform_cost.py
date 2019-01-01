from collections import deque
from queue import PriorityQueue
import heapq

from graph import GraphClass
from node import Node
from romania_problem import RomaniaProblem
import problem_generator as pg

def UCS(problem):
    visited = 0
    expanded_nodes = 0
    maximum_memory = 0

    node = Node(problem.initial_state,None,None)
    frontier = list()
    heapq.heapify(frontier)
    frontier_state = list()
    heapq.heappush(frontier,node)
    frontier_state.append(node.state)
    explored = set()
    while True:
       if len(frontier) == 0:
           return (None,None)
       node = heapq.heappop(frontier)
       visited += 1

       print("POPED: " + node.state)
       if problem.goal_test(node.state):
           return (node,(visited,expanded_nodes,maximum_memory,node.cost))
       explored.add(node.state)
       for action in problem.actions(node.state):
           g = node.cost + problem.path_cost(node.state,problem.transition(node.state,action))
           child = node.child_node(problem, action, g)
           if (child.state not in explored and child.state not in frontier_state):
                print(child.state + " <- " + child.parent.state + " : " + str(child.cost))
                heapq.heappush(frontier,child)
                expanded_nodes += 1
                maximum_memory = max(maximum_memory, len(frontier) + len(explored))
                frontier_state.append(child.state)
           elif child.state in frontier_state:
               for n in frontier:
                    if n.state == child.state and n.cost > child.cost:
                       frontier.remove(n)
                       heapq.heapify(frontier)
                       #frontier_state.remove(n.state)
                       heapq.heappush(frontier, child)
                       #frontier_state.append(child.state)
                       #break
def main():
    romania_graph = pg.get_romania_graph()
    romania_prob = RomaniaProblem("Arad","Bucharest", romania_graph)
    node, details = UCS(romania_prob)
    if node is not None:
        node.print_path()
        print(details)
    return
if __name__ == "__main__":
        main()