from triangle import Coordinate, Triangle

def hexagonDrawing(scale):
    #south
    loc = Coordinate(1, 0, 0)
    tr0 = Triangle(None, loc, False)
    #northwesth
    loc = Coordinate(0, 0, 1)
    tr1 = Triangle(None, loc, False)
    #southwest
    loc = Coordinate(2, -1, 0)
    tr2 = Triangle(None, loc, True)
    #south
    loc = Coordinate(1, 0, 0)
    tr3 = Triangle(None, loc, True)
    #northeast
    loc = Coordinate(0, 1, 0)
    tr4 = Triangle(None, loc, False)
    #southeast
    loc = Coordinate(2, 0, -1)
    tr5 = Triangle(None, loc, True)
    
    tr0.draw(scale)
    tr1.draw(scale)
    tr2.draw(scale)
    tr3.draw(scale)
    tr4.draw(scale)
    tr5.draw(scale)

def nativeHexagon(scale, coord):
    coords = list(coord.neighbors())
    s = createShape()
    s.beginShape()
    for cb in coords:
        cc = cb.cartesian()
        s.vertex(cc[0], cc[1])
    s.endShape(CLOSE)
    shape(s)

def triangleDrawEast(scale, start, end, up):
    for i in range(start, end):
        tr = Triangle(None, Coordinate(0, i), up)
        tr.draw(scale)

def triangleDrawSE(scale, start, end, up):
    for i in range(start, end):
        tr = Triangle(None, Coordinate(i, 0), up)
        tr.draw(scale)

def triangleDrawSW(scale, start, end, up):
    for i in range(start, end):
        tr = Triangle(None, Coordinate(i, -i), up)
        tr.draw(scale)

def triangleFillRect(scale, leftUpper, rightLower):
    for i in range(0, 1):
        pass

def triangleAB(scale, start, n, up):
    a,b,c = start.bary
    for i in range(0, n):
        tr = Triangle(None, Coordinate(a+i, b+i), up)
        tr.draw(scale)

def triangleBC(scale, start, n, up):
    a,b,c = start.bary
    for i in range(0, n):
        tr = Triangle(None, Coordinate(a - 2*i, b+i, c+i), up)
        tr.draw(scale)

def triangleAC(scale, start, n, up):
    a,b,c = start.bary
    for i in range(0, n):
        tr = Triangle(None, Coordinate(a+i, b - 2*i, c+i), up)
        tr.draw(scale)

def triangleESE(scale, start, n, up):
    a,b,c = start.bary
    triangleAB(scale, start, ceil(n/2), up)
    triangleAB(scale, Coordinate(a-1, b+1), floor(n/2), not up)
def demo():
    scale = 20
    #triangleAB(scale, Coordinate(1,0,0), int(mouseX/50), True)
    #triangleBC(scale, Coordinate(1,0,0), int(mouseX/50), True)
    #triangleAC(scale, Coordinate(1,0,0), int(mouseX/50), True)
    triangleESE(scale, Coordinate(1,0,0), int(mouseX/50), True)