import tkinter as tk
from PIL import Image, ImageTk
import csv
from tkinter import ttk

# create a class
class AccessEntries:
    # use init method to call the parent
    def __init__(self, parent):
        # initialize the other objects
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

        # Create password label and blank field
        password_label = tk.Label(self.access_frame, text='Enter password:', bg='light blue', font=('Georgia', 14))
        password_label.place(x=550, y=200)
        password_entry = tk.Entry(self.access_frame, show='*', font=('Arial', 12))
        password_entry.place(x=800, y=200)

        # Create access button
        access_button = tk.Button(self.access_frame, text='Access Entries', command=lambda: self.check_password(password_entry.get()), bg='magenta', font=('new times roman', 12))
        access_button.place(x=700, y=250)

        # create back button
        back_button = tk.Button(self.access_frame, text='Back', command=self.go_back, bg='white', font=('Arial', 12))
        back_button.place(x=20, y=20)
    
    # define check password
    def check_password(self, entered_password):
        # if the password is correct, show entries
        if entered_password == self.password:
            self.show_entries()
        # if not, incorrect password
        else:
            error_label = tk.Label(self.access_frame, text='Incorrect password', bg='light blue', font=('Arial', 12), fg='red')
            error_label.place(x=690, y=300)
    
    # create new window for showing the entries
    def show_entries(self):
        entries_window = tk.Toplevel(self.parent)
        entries_window.title("All Entries")

        # Create canvas
        canvas = tk.Canvas(entries_window)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create scrollbar forr canvas
        scrollbar = tk.Scrollbar(entries_window, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas to work with the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create a frame inside the canvas to hold the entries
        entries_frame = tk.Frame(canvas, bg='white')
        canvas.create_window((0, 0), window=entries_frame, anchor='nw')

        # Read the entries from the CSV file
        # Display the entries

        # Configure the canvas scrolling region

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

root = tk.Tk()
app = AccessEntries(root)
app.show()
root.mainloop()