import tkinter as tk
from PIL import Image, ImageTk
import csv

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
        back_button = tk.Button(self.search_frame, text='Back', command=self.go_back, bg='yellow', font=('new times roman', 12))
        back_button.place(x=20, y=20)

        # Create search entry label and blank field
        search_label = tk.Label(self.search_frame, text='Enter your Registered Name:', bg='light blue', font=('Georgia', 14))
        search_label.place(x=500, y=160)
        search_entry = tk.Entry(self.search_frame, font=('Times New Roman', 12))
        search_entry.place(x=800, y=160)

        # Create search button
        search_button = tk.Button(self.search_frame, text='Search', command=lambda: self.search_data(search_entry.get()), bg='yellow', font=('Arial Narrow', 12))
        search_button.place(x=700, y=210)

    # define search data
    def search_data(self, entry_id):
        # let entry found be false by searching
        entry_found = False
        # Read the CSV file and search for the entry
        with open('entries.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) > 0 and row[0] == entry_id:
                # set entry found to true and row 0-6 asccordingly
                    entry_found = True
                    name = row[0]
                    age = row[1]
                    phone = row[2]
                    location = row[3]
                    question1_answer = row[4]
                    question2_answer = row[5]
                    question3_answer = row[6]
                    # if no, not a close contact
                    if question1_answer == 'No' and question2_answer == 'No' and question3_answer == 'No':
                        result = f"Name: {name}\nAge: {age}\nPhone Number: {phone}\nLocation: {location}\nThis person is not a close contact."
                    # else, close contact
                    else:
                        result = f"Name: {name}\nAge: {age}\nPhone Number: {phone}\nLocation: {location}\nThis person is a close contact."

        # if not, print entry not found
        if not entry_found:
            result = "Entry not found."

        self.display_result(result)

    # define result display
    def display_result(self, result):
        # new window for result
        result_window = tk.Toplevel(self.parent)
        result_window.attributes("-fullscreen", True)
        result_window.title("Search Result")

        # Set background for the new window
        image = Image.open('C:\\Users\\acer\\Downloads\\nof03.png')
        background_image = ImageTk.PhotoImage(image)
        background_label = tk.Label(result_window, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_image

        # Result Label
        result_label = tk.Label(result_window, text=result, font=('Arial', 35))
        result_label.place(x=400, y=350)

        # create OK button
        ok_button = tk.Button(result_window, text='OK', command=result_window.destroy, bg='yellow', font=('new times roman', 16))
        ok_button.place(x=750, y=700)


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

root = tk.Tk()
app = SearchEntry(root)
app.show()
root.mainloop()
