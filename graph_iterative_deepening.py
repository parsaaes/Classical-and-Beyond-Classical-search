from graph import GraphClass
from node import Node
from romania_problem import RomaniaProblem
import problem_generator as pg
from graph_depth_limit import dls

def id(problem, inf):
    for i in range(0,inf):
        print("checking with limit " + str(i))
        result = dls(problem, i)
        if isinstance(result, Node):
            break
    return result


def main():
    romania_graph = pg.get_romania_graph()
    romania_prob = RomaniaProblem("Arad","Bucharest", romania_graph)
    node = id(romania_prob,7)
    if isinstance(node, Node):
        node.print_path()
    else:
        print(node)

    return

if __name__ == "__main__":
    print("ID: ")
    main()