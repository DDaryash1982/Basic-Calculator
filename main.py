
import tkinter as tk
import heapq as heap
import numpy as np
import scipy as sp
import pandas as pd
from scipy import stats
import math
import tkinter.messagebox
from tkinter.constants import SUNKEN
import sys
sys.set_int_max_str_digits(10000000)
import statistics

LARGEFONT = ("Verdana", 20)

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self,bg='grey')
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(20, weight=1)
        container.grid_columnconfigure(20, weight=1)
        self.frames = {}
        for F in (BasicCalculator, OperatingSystem, StatsCalculatorUG, UnitConverter, AreaVolume):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(BasicCalculator)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class BasicCalculator(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='black')
        frame = tk.Frame(bg="black")
        label = tk.Label(self, text="Basic Calculator",bg='black',fg='red', font=LARGEFONT)
        label.grid(row=2, column=3)

        entry = tk.Entry(self, borderwidth=5, width=50)
        entry.grid(row=4, column=3)
        maindisp = tk.Entry(self, borderwidth=5, width=50,bg='black',fg='white')
        maindisp.grid(row=4, column=3)

        def myclick(number):
                entry.insert(tk.END, number)
                maindisp.insert(tk.END, number)

        def sqrt():
            entry.insert(tk.END, "math.sqrt(")
            maindisp.insert(tk.END, "√(")

        def cbrt():
            entry.insert(tk.END, "math.cbrt(")
            maindisp.insert(tk.END, "∛(")

        def equal():
                y = str(eval(entry.get()))
                clear()
                entry.insert(0, y)
                maindisp.insert(0, y)

        def clear():
            entry.delete(0, tk.END)
            maindisp.delete(0, tk.END)

        def backspace():
            y = (entry.get()[:-1])
            z = (maindisp.get()[:-1])
            clear()
            entry.insert(0, y)
            maindisp.insert(0, z)

        def percentage():
            y = str(entry.get())
            clear()
            alpha = ""
            num = ""
            special = ""
            c = 0
            for i in range(len(y)):
                if y[i].isdigit() and c == 0:
                    num = num + y[i]
                elif y[i].isdigit() and c == 1:
                    alpha = alpha + y[i]
                else:
                    special += y[i]
                    c = 1
            if special == "*" or special == "/":
                num = float(num)
                c = float(alpha)/100
                y = str(num) + special + str(c)
                entry.insert(0, str(y))
                maindisp.insert(0, str(y))

            else:
                num = float(num)
                c = num * float(alpha) / 100
                y = str(num) + special + str(c)
                entry.insert(0, str(y))
                maindisp.insert(0, str(y))

        def neg():
            y = str(-(float(entry.get())))
            clear()
            entry.insert(0, y)
            maindisp.insert(0, y)

        def mod():
            y = float(entry.get())
            if y < 0:
                y *= -1
            clear()
            y=str(y)
            entry.insert(0, y)
            maindisp.insert(0, y)

        def sin():
            entry.insert(tk.END, "np.sin(")
            maindisp.insert(tk.END, "sin(")

        def cos():
            y = (entry.get())
            clear()
            entry.insert(tk.END, "np.cos(")
            maindisp.insert(tk.END, "cos(")

        def tan():
            y = (entry.get())
            clear()
            entry.insert(tk.END, "np.tan(")
            maindisp.insert(tk.END, "tan(")

        def sini():
            y = (entry.get())
            clear()
            entry.insert(tk.END, "np.arcsin(")
            maindisp.insert(tk.END, "asin(")

        def cosi():
            y = (entry.get())
            clear()
            entry.insert(tk.END, "np.arccos(")
            maindisp.insert(tk.END, "acos(")

        def tani():
            y = (entry.get())
            clear()
            entry.insert(tk.END, "np.arctan(")
            maindisp.insert(tk.END, "atan(")

        def sind():
            entry.insert(tk.END, "np.sin(np.rad2deg(")
            maindisp.insert(tk.END, "sin((")

        def cosd():
            entry.insert(tk.END, "np.cos(np.deg2rad(")
            maindisp.insert(tk.END, "cos((")

        def tand():
            entry.insert(tk.END, "np.tan(np.deg2rad(")
            maindisp.insert(tk.END, "tan((")

        def sinid():
            entry.insert(tk.END, "np.arcsin(np.deg2rad(")
            maindisp.insert(tk.END, "asin((")

        def cosid():
            entry.insert(tk.END, "np.arccos(np.deg2rad(")
            maindisp.insert(tk.END, "acos((")

        def tanid():
            entry.insert(tk.END, "np.arctan(np.deg2rad(")
            maindisp.insert(tk.END, "atan((")

        def power():
            y = int(entry.get())
            entry.insert(tk.END,"**")
            maindisp.insert(tk.END,"^")

        def F(n):
            return 1 if (n==1 or n==0) else n * F(n - 1)

        def factorial():
            y = (entry.get())
            z=0
            x=""
            for i in y[::-1]:
                if i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9":
                    z+=1
                    x+=i
                else:
                    break
            for i in range(z):
                backspace()
            z=x
            x=""
            for i in z[::-1]:
                x+=i
            x=int(x)
            y=F(x)
            entry.insert(tk.END, y)
            maindisp.insert(tk.END, x)
            maindisp.insert(tk.END, "!")

        def sq():
            entry.insert(tk.END,"**2")
            maindisp.insert(tk.END,"^2")

        def e():
            entry.insert(tk.END, "2.7182818285")
            maindisp.insert(tk.END, "2.7182818285")



        button_1 = tk.Button(self, text='1', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(1))
        button_1.grid(row=7, column=2)
        button_2 = tk.Button(self, text='2', padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=lambda: myclick(2))
        button_2.grid(row=7, column=3)
        button_3 = tk.Button(self, text='3', padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=lambda: myclick(3))
        button_3.grid(row=7, column=4)
        button_4 = tk.Button(self, text='4', padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=lambda: myclick(4))
        button_4.grid(row=8, column=2)
        button_5 = tk.Button(self, text='5', padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=lambda: myclick(5))
        button_5.grid(row=8, column=3)
        button_6 = tk.Button(self, text='6', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(6))
        button_6.grid(row=8, column=4)
        button_7 = tk.Button(self, text='7', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(7))
        button_7.grid(row=9, column=2)
        button_8 = tk.Button(self, text='8', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(8))
        button_8.grid(row=9, column=3)
        button_9 = tk.Button(self, text='9', padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=lambda: myclick(9))
        button_9.grid(row=9, column=4)
        button_0 = tk.Button(self, text='0', padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=lambda: myclick(0))
        button_0.grid(row=10, column=3)
        button_add = tk.Button(self, text="+", padx=15, pady=5, width=20, bg='black',fg='green', activebackground="red", command=lambda: myclick('+'))
        button_add.grid(row=11, column=2)
        button_clear = tk.Button(self, text="C", padx=15, pady=5, width=20, bg='black',fg='red', activebackground="red",command=clear)
        button_clear.grid(row=10, column=2)
        button_equal = tk.Button(self, text="=", padx=15, pady=5, width=20, bg='green',fg='white', activebackground="red",command=equal)
        button_equal.grid(row=10, column=4)
        button_subtract = tk.Button(self, text="-", padx=15, pady=5, width=20, bg='black',fg='green', activebackground="red",command=lambda: myclick('-'))
        button_subtract.grid(row=11, column=4)
        button_remainder = tk.Button(self, text="Remainder", padx=15, pady=5, width=20, bg='black',fg='green', activebackground="red",command=lambda: myclick('%'))
        button_remainder.grid(row=11, column=3)
        button_power = tk.Button(self, text="^", padx=15, pady=5, width=20, bg='black',fg='green', activebackground="red",command=power)
        button_power.grid(row=12, column=3)
        button_multiply = tk.Button(self, text="*", padx=15, pady=5, width=20, bg='black',fg='green', activebackground="red",command=lambda: myclick('*'))
        button_multiply.grid(row=12, column=4)
        button_div = tk.Button(self, text="/", padx=15, pady=5, width=20, bg='black',fg='green', activebackground="red",command=lambda: myclick('/'))
        button_div.grid(row=12, column=2)
        button_div = tk.Button(self, text="√", padx=15, pady=5, width=20, bg='black',fg='green', activebackground="red",command=sqrt)
        button_div.grid(row=13, column=3)
        button_o = tk.Button(self, text="(", padx=15, pady=5, width=20, bg='black',fg='green', activebackground="red",command=lambda: myclick('('))
        button_o.grid(row=13, column=2)
        button_c = tk.Button(self, text=")", padx=15, pady=5, width=20, bg='black',fg='green', activebackground="red",command=lambda: myclick(')'))
        button_c.grid(row=13, column=4)
        button_de = tk.Button(self, text=".", padx=15, pady=5, width=20, bg='black',fg='green', activebackground="red",command=lambda: myclick('.'))
        button_de.grid(row=14, column=2)
        button_cuberoot = tk.Button(self, text="∛", padx=15, pady=5, width=20, bg='black',fg='green', activebackground="red",command=cbrt)
        button_cuberoot.grid(row=14, column=3)
        button_Backspace = tk.Button(self, text="⌫", padx=15, pady=5, width=20, bg='green',fg='black', activebackground="red",command=backspace)
        button_Backspace.grid(row=14, column=4)
        button_percent = tk.Button(self, text="%", padx=15, pady=5, width=20, bg='black',fg='green', activebackground="red",command=percentage)
        button_percent.grid(row=15, column=2)
        button_nega = tk.Button(self, text="+/-", padx=15, pady=5, width=20, bg='black',fg='green', activebackground="red",command=neg)
        button_nega.grid(row=15, column=3)
        button_modulo = tk.Button(self, text="|x|", padx=15, pady=5, width=20, bg='black',fg='green', activebackground="red",command=mod)
        button_modulo.grid(row=15, column=4)
        button_sin = tk.Button(self, text="sin", padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=sin)
        button_sin.grid(row=16, column=2)
        button_cos = tk.Button(self, text="cos", padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=cos)
        button_cos.grid(row=16, column=3)
        button_tan = tk.Button(self, text="tan", padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=tan)
        button_tan.grid(row=16, column=4)
        button_sind = tk.Button(self, text="sin deg", padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=sind)
        button_sind.grid(row=17, column=2)
        button_cosd = tk.Button(self, text="cos deg", padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=cosd)
        button_cosd.grid(row=17, column=3)
        button_tand = tk.Button(self, text="tan deg", padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=tand)
        button_tand.grid(row=17, column=4)
        button_sini = tk.Button(self, text="sini", padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=sini)
        button_sini.grid(row=18, column=2)
        button_cosi = tk.Button(self, text="cosi", padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=cosi)
        button_cosi.grid(row=18, column=3)
        button_tani = tk.Button(self, text="tani", padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=tani)
        button_tani.grid(row=18, column=4)
        button_sinid = tk.Button(self, text="sini deg", padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=sinid)
        button_sinid.grid(row=19, column=2)
        button_cosid = tk.Button(self, text="cosi deg", padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=cosid)
        button_cosid.grid(row=19, column=3)
        button_tanid = tk.Button(self, text="tani deg", padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=tanid)
        button_tanid.grid(row=19, column=4)
        button_factorial = tk.Button(self, text="!", padx=15, pady=5, width=20, bg='black', fg='white',activebackground="red", command=factorial)
        button_factorial.grid(row=20, column=2)
        button_sq = tk.Button(self, text="x²", padx=15, pady=5, width=20, bg='black', fg='white', activebackground="red", command=sq)
        button_sq.grid(row=20, column=3)
        button_e = tk.Button(self, text="e", padx=15, pady=5, width=20, bg='black', fg='white', activebackground="red", command=e)
        button_e.grid(row=20, column=4)

        button1 = tk.Button(self, text="Operating System", bg='black',fg='green', activebackground="red",command=lambda: controller.show_frame(OperatingSystem))
        button1.grid(row=0, column=4)
        button2 = tk.Button(self, text="Ungrouped Data", bg='black',fg='green', activebackground="red",command=lambda: controller.show_frame(StatsCalculatorUG))
        button2.grid(row=0, column=6)
        button3 = tk.Button(self, text="Unit Converter", bg='black',fg='green', activebackground="red",command=lambda: controller.show_frame(UnitConverter))
        button3.grid(row=0, column=2)
        button4 = tk.Button(self, text="Area and Volume", bg='black',fg='green', activebackground="red",command=lambda: controller.show_frame(AreaVolume))
        button4.grid(row=0, column=0)
        frame.pack()


