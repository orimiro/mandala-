from triangle import Coordinate, Triangle

def hexagonDrawing(scale):
    # south
    loc = Coordinate(1, 0, 0)
    tr0 = Triangle(None, loc, False)
    # northwesth
    loc = Coordinate(0, 0, 1)
    tr1 = Triangle(None, loc, False)
    # southwest
    loc = Coordinate(2, -1, 0)
    tr2 = Triangle(None, loc, True)
    # south
    loc = Coordinate(1, 0, 0)
    tr3 = Triangle(None, loc, True)
    # northeast
    loc = Coordinate(0, 1, 0)
    tr4 = Triangle(None, loc, False)
    # southeast
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

def hexagonCircle(scale, coord, line):
    if line < 1:
        return
    edges = [coord.neighbor(i, line) for i in range(6)]
    drawLine0(scale, edges[0], edges[1])
    drawLine1(scale, edges[1], edges[2])
    drawLine2(scale, edges[2], edges[3])
    drawLine3(scale, edges[3], edges[4])
    drawLine4(scale, edges[4], edges[5])
    drawLine5(scale, edges[5], edges[0])

def drawLine0(scale, a, b):  # sharp edge south, from sharp edge to sharp edge
    while(True):
        tr = Triangle(None, a.ne(), False)
        tr.draw(scale)
        #if(a.a == b.a and a.b == b.b):
        #    break
        a = a.east()
        if(a.a == b.a and a.b == b.b):
            break
        tr = Triangle(None, a, True)
        tr.draw(scale)

def drawLine1(scale, a, b):  # sharp edge se, from sharp edge to sharp edge
    while(True):
        tr = Triangle(None, a, True)
        tr.draw(scale)
        #if(a.a == b.a and a.b == b.b):
        #    break
        a = a.ne()
        if(a.a == b.a and a.b == b.b):
            break
        tr = Triangle(None, a.nw(), False)
        tr.draw(scale)

def drawLine2(scale, a, b):  # sharp edge ne, from sharp edge to sharp edge
    while(True):
        if(a.a == b.a and a.b == b.b):
            break
        a = a.nw()
        tr = Triangle(None, a, False)
        tr.draw(scale)
        if(a.a == b.a and a.b == b.b):
            break
        tr = Triangle(None, a.sw(), True)
        tr.draw(scale)
        
def drawLine3(scale, a, b):  # sharp edge south(-1), from sharp edge to sharp edge
    while(True):
        tr = Triangle(None, a.ne(-1), True)
        tr.draw(scale)
        #if(a.a == b.a and a.b == b.b):
        #    break
        a = a.east(-1)
        if(a.a == b.a and a.b == b.b):
            break
        tr = Triangle(None, a, False)
        tr.draw(scale)
        
def drawLine4(scale, a, b):  # sharp edge se(-1), from sharp edge to sharp edge
    while(True):
        tr = Triangle(None, a, False)
        tr.draw(scale)
        #if(a.a == b.a and a.b == b.b):
        #    break
        a = a.ne(-1)
        if(a.a == b.a and a.b == b.b):
            break
        tr = Triangle(None, a.nw(-1), True)
        tr.draw(scale)
        
def drawLine5(scale, a, b):  # sharp edge ne, from sharp edge to sharp edge
    while(True):
        if(a.a == b.a and a.b == b.b):
            break
        a = a.nw(-1)
        tr = Triangle(None, a, True)
        tr.draw(scale)
        if(a.a == b.a and a.b == b.b):
            break
        tr = Triangle(None, a.sw(-1), False)
        tr.draw(scale)

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
    a, b, c = start.bary
    for i in range(0, n):
        tr = Triangle(None, Coordinate(a + i, b + i), up)
        tr.draw(scale)

def triangleBC(scale, start, n, up):
    a, b, c = start.bary
    for i in range(0, n):
        tr = Triangle(None, Coordinate(a - 2 * i, b + i, c + i), up)
        tr.draw(scale)

def triangleAC(scale, start, n, up):
    a, b, c = start.bary
    for i in range(0, n):
        tr = Triangle(None, Coordinate(a + i, b - 2 * i, c + i), up)
        tr.draw(scale)

def triangleESE(scale, start, n, up):
    a, b, c = start.bary
    triangleAB(scale, start, ceil(n / 2), up)
    triangleAB(scale, Coordinate(a - 1, b + 1), floor(n / 2), not up)
def demo():
    scale = 20
    #triangleAB(scale, Coordinate(1,0,0), int(mouseX/50), True)
    #triangleBC(scale, Coordinate(1,0,0), int(mouseX/50), True)
    #triangleAC(scale, Coordinate(1,0,0), int(mouseX/50), True)
    #triangleESE(scale, Coordinate(1, 0, 0), int(mouseX / 50), True)
    #hexagonCircle(scale, Coordinate(1, 0, 0), 1)
    c = Coordinate(1, 0, 0).sw().se()
    hexagonCircle(scale, c, int(mouseY/25))
    hexagonCircle(scale, c.ne(5), int(mouseY/25))
    hexagonCircle(scale, c.nw(5), int(mouseY/25))