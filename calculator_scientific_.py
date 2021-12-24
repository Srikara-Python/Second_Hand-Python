""" Scientific Calculator made using tkinter module
Free to copy and open-source """

from curtsies import Input
import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import math


def main():
    with Input(keynames='curses') as input_generator:
        for e in input_generator:
            print(repr(e))

root = Tk()
root.title("Sceintific Calculator")
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')
orig_color = root.cget("background")
root.configure(bg='black')

def event_handle(event):
    # Replace the window's title with event.type: input key
    # root.title("{}: {}".format(str(event.type), event.keysym))
    key = event.keysym

s1 = ttk.Style()
s1.configure('My.TFrame', background='black')

tabControl = ttk.Notebook(root)


tab1 = ttk.Frame(tabControl, style='My.TFrame')
tab2 = ttk.Frame(tabControl, style='My.TFrame')
tab3 = ttk.Frame(tabControl, style='My.TFrame')


ttk.Style().configure("TNotebook", background='black');


tabControl.add(tab1, text ='Standard')
tabControl.add(tab2, text ='Scientific')
tabControl.add(tab3, text ='Web Browser')

tabControl.grid(row=0, column=0)

tabControl2 = ttk.Notebook(tab3)
tab_link = ttk.Frame(tabControl2, style='My.TFrame')
tab_url = ttk.Frame(tabControl2, style='My.TFrame')
ttk.Style().configure("TNotebook", background='black');

tabControl2.add(tab_url, text ='Custom URL')
tabControl2.add(tab_link, text ='Quick Links')

tabControl2.grid(row=0, column=0)


def open_page():
    webbrowser.open(entry.get())

def entry_delete():
    entry.delete(0, END)

def whaturl():
    webbrowser.open(quick_link_entry.get())

def custom_quick_link():
    global urlwhat
    global quick_link_entry
    global quick_link_name

    custom_quick = Toplevel(root)

    quick_link_entry_url = Label(custom_quick, text='Enter URL :- ').grid(row=0, column=0)
    quick_link_entry = Entry(custom_quick)
    quick_link_entry.insert(0, "")
    urlwhat = quick_link_entry.get()
    quick_link_entry.grid(row=0, column=1)

    quick_link_entry_name = Label(custom_quick, text='Enter Name :- ').grid(row=1, column=0)
    quick_link_name = Entry(custom_quick)
    quick_link_name.grid(row=1, column=1)

    quick_link_button = Button(custom_quick, text="Use link", command=custom_quick_link_add).grid(row=2, column=0)
     

def custom_quick_link_add():
    if quick_link_entry.get() == "":
        error = messagebox.askokcancel("ERROR ", "Please Enter URL")
        if error == True:
            pass
        else:
            root.quit()

    else:
        # url = quick_link_entry.get()
        name = quick_link_name.get()
        button = Button(tab_link, text=name, command=whaturl)
        button.pack(side=RIGHT)


web_what = Label(tab_url, text="Enter a URL above to open it in your fav browser")
web_what.grid(row=4, column=0, columnspan=15)
entry = Entry(tab_url, width=50)
entry.insert(0, "")
entry.grid(row=2, column=0, columnspan=15)
b = Button(tab_url, text='GO TO URL', command=open_page)
b.grid(row=3, column=0)
b2 = Button(tab_url, text='clear', command=entry_delete)
b2.grid(row=3, column=1)

quick_links = Button(tab_link, text="Custom Quick Links", command=custom_quick_link)
quick_links.pack() #grid(row=3, column=2)

def github():
    webbrowser.open('www.github.com')

def linux_mint():
    webbrowser.open('www.linuxmint.com')


link1 = Button(tab_link, text="Github", command=github)
link1.pack() #(row=4, column=0)
link2 = Button(tab_link, text="linux mint", command=linux_mint)
link2.pack() #(row=4, column=1)


e = Entry(tab1, width=35, borderwidth=5)
e.grid(row=1, column=0, columnspan=10, padx=5, pady=5)
e_ = Entry(tab2, width=35, borderwidth=5)
e_.grid(row=1, column=0, columnspan=5, padx=5, pady=5)