class OperatingSystem(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='black')
        label = tk.Label(self, text="Operating System",bg='black',fg='red', font=LARGEFONT)
        label.grid(row=2, column=3)

        button1 = tk.Button(self, text="Basic Calculator", bg='black',fg='green', activebackground="red",command=lambda: controller.show_frame(BasicCalculator))
        button1.grid(row=0, column=2)
        button2 = tk.Button(self, text="Unit Converter", bg='black',fg='green', activebackground="red",command=lambda: controller.show_frame(UnitConverter))
        button2.grid(row=0, column=4)
        button3 = tk.Button(self, text="Ungrouped Data", bg='black',fg='green', activebackground="red",command=lambda: controller.show_frame(StatsCalculatorUG))
        button3.grid(row=0, column=6)
        button4 = tk.Button(self, text="Area and Volume", bg='black',fg='green', activebackground="red",command=lambda: controller.show_frame(AreaVolume))
        button4.grid(row=0, column=0)

        entry = tk.Entry(self, borderwidth=5, width=50,bg='black',fg='white')
        entry.grid(row=4, column=3)
        maindisp = tk.Entry(self, borderwidth=5, width=50,bg='black',fg='white')
        maindisp.grid(row=4, column=3)

        def myclick(number):
            entry.insert(tk.END, number)
            maindisp.insert(tk.END, number)

        def equal():
            y = str(eval(entry.get()))
            clear()
            entry.insert(0, y)
            maindisp.insert(0, y)

        def clear():
            entry.delete(0, tk.END)
            maindisp.delete(0, tk.END)

        def backspace():
            y = (entry.get()[:-1])
            z = (maindisp.get()[:-1])
            clear()
            entry.insert(0, y)
            maindisp.insert(0, z)

        button_1 = tk.Button(self, text='1', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(1))
        button_1.grid(row=7, column=2)
        button_2 = tk.Button(self, text='2', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(2))
        button_2.grid(row=7, column=3)
        button_3 = tk.Button(self, text='3', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(3))
        button_3.grid(row=7, column=4)
        button_4 = tk.Button(self, text='4', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(4))
        button_4.grid(row=8, column=2)
        button_5 = tk.Button(self, text='5', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(5))
        button_5.grid(row=8, column=3)
        button_6 = tk.Button(self, text='6', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(6))
        button_6.grid(row=8, column=4)
        button_7 = tk.Button(self, text='7', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(7))
        button_7.grid(row=9, column=2)
        button_8 = tk.Button(self, text='8', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(8))
        button_8.grid(row=9, column=3)
        button_9 = tk.Button(self, text='9', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(9))
        button_9.grid(row=9, column=4)
        button_0 = tk.Button(self, text='0', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(0))
        button_0.grid(row=10, column=3)
        button_clear = tk.Button(self, text="Clear", padx=15, pady=5, width=20, bg='black',fg='red', activebackground="red",command=clear)
        button_clear.grid(row=10, column=2)
        button_equal = tk.Button(self, text="=", padx=15, pady=5, width=20, bg='green',fg='white', activebackground="red",command=equal)
        button_equal.grid(row=10, column=4)
        button_Backspace = tk.Button(self, text="Backspace ", padx=15, pady=5, width=20, bg='black',fg='green', activebackground="red",command=backspace)
        button_Backspace.grid(row=14, column=4)

