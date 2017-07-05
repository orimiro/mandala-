from graph import Node
import test, patternGen

def setup():
    size(400,400)
    stroke(255)
    runTest()

def draw():
    translate(width/2,height/2)
    patternGen.hexagonDrawing(100)
    pass
    
    
def runTest():
    test.testNode()
    test.testNode2()
    test.testCoordinate()