import tkinter as tk
from PIL import Image, ImageTk

# create a class
class AddEntry:
    # use init method to call the parent
    def __init__(self, parent):
        # initialize the other objects
        self.parent = parent
        self.add_frame = None

# create add window method
    def create_add_window(self):
        self.add_frame = tk.Frame(self.parent, bg='white')
        self.add_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

         # Set background image
        image = Image.open('C:\\Users\\acer\\Downloads\\add_entry (1).png')
        background_image = ImageTk.PhotoImage(image)
        background_label = tk.Label(self.add_frame, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_image 

        # Create name label and blank field
        name_label = tk.Label(self.add_frame, text='Name:', bg='light blue', font=('Georgia', 14))
        name_label.place(x=600, y=160)
        self.name_entry = tk.Entry(self.add_frame, font=('Times New Roman', 12))
        self.name_entry.place(x=700, y=160)
        
        # Create age label and blank field
        # Create phone number label and blank field
        # Create location label and blank field
        # Create questions 
        # Create submit button
        # create back button
        back_button = tk.Button(self.add_frame, text='Back', command=self.go_back, bg='white', font=('Arial', 12))
        back_button.place(x=20, y=20)
        # Create label for the notification

    # define show method
    def show(self):
        self.create_add_window()
        self.add_frame.lift()

    # define hide method
    def hide(self):
        self.add_frame.destroy()

    # define go back method
    def go_back(self):
        self.hide()
        self.parent.lift()

