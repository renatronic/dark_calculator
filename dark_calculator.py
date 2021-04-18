from tkinter import *

# expressions
expression = ''

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ''
    except:
        equation.set('error')
        expression= ''

def clear():
    global expression
    expression = ''
    equation.set('0')

# main window
root = Tk()
root.title ('PocketCalculator')
root.geometry('355x475')
root.configure(bg = '#1E2228')
root.iconbitmap('calc.ico')
root.resizable(False, False)

# frame to put entry box and buttons 
button_frame = Frame(root, bg = '#1E2228')
button_frame.pack()

# entry box
equation = StringVar()
equation.set('0')
entry_box = Entry(button_frame, textvariable = equation, justify = 'right', font = ('arial', 20, 'bold'))

# buttons creation
button1 = Button(button_frame, fg = '#FFFFFF', text = '1', font = ('arial', 11, 'bold'), relief = 'groove', bd = 1, bg = '#22272E', width = 8, height = 3, command = lambda: press(1))
button2 = Button(button_frame, fg = '#FFFFFF', text = '2', font = ('arial', 11, 'bold'), relief = 'groove', bd = 1, bg = '#22272E', width = 8, height = 3, command = lambda: press(2))
button3 = Button(button_frame, fg = '#FFFFFF', text = '3', font = ('arial', 11, 'bold'), relief = 'groove', bd = 1, bg = '#22272E', width = 8, height = 3, command = lambda: press(3))
addition = Button(button_frame, fg = '#FFFFFF', text = '+', font = ('arial', 11, 'bold'), relief = 'groove', bd = 1, bg = '#22272E', width = 8, height = 3, command = lambda: press('+'))
button4 = Button(button_frame, fg = '#FFFFFF', text = '4', font = ('arial', 11, 'bold'), relief = 'groove', bd = 1, bg = '#22272E', width = 8, height = 3, command = lambda: press(4))
button5 = Button(button_frame, fg = '#FFFFFF', text = '5', font = ('arial', 11, 'bold'), relief = 'groove', bd = 1, bg = '#22272E', width = 8, height = 3, command = lambda: press(5))
button6 = Button(button_frame, fg = '#FFFFFF', text = '6', font = ('arial', 11, 'bold'), relief = 'groove', bd = 1, bg = '#22272E', width = 8, height = 3, command = lambda: press(6))
subtract = Button(button_frame, fg = '#FFFFFF', text = '-', font = ('arial', 11, 'bold'), relief = 'groove', bd = 1, bg = '#22272E', width = 8, height = 3, command = lambda: press('-'))
button7 = Button(button_frame, fg = '#FFFFFF', text = '7', font = ('arial', 11, 'bold'), relief = 'groove', bd = 1, bg = '#22272E', width = 8, height = 3, command = lambda: press(7))
button8 = Button(button_frame, fg = '#FFFFFF', text = '8', font = ('arial', 11, 'bold'), relief = 'groove', bd = 1, bg = '#22272E', width = 8, height = 3, command = lambda: press(8))
button9 = Button(button_frame, fg = '#FFFFFF', text = '9', font = ('arial', 11, 'bold'), relief = 'groove', bd = 1, bg = '#22272E', width = 8, height = 3, command = lambda: press(9))
multiply = Button(button_frame, fg = '#FFFFFF', text = '*', font = ('arial', 11, 'bold'), relief = 'groove', bd = 1, bg = '#22272E', width = 8, height = 3, command = lambda: press('*'))
decimal = Button(button_frame, fg = '#FFFFFF', text = '.', font = ('arial', 11, 'bold'), relief = 'groove', bd = 1, bg = '#22272E', width = 8, height = 3, command = lambda: press('.'))
button0 = Button(button_frame, fg = '#FFFFFF', text = '0', font = ('arial', 11, 'bold'), relief = 'groove', bd = 1, bg = '#22272E', width = 8, height = 3, command = lambda: press(0))
clear = Button(button_frame, fg = '#FFFFFF', text = 'C', font = ('arial', 11, 'bold'), relief = 'groove', bd = 1, bg = '#22272E', width = 8, height = 3, command = clear)
division = Button(button_frame, fg = '#FFFFFF', text = '/', font = ('arial', 11, 'bold'), relief = 'groove', bd = 1, bg = '#22272E', width = 8, height = 3, command = lambda: press('/'))
equal = Button(button_frame, fg = '#FFFFFF', text = '=', font = ('arial', 11, 'bold'), relief = 'groove', bd = 1, bg = '#22272E', width = 8, height = 3, command = lambda: equalpress())

# grid construction
entry_box.grid(row = 0, column = 0, columnspan = 4, ipadx = 8, ipady = 25, pady = 15)

button1.grid(row = 1, column = 0)
button2.grid(row = 1, column = 1)
button3.grid(row = 1, column = 2)
addition.grid(row = 1, column = 3)

button4.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button6.grid(row = 2, column = 2)
subtract.grid(row = 2, column = 3)

button7.grid(row = 3, column = 0)
button8.grid(row = 3, column = 1)
button9.grid(row = 3, column = 2)
multiply.grid(row = 3, column = 3)

decimal.grid(row = 4, column = 0)
button0.grid(row = 4, column = 1)
clear.grid(row = 4, column = 2)
division.grid(row = 4, column = 3)

equal.grid(row = 5, column = 0, columnspan = 4, sticky = 'nsew')

root.mainloop()