import tkinter as tk
from tkinter import *
from math import sqrt, pi

calc = Tk()
calc.title("Calculator")
calc.geometry('550x700')
calc["background"] = "#323338"
black = "#323338"
peach = "#E8C898"
matte_blue = "#275C8D"
cool_white = "#CBD9ED"
space_grey = "#888888"
grey = "#555555"
matte_green = "#93B488"
matte_red = "#905959"


def back():
    calc.destroy()


#_____________MAIN SCREEN________________
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
    basic_button =  Button(calc, text="Basic calculator", activebackground=matte_green, bg=grey, borderwidth=2, bd=4, command=basic_end, font=("Helvatica 25 bold"), activeforeground=matte_blue, foreground="white")
    basic_button.place(x=100, y=59, width=350, height=100)

    area_button =  Button(calc, text="Area calculator", activebackground=matte_green, bg=grey, borderwidth=2, bd=4, command=area_end, font=("Helvatica 25 bold"), activeforeground=matte_blue, foreground="white") 
    area_button.place(x=100, y=211, width=350, height=100)

    volume_button =  Button(calc, text="Volume calculator", activebackground=matte_green, bg=grey, borderwidth=2, command=vol_end, font=("Helvatica 20 bold"), activeforeground=matte_blue, foreground="white")
    volume_button.place(x=100, y=363, width=350, height=100)

    unit_con_button = Button(calc, text="Unit Converter", activebackground=matte_green, bg=grey, borderwidth=2, bd=4, command=unit_end, font=("Helvatica 25 bold"), activeforeground=matte_blue, foreground="white")
    unit_con_button.place(x=100,y=515, width=350, height=100) 


#_______BASIC CALCULATOR_________
def basic_calc():
    numbers = ['C','(',')','sqrt',
               '7','8','9','x²',
               '4','5','6','/',
               '1','2','3','*',
               '0','.','-','+',
               '=']

 
    result_var = tk.StringVar()
    result_entry = tk.Entry(calc, textvariable=result_var, justify='right', font=("Arial 22 bold"), bd=7, insertwidth=10, width=25, bg=cool_white)
    result_entry.grid(row=1, column=2, columnspan=5)

    def on_click(button_text):
        current_text = result_var.get()

        if button_text == "=":
            try:
                result_var.set(eval(current_text))
            except Exception as e:
                result_var.set("Error")
        elif button_text == "C":
            result_var.set("")
        elif button_text == "sqrt":
            result_var.set(sqrt(int(current_text)))
        elif button_text == "x²":
            result_var.set(int(current_text)**2)
        else:
            result_var.set(current_text + button_text)
        
    row_val = 2
    col_val = 3

    for button_text in numbers:
        Button(calc, text=button_text, width=7, height=4, command=lambda text=button_text: on_click(text), bd=5, bg=grey, activebackground=space_grey, foreground='white', activeforeground=peach, font=("Arial 11 bold"), justify='right').grid(row=row_val, column=col_val, padx=3, pady=3, sticky=tk.S)
        col_val += 1
        if col_val > 6:
            col_val = 3
            row_val += 1

    #_____EXIT BUTTON______
    back_button = Button(calc, text="EXIT", command=back, bg=matte_red, foreground="white", bd=4, activebackground="red")
    back_button.place(x=350, y=600, height=40, width=60)

    calc.geometry("450x650")



