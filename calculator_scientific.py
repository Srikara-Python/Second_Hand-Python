""" Scientific Calculator made using tkinter module
Free to copy and open-source """

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import math

root = Tk()
root.title("Sceintific Calculator")
##root.geometry("600x450+0+0")
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')
orig_color = root.cget("background")
root.configure(bg=orig_color)

tabControl = ttk.Notebook(root)
  
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Standard')
tabControl.add(tab2, text ='Scientific')

tabControl.grid(row=0, column=0)
  

def new_win():
    top = Toplevel()
    tell = Label(top, text="Make sure you read our help, about and contribute sections")
    thankyou = Label(top, text="Thankyou for using us , please do share and add suggetions to the link provided.")
    tell.pack()
    thankyou.pack()

open_button = Button(tab1, text="Click Me!", command=new_win, padx=5, pady=5)
open_button.grid(row=0, column=3)
open_button_ = Button(tab2, text="Click Me!", command=new_win, padx=5, pady=5)
open_button_.grid(row=0, column=3)


e = Entry(tab1, width=35, borderwidth=5)
e.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
e_ = Entry(tab2, width=35, borderwidth=5)
e_.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

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
    open_button.configure(bg="black", fg="white")
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
    open_button.configure(bg=orig_color, fg="black")
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

def button_exit_():
    root.quit()
    
def about_menu():
    about = Toplevel(root)
    about.geometry("320x280+0+0")
    label1 = Label(about, text="Developed By Srikara under open source licence").grid(row=0, column=1)
    label2 = Label(about, text="Date:- 19.11.2021").grid(row=1, column=1)
    label3 = Label(about, text="Made in Python using tkinter module").grid(row=2, column=1)  
    root.eval(f'tk::PlaceWindow {str(about)} center')
    
def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("600x450+0+0")
    root.eval('tk::PlaceWindow . center')


def Standard():
    root.resizable(width=False, height=False)
    root.geometry("380x450+0+0")
    root.eval('tk::PlaceWindow . center')

menubar = Menu(root)

# ManuBar 1 :
# filemenu = Menu(menubar, tearoff = 0)
# menubar.add_cascade(label = 'Mode', menu = filemenu)
# filemenu.add_command(label = "Standard", command = Standard)
# filemenu.add_command(label = "Scientific", command = Scientific)
# filemenu.add_separator()
# filemenu.add_command(label = "Exit", command = button_exit)
    

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

   if check_div == True:
        mylabel_div.destroy()

   if check_rem == True:
        mylabel_rem.destroy()

   if check_pow == True:
        mylabel_pow.destroy()

   if check_sqr == True:
        mylabel_sqr.destroy()

   
   if check_error == True:
        myerrorlabel.destroy()

   if check_pi == True:
        mylabel_pi.destroy()

   if check_sqrt == True:
        mylabel_sqrt.destroy()
        
   if check_fact == True:
        mylabel_fact.destroy()

        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def button_click_(number):
   current = e_.get()
   e_.delete(0, END)
   e_.insert(0, str(current) + str(number))


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

   if check_div == True:
        mylabel_div.destroy()

   if check_rem == True:
        mylabel_rem.destroy()

   if check_pow == True:
        mylabel_pow.destroy()

   if check_sqr == True:
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
def button_clear_():
    e_.delete(0, END)
    
def button_add():
    first_number = e.get()
    global f_num
    global op
    op = "+"
    f_num = float(first_number)
    e.delete(0, END)
def button_add_():
    first_number = e_.get()
    global f_num
    global op
    op = "+"
    f_num = float(first_number)
    e_.delete(0, END)

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



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def button_subtract_():
    first_number = e_.get()
    global f_num
    global op
    op = "-"
    f_num = float(first_number)
    e_.delete(0, END)

def button_multiply_():
    first_number = e_.get()
    global f_num
    global op
    op = "*"
    f_num = float(first_number)
    e_.delete(0, END)


def button_divide_():
    first_number = e_.get()
    global f_num
    global op
    op = "/"
    f_num = float(first_number)
    e_.delete(0, END)

def button_rem_():
    first_number = e_.get()
    global f_num
    global op
    op = "%"
    f_num = float(first_number)
    e_.delete(0, END)