e.configure(bg="white", fg='black')
e_.configure(bg="white", fg="black")



def dark_mode():
    ttk.Style().configure("TNotebook", background='black');
    s1.configure('My.TFrame', background='black')
    root.configure(bg='black')
    entry.configure(bg='black', fg='white')
    b.configure(bg='black', fg='white')
    e.configure(bg="black", fg=orig_color)
    e_.configure(bg="black", fg=orig_color)
    menubar.configure(bg='black', fg=orig_color)
    aboutmenu.configure(bg="black", fg=orig_color)
    settingsmenu.configure(bg="black", fg=orig_color)
    editmenu.configure(bg="black", fg=orig_color)

    Button_0.configure(bg="black", fg=orig_color)  
    Button_1.configure(bg="black", fg=orig_color)
    Button_2.configure(bg="black", fg=orig_color)
    Button_3.configure(bg="black", fg=orig_color)
    Button_4.configure(bg="black", fg=orig_color)
    Button_5.configure(bg="black", fg=orig_color)
    Button_6.configure(bg="black", fg=orig_color)
    Button_7.configure(bg="black", fg=orig_color)
    Button_8.configure(bg="black", fg=orig_color)
    Button_9.configure(bg="black", fg=orig_color)
    Button_add.configure(bg="black", fg=orig_color)
    Button_subtract.configure(bg="black", fg=orig_color)
    Button_divide.configure(bg="black", fg=orig_color)
    Button_multiply.configure(bg="black", fg=orig_color)
    Button_open_paranthesis.configure(bg="black", fg=orig_color)
    Button_close_paranthesis.configure(bg="black", fg=orig_color)
    Button_equal.configure(bg="black", fg=orig_color)
    Button_exit.configure(bg="black", fg=orig_color)
    Button_pi_.configure(bg="black", fg=orig_color)
    Button_sqr_.configure(bg="black", fg=orig_color)
    Button_sqrt_.configure(bg="black", fg=orig_color)
    Button_remainder_.configure(bg="black", fg=orig_color)
    Button_power_.configure(bg="black", fg=orig_color)
    Button_point.configure(bg="black", fg=orig_color)
    Button_clear.configure(bg="black", fg=orig_color)
    Button_fact_.configure(bg="black", fg=orig_color)
    Button_undo.configure(bg="black", fg=orig_color)
    Button_undo_.configure(bg="black", fg=orig_color)

    Button_0_.configure(bg="black", fg=orig_color)  
    Button_1_.configure(bg="black", fg=orig_color)
    Button_2_.configure(bg="black", fg=orig_color)
    Button_3_.configure(bg="black", fg=orig_color)
    Button_4_.configure(bg="black", fg=orig_color)
    Button_5_.configure(bg="black", fg=orig_color)
    Button_6_.configure(bg="black", fg=orig_color)
    Button_7_.configure(bg="black", fg=orig_color)
    Button_8_.configure(bg="black", fg=orig_color)
    Button_9_.configure(bg="black", fg=orig_color)
    Button_add_.configure(bg="black", fg=orig_color)
    Button_subtract_.configure(bg="black", fg=orig_color)
    Button_divide_.configure(bg="black", fg=orig_color)
    Button_multiply_.configure(bg="black", fg=orig_color)
    Button_open_paranthesis_.configure(bg="black", fg=orig_color)
    Button_close_paranthesis_.configure(bg="black", fg=orig_color)
    Button_equal_.configure(bg="black", fg=orig_color)
    Button_exit_.configure(bg="black", fg=orig_color)
    Button_point_.configure(bg="black", fg=orig_color)
    Button_clear_.configure(bg="black", fg=orig_color)

