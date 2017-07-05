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
