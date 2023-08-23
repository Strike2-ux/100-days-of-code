import tkinter as tk

#Que dicen los latinos... 
window = tk.Tk()
window.title("Calculator")
window.geometry("400x200")

answer = 0
lastNumber = 0
operator = None

def typeAnswer(value):
  global answer
  answer = f"{answer}{value}"
  answer = int(answer)
  hello["text"] = answer

def calcAnswer(thisOp):
  global answer, lastNumber, operator
  lastNumber = answer
  answer = 0
  if thisOp == "+":
    operator = "+"
  elif thisOp == "-":
    operator = "-"
  elif thisOp == "*":
    operator = "*"
  elif thisOp == "/":
    operator = "/"
  hello["text"] = answer

def calc():
  global answer, lastNumber, operator
  print(f"{lastNumber}\t{answer}\t{operator}")
  if operator =="+":
    total = lastNumber + answer
  elif operator =="-":
    total = lastNumber - answer
  elif operator =="*":
    total = lastNumber * answer
  elif operator =="/":
    total = lastNumber / answer
  answer = total
  hello["text"] = answer

hello = tk.Label(text=answer)
hello.grid(row=0, column=1)

one = tk.Button(text="1", command= lambda: typeAnswer(1))
one.grid(row=1,column=0)

two = tk.Button(text="2", command= lambda: typeAnswer(2))
two.grid(row=1,column=1)

three = tk.Button(text="3", command= lambda: typeAnswer(3))
three.grid(row=1,column=2)

four = tk.Button(text="4", command= lambda: typeAnswer(4))
four.grid(row=2,column=0)

five = tk.Button(text="5", command= lambda: typeAnswer(5))
five.grid(row=2,column=1)

six = tk.Button(text="6", command= lambda: typeAnswer(6))
six.grid(row=2,column=2)

seven = tk.Button(text="7", command= lambda: typeAnswer(7))
seven.grid(row=3,column=0)

eight = tk.Button(text="8", command= lambda: typeAnswer(8))
eight.grid(row=3,column=1)

nine = tk.Button(text="9", command= lambda: typeAnswer(9))
nine.grid(row=3,column=2)

zero = tk.Button(text="0", command= lambda: typeAnswer(0))
zero.grid(row=4,column=1)

add = tk.Button(text="+", command= lambda: calcAnswer("+"))
add.grid(row=1,column=4)

minus = tk.Button(text="-", command= lambda: calcAnswer("-"))
minus.grid(row=1,column=5)

multiply = tk.Button(text="*", command= lambda: calcAnswer("*"))
multiply.grid(row=2,column=4)

divide = tk.Button(text="/", command= lambda: calcAnswer("/"))
divide.grid(row=2,column=5)




equals = tk.Button(text="=", command=calc)
equals.grid(row=4,column=4)



tk.mainloop()
'''
import tkinter as tk
import sqlite3

window = tk.Tk()
window.title("Calculator")
window.geometry("400x400")

answer = 0
lastNumber = 0
operator = None

def typeAnswer(value):
    global answer
    answer = f"{answer}{value}"
    answer = int(answer)
    hello["text"] = answer

def calcAnswer(thisOp):
    global answer, lastNumber, operator
    lastNumber = answer
    answer = 0
    operator = thisOp
    hello["text"] = answer

def calc():
    global answer, lastNumber, operator
    if operator:
        print(f"{lastNumber}\t{answer}\t{operator}")
        if operator == "+":
            total = lastNumber + answer
        elif operator == "-":
            total = lastNumber - answer
        elif operator == "*":
            total = lastNumber * answer
        elif operator == "/":
            total = lastNumber / answer
        answer = total
        hello["text"] = answer
        operator = None

def clear():
    global answer, lastNumber, operator
    answer = 0
    lastNumber = 0
    operator = None
    hello["text"] = answer

def save_to_database():
    connection = sqlite3.connect("calculator_data.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO calculations (expression, result) VALUES (?, ?)", (hello["text"], answer))
    connection.commit()
    connection.close()

hello = tk.Label(text=answer)
hello.grid(row=0, column=1, columnspan=6)

buttons = [
    "7", "8", "9", "/", "C",
    "4", "5", "6", "*", "Save",
    "1", "2", "3", "-", " ",
    "0", "=", " ", "+", " "
]

row_index = 1
col_index = 0

for button_text in buttons:
    if button_text == " ":
        col_index += 1
        continue
    
    button = tk.Button(text=button_text, command=lambda b=button_text: button_click(b))
    button.grid(row=row_index, column=col_index)
    
    col_index += 1
    if col_index > 4:
        col_index = 0
        row_index += 1

def button_click(value):
    if value.isdigit() or value == ".":
        typeAnswer(value)
    elif value in ["+", "-", "*", "/"]:
        calcAnswer(value)
    elif value == "=":
        calc()
    elif value == "C":
        clear()
    elif value == "Save":
        save_to_database()

window.mainloop()


'''