def high_contrast_mode():
    ttk.Style().configure("TNotebook", background='black');
    s1.configure('My.TFrame', background='black')
    root.configure(bg='black')
    entry.configure(bg='white', fg='black')
    b.configure(bg='black', fg='white')
    e.configure(bg="white", fg="black")
    e_.configure(bg="white", fg="black")
    menubar.configure(bg='black', fg="white")
    aboutmenu.configure(bg="black", fg="white")
    settingsmenu.configure(bg="black", fg="white")
    editmenu.configure(bg="black", fg="white")


    Button_0.configure(bg="grey", fg="white")  
    Button_1.configure(bg="grey", fg="white")
    Button_2.configure(bg="grey", fg="white")
    Button_3.configure(bg="grey", fg="white")
    Button_4.configure(bg="grey", fg="white")
    Button_5.configure(bg="grey", fg="white")
    Button_6.configure(bg="grey", fg="white")
    Button_7.configure(bg="grey", fg="white")
    Button_8.configure(bg="grey", fg="white")
    Button_9.configure(bg="grey", fg="white")
    Button_add.configure(bg="brown", fg="white")
    Button_subtract.configure(bg="brown", fg="white")
    Button_divide.configure(bg="brown", fg="white")
    Button_multiply.configure(bg="brown", fg="white")
    Button_open_paranthesis.configure(bg="black", fg="white")
    Button_close_paranthesis.configure(bg="black", fg="white")
    Button_equal.configure(bg="orange", fg="white")
    Button_exit.configure(bg="black", fg="white")
    Button_pi_.configure(bg="indigo", fg="white")
    Button_sqr_.configure(bg="indigo", fg="white")
    Button_sqrt_.configure(bg="indigo", fg="white")
    Button_remainder_.configure(bg="indigo", fg="white")
    Button_power_.configure(bg="indigo", fg="white")
    Button_point.configure(bg="grey", fg="white")
    Button_clear.configure(bg="black", fg="white")
    Button_fact_.configure(bg="indigo", fg="white")
    Button_undo.configure(bg="black", fg="white")
    Button_undo_.configure(bg="black", fg="white")

    Button_0_.configure(bg="grey", fg="white")  
    Button_1_.configure(bg="grey", fg="white")
    Button_2_.configure(bg="grey", fg="white")
    Button_3_.configure(bg="grey", fg="white")
    Button_4_.configure(bg="grey", fg="white")
    Button_5_.configure(bg="grey", fg="white")
    Button_6_.configure(bg="grey", fg="white")
    Button_7_.configure(bg="grey", fg="white")
    Button_8_.configure(bg="grey", fg="white")
    Button_9_.configure(bg="grey", fg="white")
    Button_add_.configure(bg="brown", fg="white")
    Button_subtract_.configure(bg="brown", fg="white")
    Button_divide_.configure(bg="brown", fg="white")
    Button_multiply_.configure(bg="brown", fg="white")
    Button_open_paranthesis_.configure(bg="black", fg="white")
    Button_close_paranthesis_.configure(bg="black", fg="white")
    Button_equal_.configure(bg="orange", fg="white")
    Button_exit_.configure(bg="black", fg="white")
    Button_point_.configure(bg="grey", fg="white")
    Button_clear_.configure(bg="black", fg="white")

