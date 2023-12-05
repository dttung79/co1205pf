from tkinter import *
from tkinter import messagebox as msb

###### 1. Create window ######
window = Tk()   # Create a window
window.title("Register Retake Classes")   # Set a title
window.geometry("300x200")   # Set a size

###### 2. Event handlers ######
def btn_ok_clicked():
    total = 0
    if cb1752_checked.get() == True: # if check box is checked
        total += 300
    if cb1821_checked.get() == True:
        total += 300
    if cb1863_checked.get() == True:
        total += 300
    
    lbl_total.config(text=f'{total}$')

###### 3. Create widgets ######
lbl_select = Label(window, text="Select courses:")
lbl_select.grid(row=0, column=0)

cb1752_checked = BooleanVar() # create a boolean variable to bind with the check box
cb_1752 = Checkbutton(window, text="1752", variable=cb1752_checked)
cb_1752.grid(row=0, column=1)

cb1821_checked = BooleanVar()
cb_1821 = Checkbutton(window, text="1821", variable=cb1821_checked)
cb_1821.grid(row=1, column=1)

cb1863_checked = BooleanVar()
cb_1863 = Checkbutton(window, text="1863", variable=cb1863_checked)
cb_1863.grid(row=2, column=1)

btn_ok = Button(window, text="OK", command=btn_ok_clicked)
btn_ok.grid(row=3, column=1, sticky=W)

lbl_payment = Label(window, text="Payment:")
lbl_payment.grid(row=4, column=0)

lbl_total = Label(window, text="0$")
lbl_total.grid(row=4, column=1, sticky=W)

###### 4. Run the window ######
window.mainloop()   # Run the window in a main loop, waiting for events