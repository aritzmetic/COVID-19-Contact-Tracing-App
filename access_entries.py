import tkinter as tk
from PIL import Image, ImageTk

# create a class
class AccessEntries:
    # use init method to call the parent
    def __init__(self, parent):
        self.parent = parent
        self.access_frame = None
    # create search window method
    def create_access_window(self):
        self.access_frame = tk.Frame(self.parent, bg='white')
        self.access_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Set background image
        image = Image.open('C:\\Users\\acer\\Downloads\\access_entries.png')
        background_image = ImageTk.PhotoImage(image)
        background_label = tk.Label(self.access_frame, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_image 

        # create back button
        back_button = tk.Button(self.access_frame, text='Back', command=self.go_back, bg='white', font=('Arial', 12))
        back_button.place(x=20, y=20)

    # define show method
    def show(self):
        self.create_access_window()
        self.access_frame.lift()

    # define hide method
    def hide(self):
        self.access_frame.destroy()

    # define go back method
    def go_back(self):
        self.hide()
        self.parent.lift()

