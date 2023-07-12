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
        age_label = tk.Label(self.add_frame, text='Age:', bg='light blue', font=('Georgia', 14))
        age_label.place(x=600, y=210)
        self.age_entry = tk.Entry(self.add_frame, font=('Times New Roman', 12))
        self.age_entry.place(x=700, y=210)

        # Create phone number label and blank field
        phone_label = tk.Label(self.add_frame, text='Phone Number:', bg='light blue', font=('Georgia', 14))
        phone_label.place(x=520, y=260)
        self.phone_entry = tk.Entry(self.add_frame, font=('Times New Roman', 12))
        self.phone_entry.place(x=700, y=260)

        # Create location label and blank field
        location_label = tk.Label(self.add_frame, text='Location:', bg='light blue', font=('Georgia', 14))
        location_label.place(x=570, y=310)
        self.location_entry = tk.Entry(self.add_frame, font=('Times New Roman', 12))
        self.location_entry.place(x=700, y=310)
        
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