#________AREA CALCULATOR_________
def area_calc():

    def dropdown():
        # Create and place a label for shape selection
        global shape_label
        shape_label = tk.Label(calc, text="Select Shape:")
        shape_label.place(x=32, y=138, height=42, width=112)

        # Create a dropdown menu for shape selection
        shapes = ["Circle", "Rectangle", "Triangle"]
        global shape_var
        shape_var = tk.StringVar()
        shape_var.set("Choose a shape")  # Default selection
        global shape_menu
        shape_menu = tk.OptionMenu(calc, shape_var, *shapes)
        shape_menu.place(x=174, y=138, height=42, width=260)

        # OK Button
        global ok_button
        ok_button = Button(calc, text="OK", command=OK_button, bg=matte_green, activebackground="green", bd=4)
        ok_button.place(x=459, y=199, height=37, width=60)

        #_____EXIT BUTTON______
        back_button = Button(calc, text="EXIT", command=back, bg=matte_red, foreground="white", bd=4, activebackground="red")
        back_button.place(x=455, y=318, height=27, width=87)


    #________OK BUTTON____________
    def OK_button():

        shape = shape_var.get()

        if shape == "Circle":
            shape_menu.destroy()
            shape_label.destroy()
            ok_button.destroy()
            circle()
            
        elif shape == "Rectangle":
            shape_menu.destroy()
            shape_label.destroy()
            ok_button.destroy()
            rectangle()
            
        elif shape == "Triangle":
            shape_menu.destroy()
            shape_label.destroy()
            ok_button.destroy()
            triangle()
        else:
            area = 0  # Default value for unknown shape
     

    # Create and place entry fields for shape parameters
    #_______CIRCLE_______
    def circle():
        Radius_label = tk.Label(calc, text="Radius: ")
        Radius_label.place(x=100, y=100)

        Radius_textbox = tk.Entry(calc)
        Radius_textbox.insert(END, 0)
        Radius_textbox.place(x=170, y=100)

        #________CALCULATE BUTTON_______ 
        Calculate_button = tk.Button(calc, text="Calculate", command= lambda: C_Calculate(Radius_textbox.get()), activebackground="green", bd=3)
        Calculate_button.place(x=100, y=150)

        #___________Calculate Function__________
        def C_Calculate(input):
            area = float(input)
            if(area > 0): 
                result = pi * area ** 2
                ShowResult(result)   

        #_____EXIT BUTTON______
        back_button = Button(calc, text="EXIT", command=back, bg=matte_red, foreground="white", bd=4, activebackground="red")
        back_button.place(x=455, y=318, height=27, width=87)

        

    #_______RECTANGLE_______
    def rectangle():
        Length_label = tk.Label(calc, text="Length: ")
        Length_label.place(x=100, y=100)

        Length_textbox = tk.Entry(calc)
        Length_textbox.insert(END, 0)
        Length_textbox.place(x=170, y=100)

        Width_label = tk.Label(calc, text="Breadth: ")
        Width_label.place(x=100, y=150)

        Width_textbox = tk.Entry(calc)
        Width_textbox.insert(END, 0)
        Width_textbox.place(x=170, y=150)

        #________CALCULATE BUTTON_______
        Calculate_button = tk.Button(calc, text="Calculate", command= lambda: R_Calculate(Length_textbox.get(), Width_textbox.get()), activebackground="green", bd=3)
        Calculate_button.place(x=100, y=200)

        #___________Calculate Function_______________
        def R_Calculate(L,B):
            Length = float(L)
            Breadth = float(B)
            if(Length, Breadth > 0): 
                result = Length * Breadth
                ShowResult(result)   

        #_____EXIT BUTTON______
        back_button = Button(calc, text="EXIT", command=back, bg=matte_red, foreground="white", bd=4, activebackground="red")
        back_button.place(x=455, y=318, height=27, width=87)


    #________TRIANGLE________
    def triangle():
        Base_label = tk.Label(calc, text="Base: ")
        Base_label.place(x=100, y=100)

        Base_textbox = tk.Entry(calc)
        Base_textbox.insert(END, 0)
        Base_textbox.place(x=170, y=100)

        Height_label = tk.Label(calc, text="Height: ")
        Height_label.place(x=100, y=150)

        Height_textbox = tk.Entry(calc)
        Height_textbox.insert(END, 0)
        Height_textbox.place(x=170, y=150)

        #________CALCULATE BUTTON_______
        Calculate_button = tk.Button(calc, text="Calculate", command= lambda: R_Calculate(Base_textbox.get(), Height_textbox.get()), activebackground="green", bd=3)
        Calculate_button.place(x=100, y=200)

        #___________Calculate Function_______________
        def R_Calculate(B,H):
            Base = float(B)
            Height = float(H)
            if(Base, Height > 0): 
                result = 0.5 * Base * Height
                ShowResult(result)  

        #_____EXIT BUTTON______
        back_button = Button(calc, text="EXIT", command=back, bg=matte_red, foreground="white", bd=4, activebackground="red")
        back_button.place(x=455, y=318, height=27, width=87)
 

    #______________ShowResult Function________________
    def ShowResult(result):
        lblResult = tk.Label(calc, text="Area =" + str(result))
        lblResult.place(x=100, y=250)


    dropdown()
    calc.geometry("558x359")

    