def light_mode():
    
    ttk.Style().configure("TNotebook", background="white");
    s1.configure('My.TFrame', background="white")
    entry.configure(bg='white', fg='black')
    b.configure(bg='white', fg='black')
    b2.configure(bg='white', fg='black')
    e.configure(bg=orig_color, fg='black')
    e_.configure(bg=orig_color, fg='black')
    menubar.configure(bg="white", fg="black")
    aboutmenu.configure(bg="white", fg="black")
    settingsmenu.configure(bg="white", fg="black")
    editmenu.configure(bg="white", fg="black")


    Button_0.configure(bg="white", fg="black")  
    Button_1.configure(bg="white", fg="black")
    Button_2.configure(bg="white", fg="black")
    Button_3.configure(bg="white", fg="black")
    Button_4.configure(bg="white", fg="black")
    Button_5.configure(bg="white", fg="black")
    Button_6.configure(bg="white", fg="black")
    Button_7.configure(bg="white", fg="black")
    Button_8.configure(bg="white", fg="black")
    Button_9.configure(bg="white", fg="black")
    Button_add.configure(bg="white", fg="black")
    Button_subtract.configure(bg="white", fg="black")
    Button_divide.configure(bg="white", fg="black")
    Button_multiply.configure(bg="white", fg="black")
    Button_open_paranthesis.configure(bg="white", fg="black")
    Button_close_paranthesis.configure(bg="white", fg="black")
    Button_equal.configure(bg="white", fg="black")
    Button_exit.configure(bg="white", fg="black")
    Button_pi_.configure(bg="white", fg="black")
    Button_sqr_.configure(bg="white", fg="black")
    Button_sqrt_.configure(bg="white", fg="black")
    Button_remainder_.configure(bg="white", fg="black")
    Button_power_.configure(bg="white", fg="black")
    Button_point.configure(bg="white", fg="black")
    Button_clear.configure(bg="white", fg="black")
    Button_fact_.configure(bg="white", fg="black")
    Button_undo.configure(bg="white", fg="black")
    Button_undo_.configure(bg="white", fg="black")


    Button_0_.configure(bg="white", fg="black")  
    Button_1_.configure(bg="white", fg="black")
    Button_2_.configure(bg="white", fg="black")
    Button_3_.configure(bg="white", fg="black")
    Button_4_.configure(bg="white", fg="black")
    Button_5_.configure(bg="white", fg="black")
    Button_6_.configure(bg="white", fg="black")
    Button_7_.configure(bg="white", fg="black")
    Button_8_.configure(bg="white", fg="black")
    Button_9_.configure(bg="white", fg="black")
    Button_add_.configure(bg="white", fg="black")
    Button_subtract_.configure(bg="white", fg="black")
    Button_divide_.configure(bg="white", fg="black")
    Button_multiply_.configure(bg="white", fg="black")
    Button_open_paranthesis_.configure(bg="white", fg="black")
    Button_close_paranthesis_.configure(bg="white", fg="black")
    Button_equal_.configure(bg="white", fg="black")
    Button_point_.configure(bg="white", fg="black")
    Button_exit_.configure(bg="white", fg="black")
    Button_clear_.configure(bg="white", fg="black")


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
    

menubar = Menu(root)
# ManuBar 1 :
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Mode', menu = filemenu)
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
settingsmenu.add_command(label = "High Contrast", command = high_contrast_mode)

root.config(menu=menubar)
menubar.configure(bg="black", fg="white")
aboutmenu.configure(bg="black", fg="white")

settingsmenu.configure(bg="black", fg="white")
editmenu.configure(bg="black", fg="white")


def button_click(number):
   current = e.get()
   e.delete(0, END)
   e.insert(0, str(current) + str(number))

   current = e_.get()
   e_.delete(0, END)
   e_.insert(0, str(current) + str(number))

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

        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def button_click_(number):
   global current
   current = e_.get()
   e_.delete(0, END)
   e_.insert(0, str(current) + str(number))

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

def undo_last_():
    e_.delete(len(e_.get())-1,END)

def button_clear():
    e.delete(0, END) 
