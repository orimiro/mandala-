from graph import Node
import test
import patternGen
count=0
def setup():
    size(400,400)
    stroke(255)
    runTest()

def draw():
    translate(width/2,height/2)
    background(0x232323)
    patternGen.demo()
    #filter(BLUR,2)
    #filter(INVERT)

def runTest():
    test.testNode()
    test.testNode2()
    test.testCoordinate()