""" Scientific Calculator made using tkinter module
Free to copy and open-source """

from tkinter import *
from tkinter import messagebox
import math

root = Tk()
root.title("Sceintific Calculator")
root.geometry("410x450+0+0")
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')
orig_color = root.cget("background")
root.configure(bg=orig_color)

def new_win():
    top = Toplevel()
    tell = Label(top, text="Make sure you read our help, about and contribute sections")
    thankyou = Label(top, text="Thankyou for using us , please do share and add suggetions to the link provided.")
    tell.pack()
    thankyou.pack()

open_button = Button(root, text="Click Me!", command=new_win, padx=5, pady=5)
open_button.grid(row=0, column=3)

e = Entry(root, width=35, borderwidth=5)
e.grid(row=1, column=0, columnspan=3, padx=10, pady=10)


def dark_mode():
    root.configure(bg='black')
    Button_0.configure(bg="black", fg='white')  
    Button_1.configure(bg="black", fg='white')
    Button_2.configure(bg="black", fg='white')
    Button_3.configure(bg="black", fg='white')
    Button_4.configure(bg="black", fg='white')
    Button_5.configure(bg="black", fg='white')
    Button_6.configure(bg="black", fg='white')
    Button_7.configure(bg="black", fg='white')
    Button_8.configure(bg="black", fg='white')
    Button_9.configure(bg="black", fg='white')
    Button_add.configure(bg="black", fg='white')
    Button_subtract.configure(bg="black", fg='white')
    Button_divide.configure(bg="black", fg='white')
    Button_multiply.configure(bg="black", fg='white')
    Button_open_paranthesis.configure(bg="black", fg='white')
    Button_close_paranthesis.configure(bg="black", fg='white')
    Button_equal.configure(bg="black", fg='white')
    Button_exit.configure(bg="black", fg='white')
    Button_pi.configure(bg="black", fg='white')
    Button_sqr.configure(bg="black", fg='white')
    Button_sqrt.configure(bg="black", fg='white')
    Button_remainder.configure(bg="black", fg='white')
    Button_power.configure(bg="black", fg='white')
    Button_point.configure(bg="black", fg='white')
    Button_clear.configure(bg="black", fg='white')
    Button_fact.configure(bg="black", fg='white')
    aboutmenu.configure(bg="black", fg="white")
    filemenu.configure(bg="black", fg="white")
    settingsmenu.configure(bg="black", fg="white")
    editmenu.configure(bg="black", fg="white")
    # darkmode.configure(bg="black", fg='white')
    # lightmode.configure(bg="black", fg='white')
    e.configure(bg="black", fg='white')
    menubar.configure(bg="black", fg='white')
      
def light_mode():
    root.configure(bg=orig_color)
    Button_0.configure(bg=orig_color, fg="black")  
    Button_1.configure(bg=orig_color, fg="black")
    Button_2.configure(bg=orig_color, fg="black")
    Button_3.configure(bg=orig_color, fg="black")
    Button_4.configure(bg=orig_color, fg="black")
    Button_5.configure(bg=orig_color, fg="black")
    Button_6.configure(bg=orig_color, fg="black")
    Button_7.configure(bg=orig_color, fg="black")
    Button_8.configure(bg=orig_color, fg="black")
    Button_9.configure(bg=orig_color, fg="black")
    Button_add.configure(bg=orig_color, fg="black")
    Button_subtract.configure(bg=orig_color, fg="black")
    Button_divide.configure(bg=orig_color, fg="black")
    Button_multiply.configure(bg=orig_color, fg="black")
    Button_open_paranthesis.configure(bg=orig_color, fg="black")
    Button_close_paranthesis.configure(bg=orig_color, fg="black")
    Button_equal.configure(bg=orig_color, fg="black")
    Button_exit.configure(bg=orig_color, fg="black")
    Button_pi.configure(bg=orig_color, fg="black")
    Button_sqr.configure(bg=orig_color, fg="black")
    Button_sqrt.configure(bg=orig_color, fg="black")
    Button_remainder.configure(bg=orig_color, fg="black")
    Button_power.configure(bg=orig_color, fg="black")
    Button_point.configure(bg=orig_color, fg="black")
    Button_clear.configure(bg=orig_color, fg="black")
    Button_fact.configure(bg=orig_color, fg="black")
    settingsmenu.configure(bg=orig_color, fg="black")
    aboutmenu.configure(bg=orig_color, fg="black")
    editmenu.configure(bg=orig_color, fg="black")
    filemenu.configure(bg=orig_color, fg="black")
    # darkmode.configure(bg=orig_color, fg="black")
    # lightmode.configure(bg=orig_color, fg="black")
    e.configure(bg=orig_color, fg="black")
    menubar.configure(bg=orig_color, fg="black")


