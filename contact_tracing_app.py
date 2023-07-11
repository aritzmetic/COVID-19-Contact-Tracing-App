# Delera, Aritz B.

# Import tkinter
import tkinter as tk

# create add entry
def add_entry():
    pass
# create search entry
def search_entry():
    pass
# create access entry
def access_entries():
    pass

# create the main window
def main_window():
    # import global wildow
    global window
    # create the main window
    window = tk.Tk()
    window.title('arix')
    # size and position
    window.geometry("800x600")
    window.configure(background='white')
    # background image
    background_image = tk.PhotoImage(file=r"C:\Users\acer\Downloads\Aritzmetic's COVID-19 CONTACT TRACING APP.png")
    background_label = tk.Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    # Create buttons
    button_width = 30
    button_height = 3

    add_button = tk.Button(window, text='Add Entry', command=add_entry, bg='white', width=button_width, height=button_height, highlightthickness=0)
    add_button.place(relx=0.134, rely=0.638, anchor=tk.CENTER)

    search_button = tk.Button(window, text='Search Entry', command=search_entry, bg='white', width=button_width, height=button_height, highlightthickness=0)
    search_button.place(relx=0.394, rely=0.638, anchor=tk.CENTER)

    access_button = tk.Button(window, text='Access Entries', command=access_entries, bg='white', width=button_width, height=button_height, highlightthickness=0)
    access_button.place(relx=0.644, rely=0.638, anchor=tk.CENTER)
    # Run the GUI main loop

    window.mainloop()

    # Call the function to create the main window
main_window()



