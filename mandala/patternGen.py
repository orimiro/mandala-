from triangle import Coordinate, Triangle

def nativeHexagon(canvas, coord):
    coords = list(coord.neighbors())
    s = createShape()
    s.beginShape()
    for cb in coords:
        cc = cb.cartesian()
        s.vertex(cc[0], cc[1])
    s.endShape(CLOSE)
    shape(s)

def hexagonCircle(canvas, coord, line):
    if line < 1:
        return
    edges = [coord.neighbor(i, line) for i in range(6)]
    for i in range(6):
        drawLine(canvas, edges[i], edges[(i + 1) % 6])


def drawLine(canvas, a, b):
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
        canvas.add(tr)
        a = a.neighbor(dir)
        if(a.a == b.a and a.b == b.b):
            break
        # dir % 2 == 0 -> true/false --> with the directions you have 6
        # possibilitys
        tr = Triangle(None, coordB(a), dir % 2 == 0)
        canvas.add(tr)

def triangleDrawEast(canvas, start, end, up):
    for i in range(start, end):
        tr = Triangle(None, Coordinate(0, i), up)
        canvas.add(tr)

def triangleDrawSE(canvas, start, end, up):
    for i in range(start, end):
        tr = Triangle(None, Coordinate(i, 0), up)
        canvas.add(tr)

def triangleDrawSW(canvas, start, end, up):
    for i in range(start, end):
        tr = Triangle(None, Coordinate(i, -i), up)
        canvas.add(tr)

def triangleFillRect(canvas, leftUpper, rightLower):
    for i in range(0, 1):
        pass

def triangleAB(canvas, start, n, up):
    a, b, c = start.bary
    for i in range(0, n):
        tr = Triangle(None, Coordinate(a + i, b + i), up)
        canvas.add(tr)

def triangleBC(canvas, start, n, up):
    a, b, c = start.bary
    for i in range(0, n):
        tr = Triangle(None, Coordinate(a - 2 * i, b + i, c + i), up)
        canvas.add(tr)

def triangleAC(canvas, start, n, up):
    a, b, c = start.bary
    for i in range(0, n):
        tr = Triangle(None, Coordinate(a + i, b - 2 * i, c + i), up)
        canvas.add(tr)

def triangleESE(canvas, start, n, up):
    a, b, c = start.bary
    triangleAB(canvas, start, ceil(n / 2), up)
    triangleAB(canvas, Coordinate(a - 1, b + 1), floor(n / 2), not up)

def patterndLine2(canvas, a, dir, n, z, nr):
    # Draws a point
    dir = dir % 6
    # defining the start of the line, depending of direction:
    if(dir % 3 == 2):
        a = a.neighbor(dir).neighbor((dir + 1) % 6, 2)
    elif(dir % 3 == 1):
        a = a.neighbor(dir, 2).neighbor((dir + 1) % 6)
    else:
        a = a.neighbor(dir).neighbor((dir + 1) % 6)
    c = 0
    b = a
    while(c < n):
        tr = Triangle(
            None,
            a,
            (dir + z % 5) % 2 != 0)
        if(dir % 3 != (nr + 1) % 3):
            canvas.add(tr)
        else:
            c += 1
        tr = Triangle(
            None,
            a.neighbor((dir + 3 - z) % 6),
            (dir + z % 11) % 2 != 0)
        canvas.add(tr)
        tr = Triangle(
            None,
            a.neighbor((dir + 4 + z) % 6),
            (dir + z) % 2 != 0)
        canvas.add(tr)
        a = a.neighbor(dir).neighbor((dir + 1) % 6)
        c += 1
    if(dir % 3 == 1 and dir % 3 == (nr + 1) % 3):
        d = b.neighbor((dir + 1) % 6)
        patterndLine(canvas, d, dir - 2, 1, z)
        patterndLine(canvas, d, dir + 2, 1, z)
        d = b.neighbor((dir + z) % 6)
        drawLine(canvas, d.neighbor(dir, 2), d)
        d = b.neighbor(((dir + 1) % 6 - z) % 6).neighbor((dir + 2) % 6)
        drawLine(canvas, d, d.neighbor((dir + 1) % 6, 2))
    if(dir % 3 == 2 and dir % 3 == (nr + 1) % 3):
        d = b.neighbor((dir + 0) % 6)
        b = b.neighbor((dir - 1) % 6)
        patterndLine(canvas, d, dir - 2, 1, z)
        patterndLine(canvas, d, dir + 2, 1, z)
        d = b.neighbor((dir + z) % 6)
        drawLine(canvas, d.neighbor(dir, 2), d)
        d = b.neighbor(((dir + 1) % 6 - z) % 6).neighbor((dir + 2) % 6)
        drawLine(canvas, d, d.neighbor((dir + 1) % 6, 2))
    if(dir % 3 == 0 and dir % 3 == (nr + 1) % 3):
        d = b.neighbor((dir + 1) % 6).neighbor((dir) % 6)
        b = b.neighbor((dir) % 6)
        patterndLine(canvas, d, dir - 2, 1, z)
        patterndLine(canvas, d, dir + 2, 1, z)
        d = b.neighbor((dir + z) % 6)
        drawLine(canvas, d.neighbor(dir, 2), d)
        d = b.neighbor(((dir + 1) % 6 - z) % 6).neighbor((dir + 2) % 6)
        drawLine(canvas, d, d.neighbor((dir + 1) % 6, 2))

