from tkinter import *
from tkinter import messagebox as msb

###### 1. Create window ######
window = Tk()   # Create a window
window.title("Pizza Order")   # Set a title
window.geometry("200x300")   # Set a size

###### 2. Event handlers ######
def calculate_payment():
    total = 0
    # check which pizza is selected
    if pizza_var.get() == 1: # Seoul is selected
        total += 10
    elif pizza_var.get() == 2: # New York is selected
        total += 12
    elif pizza_var.get() == 3: # Paris is selected
        total += 15

    if cbseefood_checked.get():
        total += 3
    if cbjambon_checked.get():
        total += 2
    if cbcheese_checked.get():
        total += 1
    
    lbl_payment.config(text=f'Payment: ${total}')
    
###### 3. Create widgets ######
lbl_select = Label(window, text="Select pizza:")
lbl_select.grid(row=0, column=0, sticky=W)

pizza_var = IntVar() # create a variable to bind with the radio buttons
rb_seoul = Radiobutton(window, text="Seoul ($10)", value=1, variable=pizza_var, command=calculate_payment)
rb_seoul.grid(row=1, column=0, sticky=W)

rb_newyork = Radiobutton(window, text="New York ($12)", value=2, variable=pizza_var, command=calculate_payment)
rb_newyork.grid(row=2, column=0, sticky=W)

rb_paris = Radiobutton(window, text="Paris ($15)", value=3, variable=pizza_var, command=calculate_payment)
rb_paris.grid(row=3, column=0, sticky=W)

lbl_topping = Label(window, text="Select topping:")
lbl_topping.grid(row=4, column=0, sticky=W)

cbseefood_checked = BooleanVar() # create a boolean variable to bind with the check box
cb_seefood = Checkbutton(window, text="Seafood ($3)", variable=cbseefood_checked, command=calculate_payment)
cb_seefood.grid(row=5, column=0, sticky=W)

cbjambon_checked = BooleanVar()
cb_jambon = Checkbutton(window, text="Jambon ($2)", variable=cbjambon_checked, command=calculate_payment)
cb_jambon.grid(row=6, column=0, sticky=W)

cbcheese_checked = BooleanVar()
cb_cheese = Checkbutton(window, text="Tomato/Cheese ($1)", variable=cbcheese_checked, command=calculate_payment)
cb_cheese.grid(row=7, column=0, sticky=W)

lbl_payment = Label(window, text="Payment: $0")
lbl_payment.grid(row=8, column=0, sticky=W)

###### 4. Run the window ######
window.mainloop()   # Run the window in a main loop, waiting for events