def button_clear_():
    e_.delete(0, END)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def button_equal():

    try:
        
        result_add = e.get().find("+")
        result_sub = e.get().find("-")
        result_mult = e.get().find("*")
        result_div = e.get().find("/")


        if result_add >= 0:
            global add1
            add1 = e.get()
            add = eval(e.get())
            e.delete(0, END)
            e_.delete(0, END)
            e.insert(0, add) 
            whatfunction_add()


        if result_sub >= 0:
            global sub1
            sub1 = e.get()
            sub = eval(e.get())
            e.delete(0, END)
            e_.delete(0, END)
            e.insert(0, sub) 
            whatfunction_sub()


        if result_mult >= 0:
            global mult1
            mult1 = e.get()

            mult = eval(e.get())
            e.delete(0, END)
            e_.delete(0, END)
            e.insert(0, mult) 
            whatfunction_mult()
            
        if result_div >= 0:
            global div1
            div1 = e.get()
            div = eval(e.get())
            e.delete(0, END)
            e_.delete(0, END)
            e.insert(0, div) 
            whatfunction_div()
           
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


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def button_equal_():

    global second_number
    global myerrorlabel
    result_add = e_.get().find("+")
    result_sub = e_.get().find("-")
    result_mult = e_.get().find("*")
    result_div = e_.get().find("/")
    result_rem = e_.get().find("%")
    result_pow = e_.get().find("**")
    result_sqr = e_.get().find("* 2")
    result_pi = e_.get().find("3.141592653589793")
    result_sqrt = e_.get().find("sqrt")
    result_fact = e_.get().find("fact")
    try:
        global power_what
        power_what = e_.get()
        if result_add >= 0:
            global add2
            add2 = e_.get()
            add = eval(e_.get())
            e_.delete(0, END)
            e.delete(0, END)
            e_.insert(0, add) 
            whatfunction_add_()


        if result_sub >= 0:
            global sub2
            sub2 = e_.get()
            sub = eval(e_.get())
            e_.delete(0, END)
            e.delete(0, END)
            e_.insert(0, sub) 
            whatfunction_sub_()


        if result_mult >= 0:
            global mult2
            mult2 = e_.get()
            mult = eval(e_.get())
            e_.delete(0, END)
            e.delete(0, END)
            e_.insert(0, mult) 
            whatfunction_mult_()
            
        if result_div >= 0:
            global div2
            div2 = e_.get()
            div = eval(e_.get())
            e_.delete(0, END)
            e.delete(0, END)
            e_.insert(0, div) 
            whatfunction_div_()

        if result_rem >= 0:
            global rem2
            rem2 = e_.get()
            rem = eval(e_.get())
            e_.delete(0, END)
            e.delete(0, END)
            e_.insert(0, rem) 
            whatfunction_rem()

        if result_pow >= 0:
            pow1 = eval(e_.get())
            e_.delete(0, END)
            e.delete(0, END)
            e_.insert(0, pow1) 
            whatfunction_pow()

        if result_sqr >= 0:
            global sqr2
            sqr2 = e_.get()
            sqr = eval(e_.get())
            e_.delete(0, END)
            e.delete(0, END)
            e_.insert(0, sqr) 
            whatfunction_sqr()

        if result_pi >= 0:
            global pi2
            pi2 = e_.get()
            pi = eval(e_.get())
            e_.delete(0, END)
            e.delete(0, END)
            e_.insert(0, pi) 
            whatfunction_pi()
        
        if result_sqrt >= 0:
            global sqrt2
            sqrt2 = e_.get()
            sqrt = eval(e_.get())
            e_.delete(0, END)
            e.delete(0, END)
            e_.insert(0, sqrt) 
            whatfunction_sqrt()

        if result_fact >= 0:
            global fact2
            fact2 = e_.get()
            fact = e_.get()
            facto = int ( ''.join(filter(str.isdigit, fact) ) )
            e_.delete(0, END)
            e.delete(0, END)
            e_.insert(0, math.factorial(facto))
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

  ## Make our labels 

def whatfunction_add():
    global mylabel_add
    mylabel_add = Label(root, text= add1 + " = " + e.get(), bg='black', fg="white")
    mylabel_add.grid(row=2, column=0, columnspan=2, padx=40, pady=3)
def whatfunction_add_():
    global mylabel_add
    mylabel_add = Label(root, text= add2 + " = " + e_.get(), bg='black', fg="white")
    mylabel_add.grid(row=2, column=0, columnspan=2, padx=40, pady=3)


def whatfunction_sub():
    global mylabel_sub
    mylabel_sub = Label(root, text= sub1 +  " = " + e.get(), bg='black', fg="white")
    mylabel_sub.grid(row=2, column=0, columnspan=2, padx=40, pady=3)
def whatfunction_sub_():
    global mylabel_sub
    mylabel_sub = Label(root, text= sub2 +  " = " + e_.get(), bg='black', fg="white")
    mylabel_sub.grid(row=2, column=0, columnspan=2, padx=40, pady=3)


