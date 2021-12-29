""" Scientific Calculator made using tkinter module
Free to copy and open-source """

from datetime import datetime, time
import time
import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import math


root = Tk()
root.title("Second Hand")
root.resizable(False, False)
root.geometry('375x350')
root.eval('tk::PlaceWindow . center')
orig_color = root.cget("background")
root.configure(bg='white')

Label(root, text="test").place(x=0, y=0)


e = Entry(root, width=40, borderwidth=1)
e.place(x=0, y=25)

e.configure(bg="white", fg='black')

def button_exit():
    root.quit()

def button_click(number):
   current = e.get()
   e.delete(0, END)
   e.insert(0, str(current) + str(number))


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

   if check_pi == True:
        mylabel_pi.destroy()

   if check_sqrt == True:
        mylabel_sqrt.destroy()
        
   if check_fact == True:
        mylabel_fact.destroy()


def undo_last():
    e.delete(len(e.get())-1,END)


def button_clear():
    e.delete(0, END) 



def button_equal():

    global second_number
    global myerrorlabel
    result_add = e.get().find("+")
    result_sub = e.get().find("-")
    result_mult = e.get().find("*")
    result_div = e.get().find("/")
    result_rem = e.get().find("%")
    result_pow = e.get().find("**")
    result_sqr = e.get().find("* 2")
    result_pi = e.get().find("3.141592653589793")
    result_sqrt = e.get().find("sqrt")
    result_fact = e.get().find("fact")
    try:
        global power_what
        power_what = e.get()
        if result_add >= 0:
            global add2
            add2 = e.get()
            add = eval(e.get())
            e.delete(0, END)
            e.delete(0, END)
            e.insert(0, add) 
            whatfunction_add_()


        if result_sub >= 0:
            global sub2
            sub2 = e.get()
            sub = eval(e.get())
            e.delete(0, END)
            e.delete(0, END)
            e.insert(0, sub) 
            whatfunction_sub_()


        if result_mult >= 0:
            global mult2
            mult2 = e.get()
            mult = eval(e.get())
            e.delete(0, END)
            e.delete(0, END)
            e.insert(0, mult) 
            whatfunction_mult_()
            
        if result_div >= 0:
            global div2
            div2 = e.get()
            div = eval(e.get())
            e.delete(0, END)
            e.delete(0, END)
            e.insert(0, div) 
            whatfunction_div_()

        if result_rem >= 0:
            global rem2
            rem2 = e.get()
            rem = eval(e.get())
            e.delete(0, END)
            e.delete(0, END)
            e.insert(0, rem) 
            whatfunction_rem()

        if result_pow >= 0:
            pow1 = eval(e.get())
            e.delete(0, END)
            e.delete(0, END)
            e.insert(0, pow1) 
            whatfunction_pow()

        if result_sqr >= 0:
            global sqr2
            sqr2 = e.get()
            sqr = eval(e.get())
            e.delete(0, END)
            e.delete(0, END)
            e.insert(0, sqr) 
            whatfunction_sqr()

        if result_pi >= 0:
            global pi2
            pi2 = e.get()
            pi = eval(e.get())
            e.delete(0, END)
            e.delete(0, END)
            e.insert(0, pi) 
            whatfunction_pi()
        
        if result_sqrt >= 0:
            global sqrt2
            sqrt2 = e.get()
            sqrt = eval(e.get())
            e.delete(0, END)
            e.delete(0, END)
            e.insert(0, sqrt) 
            whatfunction_sqrt()

        if result_fact >= 0:
            global fact2
            fact2 = e.get()
            fact = e.get()
            facto = int ( ''.join(filter(str.isdigit, fact) ) )
            e.delete(0, END)
            e.delete(0, END)
            e.insert(0, math.factorial(facto))
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
        
    except SyntaxError:
        error3 = messagebox.askokcancel("Value Error ", "Did u learn maths ?")
        if error3 == True:
            pass
        else:
            root.quit()




def whatfunction_add_():
    global mylabel_add
    mylabel_add = Label(root, text= add2 + " = " + e.get(), bg='black', fg="white")
    mylabel_add.place(x=0, y=320)



def whatfunction_sub_():
    global mylabel_sub
    mylabel_sub = Label(root, text= sub2 +  " = " + e.get(), bg='black', fg="white")
    mylabel_sub.place(x=0, y=320)



def whatfunction_mult_():    
    global mylabel_mult
    mylabel_mult = Label(root, text= mult2 +  " = " + e.get(), bg='black', fg="white")
    mylabel_mult.place(x=0, y=320)


def whatfunction_div_():
    global mylabel_div
    mylabel_div = Label(root, text= div2 +  " = " + e.get(), bg='black', fg="white")
    mylabel_div.place(x=0, y=320)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def whatfunction_rem():
    global mylabel_rem
    mylabel_rem = Label(root, text= rem2 +  " = " + e.get(), bg='black', fg="white")
    mylabel_rem.place(x=0, y=320)

def whatfunction_pow():
    global mylabel_pow
    mylabel_pow = Label(root, text= power_what +  " = " + e.get(), bg='black', fg="white")
    mylabel_pow.place(x=0, y=320)

def whatfunction_sqr():
    global mylabel_sqr
    mylabel_sqr = Label(root, text= power_what +  " = " + e.get(), bg='black', fg="white")
    mylabel_sqr.place(x=0, y=320)