def patterndLine(canvas, a, dir, n, z):
    dir = dir % 6
    if(dir % 3 == 2):
        a = a.neighbor(dir).neighbor((dir + 1) % 6, 2)
    elif(dir % 3 == 1):
        a = a.neighbor(dir, 2).neighbor((dir + 1) % 6)
    else:
        a = a.neighbor(dir).neighbor((dir + 1) % 6)
    c = 0
    while(c < n):
        tr = Triangle(None, a,
                      (dir + z % 5) % 2 != 0)
        canvas.add(tr)
        tr = Triangle(None,
                      a.neighbor((dir + 3 - z) % 6),
                      (dir + z % 11) % 2 != 0)
        canvas.add(tr)
        tr = Triangle(None,
                      a.neighbor((dir + 4 + z) % 6),
                      (dir + z % 23) % 2 != 0)
        canvas.add(tr)
        a = a.neighbor(dir).neighbor((dir + 1) % 6)
        c += 1

def demo(k, canvas):
    """
    triangleAB(canvas, Coordinate(1,0,0), int(mouseX/50), True)
    triangleBC(canvas, Coordinate(1,0,0), int(mouseX/50), True)
    triangleAC(canvas, Coordinate(1,0,0), int(mouseX/50), True)
    triangleESE(canvas, Coordinate(1, 0, 0), int(mouseX / 50), True)
    hexagonCircle(canvas, Coordinate(1, 0, 0), 1)
    c = Coordinate(1, 0, 0).sw(2).se(2)
    hexagonCircle(canvas, c, int(mouseY / 25))
    hexagonCircle(canvas, c.ne(5), int(mouseY / 25))
    hexagonCircle(canvas, c.nw(5), int(mouseY / 25))
    c = Coordinate(1, 0, 0)
    for i in range(int(mouseY / 25)):
        hexagonCircle(canvas, c, i)
    """
    # hide all triangles initially
    canvas.hideAll()
    c = Coordinate(1, 0, 0)
    z = mouseY/10
    for i in range(6):
        patterndLine(canvas, c, i, 2, z)
        patterndLine2(canvas, c.neighbor(0, 9), i, 2, z, 0)
        patterndLine(canvas, c.neighbor(0, 9).neighbor(0, 9), i, 2, z)
        patterndLine2(
            canvas, c.neighbor(0, 9).neighbor(0, 9).neighbor(2, 9), i, 2, z, 2)
        patterndLine2(canvas, c.neighbor(1, 9), i, 2, z, 1)
        patterndLine(canvas, c.neighbor(1, 9).neighbor(1, 9), i, 2, z)
        patterndLine2(
            canvas, c.neighbor(1, 9).neighbor(1, 9).neighbor(3, 9), i, 2, z, 0)
        patterndLine2(canvas, c.neighbor(2, 9), i, 2, z, 2)
        patterndLine(canvas, c.neighbor(2, 9).neighbor(2, 9), i, 2, z)
        patterndLine2(
            canvas, c.neighbor(2, 9).neighbor(2, 9).neighbor(4, 9), i, 2, z, 1)
        patterndLine2(canvas, c.neighbor(3, 9), i, 2, z, 0)
        patterndLine(canvas, c.neighbor(3, 9).neighbor(3, 9), i, 2, z)
        patterndLine2(
            canvas, c.neighbor(3, 9).neighbor(3, 9).neighbor(5, 9), i, 2, z, 2)
        patterndLine2(canvas, c.neighbor(4, 9), i, 2, z, 1)
        patterndLine(canvas, c.neighbor(4, 9).neighbor(4, 9), i, 2, z)
        patterndLine2(
            canvas, c.neighbor(4, 9).neighbor(4, 9).neighbor(0, 9), i, 2, z, 0)
        patterndLine2(canvas, c.neighbor(5, 9), i, 2, z, 2)
        patterndLine(canvas, c.neighbor(5, 9).neighbor(5, 9), i, 2, z)
        patterndLine2(
            canvas, c.neighbor(5, 9).neighbor(5, 9).neighbor(1, 9), i, 2, z, 1)