def whatfunction_mult():
    global mylabel_mult
    mylabel_mult = Label(root, text= mult1 +  " = " + e.get(), bg='black', fg="white")
    mylabel_mult.grid(row=2, column=0, columnspan=2, padx=40, pady=3)
def whatfunction_mult_():    
    global mylabel_mult
    mylabel_mult = Label(root, text= mult2 +  " = " + e_.get(), bg='black', fg="white")
    mylabel_mult.grid(row=2, column=0, columnspan=2, padx=40, pady=3)

def whatfunction_div():
    global mylabel_div
    mylabel_div = Label(root, text= div1 +  " = " + e.get(), bg='black', fg="white")
    mylabel_div.grid(row=2, column=0, columnspan=2, padx=40, pady=3)
def whatfunction_div_():
    global mylabel_div
    mylabel_div = Label(root, text= div2 +  " = " + e_.get(), bg='black', fg="white")
    mylabel_div.grid(row=2, column=0, columnspan=2, padx=40, pady=3)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def whatfunction_rem():
    global mylabel_rem
    mylabel_rem = Label(root, text= rem2 +  " = " + e_.get(), bg='black', fg="white")
    mylabel_rem.grid(row=2, column=0, columnspan=2, padx=40, pady=3)

def whatfunction_pow():
    global mylabel_pow
    mylabel_pow = Label(root, text= power_what +  " = " + e_.get(), bg='black', fg="white")
    mylabel_pow.grid(row=2, column=0, columnspan=2, padx=40, pady=3)

def whatfunction_sqr():
    global mylabel_sqr
    mylabel_sqr = Label(root, text= power_what +  " = " + e_.get(), bg='black', fg="white")
    mylabel_sqr.grid(row=2, column=0, columnspan=2, padx=40, pady=3)

def whatfunction_pi():
    global mylabel_pi
    mylabel_pi = Label(root, text= power_what +  " = " + e_.get(), bg='black', fg="white")
    mylabel_pi.grid(row=2, column=0, columnspan=2, padx=40, pady=3)
  
def whatfunction_sqrt():
    global mylabel_sqrt
    mylabel_sqrt = Label(root, text= power_what +  " = " + e_.get(), bg='black', fg="white")
    mylabel_sqrt.grid(row=2, column=0, columnspan=2, padx=40, pady=3)
        
def whatfunction_fact():
    global mylabel_fact
    mylabel_fact = Label(root, text= power_what +  " = " + e_.get(), bg='black', fg="white")
    mylabel_fact.grid(row=2, column=0, columnspan=2, padx=40, pady=3)

# Define buttons

Button_1 = Button(tab1, text="1", padx=20, pady=15, bg='grey', command=lambda: button_click(1))
Button_2 = Button(tab1, text="2", padx=20, pady=15, command=lambda: button_click(2))
Button_3 = Button(tab1, text="3", padx=20, pady=15, command=lambda: button_click(3))
Button_4 = Button(tab1, text="4", padx=20, pady=15, command=lambda: button_click(4))
Button_5 = Button(tab1, text="5", padx=20, pady=15, command=lambda: button_click(5))
Button_6 = Button(tab1, text="6", padx=20, pady=15, command=lambda: button_click(6))
Button_7 = Button(tab1, text="7", padx=20, pady=15, command=lambda: button_click(7))
Button_8 = Button(tab1, text="8", padx=20, pady=15, command=lambda: button_click(8))
Button_9 = Button(tab1, text="9", padx=20, pady=15, command=lambda: button_click(9))
Button_0 = Button(tab1, text="0", padx=20, pady=15, command=lambda: button_click(0))

Button_add = Button(tab1, text="+", padx=17, pady=15, command=lambda: button_click(' + '))
Button_subtract = Button(tab1, text="-", padx=20, pady=15, command=lambda: button_click(' - '))
Button_multiply = Button(tab1, text="x", padx=18, pady=15, command=lambda: button_click(' * '))
Button_divide = Button(tab1, text="÷", padx=17, pady=15, command=lambda: button_click(' / '))

