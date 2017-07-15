from graph import Node
import test
import patternGen
count = 0
k = 0
def setup():
    size(600,600)
    #fullScreen()
    stroke(255)
    runTest()
m = False
def draw():
    global k
    translate(width / 2, height / 2)
    background(255,255,255)
    patternGen.demo(k)
    #filter(BLUR,5)
    global m
    if(mousePressed and m is False):
        m = True
    if(m and mousePressed is False):
        k += 1
        m = False
def runTest():
    test.testNode()
    test.testNode2()
    test.testCoordinate()
    test.testLineDir()