# darkmode = Button(root, text="dark mode", command=dark_mode)
# darkmode.grid(row=0, column=3)
# lightmode = Button(root, text="light mode", command=light_mode)
# lightmode.grid(row=0, column=2)


  ### Define our buttons
  
def button_exit():
    root.quit()
    
def about_menu():
    about = Toplevel()
    about.geometry("320x280+0+0")
    label1 = Label(about, text="Developed By Srikara under open source licence").grid(row=0, column=1)
    label2 = Label(about, text="Date:- 19.11.2021").grid(row=1, column=1)
    label3 = Label(about, text="Made in Python using tkinter module").grid(row=2, column=1)  
    
def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("600x450+0+0")
    root.eval('tk::PlaceWindow . center')


def Standard():
    root.resizable(width=False, height=False)
    root.geometry("410x450+0+0")
    root.eval('tk::PlaceWindow . center')

menubar = Menu(root)

# ManuBar 1 :
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Mode', menu = filemenu)
filemenu.add_command(label = "Standard", command = Standard)
filemenu.add_command(label = "Scientific", command = Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = button_exit)
    

editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Edit', menu = editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_separator()
editmenu.add_command(label = "Paste")

aboutmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'About', menu = aboutmenu)
aboutmenu.add_command(label = "About", command = about_menu)
aboutmenu.add_command(label = "Contribute")
aboutmenu.add_command(label = "Help")

aboutmenu.add_separator()

settingsmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Settings', menu = settingsmenu)
settingsmenu.add_command(label = "Light Theme", command = light_mode)
settingsmenu.add_command(label = "Dark Theme", command = dark_mode)

root.config(menu=menubar)

def button_click(number):
   current = e.get()
   e.delete(0, END)
   e.insert(0, str(current) + str(number))


   check_error = "myerrorlabel" in globals()
   check_add = "mylabel_add" in globals()
   check_pi = "mylabel_pi" in globals()
   check_sub = "mylabel_sub" in globals()
   check_mult = "mylabel_mult" in globals()
   check_div = "mylabel_div" in globals()
   check_rem = "mylabel_rem" in globals()
   check_pow = "mylabel_pow" in globals()
   check_sqr = "mylabel_sqr" in globals()
   check_sqrt = "mylabel_sqrt" in globals()
   check_fact = "mylabel_fact" in globals()

   if check_add == True:
        mylabel_add.destroy()

   if check_sub == True:
        mylabel_sub.destroy()

   if check_mult == True:
        mylabel_mult.destroy()

   if check_div== True:
        mylabel_div.destroy()

   if check_rem== True:
        mylabel_rem.destroy()

   if check_pow== True:
        mylabel_pow.destroy()

   if check_sqr== True:
        mylabel_sqr.destroy()

   
   if check_error == True:
        myerrorlabel.destroy()

   if check_pi == True:
        mylabel_pi.destroy()

   if check_sqrt == True:
        mylabel_sqrt.destroy()
        
   if check_fact == True:
        mylabel_fact.destroy()
    

def button_clear():
    e.delete(0, END) 

