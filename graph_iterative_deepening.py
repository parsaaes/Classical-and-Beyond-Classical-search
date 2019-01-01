from graph import GraphClass
from node import Node
from romania_problem import RomaniaProblem
import problem_generator as pg
from graph_depth_limit import dls

def id(problem, inf):
    visited = 0
    expanded_nodes = 0
    maximum_memory = 0

    for i in range(0,inf):
        print("checking with limit " + str(i))
        result, v, e, m = dls(problem, i)
        visited += v
        expanded_nodes += e
        maximum_memory += m
        if isinstance(result, Node):
            break
    return (result, visited, expanded_nodes, maximum_memory, result.cost)


def main():
    romania_graph = pg.get_romania_graph()
    romania_prob = RomaniaProblem("Arad","Bucharest", romania_graph)
    node, v , e, m ,c = id(romania_prob,7)
    if isinstance(node, Node):
        node.print_path()
        print((v,e,m,c))
    else:
        print(node)

    return

if __name__ == "__main__":
    print("ID: ")
    main()