def button_sqr_():
    first_number = e_.get()
    global f_num
    global op
    op = "sqr"
    f_num = float(first_number)
    e_.delete(0, END)

def button_pi_():
    first_number = e_.get()
    global f_num
    global op
    op = "pi"
    f_num = float(first_number)
    e_.delete(0, END)
    
def button_sqrt_():
    first_number = e_.get()
    global f_num
    global op
    global a 
    op = "sqrt"
    f_num = float(first_number)
    e_.delete(0, END)

def button_pow_():
    first_number = e_.get()
    global f_num
    global op
    global a 
    global powering
    op = "**"
    f_num = float(first_number)
    e_.delete(0, END)

def button_factorial_():
    first_number = e_.get()
    global f_num
    global op
    global a 
    global powering
    op = "fact"
    f_num = float(first_number)
    e_.delete(0, END)
    

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
            whatfunction_add_()


        if op == "-":
            e.insert(0, f_num - float(second_number))
            whatfunction_sub()
            whatfunction_sub_()

        if op == "*":
            e.insert(0, f_num * float(second_number))
            whatfunction_mult()
            whatfunction_mult_()


        if op == "/":
            e.insert(0, f_num / float(second_number))
            whatfunction_div()
            whatfunction_div_()


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

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def button_equal_():
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
            second_number = float(e_.get())
            e_.delete(0, END)


        if op == "+":
            e_.insert(0, f_num + float(second_number))
            whatfunction_add()
            whatfunction_add_


        if op == "-":
            e_.insert(0, f_num - float(second_number))
            whatfunction_sub()
            whatfunction_sub_()


        if op == "*":
            e_.insert(0, f_num * float(second_number))
            whatfunction_mult()
            whatfunction_mult_()


        if op == "/":
            e_.insert(0, f_num / float(second_number))
            whatfunction_div()
            whatfunction_div_()



        if op == "%":
            e_.insert(0, f_num % float(second_number))
            whatfunction_rem()

        if op == "**":
            e_.insert(0, math.pow(f_num, second_number))
            whatfunction_pow()


        if op == "sqr":
            e_.insert(0, f_num * f_num)
            whatfunction_sqr()

        if op == 'pi':
            e_.insert(0, f_num * 3.141592653589793)
            whatfunction_pi()
      
        if op == 'sqrt':
            e_.insert(0, math.sqrt(f_num))
            whatfunction_sqrt()
            
        if op == 'fact':
            e_.insert(0, math.factorial(f_num))
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
        mylabel_add.grid(row=2, column=0, columnspan=2, padx=40, pady=3)


def whatfunction_sub():
    global mylabel_sub
    if op == "-":
        mylabel_sub = Label(root, text= str(f_num ) + " " + "-" + " " + str(second_number))
        mylabel_sub.grid(row=2, column=0, columnspan=2, padx=40, pady=3)


def whatfunction_mult():
    global mylabel_mult
    if op == "*":
        mylabel_mult = Label(root, text= str(f_num ) + " " + "*" + " " + str(second_number))
        mylabel_mult.grid(row=2, column=0, columnspan=2, padx=40, pady=3)

def whatfunction_div():
    global mylabel_div
    if op == "/":
        mylabel_div = Label(root, text= str(f_num ) + " " + "/" + " " + str(second_number))
        mylabel_div.grid(row=2, column=0, columnspan=2, padx=40, pady=3)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def whatfunction_add_():
    if op == "+":
        global mylabel_add
        mylabel_add_ = Label(root, text= str(f_num ) + " " + "+" + " " + str(second_number))
        mylabel_add_.grid(row=2, column=0, columnspan=2, padx=40, pady=3)


def whatfunction_sub_():
    global mylabel_sub
    if op == "-":
        mylabel_sub_ = Label(root, text= str(f_num ) + " " + "-" + " " + str(second_number))
        mylabel_sub_.grid(row=2, column=0, columnspan=2, padx=40, pady=3)


def whatfunction_mult_():
    global mylabel_mult
    if op == "*":
        mylabel_mult_ = Label(root, text= str(f_num ) + " " + "*" + " " + str(second_number))
        mylabel_mult_.grid(row=2, column=0, columnspan=2, padx=40, pady=3)

