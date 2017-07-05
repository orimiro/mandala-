from graph import Node
import test
import patternGen

def setup():
    size(400,400)
    stroke(255)
    runTest()

def draw():
    translate(width/2,height/2)
    background(0x101010)
    patternGen.demo()

def runTest():
    test.testNode()
    test.testNode2()
    test.testCoordinate()