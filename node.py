class Node:
    def __init__(self,state,action, parent=None, cost=0):
        self.state = state
        self.action = action
        self.parent = parent
        self.cost = cost

    def __repr__(self):
        return "[{}]".format(self.state)

    def __hash__(self):
        return hash(self.state)

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __lt__(self, other):
        return self.cost < other.cost

    def print_path(self):
        print(self.path())

    def child_node(self, problem, action, now_cost=0):
        child = problem.transition(self.state, action)
        return Node(child, action, self, now_cost + problem.path_cost(self.state,child))

    def path(self):
        node = self
        final_path = list()
        while node is not None:
            final_path.append((node))
            node = node.parent
        final_path.reverse()
        return final_path