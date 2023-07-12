# import modules 
import tkinter as tk
from PIL import Image, ImageTk

# create a class
class CloseContactWindow:
    # use iniit method to call the part, image path, and self
    def __init__(self, parent, message, image_path):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("Close Contact Notification!")
        
# bg imaage
# show method
# close window by destroying it