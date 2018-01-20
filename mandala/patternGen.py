from triangle import Coordinate, Triangle

################################################################################
# # # # # # # # # # some functions to generate Patterns  # # # # # # # # # # # #
################################################################################

def hexagonCircle(canvas, coord, line):
    if line < 1:
        return
    edges = [coord.neighbor(i, line) for i in range(6)]
    for i in range(6):
        drawLine(canvas, edges[i], edges[(i + 1) % 6])


def drawLine(canvas, a, b):
    """ draws a line from coordinate a to coordinate b """
    dir = a.lineDir(b)  # getting line direction

    # a closed line of triangles consists of two "saw"-like lines
    # making two functions here to estimate the two start-points
    if(dir % 3 == 2):  # 2 and 5 --> west and east
        coordA = lambda l: l.neighbor(dir + 1)
        coordB = lambda l: l
    elif(dir % 3 == 0):  # 0 and 3 --> northeast and southwest
        coordA = lambda l: l
        coordB = lambda l: l.neighbor(dir + 1)
    else:  # (dir % 3 == 1) -> 1 and 4 --> northwest and southeast
        coordA = lambda l: l.neighbor(dir)
        coordB = lambda l: l.neighbor(dir + 2)
        
    # until break the lines will be drawn
    while(True):
        # dir % 2 != 0 -> true/false --  determins if 1. line is upwards
        canvas.show(coordA(a), dir % 2 != 0)
        a = a.neighbor(dir)
        if(a.a == b.a and a.b == b.b):
            break
        # dir % 2 == 0 -> true/false  --  determins if 2. line is upwards
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

################################################################################

def patterndLine(canvas, coord, direction, length, variation, color = None):
    """ Draws a "line-like" Pattern in a specific direction
    """
    
    direction = direction % 6 # making sure direction is between 0 and 5
    
    # replace coordinate depending on direction
    coord = starting_point_patternd_line(direction, coord)
    
    c = 0

    #if(col!=None) ctx.set_source_rgb(col[0],0.5,1)
    
    #
    while(c < length):
        canvas.show(coord,
                    (direction + variation % 5) % 2 != 0, color)
        canvas.show(coord.neighbor(direction + 3 - variation,),
                    (direction + variation % 11) % 2 != 0, color)
        canvas.show(coord.neighbor(direction + 4 + variation),
                    (direction + variation % 23) % 2 != 0, color)

        coord = coord.neighbor(direction).neighbor(direction + 1)
        c += 1

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
    pattern_stuff(canvas, a, dir, nr, z)
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
        
def patternA(canvas, coordinate, schichten, variation):
    pattern_1(canvas, coordinate, 2, variation)
    for n in range(6):
        direction = coordinate.neighbor(n, 9)
        pattern_2(canvas, direction, 2, variation, n)
        layers = direction
        for s in range(2, schichten):
            layers = layers.neighbor(n, 9)
            if(s % 2 == 0):
                pattern_1(canvas, layers, 2, variation)
            else:
                pattern_2(canvas, layers, 2, variation, n)
            d = layers.neighbor(n + 2, 9)
            pattern_2(canvas, d, 2, variation,
                     ((s % 2) * 2) + n + 2)
            for l in range(2, s):
                d = d.neighbor(n + 2, 9)
                if(s % 2 == 0):
                    if(l % 2 == 0):
                        pattern_1(canvas, d, 2, variation)
                    else:
                        pattern_2(canvas, d, 2, variation, (l % 2) + n + 1)
                else:
                    pattern_2(canvas, d, 2, variation, (l % 2) + n)

