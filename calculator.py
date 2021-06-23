from tkinter import *

root = Tk()

root.title("Calculator")

e = Entry(root , borderwidth=5,width=50)
e.grid(row = 0, column=0 , columnspan=4,padx = 20, pady=20)

e.insert(0 , "")

def buttonClick(number):
    # e.delete(0,  END)
    curr = e.get()
    e.delete(0, END)
    e.insert(0,curr + str(number))

def buttonClear():
    e.delete(0, END)

def buttonAdd():
    first_num = e.get()
    global f_num
    global operation
    f_num = int(first_num)
    operation = "+"
    e.delete(0, END)

def buttonEqual():
    second_number = e.get()
    e.delete(0, END)
    if(operation == "+"):
        e.insert(0 , int(second_number) + f_num)
    elif(operation == "-"):
        e.insert(0 ,f_num - int(second_number))
    elif(operation == "*"):
        e.insert(0 , int(second_number) * f_num)
    elif(operation == "/"):
        e.insert(0 , f_num / int(second_number))



def buttonSubtract():
    first_num = e.get()
    global f_num
    global operation
    f_num = int(first_num)
    operation = "-"
    e.delete(0, END)

def buttonDivide():
    first_num = e.get()
    global f_num
    global operation
    f_num = int(first_num)
    operation = "/"
    e.delete(0, END)

def buttonMultiply():
    first_num = e.get()
    global f_num
    global operation
    f_num = int(first_num)
    operation = "*"
    e.delete(0, END)



button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonClick(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonClick(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonClick(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonClick(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonClick(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonClick(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonClick(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonClick(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonClick(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonClick(0))

equal = Button(root, text = "=", padx = 40, pady = 20 , command=lambda: buttonEqual())
clear = Button(root, text="C", padx =40, pady = 20, command= lambda: buttonClear())

addition = Button(root, text = "+", padx = 40, pady = 20, command=lambda: buttonAdd())
subtraction = Button(root, text = "-", padx = 40, pady = 20, command=lambda: buttonSubtract())
division = Button(root, text = "/", padx = 40, pady = 20, command=lambda: buttonDivide())
multiplication = Button(root, text = "*", padx = 40, pady = 20, command=lambda: buttonMultiply())


button_0.grid(row=4 , column=1)

button_1.grid(row= 3, column=0)
button_2.grid(row=3 , column=1)
button_3.grid(row=3 , column=2)

button_4.grid(row=2 , column=0)
button_5.grid(row= 2, column=1)
button_6.grid(row= 2, column=2)

button_7.grid(row=1 , column=0)
button_8.grid(row=1 , column=1)
button_9.grid(row=1 , column=2)

equal.grid(row=4,column=2)
clear.grid(row=4, column=0)

addition.grid(row = 1, column=3)
subtraction.grid(row = 2,column=3)
division.grid(row=3, column=3)
multiplication.grid(row=4, column=3)

root.mainloop()
