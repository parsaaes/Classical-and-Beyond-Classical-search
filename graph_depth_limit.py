from graph import GraphClass
from node import Node
from romania_problem import RomaniaProblem
import problem_generator as pg

def recursive_dls(problem, src, limit, explored):
    if problem.goal_test(src.state):
        return src
    elif limit == 0:
        return 'cutoff'
    else:
        cutoff_occurred = False
        for action in problem.actions(src.state):
            child = src.child_node(problem, action)
            if child.state in explored:
                continue
            explored.add(child.state)
            result = recursive_dls(problem, child ,limit - 1,explored)
            if result == 'cutoff':
                cutoff_occurred = True
                explored.remove(child.state)
            elif result is not None:
                return result
        if cutoff_occurred:
            return 'cutoff'
        else:
            return None


def dls(problem, limit):
    src = Node(problem.initial_state,None,None)
    explored = set()
    return recursive_dls(problem, src, limit, explored)

def main():
    romania_graph = pg.get_romania_graph()
    romania_prob = RomaniaProblem("Arad","Bucharest", romania_graph)
    node = dls(romania_prob,3)
    if isinstance(node, Node):
        node.print_path()
    else:
        print(node)

    return

if __name__ == "__main__":
    print("DLS: ")
    main()