def button_add():
    first_number = e.get()
    global f_num
    global op
    op = "+"
    f_num = float(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global op
    op = "-"
    f_num = float(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global op
    op = "*"
    f_num = float(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global op
    op = "/"
    f_num = float(first_number)
    e.delete(0, END)

def button_rem():
    first_number = e.get()
    global f_num
    global op
    op = "%"
    f_num = float(first_number)
    e.delete(0, END)


def button_sqr():
    first_number = e.get()
    global f_num
    global op
    op = "sqr"
    f_num = float(first_number)

def button_pi():
    first_number = e.get()
    global f_num
    global op
    op = "pi"
    f_num = float(first_number)
    e.delete(0, END)
    
def button_sqrt():
    first_number = e.get()
    global f_num
    global op
    global a 
    op = "sqrt"
    f_num = float(first_number)
    e.delete(0, END)

def button_pow():
    first_number = e.get()
    global f_num
    global op
    global a 
    global powering
    op = "**"
    f_num = float(first_number)
    e.delete(0, END)

def button_factorial():
    first_number = e.get()
    global f_num
    global op
    global a 
    global powering
    op = "fact"
    f_num = float(first_number)
    e.delete(0, END)
    

def button_equal():
    global second_number
    global myerrorlabel

    try:
        if op == 'sqr':
            second_number = f_num

        elif op == 'pi':
            second_number = '3.141592653589793'

        elif op == 'sqrt':
            second_number = f_num
            
        elif op == 'fact':
            second_number = f_num

        else:
            second_number = float(e.get())
            e.delete(0, END)


        if op == "+":
            e.insert(0, f_num + float(second_number))
            whatfunction_add()


        if op == "-":
            e.insert(0, f_num - float(second_number))
            whatfunction_sub()


        if op == "*":
            e.insert(0, f_num * float(second_number))
            whatfunction_mult()


        if op == "/":
            e.insert(0, f_num / float(second_number))
            whatfunction_div()



        if op == "%":
            e.insert(0, f_num % float(second_number))
            whatfunction_rem()

        if op == "**":
            e.insert(0, math.pow(f_num, second_number))
            whatfunction_pow()


        if op == "sqr":
            e.insert(0, f_num * f_num)
            whatfunction_sqr()

        if op == 'pi':
            e.insert(0, f_num * 3.141592653589793)
            whatfunction_pi()
      
        if op == 'sqrt':
            e.insert(0, math.sqrt(f_num))
            whatfunction_sqrt()
            
        if op == 'fact':
            e.insert(0, math.factorial(f_num))
            whatfunction_fact()

    except NameError:
        error = messagebox.askokcancel("Name Error ", "Please Enter an valid expression")
        if error == True:
            pass
        else:
            root.quit()
            
    except ValueError:
        error2 = messagebox.askokcancel("Value Error ", "Enter an valid expression !")
        if error2 == True:
            pass
        else:
            root.quit()
        
    except ZeroDivisionError:
        error3 = messagebox.askokcancel("Value Error ", "Did u learn maths ? you can't divide zero")
        if error3 == True:
            pass
        else:
            root.quit()
        
        

  ## Make our labels 
def whatfunction_add():
    if op == "+":
        global mylabel_add
        mylabel_add = Label(root, text= str(f_num ) + " " + "+" + " " + str(second_number))
        mylabel_add.grid(row=0, column=0, columnspan=2, padx=40, pady=3)


def whatfunction_sub():
    global mylabel_sub
    if op == "-":
        mylabel_sub = Label(root, text= str(f_num ) + " " + "-" + " " + str(second_number))
        mylabel_sub.grid(row=0, column=0, columnspan=2, padx=40, pady=3)


def whatfunction_mult():
    global mylabel_mult
    if op == "*":
        mylabel_mult = Label(root, text= str(f_num ) + " " + "*" + " " + str(second_number))
        mylabel_mult.grid(row=0, column=0, columnspan=2, padx=40, pady=3)

def whatfunction_div():
    global mylabel_div
    if op == "/":
        mylabel_div = Label(root, text= str(f_num ) + " " + "/" + " " + str(second_number))
        mylabel_div.grid(row=0, column=0, columnspan=2, padx=40, pady=3)

def whatfunction_rem():
    global mylabel_rem
    if op == "%":
        mylabel_rem = Label(root, text= str(f_num ) + " " + "%" + " " + str(second_number))
        mylabel_rem.grid(row=0, column=0, columnspan=2, padx=40, pady=3)

def whatfunction_pow():
    global mylabel_pow
    if op == "**":
        mylabel_pow = Label(root, text= str(f_num ) + " " + "**" + " " + str(second_number))
        mylabel_pow.grid(row=0, column=0, columnspan=2, padx=40, pady=3)

def whatfunction_sqr():
    global mylabel_sqr
    if op == "sqr":
        mylabel_sqr = Label(root, text= str(f_num ) + " square")
        mylabel_sqr.grid(row=0, column=0, columnspan=2, padx=40, pady=3)

def whatfunction_pi():
    global mylabel_pi
    if op == "pi":
        mylabel_pi = Label(root, text= str(f_num ) + " pi")
        mylabel_pi.grid(row=0, column=0, columnspan=2, padx=40, pady=3)
  
def whatfunction_sqrt():
    global mylabel_sqrt
    if op == "sqrt":
        mylabel_sqrt = Label(root, text= str(f_num ) + " sqrt")
        mylabel_sqrt.grid(row=0, column=0, columnspan=2, padx=40, pady=3)
        
def whatfunction_fact():
    global mylabel_fact
    if op == "fact":
        mylabel_fact = Label(root, text= str(f_num ) + " factorial")
        mylabel_fact.grid(row=0, column=0, columnspan=2, padx=40, pady=3)      


# Define buttons
Button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
Button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
Button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
Button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
Button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
Button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
Button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
Button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
Button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
Button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

Button_add = Button(root, text="+", padx=35, pady=18, command=button_add)
Button_equal = Button(root, text="=", padx=40, pady=20, command=button_equal)
Button_clear = Button(root, text="clear", padx=30, pady=18, command=button_clear)
Button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
Button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
Button_divide = Button(root, text="/", padx=40, pady=20, command=button_divide)
Button_point = Button(root, text=".", padx=40, pady=20, command=lambda: button_click('.'))
Button_open_paranthesis = Button(root, text="(", padx=40, pady=20, command=lambda: button_click('('))
Button_close_paranthesis = Button(root, text=")", padx=40, pady=20, command=lambda: button_click(')'))
Button_remainder = Button(root, text="%", padx=35, pady=20, command=button_rem)
Button_power = Button(root, text="pow", padx=30, pady=20, command=button_pow)
Button_sqr = Button(root, text="sqr", padx=30, pady=20, command=button_sqr)
Button_pi = Button(root, text="pi", padx=30, pady=20, command=button_pi)
Button_sqrt = Button(root, text="sqrt", padx=30, pady=20, command=button_sqrt)
Button_fact = Button(root, text="Fact", padx=30, pady=20, command=button_factorial)


Button_exit = Button(root, text="Exit", padx=30, pady=18, command=button_exit)

#Put buttons on screen
Button_1.grid(row=4, column=0)
Button_2.grid(row=4, column=1)
Button_3.grid(row=4, column=2)

Button_4.grid(row=3, column=0)
Button_5.grid(row=3, column=1)
Button_6.grid(row=3, column=2)

Button_7.grid(row=2, column=0)
Button_8.grid(row=2, column=1)
Button_9.grid(row=2, column=2) 

Button_0.grid(row=5, column=0)
Button_point.grid(row=5, column=1)



Button_add.grid(row=2, column=3)
Button_subtract.grid(row=3, column=3)
Button_multiply.grid(row=4, column=3)
Button_divide.grid(row=5, column=3)

Button_remainder.grid(row=3, column=4)
Button_power.grid(row=2, column=4, columnspan=1)
Button_sqr.grid(row=4, column=4, columnspan=1)
Button_pi.grid(row=5, column=4, columnspan=1)
Button_sqrt.grid(row=6, column=4, columnspan=1)
Button_fact.grid(row=2, column=5, columnspan=1)




Button_clear.grid(row=5, column=2, columnspan=1)
Button_equal.grid(row=6, column=1, columnspan=1)
Button_open_paranthesis.grid(row=6, column=0)
Button_close_paranthesis.grid(row=6, column=2)


Button_exit.grid(row=1, column=3)


# Create a main loop
root.mainloop()



