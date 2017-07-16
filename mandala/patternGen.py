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
        coordA = lambda l: l.neighbor(dir + 1)
        coordB = lambda l: l
    elif(dir % 3 == 0):  # 0 and 3 --> northeast and southwest
        coordA = lambda l: l
        coordB = lambda l: l.neighbor(dir + 1)
    else:  # (dir % 3 == 1) -> 1 and 4 --> northwest and southeast
        coordA = lambda l: l.neighbor(dir)
        coordB = lambda l: l.neighbor(dir + 2)
    c = 0
    while(True):
        # dir % 2 != 0 -> true/false --> with the directions you have 6
        # possibilitys
        canvas.show(coordA(a), dir % 2 != 0)
        a = a.neighbor(dir)
        if(a.a == b.a and a.b == b.b):
            break
        # dir % 2 == 0 -> true/false --> with the directions you have 6
        # possibilitys
        canvas.show(coordB(a), dir % 2 == 0)

def triangleDrawEast(canvas, start, end, up):
    for i in range(start, end):
        canvas.show(Coordinate(0, i), up)

def triangleDrawSE(canvas, start, end, up):
    for i in range(start, end):
        canvas.show(Coordinate(i, 0), up)

def triangleDrawSW(canvas, start, end, up):
    for i in range(start, end):
        canvas.show(Coordinate(i, -i), up)

def triangleFillRect(canvas, leftUpper, rightLower):
    for i in range(0, 1):
        pass

def triangleAB(canvas, start, n, up):
    a, b, c = start.bary
    for i in range(0, n):
        canvas.show(Coordinate(a + i, b + i), up)

def triangleBC(canvas, start, n, up):
    a, b, c = start.bary
    for i in range(0, n):
        canvas.show(Coordinate(a - 2 * i, b + i, c + i), up)

def triangleAC(canvas, start, n, up):
    a, b, c = start.bary
    for i in range(0, n):
        canvas.show(Coordinate(a + i, b - 2 * i, c + i), up)

def triangleESE(canvas, start, n, up):
    a, b, c = start.bary
    triangleAB(canvas, start, ceil(n / 2), up)
    triangleAB(canvas, Coordinate(a - 1, b + 1), floor(n / 2), not up)

def patterndLine2(canvas, a, dir, n, z, nr):
    # Draws a point
    dir = dir % 6
    # defining the start of the line, depending of direction:
    if(dir % 3 == 2):
        a = a.neighbor(dir).neighbor(dir + 1, 2)
    elif(dir % 3 == 1):
        a = a.neighbor(dir, 2).neighbor(dir + 1)
    else:
        a = a.neighbor(dir).neighbor(dir + 1)
    c = 0
    b = a
    while(c < n):
        if(dir % 3 != (nr + 1) % 3):
            canvas.show(a, (dir + z % 5) % 2 != 0)
        else:
            c += 1
        canvas.show(a.neighbor(dir + 3 - z),
                    (dir + z % 11) % 2 != 0)

        canvas.show(a.neighbor(dir + 4 + z),
                    (dir + z) % 2 != 0)

        a = a.neighbor(dir).neighbor(dir + 1)
        c += 1
    if(dir % 3 == 1 and dir % 3 == (nr + 1) % 3):
        d = b.neighbor(dir + 1)
        patterndLine(canvas, d, dir - 2, 1, z)
        patterndLine(canvas, d, dir + 2, 1, z)
        d = b.neighbor(dir + z)
        drawLine(canvas, d.neighbor(dir, 2), d)
        d = b.neighbor((dir + 1) % 6 - z).neighbor(dir + 2)
        drawLine(canvas, d, d.neighbor(dir + 1, 2))
    if(dir % 3 == 2 and dir % 3 == (nr + 1) % 3):
        d = b.neighbor(dir + 0)
        b = b.neighbor(dir - 1)
        patterndLine(canvas, d, dir - 2, 1, z)
        patterndLine(canvas, d, dir + 2, 1, z)
        d = b.neighbor(dir + z)
        drawLine(canvas, d.neighbor(dir, 2), d)
        d = b.neighbor((dir + 1) % 6 - z).neighbor(dir + 2)
        drawLine(canvas, d, d.neighbor(dir + 1, 2))
    if(dir % 3 == 0 and dir % 3 == (nr + 1) % 3):
        d = b.neighbor(dir + 1).neighbor(dir)
        b = b.neighbor(dir)
        patterndLine(canvas, d, dir - 2, 1, z)
        patterndLine(canvas, d, dir + 2, 1, z)
        d = b.neighbor(dir + z)
        drawLine(canvas, d.neighbor(dir, 2), d)
        d = b.neighbor((dir + 1) % 6 - z).neighbor(dir + 2)
        drawLine(canvas, d, d.neighbor(dir + 1, 2))

def patterndLine(canvas, a, dir, n, z):
    dir = dir % 6
    if(dir % 3 == 2):
        a = a.neighbor(dir).neighbor(dir + 1, 2)
    elif(dir % 3 == 1):
        a = a.neighbor(dir, 2).neighbor(dir + 1)
    else:
        a = a.neighbor(dir).neighbor(dir + 1)
    c = 0
    while(c < n):
        canvas.show(a, (dir + z % 5) % 2 != 0)

        canvas.show(a.neighbor(dir + 3 - z),
                    (dir + z % 11) % 2 != 0)

        canvas.show(a.neighbor(dir + 4 + z),
                    (dir + z % 23) % 2 != 0)

        a = a.neighbor(dir).neighbor(dir + 1)
        c += 1

def pattern1(canvas, coordinate, size, variation):
    for i in range(6):
        patterndLine(canvas, coordinate, i, size, variation)

def pattern2(canvas, coordinate, size, variation, direction):
    for i in range(6):
        patterndLine2(canvas, coordinate, i, 2, variation, direction)

def demo(canvas):
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
    z = mouseY / 10

    schichten = 4
    pattern1(canvas, c, 2, z)
    for n in range(6):
        direction = c.neighbor(n, 9)
        pattern2(canvas, direction, 2, z, n)
        layers = direction
        for s in range(2, schichten):
            layers = layers.neighbor(n, 9)
            if(s % 2 == 0):
                pattern1(canvas, layers, 2, z)
            else:
                pattern2(canvas, layers, 2, z, n)
            d = layers.neighbor(n + 2, 9)
            pattern2(canvas, d, 2, z,
                     ((s % 2) * 2) + n + 2)
            for l in range(2, s):
                d = d.neighbor(n + 2, 9)
                if(s % 2 == 0):
                    if(l % 2 == 0):
                        pattern1(canvas, d, 2, z)
                    else:
                        pattern2(canvas, d, 2, z, (l % 2) + n + 1)
                else:
                    pattern2(canvas, d, 2, z, (l % 2) + n)
