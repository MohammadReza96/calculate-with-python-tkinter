#programed by Mohammadrz96
#----------------------------------------------------------- reqirments
from tkinter import *
#----------------------------------------------------------- optional module
import os 
os.system('cls')
#----------------------------------------------------------- creating functions
def buttom_click(number):
    current_number=myentry_1.get()
    myentry_1.delete(0,END)
    myentry_1.insert(0,str(current_number)+str(number))
#-------------plus(+)
n1=0
sign=" "  
def plus(event):
    label_1.config(text="plus")
    global n1
    global sign
    try:
        first_number=float(myentry_1.get())
    except ValueError:
        first_number=myentry_1.get()
    n1=first_number
    sign="plus"
    myentry_1.delete(0,END)
    print(n1)
#-------------minus(-)
def minus(number):
    label_1.config(text="minus")
    global n1
    global sign
    try:
        first_number=float(myentry_1.get())
    except ValueError:
        first_number=myentry_1.get()
    n1=first_number
    sign="minus"
    myentry_1.delete(0,END)
    print(n1)
#-------------times (*)
def times(number):
    label_1.config(text="times")
    global n1
    global sign
    try:
        first_number=float(myentry_1.get())
    except ValueError:
        first_number=myentry_1.get()
        
    # first_number=float(myentry_1.get())
    n1=first_number
    sign="times"
    myentry_1.delete(0,END)
    print(n1)
#-------------divide (/)
def divide(number):
    label_1.config(text="divide")
    global n1
    global sign
    try:
        first_number=float(myentry_1.get())
    except ValueError:
        first_number=myentry_1.get()
    # first_number=float(myentry_1.get())
    n1=first_number
    sign="divide"
    myentry_1.delete(0,END)
    print(n1)
#------------- equal (=)
def equal(number):
    label_1.config(text="equal")
    global sign
    global n1
    secend_number=myentry_1.get()
    myentry_1.delete(0,END)
    if sign=="plus":
        try:
            if int(secend_number) and n1=='infinite ...':
                res='infinite ...'
            elif int(secend_number) and n1=='impossible ...':
                res='impossible ...'
            else:
                res=n1+float(secend_number)
        except TypeError:
            res='impossible ...'
        myentry_1.insert(0,res)
    elif sign=="minus":
        try:
            if int(secend_number) and n1=='infinite ...':
                res='infinite ...'
            elif int(secend_number) and n1=='impossible ...':
                res='impossible ...'
            else:
                res=n1-float(secend_number)
        except TypeError:
            res='impossible ...'
        myentry_1.insert(0,res) 
        
        
        # myentry_1.insert(0,n1-float(secend_number))
    elif sign=="times":
        try:
            if int(secend_number)==0 and n1=='infinite ...':
                res=0
            elif int(secend_number) and n1=='infinite ...':
                res='infinite ...'
            elif int(secend_number)==0 and n1=='impossible ...':
                res='impossible ...'
            else:
                res=n1*float(secend_number)
        except TypeError:
            res='impossible ...'
        myentry_1.insert(0,res) 
    else:
        try:
            res=n1/float(secend_number)
        except ZeroDivisionError:
            res='infinite ...'
        except ValueError:
            res='impossible ...'
        except TypeError:
            res='impossible ...'
        myentry_1.insert(0,res)
    sign=""
#----------------------------------------------------------- clear
def clear(event):  
    label_1.config(text="clear")
    myentry_1.delete(0,END)
#----------------------------------------------------------- enter & leave ravadid
def func0(event):
    button_0.config(bg="#F18F01",fg="#ffffff")
def func00(event):
    button_0.config(bg="#f0f0f0",fg="#000000")
def func1(event):
    button_1.config(bg="#F18F01",fg="#ffffff")
def func11(event):
    button_1.config(bg="#f0f0f0",fg="#000000")
def func2(event):
    button_2.config(bg="#F18F01",fg="#ffffff")
def func22(event):
    button_2.config(bg="#f0f0f0",fg="#000000")
def func3(event):
    button_3.config(bg="#F18F01",fg="#ffffff")
def func33(event):
    button_3.config(bg="#f0f0f0",fg="#000000")
def func4(event):
    button_4.config(bg="#F18F01",fg="#ffffff")
def func44(event):
    button_4.config(bg="#f0f0f0",fg="#000000")
def func5(event):
    button_5.config(bg="#F18F01",fg="#ffffff")
def func55(event):
    button_5.config(bg="#f0f0f0",fg="#000000")
def func6(event):
    button_6.config(bg="#F18F01",fg="#ffffff")
def func66(event):
    button_6.config(bg="#f0f0f0",fg="#000000")
def func7(event):
    button_7.config(bg="#F18F01",fg="#ffffff")
def func77(event):
    button_7.config(bg="#f0f0f0",fg="#000000")
def func8(event):
    button_8.config(bg="#F18F01",fg="#ffffff")
def func88(event):
    button_8.config(bg="#f0f0f0",fg="#000000")
def func9(event):
    button_9.config(bg="#F18F01",fg="#000000")
def func99(event):
    button_9.config(bg="#f0f0f0",fg="#000000")
#----------------------------------------------------------- + / - / * / "/" / clear / equal    enter & leave ravadid
def funcp(event):
    button_plus.config(bg="#F18F01",fg="#000000")
def funcp1(event):
    button_plus.config(bg="#f0f0f0",fg="#000000")
def funcm(event):
    button_minus.config(bg="#F18F01",fg="#000000")
