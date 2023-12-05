from tkinter import *
from tkinter.ttk import *

#### 1. CREATE THE WINDOW ####
window = Tk()
window.title("Movie Ticket Info")
window.geometry('300x200')

#### 2. EVENT HANDLERS ####


#### 3. WIDGETS ####
lbl_movie = Label(window, text="Choose a movie:")
lbl_movie.grid(row=0, column=0, sticky=E)

cbb_movie = Combobox(window, width=15, state='readonly')
cbb_movie.grid(row=0, column=1, sticky=W)

lbl_name = Label(window, text="Name:")
lbl_name.grid(row=1, column=0, sticky=E)

txt_name = Entry(window, width=15, state='readonly')
txt_name.grid(row=1, column=1, sticky=W)

lbl_director = Label(window, text="Director:")
lbl_director.grid(row=2, column=0, sticky=E)

txt_director = Entry(window, width=15, state='readonly')
txt_director.grid(row=2, column=1, sticky=W)

lbl_time = Label(window, text="Time:")
lbl_time.grid(row=3, column=0, sticky=E)

txt_time = Entry(window, width=15, state='readonly')
txt_time.grid(row=3, column=1, sticky=W)

lbl_price = Label(window, text="Price:")
lbl_price.grid(row=4, column=0, sticky=E)

txt_price = Entry(window, width=15, state='readonly')
txt_price.grid(row=4, column=1, sticky=W)

#### 4. RUN THE MAIN LOOP ####
window.mainloop()