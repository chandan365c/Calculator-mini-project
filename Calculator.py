# Calculator-mini-project
import tkinter
from tkinter import *
calc = Tk()
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
    dropdown


#_________UNIT CONVERTER_________
def unit_calc():
    entry 

options_screen()
calc.mainloop()