#______VOLUME CALCULATOR______
def volume_calc():
    def destruction():          
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
    cuboid_button =  Button(calc, text="Cuboid", activebackground=matte_green, bg=grey, borderwidth=2, command=cuboid, font=("Helvatica 25 bold"), activeforeground=matte_blue, foreground="white", bd=3)
    cuboid_button.place(x=100, y=100, width=350, height=100)
    cone_button =  Button(calc, text="Cone", activebackground=matte_green, bg=grey, borderwidth=2, command=cone, font=("Helvatica 25 bold"), activeforeground=matte_blue, foreground="white", bd=3)
    cone_button.place(x=100, y=250, width=350, height=100)
    sphere_button =  Button(calc, text="Sphere", activebackground=matte_green, bg=grey, borderwidth=2, command=sphere, font=("Helvatica 25 bold"), activeforeground=matte_blue, foreground="white", bd=3)
    sphere_button.place(x=100, y=400, width=350, height=100)
    cylinder_button = Button(calc, text="Cylinder", activebackground=matte_green, bg=grey, borderwidth=2, command=cylinder, font=("Helvatica 25 bold"), activeforeground=matte_blue, foreground="white", bd=3)
    cylinder_button.place(x=100,y=550, width=350, height=100) 

#_________UNIT CONVERTER_________
def unit_calc():
    def destruction():          
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
    feet_metres =  Button(calc, text="Feet to Metres", activebackground=matte_green, bg=grey, borderwidth=2, command=feet, font=("Helvatica 15 bold"), activeforeground=matte_blue, foreground="white", bd=4)
    feet_metres.place(x=150, y=100, width=250, height=50)
    metres_feet =  Button(calc, text="Metres to Feet", activebackground=matte_green, bg=grey, borderwidth=2, command=metres, font=("Helvatica 15 bold"), activeforeground=matte_blue, foreground="white", bd=4)
    metres_feet.place(x=150, y=200, width=250, height=50)
    acres_km2 = Button(calc, text="Acres to Sq.Kilometre", activebackground=matte_green, bg=grey, borderwidth=2, command=acres, font=("Helvatica 12 bold"), activeforeground=matte_blue, foreground="white", bd=4)
    acres_km2.place(x=150,y=300, width=250, height=50)
    km2_acres =  Button(calc, text="Sq.Kilometres to Acres", activebackground=matte_green, bg=grey, borderwidth=2, command=km2, font=("Helvatica 12 bold"), activeforeground=matte_blue, foreground="white", bd=4)
    km2_acres.place(x=150, y=400, width=250, height=50)
    pounds_kgs =  Button(calc, text="Pounds to KGs", activebackground=matte_green, bg=grey, borderwidth=2, command=pounds, font=("Helvatica 15 bold"), activeforeground=matte_blue, foreground="white", bd=4)
    pounds_kgs.place(x=150, y=500, width=250, height=50)
    kgs_pounds = Button(calc, text="KGs to Pounds", activebackground=matte_green, bg=grey, borderwidth=2, command=kgs, font=("Helvatica 15 bold"), activeforeground=matte_blue, foreground="white", bd=4)
    kgs_pounds.place(x=150,y=600, width=250, height=50)

options_screen()
calc.mainloop()