class AreaVolume(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='black')
        label = tk.Label(self, text="Area and Volume",bg='black',fg='red', font=LARGEFONT)
        label.grid(row=2, column=3)

        entry = tk.Entry(self, borderwidth=5, width=50,bg='black',fg='white')
        entry.grid(row=4, column=3)
        maindisp = tk.Entry(self, borderwidth=5, width=50,bg='black',fg='white')
        maindisp.grid(row=4, column=3)

        button1 = tk.Button(self, text="Basic Calculator", bg='black',fg='green', activebackground="red",command=lambda: controller.show_frame(BasicCalculator))
        button1.grid(row=0, column=0)
        button2 = tk.Button(self, text="Grouped Data", bg='black',fg='green', activebackground="red",command=lambda: controller.show_frame(UnitConverter))
        button2.grid(row=0, column=2)
        button3 = tk.Button(self, text="Ungrouped Data", bg='black',fg='green', activebackground="red",command=lambda: controller.show_frame(StatsCalculatorUG))
        button3.grid(row=0, column=6)
        button4 = tk.Button(self, text="Operating System", bg='black',fg='green', activebackground="red",command=lambda: controller.show_frame(OperatingSystem))
        button4.grid(row=0, column=4)

        def myclick(number):
            entry.insert(tk.END, number)
            maindisp.insert(tk.END, number)

        def equal():
            y = str(eval(entry.get()))
            clear()
            entry.insert(0, y)
            maindisp.insert(0, y)

        def clear():
            entry.delete(0, tk.END)
            maindisp.delete(0, tk.END)

        def backspace():
            y = (entry.get()[:-1])
            z = (maindisp.get()[:-1])
            clear()
            entry.insert(0, y)
            maindisp.insert(0, z)


        button_1 = tk.Button(self, text='1', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(1))
        button_1.grid(row=7, column=2)
        button_2 = tk.Button(self, text='2', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(2))
        button_2.grid(row=7, column=3)
        button_3 = tk.Button(self, text='3', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(3))
        button_3.grid(row=7, column=4)
        button_4 = tk.Button(self, text='4', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(4))
        button_4.grid(row=8, column=2)
        button_5 = tk.Button(self, text='5', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(5))
        button_5.grid(row=8, column=3)
        button_6 = tk.Button(self, text='6', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(6))
        button_6.grid(row=8, column=4)
        button_7 = tk.Button(self, text='7', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(7))
        button_7.grid(row=9, column=2)
        button_8 = tk.Button(self, text='8', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(8))
        button_8.grid(row=9, column=3)
        button_9 = tk.Button(self, text='9', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(9))
        button_9.grid(row=9, column=4)
        button_0 = tk.Button(self, text='0', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(0))
        button_0.grid(row=10, column=3)
        button_clear = tk.Button(self, text="Clear", padx=15, pady=5, width=20, bg='black',fg='red', activebackground="red",command=clear)
        button_clear.grid(row=10, column=2)
        button_equal = tk.Button(self, text="=", padx=15, pady=5, width=20, bg='green',fg='white', activebackground="red",command=equal)
        button_equal.grid(row=10, column=4)
        button_Backspace = tk.Button(self, text="Backspace ", padx=15, pady=5, width=20, bg='black',fg='green', activebackground="red",command=backspace)
        button_Backspace.grid(row=14, column=3)
        label = tk.Label(self, text="Area",bg='black',fg='red')
        label.grid(row=14, column=2)
        label = tk.Label(self, text="Volume",bg='black',fg='red')
        label.grid(row=14, column=4)
        button_Circle = tk.Button(self, text="Circle", padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=backspace)
        button_Circle.grid(row=15, column=2)
        button_Square = tk.Button(self, text="Square", padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=backspace)
        button_Square.grid(row=16, column=2)
        button_Rectangle = tk.Button(self, text="Rectangle", padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=backspace)
        button_Rectangle.grid(row=17, column=2)
        button_Triangle = tk.Button(self, text="Triangle ", padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=backspace)
        button_Triangle.grid(row=18, column=2)


