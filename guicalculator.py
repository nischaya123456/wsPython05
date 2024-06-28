import tkinter as tk

# Global declare the expression variable
expression = ""

# Create press function in the expression_field
def press(num):
    global expression
    if num == '<-':
        expression = expression[:-1]
    else:
        expression = expression + str(num)
    # Update expression
    equation.set(expression)

def clear():
    global expression
    if len(expression) >= 3:
        expression = expression[:-3]
    else:
        expression = ""
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("error")
        expression = ""

app = tk.Tk()

# Set Background color of GUI Window
app.configure(background="white")

# Set title
app.title("Simple Calculator")

# Set size of window
app.geometry("335x355")

equation = tk.StringVar()

# Create TextBox for expression
expression_field = tk.Entry(app, textvariable=equation, bg="snow", font=('Arial 20'), width=22, justify="right", relief="solid")
expression_field.grid(columnspan=4, pady=10)

# Create Button Number
btnPercent = tk.Button(app, text=" % ", bg="cornsilk", fg="dim gray", command=lambda: press('%'), height=3, width=10).grid(row=2, pady=2, column=0)
btnCE = tk.Button(app, text=" CE ", bg="cornsilk", fg="dim gray", command=lambda: clear(), height=3, width=10).grid(row=2, pady=2, column=1)
btnC = tk.Button(app, text=" C ", command=lambda: clear(), bg="cornsilk", fg="dim gray", height=3, width=10).grid(row=2, pady=2, column=2)
btnDelete = tk.Button(app, text=" <- ", bg="salmon", fg="cornsilk", command=lambda: press('<-'), height=3, width=10).grid(row=2, pady=2, column=3)

# line Number 7-9 and X
btn7 = tk.Button(app, text=" 7 ", bg="misty rose", fg="dim gray", command=lambda: press(7), height=3, width=10).grid(row=3, pady=2, column=0)
btn8 = tk.Button(app, text=" 8 ", bg="misty rose", fg="dim gray", command=lambda: press(8), height=3, width=10).grid(row=3, pady=2, column=1)
btn9 = tk.Button(app, text=" 9 ", bg="misty rose", fg="dim gray", command=lambda: press(9), height=3, width=10).grid(row=3, pady=2, column=2)
btnMultiplied = tk.Button(app, text=" * ", bg="cornsilk", fg="dim gray", command=lambda: press('*'), height=3, width=10).grid(row=3, pady=2, column=3)

# line Number 4-6 and -
btn4 = tk.Button(app, text=" 4 ", bg="misty rose", fg="dim gray", command=lambda: press(4), height=3, width=10).grid(row=4, pady=2, column=0)
btn5 = tk.Button(app, text=" 5 ", bg="misty rose", fg="dim gray", command=lambda: press(5), height=3, width=10).grid(row=4, pady=2, column=1)
btn6 = tk.Button(app, text=" 6 ", bg="misty rose", fg="dim gray", command=lambda: press(6), height=3, width=10).grid(row=4, pady=2, column=2)
btnMinus = tk.Button(app, text=" - ", bg="cornsilk", fg="dim gray", command=lambda: press('-'), height=3, width=10).grid(row=4, pady=2, column=3)

# line Number 1-3 and +
btn1 = tk.Button(app, text=" 1 ", bg="misty rose", fg="dim gray", command=lambda: press(1), height=3, width=10).grid(row=5, pady=2, column=0)
btn2 = tk.Button(app, text=" 2 ", bg="misty rose", fg="dim gray", command=lambda: press(2), height=3, width=10).grid(row=5, pady=2, column=1)
btn3 = tk.Button(app, text=" 3 ", bg="misty rose", fg="dim gray", command=lambda: press(3), height=3, width=10).grid(row=5, pady=2, column=2)
btnPlus = tk.Button(app, text=" + ", bg="cornsilk", fg="dim gray", command=lambda: press('+'), height=3, width=10).grid(row=5, pady=2, column=3)

# line Number / and 0 and . and =
btnDivide = tk.Button(app, text=" / ", bg="pale turquoise", fg="salmon", command=lambda: press('/'), height=3, width=10).grid(row=6, pady=2, column=0)
btn0 = tk.Button(app, text=" 0 ", bg="misty rose", fg="dim gray", command=lambda: press(0), height=3, width=10).grid(row=6, pady=2, column=1)
btnDecimal = tk.Button(app, text=" . ", bg="pale turquoise", fg="salmon", command=lambda: press('.'), height=3, width=10).grid(row=6, pady=2, column=2)
btnEqual = tk.Button(app, text=" = ", bg="cornsilk", fg="dim gray", command=lambda: equalpress(), height=3, width=10).grid(row=6, pady=2, column=3)

app.mainloop()
