from graph import Node

class Triangle:  # shape?

    def __init__(self, node, coordinate, up, color=None):
        self.node = node
        self.coordinate = coordinate
        self.up = up
        self.color = color

    def draw(self, scale):
        s = createShape()
        s.beginShape()
        coordinates = self.points()
        for c in coordinates:
            cart = c.cartesian(scale)
            s.vertex(cart[0], cart[1])
        s.endShape(CLOSE)
        shape(s)

    def points(self):
        if(self.up is False):
            return (Coordinate(self.coordinate.a + 1, self.coordinate.b),
                    Coordinate(self.coordinate.a + 1, self.coordinate.b - 1),
                    self.coordinate)
        else:
            return (Coordinate(self.coordinate.a - 1, self.coordinate.b),
                    Coordinate(self.coordinate.a - 1, self.coordinate.b + 1),
                    self.coordinate)


h = sqrt(0.75)  # height of the triangle

class Coordinate:

    def __init__(self, a, b, c=None):
        self.a = a
        self.b = b
        self.c = c
        if(self.c is None):
            self.c = 1 - (a + b)
        if (self.a + self.b + self.c != 1):
            raise Exception("barys are != 1")
        self.bary = (self.a, self.b, self.c)

    def cartesian(self, scale):
        x = 0.5 * self.bary[1] - 0.5 * self.bary[2]
        y = - h * self.bary[1] - h * self.bary[2]
        return (scale * x, scale * y)
