from math import sqrt
import cairo

h = sqrt(0.75)  # height of the triangle

# from graph import Node
# importing that later, when i understand it

class Canvas:
    # triangles will be stored in canvases
    
    def __init__(self, scale, width, height):
        self.scale = scale
        self.triangles = []
        self.drawn = False
        self.width = width
        self.height = height

    def __str__(self):
        s = ''
        for i, ts in enumerate(self.triangles):
            for j, t in enumerate(ts):
                if t:
                    mapped = '{} {}  '.format(i,j)
                    s = s + mapped + t.__str__() + '\n'
        return s

    def mapCoordinates(self, coordinate, up):
        # works
        
        # map negative coordinates to odd and positive to even indices
        mapCoordA = lambda i, up: 2 * i if i >= 0 else -2 * i -1
        # leave space for two triangles per coordinate (up and down)
        mapCoordB = lambda i, up: (
            2 if up else 0) + (4 * i if i >= 0 else -4 * i -1)
        a = mapCoordA(coordinate.a, up)
        b = mapCoordB(coordinate.b, up)
        return(a, b)

    def show(self, coordinate, up, color = None):
        s = self.scale
        width = self.width
        height = self.height
        cart = coordinate.cartesian(s)
        """ doesnt work :/
        if(cart[0] > -width / 2 + s / 2  # only show in screen
           and cart[0] < width / 2 - s / 2
           and cart[1] > -height / 2 + s
           and cart[1] < height / 2 - s):
        """
        tr = self.get(coordinate, up)
        if tr is None:
            self.add(Triangle(coordinate, up, color))
            tr = self.get(coordinate, up)
        elif color is not None:
            tr.setColor(color)
            
        tr.show()
        
    def hideAll(self):
        for ts in self.triangles:
            for t in ts:
                if t:
                    t.hide()

    def add(self, triangle, overwrite=False):
        coordinate = triangle.coordinate
        up = triangle.up
        a, b = self.mapCoordinates(coordinate, up)
        # expand array if neccessary
        la = len(self.triangles)
        if la <= a:
            for _ in range(la, a+1):
                # add individual empty lists
                self.triangles += [[]]
        # expand array for second coordinate
        lb = len(self.triangles[a])
        if lb <= b:
            self.triangles[a] += (b - lb + 1) * [None]

        # store triangle if there is none yet
        if self.triangles[a][b] is None or overwrite:
            # add bidirectional ink between triangle and canvas
            self.triangles[a][b] = triangle
            triangle.addCanvas(self)
        return self.triangles[a][b]

    def get(self, coordinate, up):
        a,b = self.mapCoordinates(coordinate, up)
        if len(self.triangles) > a:
            if len(self.triangles[a]) > b:
                   return self.triangles[a][b]
    """
    def makeTriangle(self, up,  a, b, color = 'BLACK'):
        cor = Coordinate(a,b)
        tr =  Triangle(cor, up, color)
        self.add(tr, True)
        self.drawn = False
    """

    def draw(self, ctx, pri=False):
        #draws all triangles to the screen
        
        scale = self.scale
        for ts in self.triangles:
            for t in ts:
                if t:
                    t.draw(ctx, scale)
        if pri:
            print(self)
            
        self.drawn = True

class Triangle:
    # class for drawing and modifying triangles
    # win:         window to draw in
    # coordinate:  the central edge
    # up(boolean): central edge above or below the triangle 
    
    def __init__(self, coordinate, up, color = None):
        self.coordinate = coordinate
        self.up = up
        self.color = color
        self.canvas = None
        self.visible = True

    def __str__(self):
        u = 'UP' if self.up else 'DOWN'
        
        return '{0}\t{1}\t{2}'.format(str(self.coordinate), u, self.color)

    def points(self):
        # returns all edges
        if(self.up is False):
            return (Coordinate(self.coordinate.a + 1, self.coordinate.b),
                    Coordinate(self.coordinate.a + 1, self.coordinate.b - 1),
                    self.coordinate)
        else:
            return (Coordinate(self.coordinate.a - 1, self.coordinate.b),
                    Coordinate(self.coordinate.a - 1, self. coordinate.b + 1),
                    self.coordinate)

    def draw(self, ctx, scale):
        
        if self.visible:
            coordinates = self.points()
            cart = coordinates[0].cartesian(scale)
            x, y  = cart[0], cart[1]
            cart = coordinates[1].cartesian(scale)
            x1,y1 = cart[0], cart[1]
            cart = coordinates[2].cartesian(scale)
            x2,y2 = cart[0], cart[1]
            
            color = self.color
            if color is not None:
                ctx.set_source_rgb(color[0],color[1],color[2])
            """
            ctx.new_path()
            ctx.move_to(x,y)
            ctx.line_to(x1, y1)
            ctx.line_to(x2, y2)
            ctx.close_path()
            
            ctx.stroke()
            """

            ctx.new_path()
            ctx.move_to(x,y)
            ctx.line_to(x1, y1)
            ctx.line_to(x2, y2)
            ctx.close_path()

            ctx.fill()
            """
            #"""

    def setColor(self, color):
        self.color = color
            
    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False
            
    def addCanvas(self, canvas):
        self.canvas = canvas

    def getMid(self):
        coordinates = self.points()
        x = (coordinates[0].a + coordinates[1].a + coordinates[2].a) / 3
        y = (coordinates[0].b + coordinates[1].b + coordinates[2].b) / 3
        return Coordinate(x,y)
        
class Coordinate:
    # points in a barycentric coordinate system

    def __init__(self, a, b, c=None):
        self.a = a
        self.b = b
        self.c = c
        if(self.c is None): 
            self.c = 1-(a+b)
        if(int(self.a + self.b + self.c + 0.000000001) != 1):
            raise Exception("barys are != 1")
        self.bary = (self.a, self.b, self.c)

    def __eq__(self, other):
        # if you know a and b of a coordinate, you can estimate c
        # so we only compare a and b
        b1 = self.bary
        b2 = other.bary
        return b1[0] == b2[0] and b1[1] == b2[1]

    def __str__(self):
        b = self.bary
        return "({},{},{})".format(b[0], b[1], b[2])

    def cartesian(self, scale):
        # returns the coordinate as cartesian tuple
        
        x = 0.5 * self.bary[0] - 0.5 * self.bary[1]
        y = - h * self.bary[0] - h * self.bary[1]
        return (scale * x, scale * y)

    def bary_sameLine(self, coord):
        """ checks if two coordinates are on the same line in the bary-grid """
        return (coord.a == self.a or coord.b == self.b or coord.c == self.c)

    def lineDir(self, i):
        """ 
        gives out direction if you go from self to coord 
        only works if coords are on the same line
        """
        if(self.bary_sameLine(i)):
            if(i.c == self.c and i.a >= self.a and i.b <= self.b):
                return 0 # northeast
            if(i.b == self.b and i.a >= self.a and i.c <= self.c):
                return 1 # northwest
            if(i.a == self.a and i.b >= self.b and i.c <= self.c):
                return 2 # west
            if(i.c == self.c and i.a <= self.a and i.b >= self.b):
                return 3 # southwest
            if(i.b == self.b and i.a <= self.a and i.c >= self.c):
                return 4 # southeast
            if(i.a == self.a and i.b <= self.b and i.c >= self.c):
                return 5 # east
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