def patternB(canvas, coordinate, schichten, variation):
    pattern_1(canvas, coordinate, 2, variation)
    for n in range(6):
        direction = coordinate.neighbor(n, 9)
        pattern_2(canvas, direction, 2, variation+1, n)
        layers = direction
        for s in range(2, schichten):
            layers = layers.neighbor(n, 9)
            if(s % 2 == 0):
                pattern_1(canvas, layers, 2, variation+s)
            else:
                pattern_2(canvas, layers, 2, variation+s, n)
            d = layers.neighbor(n + 2, 9)
            pattern_2(canvas, d, 2, variation+s,
                     ((s % 2) * 2) + n + 2)
            for l in range(2, s):
                d = d.neighbor(n + 2, 9)
                if(s % 2 == 0):
                    if(l % 2 == 0):
                        pattern_1(canvas, d, 2, variation+s)
                    else:
                        pattern_2(canvas, d, 2, variation+s, (l % 2) + n + 1)
                else:
                    pattern_2(canvas, d, 2, variation+s, (l % 2) + n)

def pattern_1(canvas, coordinate, size, variation,r,g,b):
    for i in range(6):
        if (i % 3 == 0):
            patterndLine(canvas, coordinate, i, size, variation,g)
        if (i % 3 == 1):
            patterndLine(canvas, coordinate, i, size, variation,b)
        if (i % 3 == 2):
            patterndLine(canvas, coordinate, i, size, variation,r)

def pattern_2(canvas, coordinate, size, variation, direction):
    for i in range(6):
        patterndLine2(canvas, coordinate, i, size, variation, direction)

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
    #patternA(canvas, c, schichten, z)
    patternB(canvas, c, schichten, z)

    
""" has to be ported to cairo
def nativeHexagon(canvas, coord):
    coords = list(coord.neighbors())
    s = createShape()
    s.beginShape()
    for cb in coords:
        cc = cb.cartesian()
        s.vertex(cc[0], cc[1])
    s.endShape(CLOSE)
    shape(s)
"""

################################################################################
# helper functions:

def starting_point_patternd_line(direction, coord):
    if(direction % 3 == 2):
        return coord.neighbor(direction).neighbor(direction + 1, 2)
    elif(direction % 3 == 1):
        return coord.neighbor(direction, 2).neighbor(direction + 1)
    else:
        return coord.neighbor(direction).neighbor(direction + 1)
    
def pattern_stuff(canvas, coord, direction, nr, z):
    """
    i dont understand this anymore, but need it for patter creation
    """
    
    if(direction % 3 == 1 and direction % 3 == (nr + 1) % 3):
        temp_coord = coord.neighbor(direction + 1)
        patterndLine(canvas, temp_coord, direction - 2, 1, z)
        patterndLine(canvas, temp_coord, direction + 2, 1, z)
        temp_coord = coord.neighbor(direction + z)
        drawLine(canvas, temp_coord.neighbor(direction, 2), temp_coord)
        temp_coord = coord.neighbor((direction + 1) % 6 - z).neighbor(direction + 2)
        drawLine(canvas, temp_coord, temp_coord.neighbor(direction + 1, 2))
        
    if(direction % 3 == 2 and direction % 3 == (nr + 1) % 3):
        temp_coord = coord.neighbor(direction + 0)
        coord = coord.neighbor(direction - 1)
        patterndLine(canvas, temp_coord, direction - 2, 1, z)
        patterndLine(canvas, temp_coord, direction + 2, 1, z)
        temp_coord = coord.neighbor(direction + z)
        drawLine(canvas, temp_coord.neighbor(direction, 2), temp_coord)
        temp_coord = coord.neighbor((direction + 1) % 6 - z).neighbor(direction + 2)
        drawLine(canvas, temp_coord, temp_coord.neighbor(direction + 1, 2))
        
    if(direction % 3 == 0 and direction % 3 == (nr + 1) % 3):
        temp_coord = coord.neighbor(direction + 1).neighbor(direction)
        coord = coord.neighbor(direction)
        patterndLine(canvas, temp_coord, direction - 2, 1, z)
        patterndLine(canvas, temp_coord, direction + 2, 1, z)
        temp_coord = coord.neighbor(direction + z)
        drawLine(canvas, temp_coord.neighbor(direction, 2), temp_coord)
        temp_coord = coord.neighbor((direction + 1) % 6 - z).neighbor(direction + 2)
        drawLine(canvas, temp_coord, temp_coord.neighbor(direction + 1, 2))
    
