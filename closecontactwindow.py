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
        image = Image.open(image_path)
        background_image = ImageTk.PhotoImage(image)
        background_label = tk.Label(self.window, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_image
        
        ok_button = tk.Button(self.window, text="OK", command=self.close_window, bg='yellow', font=('new times roman', 16))
        ok_button.place(x=750, y=700)

# show method
def show(self):
    self.window.transient(self.parent)
    self.parent.wait_window(self.window)

# close window by destroying it
def close_window(self):
    self.window.destroy()