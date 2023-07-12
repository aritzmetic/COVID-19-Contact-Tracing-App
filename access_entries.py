import tkinter as tkinter
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
        # create back button
        back_button = tk.Button(self.access_frame, text='Back', command=self.go_back, bg='white')
        back_button.pack()

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

