from tkinter import *
from tkinter import messagebox as msb

###### 1. Create window ######
window = Tk()   # Create a window
window.title("First GUI application")   # Set a title
window.geometry("400x200")   # Set a size

###### 2. Event handlers ######
def btn_hello_clicked():
    # get the first name from the text box
    first_name = txt_firstname.get()
    # get the last name from the text box
    last_name = txt_lastname.get()
    # show a message box with the full name
    full_name = first_name + " " + last_name
    msb.showinfo("Full name", full_name)

###### 3. Create widgets ######
# create a label on the window with text "First name:"
lbl_firstname = Label(window, text="First name:")
# place the label on the window at (0, 0) position
lbl_firstname.grid(row=0, column=0)

# create a text box on the window
txt_firstname = Entry(window)
# place the text box on the window at (0, 1) position
txt_firstname.grid(row=0, column=1)

lbl_lastname = Label(window, text="Last name:")
lbl_lastname.grid(row=1, column=0)

txt_lastname = Entry(window)
txt_lastname.grid(row=1, column=1)

btn_hello = Button(window, text="Hello", command=btn_hello_clicked)
btn_hello.grid(row=2, column=1, sticky=W)

###### 4. Run the window ######
window.mainloop()   # Run the window in a main loop, waiting for events