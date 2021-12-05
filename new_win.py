from tkinter import Label, Toplevel


def new_wind():
    top = Toplevel()
    tell = Label(top, text="Make sure you read our help, about and contribute sections")
    thankyou = Label(top, text="Thankyou for using us , please do share and add suggetions to the link provided.")
    tell.pack()
    thankyou.pack()
