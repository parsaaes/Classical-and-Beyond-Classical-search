class Node:
    def __init__(self,state,action, parent=None):
        self.state = state
        self.action = action
        self.parent = parent

    def __repr__(self):
        return "[{}]".format(self.state)

    def __hash__(self):
        return hash(self.state)

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def print_path(self):
        print(self.path())

    def child_node(self, problem, action):
        return Node(problem.transition(self.state, action), action, self)

    def path(self):
        node = self
        final_path = list()
        while node is not None:
            final_path.append(node)
            node = node.parent
        final_path.reverse()
        return final_path