def whatfunction_pi():
    global mylabel_pi
    mylabel_pi = Label(root, text= power_what +  " = " + e.get(), bg='black', fg="white")
    mylabel_pi.place(x=0, y=320)
  
def whatfunction_sqrt():
    global mylabel_sqrt
    mylabel_sqrt = Label(root, text= power_what +  " = " + e.get(), bg='black', fg="white")
    mylabel_sqrt.place(x=0, y=320)
        
def whatfunction_fact():
    global mylabel_fact
    mylabel_fact = Label(root, text= power_what +  " = " + e.get(), bg='black', fg="white")
    mylabel_fact.place(x=0, y=320)




Button_1_ = Button(root, text="1", padx=20, pady=15, bg='white', command=lambda: button_click(1 ))
Button_2_ = Button(root, text="2", padx=20, pady=15, bg='white', command=lambda: button_click(2 ))
Button_3_ = Button(root, text="3", padx=20, pady=15, bg='white', command=lambda: button_click(3 ))
Button_4_ = Button(root, text="4", padx=20, pady=15, bg='white', command=lambda: button_click(4 ))
Button_5_ = Button(root, text="5", padx=20, pady=15, bg='white', command=lambda: button_click(5 ))
Button_6_ = Button(root, text="6", padx=20, pady=15, bg='white', command=lambda: button_click(6 ))
Button_7_ = Button(root, text="7", padx=20, pady=15, bg='white', command=lambda: button_click(7 ))
Button_8_ = Button(root, text="8", padx=20, pady=15, bg='white', command=lambda: button_click(8 ))
Button_9_ = Button(root, text="9", padx=20, pady=15, bg='white', command=lambda: button_click(9 ))
Button_0_ = Button(root, text="0", padx=20, pady=15, bg='white', command=lambda: button_click(0 ))

Button_add_ = Button(root, text="+", padx=17, pady=15, bg='white', command=lambda: button_click(' + '))
Button_subtract_ = Button(root, text="-", padx=20, pady=15, bg='white', command=lambda: button_click(' - '))
Button_multiply_ = Button(root, text="x", padx=18, pady=15, bg='white', command=lambda: button_click(' * '))
Button_divide_ = Button(root, text="÷", padx=17, pady=15, bg='white', command=lambda: button_click(' / '))

Button_equal_ = Button(root, text="=", padx=25, pady=10, command=button_equal, bg='green', fg='white', highlightbackground='green', highlightcolor='green', highlightthickness=1)
Button_clear_ = Button(root, text="clear", padx=8, pady=15, bg='white', command=button_clear)

Button_point_ = Button(root, text=".", padx=22, pady=15, bg='white', command=lambda: button_click('.'))
Button_open_paranthesis_ = Button(root, text="(", padx=20, bg='white', pady=15, command=lambda: button_click('('))
Button_close_paranthesis_ = Button(root, text=")", padx=20, bg='white', pady=15, command=lambda: button_click(')'))
Button_remainder_ = Button(root, text="%", padx=15, pady=15, bg='white', command=lambda: button_click(' % '))
Button_power_ = Button(root, text="x^y", padx=8, pady=15, bg='white', command=lambda: button_click(' ** '))

Button_sqr_ = Button(root, text="x^2", padx=8, pady=15, bg='white', command=lambda: button_click(' * ' + e.get()))
Button_pi_ = Button(root, text="pi", padx=15, pady=15, bg='white', command=lambda: button_click(' * 3.141592653589793 '))
Button_sqrt_ = Button(root, text="√", padx=17, pady=15, bg='white', command=lambda: button_click(' ** 0.5 '))
Button_fact_ = Button(root, text="x!", padx=15, pady=15, bg='white', command=lambda: button_click(' fact'))
Button_undo_ = Button(root, text="⌫", padx=17, pady=15, bg='white', command=undo_last)

Button_exit_ = Button(root, text="Exit", padx=8, pady=15, bg='white', command=button_exit)


Button_equal_.place(x=230 , y=260)

Button_1_.place(x=0 , y=51 )
Button_2_.place(x=54 , y=51 )
Button_3_.place(x=108 , y=51 )
Button_add_.place(x=162 , y=51 )

Button_4_.place(x=0 , y=102 )
Button_5_.place(x=54 , y=102 )
Button_6_.place(x=108 , y=102 )
Button_subtract_.place(x=162 , y=102 )

Button_7_.place(x=0 , y=153 )
Button_8_.place(x=54 , y=153 )
Button_9_.place(x=108 , y=153 )
Button_multiply_.place(x=162 , y=153 )

Button_0_.place(x=0 , y=204 )
Button_point_.place(x=54 , y=204 )
Button_divide_.place(x=108 , y=204 )
Button_remainder_.place(x=162 , y=204 )






Button_power_.place(x=216 , y=51 )
Button_sqr_.place(x=216 , y=102)
Button_pi_.place(x=216 , y=153 )
Button_sqrt_.place(x=216 , y=204 )
Button_fact_.place(x=270 , y=51 )


Button_clear_.place(x=0 , y=258 )

Button_open_paranthesis_.place(x=115 , y=258 )
Button_close_paranthesis_.place(x=168 , y=258 )
Button_undo_.place(x=54 , y=258 )


# Button_exit_.place(x=0 , y=258 )






root.mainloop()

