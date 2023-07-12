import tkinter as tk
from PIL import Image, ImageTk

# create a class
class SearchEntry:
    # use init method to call the parent
    def __init__(self, parent):
        self.parent = parent
        self.search_frame = None
    # create search window method
    def create_search_window(self):
        self.search_frame = tk.Frame(self.parent, bg='white')
        self.search_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Set background image
        image = Image.open('C:\\Users\\acer\\Downloads\\search_entry.png')
        background_image = ImageTk.PhotoImage(image)
        background_label = tk.Label(self.search_frame, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_image 
        
        # create back button
        back_button = tk.Button(self.search_frame, text='Back', command=self.go_back, bg='white', font=('Arial', 12))
        back_button.place(x=20, y=20)

        # Create search entry label and blank field
        # Create search button

    # define search data
        # let entry found be false by searching
        # Read the CSV file and search for the entry
            # set entry found to true and row 0-6 asccordingly
                # if no, not a close contact
                # else, close contact
        # if not, print entry not found

    # define result display
    # create OK button


    # define show method
    def show(self):
        self.create_search_window()
        self.search_frame.lift()

    # define hide method
    def hide(self):
        self.search_frame.destroy()

    # define go back method
    def go_back(self):
        self.hide()
        self.parent.lift()
