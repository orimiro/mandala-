#!/usr/bin/env python3
"""
a simple program to draw triangles in gtk+ (PyGObject)
using pycairo and some selfwriten stuff (triangles)

documentation:
https://pycairo.readthedocs.io/en/latest/index.html

"""
################################################################################
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib

from animator import mandalaAnimation

################################################################################
class mainwindow(Gtk.Window):
    """
    The left side of the Window is a Cairo Screen,
    the right side of the Window
    """
    def __init__(self):
        Gtk.Window.__init__(self, title= "Triangle Project")
        self.set_default_size(1000,600)
        
        self.grid = Gtk.Grid()
        self.add(self.grid)
        
        self.animator = mandalaAnimation(self)
        self.animator.set_size_request(600,600)
        self.grid.attach_next_to(self.animator, None,
                                 Gtk.PositionType.RIGHT,1,4)
        
        self.setup_box = self.lable_with_button_box("setup", "update")
        self.grid.attach_next_to(self.setup_box, self.animator,
                                 Gtk.PositionType.RIGHT,1,1)
        
        self.setup_text_and_window = self.make_TextBox()
        self.grid.attach_next_to(self.setup_text_and_window[1], self.setup_box,
                                 Gtk.PositionType.BOTTOM,1,1)
    
        self.draw_box = self.lable_with_button_box("draw", "update")
        self.grid.attach_next_to(self.draw_box, self.setup_text_and_window[1],
                                 Gtk.PositionType.BOTTOM,1,1)
        
        self.draw_text_and_window = self.make_TextBox()
        self.grid.attach_next_to(self.draw_text_and_window[1], self.draw_box,
                                 Gtk.PositionType.BOTTOM,1,1)
        
        self.setup_text_and_window[0].get_buffer().set_text(
"""
self.can = Canvas(15,self.width,self.height)
can = self.can

self.x=0

"""
        )
        
        self.draw_text_and_window[0].get_buffer().set_text(
"""# ctx is cairo context

self.x+=0.1
self.x%=10
pattern_1(self.can, Coordinate(0,0), 3, int(self.x),(1,0,0),(0,1,0),(0,0,1))

self.can.draw(ctx)

self.can.hideAll()

ctx.set_source_rgb(0.5,0.5,1)
"""
        )

    def lable_with_button_box(self, labeltext, buttontext):
        label = Gtk.Label(labeltext)
        button = Gtk.Button(label="update")
        box = Gtk.Box()
        if(labeltext == "setup"):
            button.connect("clicked", self.setup_clicked)
        if(labeltext == "draw"):
            button.connect("clicked", self.draw_clicked)
        box.pack_start(label, True, True, 0)
        box.pack_start(button, True, True, 0)
        return box

    def make_TextBox(self):
        text = Gtk.TextView()
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        scrolledwindow.add(text)
        scrolledwindow.set_size_request(400,300)
        return (text,scrolledwindow)

    def setup_clicked(self,widget):
        self.animator.set_setup(self
                                .setup_text_and_window[0]
                                .get_buffer().props.text)

    def draw_clicked(self,widget):
        self.animator.set_draw(self
                               .draw_text_and_window[0]
                               .get_buffer().props.text)
        
################################################################################

if __name__ == '__main__':
    win = mainwindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    win.setup_clicked(None)
    win.draw_clicked(None)
    win.move(0,0)
    Gtk.main()
