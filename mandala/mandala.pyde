from graph import Node
import test
import patternGen
import triangle
scale = 10
canvas = triangle.Canvas(scale)
def setup():
    size(600,600)
    #fullScreen()
    stroke(255)
    smooth()
    runTest()
def draw():
    translate(width / 2, height / 2)
    background(255)
    patternGen.demo(canvas)
    #filter(BLUR,5)
    canvas.draw()
def runTest():
    test.testNode()
    test.testNode2()
    test.testCoordinate()
    test.testLineDir()