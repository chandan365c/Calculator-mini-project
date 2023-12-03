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
        volume_button.destroy()

    def basic_end():    #Destroy Basic button and open basic calculator
        destruction()
        basic_calc()
    def area_end():     #Destroy Area button and open area calculator
        destruction()
        area_calc()
    def unit_end():     #Destroy Unit button and give unit converter
        destruction()
        unit_calc()
    def vol_end():
        destruction()
        volume_calc()

    #__________Basic, Area, Unit Buttons_________________
    basic_button =  Button(calc, text="Basic calculator", activebackground=peach, bg=black, borderwidth=2, command=basic_end, font=("Helvatica", 32), activeforeground=matte_blue)
    basic_button.place(x=100, y=100, width=350, height=100)
    area_button =  Button(calc, text="Area calculator", activebackground=peach, bg=black, borderwidth=2, command=area_end, font=("Helvatica", 32), activeforeground=matte_blue)
    area_button.place(x=100, y=250, width=350, height=100)
    volume_button =  Button(calc, text="Volume calculator", activebackground=peach, bg=black, borderwidth=2, command=vol_end, font=("Helvatica", 32), activeforeground=matte_blue)
    volume_button.place(x=100, y=400, width=350, height=100)
    unit_con_button = Button(calc, text="Unit Converter", activebackground=peach, bg=black, borderwidth=2, command=unit_end, font=("Helvatica", 32), activeforeground=matte_blue)
    unit_con_button.place(x=100,y=550, width=350, height=100) 


#_______BASIC CALCULATOR_________
def basic_calc():
    no = ['C','(',')','mod','x!',
          '7','8','9','/','√',
          '4','5','6','*','x^2',
          '1','2','3','-','x^y',
          '0','.','%','+','=']


#________AREA CALCULATOR_________
def area_calc():
    return 0 #Do the area calculator part

