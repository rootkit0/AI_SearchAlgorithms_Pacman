class Node:
    def __init__(self, _state, _parent=None, _action=None, _cost=0):
        self.state = _state
        self.parent = _parent
        self.action = _action
        self.cost = _cost

    def path(self):
        path = []
        current = self
        while current.parent != None:
            path.append(current.action)
            current = current.parent
        return list(reversed(path))

    def getCost(self):
        count = 0
        current = self
        while current.parent != None:
            count += current.cost
            current = current.parent
        return count

if __name__ == '__main__':
    n1 = Node('e1')
    n2 = Node('e2', n1,'north', 0)
    n3 = Node('e3', n2, 'south', 0)
