import cairo
import gi
import math
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib
"""
a little bit copied from:
https://github.com/fossasia/susi_linux/blob/master/main/ui/animators.py
but licenses are compatible (apache v2 and gnu v3)
"""

################################################################################
class Animator(Gtk.DrawingArea):
    def __init__(self, **properties):
        super().__init__(**properties)
        self.connect("draw", self.do_drawing)
        GLib.timeout_add(50, self.tick)

    def tick(self):
        self.queue_draw()
        return True

    def do_drawing(self, widget, ctx):
        self.draw(ctx,
                  widget.get_allocated_width(),
                  widget.get_allocated_height())

    def draw(self, ctx, width, heigth):
        pass

################################################################################

from triangle import *
from patternGen import *

class mandalaAnimation(Animator):
    def __init__(self, window, **properties):
        super().__init__(**properties)
        self.window = window
        self.setup = ""
        self.draw_ = ""
        self.width = 0
        self.height = 0
        
    def draw(self, ctx, width, height):
        self.width = width
        self.height = height
        #draw:
        ctx.translate(width/2, height/2)
        ctx.rotate(math.pi/3*2)
        exec(self.draw_)

    def triangle(self, up,x,y):
        self.can.makeTriangle(up,x,y)

    def set_setup(self,text):
        try:
            self.setup = text
            exec(self.setup)
        except Exception as error:
            print(error)

    def set_draw(self,text):
        try:
            self.draw_ = text
        except Exception as error:
            print(error)
            
################################################################################