class StatsCalculatorUG(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='black')
        label = tk.Label(self, text="Ungrouped Data",bg='black',fg='red', font=LARGEFONT)
        label.grid(row=2, column=3)

        button1 = tk.Button(self, text="Basic Calculator", bg='black',fg='green', activebackground="red",command=lambda: controller.show_frame(BasicCalculator))
        button1.grid(row=0, column=2)
        button2 = tk.Button(self, text="Operating System", bg='black',fg='green', activebackground="red",command=lambda: controller.show_frame(OperatingSystem))
        button2.grid(row=0, column=6)
        button2 = tk.Button(self, text="Unit Converter", bg='black',fg='green', activebackground="red",command=lambda: controller.show_frame(UnitConverter))
        button2.grid(row=0, column=4)
        button4 = tk.Button(self, text="Area and Volume", bg='black',fg='green', activebackground="red",command=lambda: controller.show_frame(AreaVolume))
        button4.grid(row=0, column=0)

        entry = tk.Entry(self, borderwidth=5, width=50,bg='black',fg='white')
        entry.grid(row=4, column=3)
        maindisp = tk.Entry(self, borderwidth=5, width=50,bg='black',fg='white')
        maindisp.grid(row=4, column=3)

        def myclick(number):
            entry.insert(tk.END, number)
            maindisp.insert(tk.END, number)

        def equal():
            y = str(eval(entry.get()))
            clear()
            entry.insert(0, y)
            maindisp.insert(0, y)

        def clear():
            entry.delete(0, tk.END)
            maindisp.delete(0, tk.END)

        def backspace():
            y = (entry.get()[:-1])
            z = (maindisp.get()[:-1])
            clear()
            entry.insert(0, y)
            maindisp.insert(0, z)

        def mean():
            entry.insert(tk.END, "np.mean([")
            maindisp.insert(tk.END, "mean([")

        def median():
            entry.insert(tk.END, "np.median([")
            maindisp.insert(tk.END, "median([")

        def mode():
            entry.insert(tk.END, "statistics.mode([")
            maindisp.insert(tk.END, "mode([")

        def std():
            entry.insert(tk.END, "np.std([")
            maindisp.insert(tk.END, "std([")

        def var():
            entry.insert(tk.END, "np.var([")
            maindisp.insert(tk.END, "var([")

        def gmean():
            entry.insert(tk.END, "stats.gmean([")
            maindisp.insert(tk.END, "gmean([")

        def hmean():
            entry.insert(tk.END, "statistics.harmonic_mean([")
            maindisp.insert(tk.END, "hmean([")

        def skew():
            entry.insert(tk.END, "stats.skew([")
            maindisp.insert(tk.END, "skew([")

        def kurto():
            entry.insert(tk.END, "stats.kurtosis([")
            maindisp.insert(tk.END, "kurtosis([")

        def core():
            entry.insert(tk.END, "np.correlate([ ")
            maindisp.insert(tk.END, "correlation([")

        def mh():
            entry.insert(tk.END, "statistics.median_high([")
            maindisp.insert(tk.END, "median high([")

        def ml():
            entry.insert(tk.END, "statistics.median_low([")
            maindisp.insert(tk.END, "median low([")

        def dec():
            entry.insert(tk.END, "([")
            maindisp.insert(tk.END, "decile([")

        def quar():
            entry.insert(tk.END, "np.quantile([ ")
            maindisp.insert(tk.END, "quartile([")

        def per():
            entry.insert(tk.END, "np.percentile([")
            maindisp.insert(tk.END, "percentile([")


        button_1 = tk.Button(self, text='1', padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=lambda: myclick(1))
        button_1.grid(row=7, column=2)
        button_2 = tk.Button(self, text='2', padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=lambda: myclick(2))
        button_2.grid(row=7, column=3)
        button_3 = tk.Button(self, text='3', padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=lambda: myclick(3))
        button_3.grid(row=7, column=4)
        button_4 = tk.Button(self, text='4', padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=lambda: myclick(4))
        button_4.grid(row=8, column=2)
        button_5 = tk.Button(self, text='5', padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=lambda: myclick(5))
        button_5.grid(row=8, column=3)
        button_6 = tk.Button(self, text='6', padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=lambda: myclick(6))
        button_6.grid(row=8, column=4)
        button_7 = tk.Button(self, text='7', padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=lambda: myclick(7))
        button_7.grid(row=9, column=2)
        button_8 = tk.Button(self, text='8', padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=lambda: myclick(8))
        button_8.grid(row=9, column=3)
        button_9 = tk.Button(self, text='9', padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=lambda: myclick(9))
        button_9.grid(row=9, column=4)
        button_0 = tk.Button(self, text='0', padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=lambda: myclick(0))
        button_0.grid(row=10, column=3)
        button_a = tk.Button(self, text=',', padx=15, pady=5, width=20,bg='black',fg='green', activebackground="red", command=lambda: myclick(','))
        button_a.grid(row=11, column=3)
        button_mean = tk.Button(self, text='Mean', padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=mean)
        button_mean.grid(row=14, column=3)
        button_median = tk.Button(self, text='Median', padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=median)
        button_median.grid(row=16, column=3)
        button_mode = tk.Button(self, text='Mode', padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=mode)
        button_mode.grid(row=13, column=3)
        button_sd = tk.Button(self, text='Standard Deviation', padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=std)
        button_sd.grid(row=13, column=2)
        button_var = tk.Button(self, text='Variance', padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=var)
        button_var.grid(row=13, column=4)
        button_o = tk.Button(self, text="(", padx=15, pady=5, width=20,bg='black',fg='green', activebackground="red", command=lambda: myclick('('))
        button_o.grid(row=11, column=2)
        button_c = tk.Button(self, text=")", padx=15, pady=5, width=20,bg='black',fg='green', activebackground="red", command=lambda: myclick(')'))
        button_c.grid(row=11, column=4)
        button_equal = tk.Button(self, text="=", padx=15, pady=5, width=20,bg='green',fg='white', activebackground="red", command=equal)
        button_equal.grid(row=10, column=4)
        button_clear = tk.Button(self, text="Clear", padx=15, pady=5, width=20,bg='black',fg='red', activebackground="red", command=clear)
        button_clear.grid(row=10, column=2)
        button_bo = tk.Button(self, text="[", padx=15, pady=5, width=20,bg='black',fg='green', activebackground="red", command=lambda: myclick('['))
        button_bo.grid(row=12, column=2)
        button_bc = tk.Button(self, text="]", padx=15, pady=5, width=20,bg='black',fg='green', activebackground="red", command=lambda: myclick(']'))
        button_bc.grid(row=12, column=4)
        button_geometric = tk.Button(self, text="Geometric Mean", padx=15,bg='black',fg='white', activebackground="red", pady=5, width=20, command=gmean)
        button_geometric.grid(row=14, column=4)
        button_harmonicmean = tk.Button(self, text="Harmonic Mean", padx=15,bg='black',fg='white', activebackground="red", pady=5, width=20, command=hmean)
        button_harmonicmean.grid(row=14, column=2)
        button_skewness = tk.Button(self, text="Skewness", padx=15, pady=5,bg='black',fg='white', activebackground="red", width=20, command=skew)
        button_skewness.grid(row=15, column=2)
        button_kurtosis = tk.Button(self, text="Kurtosis", padx=15, pady=5,bg='black',fg='white', activebackground="red", width=20, command=kurto)
        button_kurtosis.grid(row=15, column=3)
        button_correlation = tk.Button(self, text="Correlation", padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=core)
        button_correlation.grid(row=15, column=4)
        button_median_high = tk.Button(self, text="Median_High", padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=mh)
        button_median_high.grid(row=16, column=2)
        button_median_low = tk.Button(self, text="Median_Low", padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=ml)
        button_median_low.grid(row=16, column=4)
        button_deciles = tk.Button(self, text="Decile na", padx=15, pady=5, width=20,bg='black',fg='red', activebackground="red", command=dec)
        button_deciles.grid(row=17, column=3)
        button_quartiles = tk.Button(self, text="Quartile", padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=quar)
        button_quartiles.grid(row=17, column=2)
        button_percentile = tk.Button(self, text="Percentile", padx=15, pady=5, width=20,bg='black',fg='white', activebackground="red", command=per)
        button_percentile.grid(row=17, column=4)
        button_de = tk.Button(self, text=".", padx=15, pady=5, width=20,bg='black',fg='green', activebackground="red", command=lambda: myclick('.'))
        button_de.grid(row=12, column=3)
        button_Backspace = tk.Button(self, text="Backspace ", padx=15, pady=5, width=20,bg='black',fg='green', activebackground="red", command=backspace)
        button_Backspace.grid(row=18, column=2)