def whatfunction_div_():
    global mylabel_div
    if op == "/":
        mylabel_div_ = Label(root, text= str(f_num ) + " " + "/" + " " + str(second_number))
        mylabel_div_.grid(row=2, column=0, columnspan=2, padx=40, pady=3)
def whatfunction_rem():
    global mylabel_rem
    if op == "%":
        mylabel_rem = Label(root, text= str(f_num ) + " " + "%" + " " + str(second_number))
        mylabel_rem.grid(row=2, column=0, columnspan=2, padx=40, pady=3)

def whatfunction_pow():
    global mylabel_pow
    if op == "**":
        mylabel_pow = Label(root, text= str(f_num ) + " " + "**" + " " + str(second_number))
        mylabel_pow.grid(row=2, column=0, columnspan=2, padx=40, pady=3)

def whatfunction_sqr():
    global mylabel_sqr
    if op == "sqr":
        mylabel_sqr = Label(root, text= str(f_num ) + " square")
        mylabel_sqr.grid(row=2, column=0, columnspan=2, padx=40, pady=3)

def whatfunction_pi():
    global mylabel_pi
    if op == "pi":
        mylabel_pi = Label(root, text= str(f_num ) + " pi")
        mylabel_pi.grid(row=2, column=0, columnspan=2, padx=40, pady=3)
  
def whatfunction_sqrt():
    global mylabel_sqrt
    if op == "sqrt":
        mylabel_sqrt = Label(root, text= str(f_num ) + " sqrt")
        mylabel_sqrt.grid(row=2, column=0, columnspan=2, padx=40, pady=3)
        
def whatfunction_fact():
    global mylabel_fact
    if op == "fact":
        mylabel_fact = Label(root, text= str(f_num ) + " factorial")
        mylabel_fact.grid(row=2, column=0, columnspan=2, padx=40, pady=3)      


# Define buttons
#def standard():


Button_1 = Button(tab1, text="1", padx=40, pady=20, command=lambda: button_click(1))
Button_2 = Button(tab1, text="2", padx=40, pady=20, command=lambda: button_click(2))
Button_3 = Button(tab1, text="3", padx=40, pady=20, command=lambda: button_click(3))
Button_4 = Button(tab1, text="4", padx=40, pady=20, command=lambda: button_click(4))
Button_5 = Button(tab1, text="5", padx=40, pady=20, command=lambda: button_click(5))
Button_6 = Button(tab1, text="6", padx=40, pady=20, command=lambda: button_click(6))
Button_7 = Button(tab1, text="7", padx=40, pady=20, command=lambda: button_click(7))
Button_8 = Button(tab1, text="8", padx=40, pady=20, command=lambda: button_click(8))
Button_9 = Button(tab1, text="9", padx=40, pady=20, command=lambda: button_click(9))
Button_0 = Button(tab1, text="0", padx=40, pady=20, command=lambda: button_click(0))

Button_add = Button(tab1, text="+", padx=35, pady=18, command=button_add)
Button_equal = Button(tab1, text="=", padx=40, pady=20, command=button_equal)
Button_clear = Button(tab1, text="clear", padx=30, pady=18, command=button_clear)
Button_subtract = Button(tab1, text="-", padx=40, pady=20, command=button_subtract)
Button_multiply = Button(tab1, text="*", padx=40, pady=20, command=button_multiply)
Button_divide = Button(tab1, text="/", padx=40, pady=20, command=button_divide)
Button_point = Button(tab1, text=".", padx=40, pady=20, command=lambda: button_click('.'))
Button_open_paranthesis = Button(tab1, text="(", padx=40, pady=20, command=lambda: button_click('('))
Button_close_paranthesis = Button(tab1, text=")", padx=40, pady=20, command=lambda: button_click_(')'))



Button_exit = Button(tab1, text="Exit", padx=30, pady=18, command=button_exit)

""""""""""""""""""""""""""""""""""""""""""

