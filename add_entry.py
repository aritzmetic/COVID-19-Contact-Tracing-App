import tkinter as tk
from PIL import Image, ImageTk
import csv
from closecontactwindow import CloseContactWindow

# create a class
class AddEntry:
    # use init method to call the parent
    def __init__(self, parent):
        # initialize the other objects
        self.parent = parent
        self.add_frame = None
        self.name_entry = None
        self.age_entry = None
        self.phone_entry = None
        self.location_entry = None
        self.question1_choice = tk.StringVar()
        self.question2_choice = tk.StringVar()
        self.question3_choice = tk.StringVar()
        self.notification_label = None

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
        question_label = tk.Label(self.add_frame, text='Questions:', bg='light green', font=('Times New Roman', 14))
        question_label.place(x=700, y=370)

        question1 = tk.Label(self.add_frame, text='1. Are you experiencing any symptoms in the past 7 days', bg='light blue', font=('Times New Roman', 10))
        question1.place(x=400, y=410)
        question1_radio_yes = tk.Radiobutton(self.add_frame, text='Yes', variable=self.question1_choice, value='Yes', bg='cyan', font=('Arial', 8))
        question1_radio_yes.place(x=900, y=410)
        question1_radio_no = tk.Radiobutton(self.add_frame, text='No', variable=self.question1_choice, value='No', bg='cyan', font=('Arial', 8))
        question1_radio_no.place(x=950, y=410)

        question2 = tk.Label(self.add_frame, text='2. Have you been in contact with a COVID-19 positive person?', bg='light blue', font=('Times New Roman', 10))
        question2.place(x=400, y=440)
        question2_radio_yes = tk.Radiobutton(self.add_frame, text='Yes', variable=self.question2_choice, value='Yes', bg='cyan', font=('Arial', 8))
        question2_radio_yes.place(x=900, y=440)
        question2_radio_no = tk.Radiobutton(self.add_frame, text='No', variable=self.question2_choice, value='No', bg='cyan', font=('Arial', 8))
        question2_radio_no.place(x=950, y=440)

        question3 = tk.Label(self.add_frame, text='3. Have you been tested for Covid-19 in the last 14 days?', bg='light blue', font=('Times New Roman', 10))
        question3.place(x=400, y=470)
        question3_radio_yes = tk.Radiobutton(self.add_frame, text='Yes', variable=self.question3_choice, value='Yes', bg='cyan', font=('Arial', 8))
        question3_radio_yes.place(x=900, y=470)
        question3_radio_no = tk.Radiobutton(self.add_frame, text='No', variable=self.question3_choice, value='No', bg='cyan', font=('Arial', 8))
        question3_radio_no.place(x=950, y=470)

        # Create submit button
        submit_button = tk.Button(self.add_frame, text='Submit', command=self.submit_data, bg='yellow', font=('pridi', 12))
        submit_button.place(x=700, y=540)

        # create back button
        back_button = tk.Button(self.add_frame, text='Back', command=self.go_back, bg='yellow', font=('new times roman', 12))
        back_button.place(x=20, y=20)

        # Create label for the notification
        self.notification_label = tk.Label(self.add_frame, text='', bg='white', font=('Arial', 14))
        self.notification_label.place(x=20, y=440)

        # define submit data
    def submit_data(self):
        # retrieve the entered data
        name = self.name_entry.get()
        age = self.age_entry.get()
        phone = self.phone_entry.get()
        location = self.location_entry.get()
        question1_answer = self.question1_choice.get()
        question2_answer = self.question2_choice.get()
        question3_answer = self.question3_choice.get()
            
        # save using CVS
        with open('entries.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, age, phone, location, question1_answer, question2_answer, question3_answer])
        # contact tracing notification and condition
        if question1_answer == 'No' and question2_answer == 'No' and question3_answer == 'No':
            # Display window 1 if not a close contact
            window1 = CloseContactWindow(self.parent, "You are not a close contact person.", "C:\\Users\\acer\\Downloads\\nof01.png")
            window1.show()
        else:
            # Display window 2 if a close contact
            window2 = CloseContactWindow(self.parent, "You are a close contact person.", "C:\\Users\\acer\\Downloads\\nof2.png")
            window2.show()


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
