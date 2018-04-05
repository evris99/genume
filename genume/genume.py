#!/usr/bin/env python3

import gi
import os
#Check for correct Gtk version
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from file import write_to_file

#A window object with an entry box to specify where
#the output should be saved and a button to start the process
class MainWindow(Gtk.Window):

    def __init__(self):

        #A simple window titled Genume
        Gtk.Window.__init__(self, title="Genume")
        self.set_border_width(15)

        #Set the widgets vertically
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        self.add(box)

        label = Gtk.Label("Enter path to save enumeration output")
        box.pack_start(label, True, True, 0)

        #An entry box with the currect directory as the default value
        self.entry = Gtk.Entry()
        self.entry.set_text(os.getcwd()+"/genume.txt")
        box.pack_start(self.entry, True, True, 0)

        self.button = Gtk.Button(label="START ENUMERATION")
        self.button.connect("clicked", self.button_clicked)
        box.pack_start(self.button, True, True, 0)

    def button_clicked(self, widget):
        write_to_file(self.entry.get_text())

if __name__ == '__main__':
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