def funcm1(event):
    button_minus.config(bg="#f0f0f0",fg="#000000")
def funct(event):
    button_times.config(bg="#F18F01",fg="#000000")
def funct1(event):
    button_times.config(bg="#f0f0f0",fg="#000000")
def funcd(event):
    button_divide.config(bg="#F18F01",fg="#000000")
def funcd1(event):
    button_divide.config(bg="#f0f0f0",fg="#000000")
def funce(event):
    button_equal.config(bg="#F18F01",fg="#000000")
def funce1(event):
    button_equal.config(bg="#f0f0f0",fg="#000000")
def funcc(event):
    button_clear.config(bg="#F18F01",fg="#000000")
def funcc1(event):
    button_clear.config(bg="#f0f0f0",fg="#000000")
#----------------------------------------------------------- body of calculator
root=Tk()
myentry_1=Entry(root,borderwidth=5,width=35)
root.title("Calculator (Ver1)")
root.resizable(width=False,height=False)
#-----------------------------------------------------------
label_1=Label(root,text="cacio",fg="#000000",padx=10,pady=5)
#----------------------------------------------------------- number button making
button_1=Button(root,text=1,width=4,padx=20,pady=10)
button_2=Button(root,text=2,width=4,padx=20,pady=10)
button_3=Button(root,text=3,width=4,padx=20,pady=10)
button_4=Button(root,text=4,width=4,padx=20,pady=10)
button_5=Button(root,text=5,width=4,padx=20,pady=10)
button_6=Button(root,text=6,width=4,padx=20,pady=10)
button_7=Button(root,text=7,width=4,padx=20,pady=10)
button_8=Button(root,text=8,width=4,padx=20,pady=10)
button_9=Button(root,text=9,width=4,padx=20,pady=10)
button_0=Button(root,text=0,width=4,padx=20,pady=10)
#----------------------------------------------------------- +/-/'/'/*/clear button making
button_clear=Button(root,text="clear",width=4,padx=20,pady=10)
button_equal=Button(root,text="=",width=4,padx=20,pady=10)
button_plus=Button(root,text='+',width=4,padx=20,pady=10)
button_minus=Button(root,text='-',width=4,padx=20,pady=10)
button_divide=Button(root,text='/',width=4,padx=20,pady=10)
button_times=Button(root,text='*',width=4,padx=20,pady=10)
myentry_1.grid(row=0,column=0,columnspan=3,padx=5,pady=5)
#----------------------------------------------------------- number box griding
button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_0.grid(row=4,column=0)
#----------------------------------------------------------- clear/= box griding
button_clear.grid(row=4,column=1)
button_equal.grid(row=4,column=2)
#-----------------------------------------------------------  +/-/*/'/'/ box griding
button_plus.grid(row=1,column=3)
button_minus.grid(row=2,column=3)
button_times.grid(row=3,column=3)
button_divide.grid(row=4,column=3)
#----------------------------------------------------------- entry box griding
label_1.grid(row=0,column=3)
#----------------------------------------------------------- +/-/*/'/'//=/clear/ binding
button_clear.bind("<Button>",clear)
button_plus.bind("<Button>",plus)
button_minus.bind("<Button>",minus)
button_times.bind("<Button>",times)
button_divide.bind("<Button>",divide)
button_equal.bind("<Button>",equal)
#----------------------------------------------------------- number clicking binding
button_1.bind("<Button>",lambda x :buttom_click(1))
button_2.bind("<Button>",lambda x :buttom_click(2))
button_3.bind("<Button>",lambda x :buttom_click(3))
button_4.bind("<Button>",lambda x :buttom_click(4))
button_5.bind("<Button>",lambda x :buttom_click(5))
button_6.bind("<Button>",lambda x :buttom_click(6))
button_7.bind("<Button>",lambda x :buttom_click(7))
button_8.bind("<Button>",lambda x :buttom_click(8))
button_9.bind("<Button>",lambda x :buttom_click(9))
button_0.bind("<Button>",lambda x :buttom_click(0))
#----------------------------------------------------------- optional functions
button_0.bind("<Enter>",func0)
button_0.bind("<Leave>",func00)
button_1.bind("<Enter>",func1)
button_1.bind("<Leave>",func11)
button_2.bind("<Enter>",func2)
button_2.bind("<Leave>",func22)
button_3.bind("<Enter>",func3)
button_3.bind("<Leave>",func33)
button_4.bind("<Enter>",func4)
button_4.bind("<Leave>",func44)
button_5.bind("<Enter>",func5)
button_5.bind("<Leave>",func55)
button_6.bind("<Enter>",func6)
button_6.bind("<Leave>",func66)
button_7.bind("<Enter>",func7)
button_7.bind("<Leave>",func77)
button_8.bind("<Enter>",func8)
button_8.bind("<Leave>",func88)
button_9.bind("<Enter>",func9)
button_9.bind("<Leave>",func99)
#-----------------------------------------------------------
button_plus.bind("<Enter>",funcp)
button_plus.bind("<Leave>",funcp1)
button_minus.bind("<Enter>",funcm)
button_minus.bind("<Leave>",funcm1)
button_times.bind("<Enter>",funct)
button_times.bind("<Leave>",funct1)
button_divide.bind("<Enter>",funcd)
button_divide.bind("<Leave>",funcd1)
button_clear.bind("<Enter>",funcc)
button_clear.bind("<Leave>",funcc1)
button_equal.bind("<Enter>",funce)
button_equal.bind("<Leave>",funce1)
root.mainloop()