Button_undo = Button(tab1, text="⌫ ", padx=17, pady=15, command=undo_last)

Button_equal = Button(tab1, text="=", padx=18, pady=15, command=button_equal)
Button_clear = Button(tab1, text="clear", padx=8, pady=15, command=button_clear)


Button_point = Button(tab1, text=".", padx=22, pady=15, command=lambda: button_click('.'))
Button_open_paranthesis = Button(tab1, text="(", padx=20, pady=15, command=lambda: button_click('('))
Button_close_paranthesis = Button(tab1, text=")", padx=20, pady=15, command=lambda: button_click(')'))



Button_exit = Button(tab1, text="Exit", padx=8, pady=15, command=button_exit)


""""""""""""""""""""""""""""""""""""""""""

##def advanced():
Button_1_ = Button(tab2, text="1", padx=20, pady=15, command=lambda: button_click(1))
Button_2_ = Button(tab2, text="2", padx=20, pady=15, command=lambda: button_click(2))
Button_3_ = Button(tab2, text="3", padx=20, pady=15, command=lambda: button_click(3))
Button_4_ = Button(tab2, text="4", padx=20, pady=15, command=lambda: button_click(4))
Button_5_ = Button(tab2, text="5", padx=20, pady=15, command=lambda: button_click(5))
Button_6_ = Button(tab2, text="6", padx=20, pady=15, command=lambda: button_click(6))
Button_7_ = Button(tab2, text="7", padx=20, pady=15, command=lambda: button_click(7))
Button_8_ = Button(tab2, text="8", padx=20, pady=15, command=lambda: button_click(8))
Button_9_ = Button(tab2, text="9", padx=20, pady=15, command=lambda: button_click(9))
Button_0_ = Button(tab2, text="0", padx=20, pady=15, command=lambda: button_click(0))

Button_add_ = Button(tab2, text="+", padx=17, pady=15, command=lambda: button_click('+'))
Button_subtract_ = Button(tab2, text="-", padx=20, pady=15, command=lambda: button_click('-'))
Button_multiply_ = Button(tab2, text="x", padx=18, pady=15, command=lambda: button_click('*'))
Button_divide_ = Button(tab2, text="÷", padx=17, pady=15, command=lambda: button_click('/'))

Button_equal_ = Button(tab2, text="=", padx=20, pady=15, command=button_equal_)
Button_clear_ = Button(tab2, text="clear", padx=8, pady=15, command=button_clear_)

Button_point_ = Button(tab2, text=".", padx=22, pady=15, command=lambda: button_click_('.'))
Button_open_paranthesis_ = Button(tab2, text="(", padx=20, pady=15, command=lambda: button_click_('('))
Button_close_paranthesis_ = Button(tab2, text=")", padx=20, pady=15, command=lambda: button_click_(')'))
Button_remainder_ = Button(tab2, text="%", padx=20, pady=15, command=lambda: button_click('%'))
Button_power_ = Button(tab2, text="x^y", padx=12, pady=15, command=lambda: button_click('**'))

Button_sqr_ = Button(tab2, text="x^2", padx=12, pady=15, command=lambda: button_click(' * ' + e_.get()))
Button_pi_ = Button(tab2, text="pi", padx=20, pady=15, command=lambda: button_click('* 3.141592653589793'))
Button_sqrt_ = Button(tab2, text="√", padx=17, pady=15, command=lambda: button_click(' ** 0.5'))
Button_fact_ = Button(tab2, text="x!", padx=17, pady=15, command=lambda: button_click(' fact'))
Button_undo_ = Button(tab2, text="⌫", padx=17, pady=15, command=undo_last_)

Button_exit_ = Button(tab2, text="Exit", padx=8, pady=15, command=button_exit_)


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
Button_undo.grid(row=2, column=4)


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
Button_undo_.grid(row=3, column=5, columnspan=1)


Button_exit_.grid(row=6, column=3)


# Create a main loop
light_mode()

event_sequence = '<KeyPress>'
root.bind(event_sequence, event_handle)
root.bind('<KeyRelease>', event_handle)
root.mainloop()

