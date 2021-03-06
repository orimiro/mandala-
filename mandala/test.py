from graph import Node
from triangle import Coordinate
from triangle import Triangle

def testNode():
    a = Node(None)
    b = Node(None)
    c = Node(None, a, b)
    d = Node(None, a)
    e = Node(None, c)
    assert(a not in a.children)
    assert(a not in b.children)
    assert(a in c.children)
    assert(a in d.children)
    assert(a in d.children)
    assert(b not in a.children)
    assert(b not in b.children)
    assert(b in c.children)
    assert(b not in d.children)
    assert(b not in e.children)
    assert(c in a.children)
    assert(c in b.children)
    assert(c not in c.children)
    assert(c not in d.children)
    assert(c in e.children)
    assert(d in a.children)
    assert(d not in b.children)
    assert(d not in c.children)
    assert(d not in d.children)
    assert(d not in e.children)
    assert(e not in a.children)
    assert(e not in b.children)
    assert(e in c.children)
    assert(e not in d.children)
    assert(e not in e.children)
def testNode2():
    a = Node(None)
    b = Node(None)
    c = Node(None, a, b)
    d = Node(None, a, b)
    e = Node(None, c, d)
    assert(a not in a.children)
    assert(a not in b.children)
    assert(a in c.children)
    assert(a in d.children)
    assert(a not in e.children)
    assert(b not in a.children)
    assert(b not in b.children)
    assert(b in c.children)
    assert(b in d.children)
    assert(b not in e.children)
    assert(c in a.children)
    assert(c in b.children)
    assert(c not in c.children)
    assert(c not in d.children)
    assert(c in e.children)
    assert(d in a.children)
    assert(d in b.children)
    assert(d not in c.children)
    assert(d not in d.children)
    assert(d in e.children)
    assert(e not in a.children)
    assert(e not in b.children)
    assert(e in c.children)
    assert(e in d.children)
    assert(e not in e.children)

def testCoordinate():
    g = Coordinate(1, 0, 0)
    assert(g.cartesian(1) == (0, 0))
    g = Coordinate(0, 1, 0)
    assert(g.cartesian(1) == (0.5, - sqrt(0.75))
           ), "Wrong cartesian coordinates: {}".format(g.cartesian(1))
    g = Coordinate(0, 0, 1)
    assert(g.cartesian(1) == (-0.5, - sqrt(0.75))
           ), "Wrong cartesian coordinates: {}".format(g.cartesian(1))
    assert(g == Coordinate(0, 0, 1))
    assert(g != Coordinate(1, 0, 0))
    assert(g != Coordinate(0, 1, 0))
def triangleDrawing(scale):
    loc = Coordinate(1, 0, 0)
    tr = Triangle(None, loc, True)
    tr.draw(scale)
def testLineDir():
    a = Coordinate(1, 0, 0)
    b = a.sw(3)
    c = a.se(3)
    assert(a.lineDir(b) == 0)
    assert(a.lineDir(c) == 1)
    assert(b.lineDir(c) == 2)
    assert(b.lineDir(a) == 3)
    assert(c.lineDir(a) == 4)
    assert(c.lineDir(b) == 5)
    try:
        a.ne().nw().lineDir(a)
    except Exception as exp:
        y = str(exp)
    assert(y == "barys are on different lines")
