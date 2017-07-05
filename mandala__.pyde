from graph import Node

class Triangle:  # shape?

    def __init__(self, node, coordinates, color=None):
        self.node = node
        self.coordinates = coordinates
        self.color = color

    def draw(self):
        pass

h = sqrt(0.75)  # height of the triangle
class Coordinate:
    def __init__(self, a, b, c=None):
        if(c is None):
            c = 1 - (a+b)
        if (a + b + c != 1):
            raise Exception("barys are != 1")
        self.bary = (a, b, c)

    def cartesian(self, scale):
        x = 0.5 * self.bary[1] - 0.5 * self.bary[2]
        y = - h * self.bary[1] - h * self.bary[2]
        return (scale * x, scale * y)
