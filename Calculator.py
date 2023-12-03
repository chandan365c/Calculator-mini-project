# Calculator-mini-project
import tkinter
from tkinter import *
calc = tkinter.Tk()
calc.title("Calculator")
calc.geometry('550x700')
calc["background"] = "#323338"
black= "#323338"
peach="#E8C898"
matte_blue="#275C8D"

def options_screen():
    def destruction():          #To clear the basic, area and unit buttons
        basic_button.destroy()
        area_button.destroy()
        unit_con_button.destroy()

    def basic_end():    #Destroy Basic button and open basic calculator
        destruction()
        basic_calc()
    def area_end():     #Destroy Area button and open area calculator
        destruction()
        area_calc()
    def unit_end():     #Destroy Unit button and give unit converter
        destruction()
        unit_calc()

    #__________Basic, Area, Unit Buttons_________________
    basic_button =  Button(calc, text="Basic calculator", activebackground=peach, bg=black, borderwidth=2, command=basic_end, font=("Helvatica", 32), activeforeground=matte_blue)
    basic_button.place(x=100, y=76, width=350, height=100)
    area_button =  Button(calc, text="Area calculator", activebackground=peach, bg=black, borderwidth=2, command=area_end, font=("Helvatica", 32), activeforeground=matte_blue)
    area_button.place(x=100, y=269, width=350, height=100)
    unit_con_button = Button(calc, text="Unit Converter", activebackground=peach, bg=black, borderwidth=2, command=unit_end, font=("Helvatica", 32), activeforeground=matte_blue)
    unit_con_button.place(x=100,y=462, width=350, height=100) 


#_______BASIC CALCULATOR_________
def basic_calc():
    no = ['C','(',')','mod','x!',
          '7','8','9','/','√',
          '4','5','6','*','x^2',
          '1','2','3','-','x^y',
          '0','.','%','+','=']


#________AREA CALCULATOR_________
def area_calc():
    return 0


#_________UNIT CONVERTER_________
def unit_calc():
    def destruction():          #To clear the basic, area and unit buttons
        feet_metres.destroy()
        metres_feet.destroy()
        acres_km2.destroy()
        km2_acres.destroy()
        pounds_kgs.destroy()
        kgs_pounds.destroy()
    def feet():
        destruction()
    def metres():
        destruction()
    def acres():
        destruction()
    def km2():
        destruction()
    def pounds():
        destruction()
    def kgs():
        destruction()
    feet_metres =  Button(calc, text="Feet to Metres", activebackground=peach, bg=black, borderwidth=2, command=feet, font=("Helvatica", 16), activeforeground=matte_blue)
    feet_metres.place(x=150, y=100, width=250, height=50)
    metres_feet =  Button(calc, text="Metres to Feet", activebackground=peach, bg=black, borderwidth=2, command=metres, font=("Helvatica", 16), activeforeground=matte_blue)
    metres_feet.place(x=150, y=200, width=250, height=50)
    acres_km2 = Button(calc, text="Acres to Sq. Kilometre", activebackground=peach, bg=black, borderwidth=2, command=acres, font=("Helvatica", 16), activeforeground=matte_blue)
    acres_km2.place(x=150,y=300, width=250, height=50)
    km2_acres =  Button(calc, text="Sq. Kilometres to Acres", activebackground=peach, bg=black, borderwidth=2, command=km2, font=("Helvatica", 16), activeforeground=matte_blue)
    km2_acres.place(x=150, y=400, width=250, height=50)
    pounds_kgs =  Button(calc, text="Pounds to Kgs", activebackground=peach, bg=black, borderwidth=2, command=pounds, font=("Helvatica", 16), activeforeground=matte_blue)
    pounds_kgs.place(x=150, y=500, width=250, height=50)
    kgs_pounds = Button(calc, text="Kgs to pounds", activebackground=peach, bg=black, borderwidth=2, command=kgs, font=("Helvatica", 16), activeforeground=matte_blue)
    kgs_pounds.place(x=150,y=600, width=250, height=50)

options_screen()
calc.mainloop()
