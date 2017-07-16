from graph import Node

class Canvas:

    def __init__(self, scale):
        self.scale = scale
        self.triangles = []

    def mapCoordinates(self, coordinate, up):
        # yeah, change this when there is time...
        # map negative coordinate to odd and positive ones to even indices
        mapCoordA = lambda i, up: 2 * i if i >= 0 else -2 * i - 1
        # leave space for two triangles per coordinate (up and down)
        mapCoordB = lambda i, up: (
            2 if up else 0) + (4 * i if i >= 0 else -4 * i - 1)
        a = mapCoordA(coordinate.a, up)
        b = mapCoordB(coordinate.b, up)
        return (a, b)

    def show(self, coordinate, up):
        s = self.scale
        cart = coordinate.cartesian(s)
        if(cart[0] > -width / 2 + s / 2  # only show in screen
           and cart[0] < width / 2 - s / 2
           and cart[1] > -height / 2 + s
           and cart[1] < height / 2 - s):
            tr = self.get(coordinate, up)
            if tr is None:
                self.add(Triangle(None, coordinate, up))
                tr = self.get(coordinate, up)
            tr.show()

    def add(self, triangle, overwrite=False):
        coordinate = triangle.coordinate
        up = triangle.up
        a, b = self.mapCoordinates(coordinate, up)
        # expand array if neccessary
        la = len(self.triangles)
        if la <= a:
            for _ in range(la, a + 1):
                # add individual empty lists
                self.triangles += [[]]
        # expand array for second coordinate
        lb = len(self.triangles[a])
        if lb <= b:
            self.triangles[a] += (b - lb + 1) * [None]

        # store triangle if there is none yet
        if self.triangles[a][b] is None or overwrite:
        # add bidirectional link between triangle and canvas
            self.triangles[a][b] = triangle
            triangle.addCanvas(self)
        return self.triangles[a][b]

    def rm(self, coordinate, up):
        a, b = self.mapCoordinates(coordinate, up)
        if len(self.triangles) > a:
            if len(self.triangles[a]) > b:
                self.triangles[a][b] = None

    def get(self, coordinate, up):
        a, b = self.mapCoordinates(coordinate, up)
        if len(self.triangles) > a:
            if len(self.triangles[a]) > b:
                return self.triangles[a][b]

    def getNeighbor(self, triangle, direction):
        pass

    def draw(self):
        scale = self.scale
        for ts in self.triangles:
            for t in ts:
                if t:
                    t.draw(scale)

    def hideAll(self):
        for ts in self.triangles:
            for t in ts:
                if t:
                    t.hide()

    def showAll(self):
        for ts in self.triangles:
            for t in ts:
                if t:
                    t.show()

class Triangle:

    def __init__(self, node, coordinate, up, color='#000000'):
        self.node = node
        self.coordinate = coordinate
        self.up = up
        self.color = color
        self.canvas = None
        self.visible = True

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False

    def addCanvas(self, canvas):
        self.canvas = canvas

    def draw(self, scale):
        if self.visible:
            stroke(self.color)
            fill(self.color)
            # strokeWeight(0.5)
            noStroke()
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

    def getNeighbor(self, direction):
        """return neighbor if canvas is set"""
        if self.canvas is not None:
            return self.canvas.getNeighbor(self, direction)
        return None

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
        return b1[0] == b2[0] and b1[1] == b2[1]  # no need to check 3rd

    def cartesian(self, scale):
        x = 0.5 * self.bary[1] - 0.5 * self.bary[2]
        y = - h * self.bary[1] - h * self.bary[2]
        return (scale * x, scale * y)

    def bary_sameLine(self, i):
        return (i.a == self.a or i.b == self.b or i.c == self.c)

    def lineDir(self, i):
        if(self.bary_sameLine(i)):
            if(i.c == self.c and i.a >= self.a and i.b <= self.b):
                return 0
            if(i.b == self.b and i.a >= self.a and i.c <= self.c):
                return 1
            if(i.a == self.a and i.b >= self.b and i.c <= self.c):
                return 2
            if(i.c == self.c and i.a <= self.a and i.b >= self.b):
                return 3
            if(i.b == self.b and i.a <= self.a and i.c >= self.c):
                return 4
            if(i.a == self.a and i.b <= self.b and i.c >= self.c):
                return 5
        else:
            raise Exception("barys are on different lines")

    def east(self, n=1):
        return Coordinate(self.a, self.b + n)

    def west(self, n=1):
        return self.east(-n)

    def se(self, n=1):
        return Coordinate(self.a + n, self.b)

    def nw(self, n=1):
        return self.se(-n)

    def sw(self, n=1):
        return Coordinate(self.a + n, self.b - n)

    def ne(self, n=1):
        return self.sw(-n)

    def neighbor(self, dir, n=1):
        dir = dir % 6
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

    def copy(self):
        return Coordinate(self.a, self.b)

    def __str__(self):
        b = self.bary
        return "({},{},{})".format(b[0], b[1], b[2])
