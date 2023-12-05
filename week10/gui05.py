from tkinter import *
from tkinter import messagebox as msb

###### 1. Create window ######
window = Tk()   # Create a window
window.title("Ticket Booking")   # Set a title
window.geometry("350x350")   # Set a size

###### 2. Event handlers ######
def btn_ok_clicked():
    city_from = txt_from.get()
    city_to = txt_to.get()
    price = int(txt_price.get())

    info = lbl_ticket_info.cget("text") # get the current text of the label
    info += f' {city_from} to {city_to} (${price})'
    
    lbl_ticket_info.config(text=info)

    weight = int(txt_baggages.get())
    extra_weight = 0 if weight <= 7 else weight - 7
    extra_weight_price = extra_weight * 5

    overweight_info = lbl_overweight.cget("text")
    overweight_info += f' {extra_weight}kg (${extra_weight_price})'

    lbl_overweight.config(text=overweight_info)

    extra_service = 0
    if cbseat_selected.get():
        extra_service += 5
    if cbdinner_selected.get():
        extra_service += 10
    
    extra_info = lbl_extra_info.cget("text")
    extra_info += f' ${extra_service}'
    lbl_extra_info.config(text=extra_info)

    total = price + extra_weight_price + extra_service
    lbl_total.config(text=f'Total: ${total}')
    
###### 3. Create widgets ######
lbl_from = Label(window, text="From:")
lbl_from.grid(row=0, column=0, sticky=E)

txt_from = Entry(window)
txt_from.grid(row=0, column=1, sticky=W)

lbl_to = Label(window, text="To:")
lbl_to.grid(row=1, column=0, sticky=E)

txt_to = Entry(window)
txt_to.grid(row=1, column=1, sticky=W)

lbl_price = Label(window, text="Price:")
lbl_price.grid(row=2, column=0, sticky=E)

txt_price = Entry(window)
txt_price.grid(row=2, column=1, sticky=W)

lbl_baggages = Label(window, text="Baggages (max 7kg):")
lbl_baggages.grid(row=3, column=0, sticky=E)

txt_baggages = Entry(window)
txt_baggages.grid(row=3, column=1, sticky=W)

lbl_extra = Label(window, text="Extra:")
lbl_extra.grid(row=4, column=0, sticky=E)

cbseat_selected = BooleanVar()
cb_seat = Checkbutton(window, text="Seat ($5)", variable=cbseat_selected)
cb_seat.grid(row=4, column=1, sticky=W)

cbdinner_selected = BooleanVar()
cb_dinner = Checkbutton(window, text="Dinner ($10)", variable=cbdinner_selected)
cb_dinner.grid(row=5, column=1, sticky=W)

btn_ok = Button(window, text="OK", command=btn_ok_clicked)
btn_ok.grid(row=6, column=1, sticky=W)

lbl_ticket_info = Label(window, text="Ticket info:")
lbl_ticket_info.grid(row=7, column=0, sticky=W, columnspan=2)

lbl_overweight = Label(window, text="Overweight:")
lbl_overweight.grid(row=8, column=0, sticky=W, columnspan=2)

lbl_extra_info = Label(window, text="Extra info:")
lbl_extra_info.grid(row=9, column=0, sticky=W, columnspan=2)

lbl_total = Label(window, text="Total:")
lbl_total.grid(row=10, column=0, sticky=W, columnspan=2)
###### 4. Run the window ######
window.mainloop()   # Run the window in a main loop, waiting for events