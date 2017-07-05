class Graph():
    def __init__(self):
        pass
    
    
class Node:
    def __init__(self, triangle, *children):
        self.children = set(children)
        for c in children:
            c.add(self)
    def add(self, child):
        self.children |= set([child])