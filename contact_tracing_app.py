# Delera, Aritz B.

# Import tkinter
import tkinter as tk
from PIL import Image, ImageTk
from add_entry import AddEntry
from search_entry import SearchEntry
from access_entries import AccessEntries

# Create a Class
class MainWindow:
    # use init method
    def __init__(self):
        # create the main window
        self.window = tk.Tk()
        self.window.title('arix')
        # size and position
        self.window.geometry("800x600")
        self.window.configure(background='white')
        # create frame
        self.frame = tk.Frame(self.window, bg='white')
        self.frame.pack(fill='both', expand=True)
        self.background_photo = None

        self.create_main_window()

# create the main window
    def create_main_window(self):
        # background image
        background_image = Image.open(r"C:/Users/acer/Downloads/Aritzmetic's COVID-19 CONTACT TRACING APP.png")
        self.background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(self.frame, image=self.background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create buttons
        button_width = 30
        button_height = 3

        add_button = tk.Button(self.frame, text='Add Entry', command=self.open_add_entry, bg='white', width=button_width, height=button_height, highlightthickness=0)
        add_button.place(relx=0.134, rely=0.638, anchor=tk.CENTER)

        search_button = tk.Button(self.frame, text='Search Entry', command=self.open_search_entry, bg='white', width=button_width, height=button_height, highlightthickness=0)
        search_button.place(relx=0.394, rely=0.638, anchor=tk.CENTER)

        access_button = tk.Button(self.frame, text='Access Entries', command=self.open_access_entries, bg='white', width=button_width, height=button_height, highlightthickness=0)
        access_button.place(relx=0.644, rely=0.638, anchor=tk.CENTER)

    # create instance and widgets to the buttons
        self.add_entry_widget = AddEntry(self.frame)
        self.search_entry_widget = SearchEntry(self.frame)
        self.access_entries_widget = AccessEntries(self.frame)

    def open_add_entry(self):
        self.add_entry_widget.show()

    def open_search_entry(self):
        self.search_entry_widget.show()

    def open_access_entries(self):
        self.access_entries_widget.show()

    def run(self):
        self.window.mainloop()