class UnitConverter(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='black')
        label = tk.Label(self, text="Grouped Data",bg='black',fg='red', font=LARGEFONT)
        label.grid(row=2, column=3)

        button1 = tk.Button(self, text="Basic Calculator", bg='black',fg='green', activebackground="red",command=lambda: controller.show_frame(BasicCalculator))
        button1.grid(row=0, column=2)
        button2 = tk.Button(self, text="Operating System",bg='black',fg='green', activebackground="red", command=lambda: controller.show_frame(OperatingSystem))
        button2.grid(row=0, column=4)
        button3 = tk.Button(self, text="Ungrouped Data", bg='black',fg='green', activebackground="red",command=lambda: controller.show_frame(StatsCalculatorUG))
        button3.grid(row=0, column=6)
        button4 = tk.Button(self, text="Area and Volume", bg='black',fg='green', activebackground="red",command=lambda: controller.show_frame(AreaVolume))
        button4.grid(row=0, column=0)

        entry = tk.Entry(self, borderwidth=5, width=50,bg='black',fg='white')
        entry.grid(row=4, column=3)
        maindisp = tk.Entry(self, borderwidth=5, width=50,bg='black',fg='white')
        maindisp.grid(row=4, column=3)

        def myclick(number):
            entry.insert(tk.END, number)
            maindisp.insert(tk.END, number)

        def equal():
            y = str(eval(entry.get()))
            clear()
            entry.insert(0, y)
            maindisp.insert(0, y)

        def clear():
            entry.delete(0, tk.END)
            maindisp.delete(0, tk.END)

        def backspace():
            y = (entry.get()[:-1])
            z = (maindisp.get()[:-1])
            clear()
            entry.insert(0, y)
            maindisp.insert(0, z)

        button_1 = tk.Button(self, text='1', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(1))
        button_1.grid(row=8, column=2)
        button_2 = tk.Button(self, text='2', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(2))
        button_2.grid(row=8, column=3)
        button_3 = tk.Button(self, text='3', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(3))
        button_3.grid(row=8, column=4)
        button_4 = tk.Button(self, text='4', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(4))
        button_4.grid(row=9, column=2)
        button_5 = tk.Button(self, text='5', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(5))
        button_5.grid(row=9, column=3)
        button_6 = tk.Button(self, text='6', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(6))
        button_6.grid(row=9, column=4)
        button_7 = tk.Button(self, text='7', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(7))
        button_7.grid(row=10, column=2)
        button_8 = tk.Button(self, text='8', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(8))
        button_8.grid(row=10, column=3)
        button_9 = tk.Button(self, text='9', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(9))
        button_9.grid(row=10, column=4)
        button_0 = tk.Button(self, text='0', padx=15, pady=5, width=20, bg='black',fg='white', activebackground="red",command=lambda: myclick(0))
        button_0.grid(row=11, column=3)
        button_clear = tk.Button(self, text="Clear", padx=15, pady=5, width=20, bg='black',fg='red', activebackground="red",command=clear)
        button_clear.grid(row=11, column=2)
        button_equal = tk.Button(self, text="=", padx=15, pady=5, width=20, bg='green',fg='white', activebackground="red",command=equal)
        button_equal.grid(row=11, column=4)
        button_Backspace = tk.Button(self, text="Backspace ", padx=15, pady=5, width=20, bg='black',fg='green', activebackground="red",command=backspace)
        button_Backspace.grid(row=14, column=4)

app = tkinterApp()
app.mainloop()