##def advanced():
Button_1_ = Button(tab2, text="1", padx=40, pady=20, command=lambda: button_click_(1))
Button_2_ = Button(tab2, text="2", padx=40, pady=20, command=lambda: button_click_(2))
Button_3_ = Button(tab2, text="3", padx=40, pady=20, command=lambda: button_click_(3))
Button_4_ = Button(tab2, text="4", padx=40, pady=20, command=lambda: button_click_(4))
Button_5_ = Button(tab2, text="5", padx=40, pady=20, command=lambda: button_click_(5))
Button_6_ = Button(tab2, text="6", padx=40, pady=20, command=lambda: button_click_(6))
Button_7_ = Button(tab2, text="7", padx=40, pady=20, command=lambda: button_click_(7))
Button_8_ = Button(tab2, text="8", padx=40, pady=20, command=lambda: button_click_(8))
Button_9_ = Button(tab2, text="9", padx=40, pady=20, command=lambda: button_click_(9))
Button_0_ = Button(tab2, text="0", padx=40, pady=20, command=lambda: button_click_(0))

Button_add_ = Button(tab2, text="+", padx=35, pady=18, command=button_add_)
Button_equal_ = Button(tab2, text="=", padx=40, pady=20, command=button_equal_)
Button_clear_ = Button(tab2, text="clear", padx=30, pady=18, command=button_clear_)
Button_subtract_ = Button(tab2, text="-", padx=40, pady=20, command=button_subtract_)
Button_multiply_ = Button(tab2, text="*", padx=40, pady=20, command=button_multiply_)
Button_divide_ = Button(tab2, text="/", padx=40, pady=20, command=button_divide_)
Button_point_ = Button(tab2, text=".", padx=40, pady=20, command=lambda: button_click_('.'))
Button_open_paranthesis_ = Button(tab2, text="(", padx=40, pady=20, command=lambda: button_click_('('))
Button_close_paranthesis_ = Button(tab2, text=")", padx=40, pady=20, command=lambda: button_click_(')'))
Button_remainder_ = Button(tab2, text="%", padx=35, pady=20, command=button_rem_)
Button_power_ = Button(tab2, text="pow", padx=30, pady=20, command=button_pow_)
Button_sqr_ = Button(tab2, text="sqr", padx=30, pady=20, command=button_sqr_)
Button_pi_ = Button(tab2, text="pi", padx=30, pady=20, command=button_pi_)
Button_sqrt_ = Button(tab2, text="sqrt", padx=30, pady=20, command=button_sqrt_)
Button_fact_ = Button(tab2, text="Fact", padx=30, pady=20, command=button_factorial_)


Button_exit_ = Button(tab2, text="Exit", padx=30, pady=18, command=button_exit_)
##


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

Button_clear.grid(row=5, column=2, columnspan=1)
Button_equal.grid(row=6, column=1, columnspan=1)
Button_open_paranthesis.grid(row=6, column=0)
Button_close_paranthesis.grid(row=6, column=2)


Button_exit.grid(row=6, column=3)

""""""""""""""""""""""""""""""""""""""""""""""""""""""

Button_1_.grid(row=4, column=0)
Button_2_.grid(row=4, column=1)
Button_3_.grid(row=4, column=2)

Button_4_.grid(row=3, column=0)
Button_5_.grid(row=3, column=1)
Button_6_.grid(row=3, column=2)

Button_7_.grid(row=2, column=0)
Button_8_.grid(row=2, column=1)
Button_9_.grid(row=2, column=2) 

Button_0_.grid(row=5, column=0)
Button_point_.grid(row=5, column=1)



Button_add_.grid(row=2, column=3)
Button_subtract_.grid(row=3, column=3)
Button_multiply_.grid(row=4, column=3)
Button_divide_.grid(row=5, column=3)
Button_remainder_.grid(row=3, column=4)
Button_power_.grid(row=2, column=4, columnspan=1)
Button_sqr_.grid(row=4, column=4, columnspan=1)
Button_pi_.grid(row=5, column=4, columnspan=1)
Button_sqrt_.grid(row=6, column=4, columnspan=1)
Button_fact_.grid(row=2, column=5, columnspan=1)




Button_clear_.grid(row=5, column=2, columnspan=1)
Button_equal_.grid(row=6, column=1, columnspan=1)
Button_open_paranthesis_.grid(row=6, column=0)
Button_close_paranthesis_.grid(row=6, column=2)


Button_exit_.grid(row=6, column=3)



# Create a main loop
root.mainloop()



