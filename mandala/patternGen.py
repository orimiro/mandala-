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
    for i in range(6):
        drawLine(scale, edges[i], edges[(i + 1) % 6])


def drawLine(scale, a, b):
    dir = a.lineDir(b)  # getting line direction
    if(dir % 3 == 2):  # 2 and 5 --> west and east
        coordA = lambda l: l.neighbor((dir + 1) % 6)
        coordB = lambda l: l
    elif(dir % 3 == 0):  # 0 and 3 --> northeast and southwest
        coordA = lambda l: l
        coordB = lambda l: l.neighbor((dir + 1) % 6)
    else:  # (dir % 3 == 1) -> 1 and 4 --> northwest and southeast
        coordA = lambda l: l.neighbor((dir) % 6)
        coordB = lambda l: l.neighbor((dir + 2) % 6)
    c = 0
    while(True):
        # dir % 2 != 0 -> true/false --> with the directions you have 6
        # possibilitys
        tr = Triangle(None, coordA(a), dir % 2 != 0)
        tr.draw(scale)
        a = a.neighbor(dir)
        if(a.a == b.a and a.b == b.b):
            break
        # dir % 2 == 0 -> true/false --> with the directions you have 6
        # possibilitys
        tr = Triangle(None, coordB(a), dir % 2 == 0)
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

def patterndLine(scale, a, dir, n, z):
    # Draws a patternd Line
    dir = dir % 6
    if(dir % 3 == 2):
        a = a.neighbor(dir).neighbor((dir + 1) % 6, 2)
    elif(dir % 3 == 1):
        a = a.neighbor(dir, 2).neighbor((dir + 1) % 6)
    else:
        a = a.neighbor(dir).neighbor((dir + 1) % 6)
    c = 0
    while(c < n):
        tr = Triangle(
            None,
            a,
            (dir + z % 5) % 2 != 0)
        tr.draw(scale)
        tr = Triangle(
            None,
            a.neighbor((dir + 3 - z) % 6),
            (dir + z % 11) % 2 != 0)
        tr.draw(scale)
        tr = Triangle(
            None,
            a.neighbor((dir + 4 + z) % 6),
            (dir + z % 23) % 2 != 0)
        tr.draw(scale)
        a = a.neighbor(dir).neighbor((dir + 1) % 6)
        c += 1

def demo():
    scale = 10
    """
    triangleAB(scale, Coordinate(1,0,0), int(mouseX/50), True)
    triangleBC(scale, Coordinate(1,0,0), int(mouseX/50), True)
    triangleAC(scale, Coordinate(1,0,0), int(mouseX/50), True)
    triangleESE(scale, Coordinate(1, 0, 0), int(mouseX / 50), True)
    hexagonCircle(scale, Coordinate(1, 0, 0), 1)
    c = Coordinate(1, 0, 0).sw(2).se(2)
    hexagonCircle(scale, c, int(mouseY / 25))
    hexagonCircle(scale, c.ne(5), int(mouseY / 25))
    hexagonCircle(scale, c.nw(5), int(mouseY / 25))
    c = Coordinate(1, 0, 0)
    for i in range(int(mouseY / 25)):
        hexagonCircle(scale, c, i)
    """
    c = Coordinate(1, 0, 0)
    for i in range(6):
        patterndLine(scale, c, i, 2, mouseY / 10)
        patterndLine(scale, c.neighbor(0, 9), i, 2, mouseY / 10)
        patterndLine(scale, c.neighbor(0, 9).neighbor(0, 9), i, 2, mouseY / 10)
        patterndLine(scale, c.neighbor(0, 9).neighbor(
            0, 9).neighbor(2, 9), i, 2, mouseY / 10)
        patterndLine(scale, c.neighbor(1, 9), i, 2, mouseY / 10)
        patterndLine(scale, c.neighbor(1, 9).neighbor(1, 9), i, 2, mouseY / 10)
        patterndLine(scale, c.neighbor(1, 9).neighbor(
            1, 9).neighbor(3, 9), i, 2, mouseY / 10)
        patterndLine(scale, c.neighbor(2, 9), i, 2, mouseY / 10)
        patterndLine(scale, c.neighbor(2, 9).neighbor(2, 9), i, 2, mouseY / 10)
        patterndLine(scale, c.neighbor(2, 9).neighbor(
            2, 9).neighbor(4, 9), i, 2, mouseY / 10)
        patterndLine(scale, c.neighbor(3, 9), i, 2, mouseY / 10)
        patterndLine(scale, c.neighbor(3, 9).neighbor(3, 9), i, 2, mouseY / 10)
        patterndLine(scale, c.neighbor(3, 9).neighbor(
            3, 9).neighbor(5, 9), i, 2, mouseY / 10)
        patterndLine(scale, c.neighbor(4, 9), i, 2, mouseY / 10)
        patterndLine(scale, c.neighbor(4, 9).neighbor(4, 9), i, 2, mouseY / 10)
        patterndLine(scale, c.neighbor(4, 9).neighbor(
            4, 9).neighbor(0, 9), i, 2, mouseY / 10)
        patterndLine(scale, c.neighbor(5, 9), i, 2, mouseY / 10)
        patterndLine(scale, c.neighbor(5, 9).neighbor(5, 9), i, 2, mouseY / 10)
        patterndLine(scale, c.neighbor(5, 9).neighbor(
            5, 9).neighbor(1, 9), i, 2, mouseY / 10)
