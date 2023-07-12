import tkinter as tkinter
# create a class
class AddEntry:
    # use init method to call the parent
    def __init__(self, parent):
        self.parent = parent
        self.add_frame = None

# create add window method
    def create_add_window(self):
        self.add_frame = tk.Frame(self.parent, bg='white')
        self.add_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        # create back button
        back_button = tk.Button(self.add_frame, text='Back', command=self.go_back, bg='white')
        back_button.pack()

# define show method
# define hide method
# defien go back method

