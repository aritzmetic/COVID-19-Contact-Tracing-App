# Delera, Aritz B.

# Import tkinter
import tkinter as tk

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
    # Run the GUI main loop

    window.mainloop()

    # Call the function to create the main window
main_window()


# create add entry
# create search entry
# create access entry

