from tkinter import *
#-----------------------------------------------------------------------
import os
os.system('cls')
#-----------------------------------------------------------------------
class Calculator:
    number1=0
    sign=""
    def __init__(self) -> None:
        self.main_window=Tk()
        self.main_window.title("Calculator (Ver1)")
        self.myentry_1=Entry(self.main_window,borderwidth=5,width=35)
        #----------------------------------------------------------- label main
        self.label_1=Label(self.main_window,text="cacio",fg="#000000",padx=10,pady=5)
        #----------------------------------------------------------- stick label main
        self.label_1.grid(row=0,column=3)
        #----------------------------------------------------------- buttons
        self.button_1=Button(self.main_window,text=1,width=4,padx=20,pady=10)
        self.button_2=Button(self.main_window,text=2,width=4,padx=20,pady=10)
        self.button_3=Button(self.main_window,text=3,width=4,padx=20,pady=10)
        self.button_4=Button(self.main_window,text=4,width=4,padx=20,pady=10)
        self.button_5=Button(self.main_window,text=5,width=4,padx=20,pady=10)
        self.button_6=Button(self.main_window,text=6,width=4,padx=20,pady=10)
        self.button_7=Button(self.main_window,text=7,width=4,padx=20,pady=10)
        self.button_8=Button(self.main_window,text=8,width=4,padx=20,pady=10)
        self.button_9=Button(self.main_window,text=9,width=4,padx=20,pady=10)
        self.button_0=Button(self.main_window,text=0,width=4,padx=20,pady=10)
        #----------------------------------------------------------- stick buttons1
        self.button_1.grid(row=1,column=0)
        self.button_2.grid(row=1,column=1)
        self.button_3.grid(row=1,column=2)
        self.button_4.grid(row=2,column=0)
        self.button_5.grid(row=2,column=1)
        self.button_6.grid(row=2,column=2)
        self.button_7.grid(row=3,column=0)
        self.button_8.grid(row=3,column=1)
        self.button_9.grid(row=3,column=2)
        self.button_0.grid(row=4,column=0)
        #----------------------------------------------------------- buttons (clear = + - * /)
        self.button_clear=Button(self.main_window,text="clear",width=4,padx=20,pady=10)
        self.button_equal=Button(self.main_window,text="=",width=4,padx=20,pady=10)
        self.button_plus=Button(self.main_window,text='+',width=4,padx=20,pady=10)
        self.button_minus=Button(self.main_window,text='-',width=4,padx=20,pady=10)
        self.button_divide=Button(self.main_window,text='/',width=4,padx=20,pady=10)
        self.button_times=Button(self.main_window,text='*',width=4,padx=20,pady=10)
        self.myentry_1.grid(row=0,column=0,columnspan=3,padx=5,pady=5)
        #----------------------------------------------------------- stick buttons2
        self.button_clear.grid(row=4,column=1)
        self.button_equal.grid(row=4,column=2)
        self.button_plus.grid(row=1,column=3)
        self.button_minus.grid(row=2,column=3)
        self.button_times.grid(row=3,column=3)
        self.button_divide.grid(row=4,column=3)
        #----------------------------------------------------------- bind functions numbers
        (self.button_1).bind("<Button>",self.buttom_click1)
        (self.button_2).bind("<Button>",self.buttom_click2)
        (self.button_3).bind("<Button>",self.buttom_click3)
        (self.button_4).bind("<Button>",self.buttom_click4)
        (self.button_5).bind("<Button>",self.buttom_click5)
        (self.button_6).bind("<Button>",self.buttom_click6)
        (self.button_7).bind("<Button>",self.buttom_click7)
        (self.button_8).bind("<Button>",self.buttom_click8)
        (self.button_9).bind("<Button>",self.buttom_click9)
        (self.button_0).bind("<Button>",self.buttom_click0)
        #----------------------------------------------------------- bind functions animations (enter leave)
        self.button_0.bind("<Enter>",self.func0)
        self.button_0.bind("<Leave>",self.func00)
        self.button_1.bind("<Enter>",self.func1)
        self.button_1.bind("<Leave>",self.func11)
        self.button_2.bind("<Enter>",self.func2)
        self.button_2.bind("<Leave>",self.func22)
        self.button_3.bind("<Enter>",self.func3)
        self.button_3.bind("<Leave>",self.func33)
        self.button_4.bind("<Enter>",self.func4)
        self.button_4.bind("<Leave>",self.func44)
        self.button_5.bind("<Enter>",self.func5)
        self.button_5.bind("<Leave>",self.func55)
        self.button_6.bind("<Enter>",self.func6)
        self.button_6.bind("<Leave>",self.func66)
        self.button_7.bind("<Enter>",self.func7)
        self.button_7.bind("<Leave>",self.func77)
        self.button_8.bind("<Enter>",self.func8)
        self.button_8.bind("<Leave>",self.func88)
        self.button_9.bind("<Enter>",self.func9)
        self.button_9.bind("<Leave>",self.func99)

        self.button_plus.bind("<Enter>",self.funcp)
        self.button_plus.bind("<Leave>",self.funcp1)
        self.button_minus.bind("<Enter>",self.funcm)
        self.button_minus.bind("<Leave>",self.funcm1)
        self.button_times.bind("<Enter>",self.funct)
        self.button_times.bind("<Leave>",self.funct1)
        self.button_divide.bind("<Enter>",self.funcd)
        self.button_divide.bind("<Leave>",self.funcd1)
        self.button_clear.bind("<Enter>",self.funcc)
        self.button_clear.bind("<Leave>",self.funcc1)
        self.button_equal.bind("<Enter>",self.funce)
        self.button_equal.bind("<Leave>",self.funce1)
        #----------------------------------------------------------- bind functions (clear + - * / =)
        self.button_plus.bind("<Button>",self.plus)
        self.button_minus.bind("<Button>",self.minus)
        self.button_times.bind("<Button>",self.times)
        self.button_divide.bind("<Button>",self.divide)
        self.button_equal.bind("<Button>",self.equal)
        self.button_clear.bind("<Button>",self.clear)
        #-----------------------------------------------------------
        self.main_window.mainloop()
    #----------------------------------------------------------- functions (clear + - * / =)
    def buttom_click1(self,event):
        current_number=self.myentry_1.get()
        self.myentry_1.delete(0,END)
        self.myentry_1.insert(0,str(current_number)+str(1))
    def buttom_click2(self,event):
        current_number=self.myentry_1.get()
        self.myentry_1.delete(0,END)
        self.myentry_1.insert(0,str(current_number)+str(2))
    def buttom_click3(self,event):
        current_number=self.myentry_1.get()
        self.myentry_1.delete(0,END)
        self.myentry_1.insert(0,str(current_number)+str(3))
    def buttom_click4(self,event):
        current_number=self.myentry_1.get()
        self.myentry_1.delete(0,END)
        self.myentry_1.insert(0,str(current_number)+str(4))
    def buttom_click5(self,event):
        current_number=self.myentry_1.get()
        self.myentry_1.delete(0,END)
        self.myentry_1.insert(0,str(current_number)+str(5))
    def buttom_click6(self,event):
        current_number=self.myentry_1.get()
        self.myentry_1.delete(0,END)
        self.myentry_1.insert(0,str(current_number)+str(6))
    def buttom_click7(self,event):
        current_number=self.myentry_1.get()
        self.myentry_1.delete(0,END)
        self.myentry_1.insert(0,str(current_number)+str(7))
    def buttom_click8(self,event):
        current_number=self.myentry_1.get()
        self.myentry_1.delete(0,END)
        self.myentry_1.insert(0,str(current_number)+str(8))
    def buttom_click9(self,event):
        current_number=self.myentry_1.get()
        self.myentry_1.delete(0,END)
        self.myentry_1.insert(0,str(current_number)+str(9))
    def buttom_click0(self,event):
        current_number=self.myentry_1.get()
        self.myentry_1.delete(0,END)
        self.myentry_1.insert(0,str(current_number)+str(0))
    #----------------------------------------------------------- functions aimations (enter leave)
    def func0(self,event):
        self.button_0.config(bg="#F18F01",fg="#ffffff")
    def func00(self,event):
        self.button_0.config(bg="#f0f0f0",fg="#000000")
    def func1(self,event):
        self.button_1.config(bg="#F18F01",fg="#ffffff")
    def func11(self,event):
        self.button_1.config(bg="#f0f0f0",fg="#000000")
    def func2(self,event):
        self.button_2.config(bg="#F18F01",fg="#ffffff")
    def func22(self,event):
        self.button_2.config(bg="#f0f0f0",fg="#000000")
    def func3(self,event):
        self.button_3.config(bg="#F18F01",fg="#ffffff")
    def func33(self,event):
        self.button_3.config(bg="#f0f0f0",fg="#000000")
    def func4(self,event):
        self.button_4.config(bg="#F18F01",fg="#ffffff")
    def func44(self,event):
        self.button_4.config(bg="#f0f0f0",fg="#000000")
    def func5(self,event):
        self.button_5.config(bg="#F18F01",fg="#ffffff")
    def func55(self,event):
        self.button_5.config(bg="#f0f0f0",fg="#000000")
    def func6(self,event):
        self.button_6.config(bg="#F18F01",fg="#ffffff")
    def func66(self,event):
        self.button_6.config(bg="#f0f0f0",fg="#000000")
    def func7(self,event):
        self.button_7.config(bg="#F18F01",fg="#ffffff")
    def func77(self,event):
        self.button_7.config(bg="#f0f0f0",fg="#000000")
    def func8(self,event):
        self.button_8.config(bg="#F18F01",fg="#ffffff")
    def func88(self,event):
        self.button_8.config(bg="#f0f0f0",fg="#000000")
    def func9(self,event):
        self.button_9.config(bg="#F18F01",fg="#000000")
    def func99(self,event):
        self.button_9.config(bg="#f0f0f0",fg="#000000")
    #-----------------------------------------------------------
    def funcp(self,event):
        self.button_plus.config(bg="#F18F01",fg="#000000")
    def funcp1(self,event):
        self.button_plus.config(bg="#f0f0f0",fg="#000000")
    def funcm(self,event):
        self.button_minus.config(bg="#F18F01",fg="#000000")
    def funcm1(self,event):
        self.button_minus.config(bg="#f0f0f0",fg="#000000")
    def funct(self,event):
        self.button_times.config(bg="#F18F01",fg="#000000")
    def funct1(self,event):
        self.button_times.config(bg="#f0f0f0",fg="#000000")
    def funcd(self,event):
        self.button_divide.config(bg="#F18F01",fg="#000000")
    def funcd1(self,event):
        self.button_divide.config(bg="#f0f0f0",fg="#000000")
    def funce(self,event):
        self.button_equal.config(bg="#F18F01",fg="#000000")
    def funce1(self,event):
        self.button_equal.config(bg="#f0f0f0",fg="#000000")
    def funcc(self,event):
        self.button_clear.config(bg="#F18F01",fg="#000000")
    def funcc1(self,event):
        self.button_clear.config(bg="#f0f0f0",fg="#000000")
    #----------------------------------------------------------- functions (clear + - * / = )
    def plus(self,event):
        self.label_1.config(text="plus")
        try:
            first_number=float(self.myentry_1.get())
        except ValueError:
            first_number=self.myentry_1.get()
        Calculator.number1=first_number
        Calculator.sign="plus"
        self.myentry_1.delete(0,END)
    def minus(self,event):
        self.label_1.config(text="minus")
        try:
            first_number=float(self.myentry_1.get())
        except ValueError:
            first_number=self.myentry_1.get()
        Calculator.number1=first_number
        Calculator.sign="minus"
        self.myentry_1.delete(0,END)
    def times(self,event):
        self.label_1.config(text="times")
        try:
            first_number=float(self.myentry_1.get())
        except ValueError:
            first_number=self.myentry_1.get()
        Calculator.number1=first_number
        Calculator.sign="times"
        self.myentry_1.delete(0,END)
    def divide(self,event):
        self.label_1.config(text="divide")
        try:
            first_number=float(self.myentry_1.get())
        except ValueError:
            first_number=self.myentry_1.get()
        Calculator.number1=first_number
        Calculator.sign="divide"
        self.myentry_1.delete(0,END)
    def equal(self,event):
        self.label_1.config(text="equal")
        secend_number=self.myentry_1.get()
        self.myentry_1.delete(0,END)
        if Calculator.sign=="plus":
            try:
                if int(secend_number) and Calculator.number1=='infinite ...':
                    res='infinite ...'
                elif int(secend_number) and Calculator.number1=='impossible ...':
                    res='impossible ...'
                else:
                    res=Calculator.number1+float(secend_number)
            except TypeError:
                res='impossible ...'
            self.myentry_1.insert(0,res)
        elif Calculator.sign=="minus":
            try:
                if int(secend_number) and Calculator.number1=='infinite ...':
                    res='infinite ...'
                elif int(secend_number) and Calculator.number1=='impossible ...':
                    res='impossible ...'
                else:
                    res=Calculator.number1-float(secend_number)
            except TypeError:
                res='impossible ...'
            self.myentry_1.insert(0,res)
        elif Calculator.sign=="times":
            try:
                if int(secend_number)==0 and Calculator.number1=='infinite ...':
                    res=0
                elif int(secend_number) and Calculator.number1=='infinite ...':
                    res='infinite ...'
                elif int(secend_number) and Calculator.number1=='impossible ...':
                    res='impossible ...'
                else:
                    res=Calculator.number1*float(secend_number)
            except TypeError:
                res='impossible ...'
            self.myentry_1.insert(0,res)
        else:
            try:
                res=Calculator.number1/float(secend_number)
            except ZeroDivisionError:
                res='infinite ...'
            except ValueError:
                res='impossible ...'
            except TypeError:
                res='impossible ...'
            self.myentry_1.insert(0,res)
        Calculator.sign=""
    def clear(self,event):  
        self.label_1.config(text="clear")
        self.myentry_1.delete(0,END)
    #----------------------------------------------------------- function (enter leave)
    def func0(self,event):
        self.button_0.config(bg="#F18F01",fg="#ffffff")
    def func00(self,event):
        self.button_0.config(bg="#f0f0f0",fg="#000000")
    def func1(self,event):
        self.button_1.config(bg="#F18F01",fg="#ffffff")
    def func11(self,event):
        self.button_1.config(bg="#f0f0f0",fg="#000000")
    def func2(self,event):
        self.button_2.config(bg="#F18F01",fg="#ffffff")
    def func22(self,event):
        self.button_2.config(bg="#f0f0f0",fg="#000000")
    def func3(self,event):
        self.button_3.config(bg="#F18F01",fg="#ffffff")
    def func33(self,event):
        self.button_3.config(bg="#f0f0f0",fg="#000000")
    def func4(self,event):
        self.button_4.config(bg="#F18F01",fg="#ffffff")
    def func44(self,event):
        self.button_4.config(bg="#f0f0f0",fg="#000000")
    def func5(self,event):
        self.button_5.config(bg="#F18F01",fg="#ffffff")
    def func55(self,event):
        self.button_5.config(bg="#f0f0f0",fg="#000000")
    def func6(self,event):
        self.button_6.config(bg="#F18F01",fg="#ffffff")
    def func66(self,event):
        self.button_6.config(bg="#f0f0f0",fg="#000000")
    def func7(self,event):
        self.button_7.config(bg="#F18F01",fg="#ffffff")
    def func77(self,event):
        self.button_7.config(bg="#f0f0f0",fg="#000000")
    def func8(self,event):
        self.button_8.config(bg="#F18F01",fg="#ffffff")
    def func88(self,event):
        self.button_8.config(bg="#f0f0f0",fg="#000000")
    def func9(self,event):
        self.button_9.config(bg="#F18F01",fg="#000000")
    def func99(self,event):
        self.button_9.config(bg="#f0f0f0",fg="#000000")
    #----------------------------------------------------------- + / - / * / "/" / clear / equal    enter & leave ravadid
    def funcp(self,event):
        self.button_plus.config(bg="#F18F01",fg="#000000")
    def funcp1(self,event):
        self.button_plus.config(bg="#f0f0f0",fg="#000000")
    def funcm(self,event):
        self.button_minus.config(bg="#F18F01",fg="#000000")
    def funcm1(self,event):
        self.button_minus.config(bg="#f0f0f0",fg="#000000")
    def funct(self,event):
        self.button_times.config(bg="#F18F01",fg="#000000")
    def funct1(self,event):
        self.button_times.config(bg="#f0f0f0",fg="#000000")
    def funcd(self,event):
        self.button_divide.config(bg="#F18F01",fg="#000000")
    def funcd1(self,event):
        self.button_divide.config(bg="#f0f0f0",fg="#000000")
    def funce(self,event):
        self.button_equal.config(bg="#F18F01",fg="#000000")
    def funce1(self,event):
        self.button_equal.config(bg="#f0f0f0",fg="#000000")
    def funcc(self,event):
        self.button_clear.config(bg="#F18F01",fg="#000000")
    def funcc1(self,event):
        self.button_clear.config(bg="#f0f0f0",fg="#000000")
#-----------------------------------------------------------
cal=Calculator()