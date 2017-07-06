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
        noStroke()
        fill(0,100,100)
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
    def __eq__(self, other):
        b1 = self.bary
        b2 = other.bary
        return b1[0] == b2[0] and b1[1] == b2[1] # no need to check 3rd
    def cartesian(self, scale):
        x = 0.5 * self.bary[1] - 0.5 * self.bary[2]
        y = - h * self.bary[1] - h * self.bary[2]
        return (scale * x, scale * y)

    def east(self, n=1):
        return Coordinate(self.a, self.b+n)
    def west(self, n=1):
        return self.east(-n)
    def se(self, n=1):
        return Coordinate(self.a+n, self.b)
    def nw(self, n=1):
        return self.se(-n)
    def sw(self, n=1):
        return Coordinate(self.a+n, self.b-n)
    def ne(self, n=1):
        return self.sw(-n)
    
    def neighbor(self, dir, n=1):
        if dir == 0:
            return self.sw(n)
        elif dir == 1:
            return self.se(n)
        elif dir == 2:
            return self.east(n)
        elif dir == 3:
            return self.sw(-n)
        elif dir == 4:
            return self.se(-n)
        elif dir == 5:
            return self.east(-n)

    def neighbors(self, n=1):
        yield self.sw(n)
        yield self.se(n)
        yield self.east(n)
        yield self.sw(-n)
        yield self.se(-n)
        yield self.east(-n)
    def __str__(self):
        b = self.bary
        return "({},{},{})".format(b[0], b[1], b[2])