def volume_calc():
    def destruction():          #To clear the basic, area and unit buttons
        cuboid_button.destroy()
        cone_button.destroy()
        sphere_button.destroy()
        cylinder_button.destroy()
    def cuboid():
        destruction()
        Label(calc,text="Enter Value of length").grid(row=0)
        Label(calc,text="Enter Value of breadth").grid(row=1)
        Label(calc,text="Enter Value of height").grid(row=2)
        g=Entry(calc)
        h=Entry(calc)
        i=Entry(calc)
        g.grid(row=0,column=1)
        h.grid(row=1,column=1)
        i.grid(row=2,column=1)
        def calc1():
            ganj.destroy()
            j=g.get()
            k=h.get()
            l=i.get()
            m=float(j)*float(k)*float(l)
            z=Label(calc,text=f"{m} cubic units ")
            z.grid(row=3,column=1)
        ganj=Button(calc, text="Calculate", command=calc1)
        ganj.grid(row=3, column=1)
    def cone():
        destruction()
        Label(calc,text="Enter Value of radius").grid(row=0)
        Label(calc,text="Enter Value of height").grid(row=1)
        g=Entry(calc)
        h=Entry(calc)
        g.grid(row=0,column=1)
        h.grid(row=1,column=1)
        def calc1():
            ganj.destroy()
            pi=3.14
            j=g.get()
            k=h.get()
            m=pi*float(j)**2*float(k)/3
            z=Label(calc,text=f"{m} cubic units ")
            z.grid(row=2,column=1)
        ganj=Button(calc, text="Calculate", command=calc1)
        ganj.grid(row=2, column=1)
    def sphere():
        destruction()
        Label(calc,text="Enter Value of radius").grid(row=0)
        g=Entry(calc)
        g.grid(row=0,column=1)
        def calc1():
            ganj.destroy()
            pi=3.14
            j=g.get()
            m=4/3*pi*float(j)**3
            z=Label(calc,text=f"{m} cubic units ")
            z.grid(row=1,column=1)
        ganj=Button(calc, text="Calculate", command=calc1)
        ganj.grid(row=1, column=1)
    def cylinder():
        destruction()
        Label(calc,text="Enter Value of radius").grid(row=0)
        Label(calc,text="Enter Value of height").grid(row=1)
        g=Entry(calc)
        h=Entry(calc)
        g.grid(row=0,column=1)
        h.grid(row=1,column=1)
        def calc1():
            ganj.destroy()
            pi=3.14
            j=g.get()
            k=h.get()
            m=pi*float(j)**2*float(k)
            z=Label(calc,text=f"{m} cubic units ")
            z.grid(row=2,column=1)
        ganj=Button(calc, text="Calculate", command=calc1)
        ganj.grid(row=2, column=1)
    cuboid_button =  Button(calc, text="Cuboid", activebackground=peach, bg=black, borderwidth=2, command=cuboid, font=("Helvatica", 32), activeforeground=matte_blue)
    cuboid_button.place(x=100, y=100, width=350, height=100)
    cone_button =  Button(calc, text="Cone", activebackground=peach, bg=black, borderwidth=2, command=cone, font=("Helvatica", 32), activeforeground=matte_blue)
    cone_button.place(x=100, y=250, width=350, height=100)
    sphere_button =  Button(calc, text="Sphere", activebackground=peach, bg=black, borderwidth=2, command=sphere, font=("Helvatica", 32), activeforeground=matte_blue)
    sphere_button.place(x=100, y=400, width=350, height=100)
    cylinder_button = Button(calc, text="Cylinder", activebackground=peach, bg=black, borderwidth=2, command=cylinder, font=("Helvatica", 32), activeforeground=matte_blue)
    cylinder_button.place(x=100,y=550, width=350, height=100) 

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
        Label(calc,text="Enter Value in feet").grid(row=0)
        g=Entry(calc)
        g.grid(row=0,column=1)
        def convert1():
            ganj.destroy()
            h=g.get()
            k=float(h)/3.281
            l=Label(calc,text=f"{k} metres ")
            l.grid(row=1,column=0)
        ganj=Button(calc, text="Convert", command=convert1)
        ganj.grid(row=2, column=1)
    def metres():
        destruction()
        Label(calc,text="Enter Value in metres").grid(row=0)
        g=Entry(calc)
        g.grid(row=0,column=1)
        def convert2():
            ganj.destroy()
            h=g.get()
            k=float(h)*3.281
            l=Label(calc,text=f"{k} feet ")
            l.grid(row=1,column=0)
        ganj=Button(calc, text="Convert", command=convert2)
        ganj.grid(row=2, column=1)
    def acres():
        destruction()
        Label(calc,text="Enter Value in acres").grid(row=0)
        g=Entry(calc)
        g.grid(row=0,column=1)
        def convert3():
            ganj.destroy()
            h=g.get()
            k=float(h)/247.1
            l=Label(calc,text=f"{k} Sq. Kilometres ")
            l.grid(row=1,column=0)
        ganj=Button(calc, text="Convert", command=convert3)
        ganj.grid(row=2, column=1)
    def km2():
        destruction()
        Label(calc,text="Enter Value in square kilometres").grid(row=0)
        g=Entry(calc)
        g.grid(row=0,column=1)
        def convert4():
            ganj.destroy()
            h=g.get()
            k=float(h)*247.1
            l=Label(calc,text=f"{k} acres ")
            l.grid(row=1,column=0)
        ganj=Button(calc, text="Convert", command=convert4)
        ganj.grid(row=2, column=1)
    def pounds():
        destruction()
        Label(calc,text="Enter Value in pounds").grid(row=0)
        g=Entry(calc)
        g.grid(row=0,column=1)
        def convert5():
            ganj.destroy()
            h=g.get()
            k=float(h)/2.205
            l=Label(calc,text=f"{k} Kgs ")
            l.grid(row=1,column=0)
        ganj=Button(calc, text="Convert", command=convert5)
        ganj.grid(row=2, column=1)
    def kgs():
        destruction()
        Label(calc,text="Enter Value in kgs").grid(row=0)
        g=Entry(calc)
        g.grid(row=0,column=1)
        def convert6():
            ganj.destroy()
            h=g.get()
            k=float(h)*2.205
            l=Label(calc,text=f"{k} Pounds ")
            l.grid(row=1,column=0)
        ganj=Button(calc, text="Convert", command=convert6)
        ganj.grid(row=2, column=1)
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
