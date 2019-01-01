from collections import defaultdict

from graph import GraphClass


def get_romania_graph():
        romania = GraphClass(20)
        romania.add_edge("Oradea", "Zerind", 71)
        romania.add_edge("Oradea", "Sibiu", 151)
        romania.add_edge("Zerind", "Arad", 75)
        romania.add_edge("Arad", "Sibiu", 140)
        romania.add_edge("Arad", "Timisoara", 118)
        romania.add_edge("Timisoara", "Lugoj", 111)
        romania.add_edge("Lugoj", "Mehadia", 70)
        romania.add_edge("Mehadia", "Dobreta", 75)
        romania.add_edge("Dobreta", "Craiova", 120)
        romania.add_edge("Craiova", "Rimnicu Vilcea", 146)
        romania.add_edge("Rimnicu Vilcea", "Sibiu", 80)
        romania.add_edge("Rimnicu Vilcea", "Pitesti", 97)
        romania.add_edge("Craiova", "Pitesti", 138)
        romania.add_edge("Sibiu", "Fagaras", 99)
        romania.add_edge("Bucharest", "Fagaras", 211)
        romania.add_edge("Bucharest", "Pitesti", 101)
        romania.add_edge("Bucharest", "Giurgiu", 90)
        romania.add_edge("Bucharest", "Urziceni", 85)
        romania.add_edge("Hirsova", "Urziceni", 98)
        romania.add_edge("Hirsova", "Eforie", 86)
        romania.add_edge("Vaslui", "Urziceni", 142)
        romania.add_edge("Vaslui", "Iasi", 92)
        romania.add_edge("Neamt", "Iasi", 87)
        return romania

def romania_huristic():
    h = defaultdict(list)
    h["Arad"] = 366
    h["Bucharest"] = 0
    h["Craiova"] = 160
    h["Dobreta"] = 242
    h["Eforie"] = 161
    h["Fagaras"] = 178
    h["Giurgiu"] = 77
    h["Hirsova"] = 151
    h["Iasi"] = 226
    h["Lugoj"] = 244
    h["Mehadia"] = 241
    h["Neamt"] = 234
    h["Oradea"] = 380
    h["Pitesti"] = 98
    h["Rimnicu Vilcea"] = 193
    h["Sibiu"] = 253
    h["Timisoara"] = 329
    h["Urziceni"] = 80
    h["Vaslui"] = 199
    h["Zerind"] = 374
    return h
