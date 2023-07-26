"""
Description:
  Graphical user interface that displays the official artwork for a
  user-specified Pokemon, which can be set as the desktop background image.

Usage:
  python poke_image_viewer.py
"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import ctypes
import os
import poke_api
import image_lib
import inspect

# Get the script and images directory
script_name = inspect.getframeinfo(inspect.currentframe()).filename
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, 'images')

# TODO: Create the images directory if it does not exist
if not os.path.isdir(images_dir)
    os.makedirs(images_dir)

# Create the main window
root = Tk()
root.title("Awesome App")
root.geometry('600x600')

# TODO: Set the icon

# TODO: Create frames

# TODO: Populate frames with widgets and define event handler functions

root.mainloop()