from graph import Node
import test
import patternGen

def setup():
    size(400,400)
    stroke(255)
    runTest()

def draw():
    translate(width/2,height/2)
    patternGen.hexagonDrawing(100)
    background(0x101010)
    patternGen.triangleDrawSW(20, 0, int(mouseX / 50), True)
    patternGen.triangleDrawSE(20, 0, int(mouseX / 50), True)

def runTest():
    test.testNode()
    test.testNode2()
    test.testCoordinate()
