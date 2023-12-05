from tkinter import *
from tkinter import messagebox as msb

###### 1. Create window ######
window = Tk()   # Create a window
window.title("Payment")   # Set a title
window.geometry("400x250")   # Set a size

###### 2. Event handlers ######
def btn_ok_clicked():
    try:
        price = int(txt_price.get())            # get the price from the text box
        quantity = int(txt_quantity.get())      # get the quantity from the text box
        total_payment = f'{price * quantity}$'  # calculate the total payment

        lbl_total.config(text=total_payment)    # set the total payment to the label
    except ValueError:
        msb.showerror("Error", "Please enter numbers for price & quantity!")

###### 3. Create widgets ######
lbl_product = Label(window, text="Product:")
lbl_product.grid(row=0, column=0)

txt_product = Entry(window)
txt_product.grid(row=0, column=1)

lbl_price = Label(window, text="Price:")
lbl_price.grid(row=1, column=0)

txt_price = Entry(window)
txt_price.grid(row=1, column=1)

lbl_quantity = Label(window, text="Quantity:")
lbl_quantity.grid(row=2, column=0)

txt_quantity = Entry(window)
txt_quantity.grid(row=2, column=1)

btn_ok = Button(window, text="OK", command=btn_ok_clicked)
btn_ok.grid(row=3, column=1, sticky=W)

lbl_payment = Label(window, text="Payment:")
lbl_payment.grid(row=4, column=0)

lbl_total = Label(window, text="0$")
lbl_total.grid(row=4, column=1, sticky=W)

###### 4. Run the window ######
window.mainloop()   