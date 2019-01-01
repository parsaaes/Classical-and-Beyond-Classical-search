from graph import GraphClass
from node import Node
from romania_problem import RomaniaProblem
import problem_generator as pg

def recursive_dls(problem, src, limit):
    visited = 0
    expanded_nodes = 0
    maximum_memory = 0

    visited += 1
    if problem.goal_test(src.state):
        return (src, visited, expanded_nodes, maximum_memory + 1)
    elif limit == 0:
        return ('cutoff', visited, expanded_nodes, maximum_memory + 1)
    else:
        cutoff_occurred = False
        for action in problem.actions(src.state):
            child = src.child_node(problem, action, src.cost + 1)
            expanded_nodes += 1
            result, v1, e1, m1 = recursive_dls(problem, child ,limit - 1)
            visited += v1
            expanded_nodes += e1
            maximum_memory += m1
            if result == 'cutoff':
                cutoff_occurred = True
            elif result is not None:
                return (result, visited, expanded_nodes, maximum_memory + 1)
        if cutoff_occurred:
            return ('cutoff', visited, expanded_nodes, maximum_memory + 1)
        else:
            return (None, visited, expanded_nodes, maximum_memory + 1)


def dls(problem, limit):
    src = Node(problem.initial_state,None,None)
    return recursive_dls(problem, src, limit)

def main():
    romania_graph = pg.get_romania_graph()
    romania_prob = RomaniaProblem("Arad","Bucharest", romania_graph)
    node, v, e, n = dls(romania_prob,2)
    if isinstance(node, Node):
        node.print_path()
        print((v, e, n, node.cost))
    else:
        print(node)

    return

if __name__ == "__main__":
    print("DLS: ")
    main()