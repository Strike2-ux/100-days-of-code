import tkinter as tk
from PIL import Image, ImageTk
#latinos hey, how are you.

window = tk.Tk()
window.title("Guess Who?")
window.geometry("400x400")

label = "Guess Who?"

def showImage():
  person = text.get("1.0", "end")
  if person.lower().strip() == "mo":
    canvas.itemconfig(container, image=mo)
  elif person.lower().strip() == "charlotte":
    canvas.itemconfig(container, image=charlotte)
  elif person.lower().strip() == "gerald":
    canvas.itemconfig(container, image=gerald)
  elif person.lower().strip() == "katie":
    canvas.itemconfig(container, image=katie)
  else:
    hello["text"] = "Unable to find this user"

hello = tk.Label(text=label)
hello.pack()
text = tk.Text(window, height=1, width=30)
text.pack()
button = tk.Button(text="Find", command=showImage)
button.pack()
canvas = tk.Canvas(window, width=400, height=380)
canvas.pack()
charlotte = ImageTk.PhotoImage(Image.open("guessWho/charlotte.jpg"))
gerald = ImageTk.PhotoImage(Image.open("guessWho/gerald.jpg"))
katie = ImageTk.PhotoImage(Image.open("guessWho/katie.jpg"))
mo = ImageTk.PhotoImage(Image.open("guessWho/mo.jpg"))
container = canvas.create_image(150,1,image=mo)

tk.mainloop()


'''
import tkinter as tk
from PIL import Image, ImageTk
import sqlite3

window = tk.Tk()
window.title("Guess Who?")
window.geometry("400x400")

label = "Guess Who?"

def showImage():
    person = text.get("1.0", "end").strip().lower()

    connection = sqlite3.connect("guess_who_data.db")
    cursor = connection.cursor()

    cursor.execute("SELECT image_path FROM people WHERE name=?", (person,))
    result = cursor.fetchone()
    
    connection.close()

    if result:
        image_path = result[0]
        canvas.itemconfig(container, image=ImageTk.PhotoImage(Image.open(image_path)))
        hello["text"] = ""
    else:
        hello["text"] = "Unable to find this user"

hello = tk.Label(text=label)
hello.pack()

text = tk.Text(window, height=1, width=30)
text.pack()

button = tk.Button(text="Find", command=showImage)
button.pack()

canvas = tk.Canvas(window, width=400, height=380)
canvas.pack()

container = canvas.create_image(150, 1, image=None)  # Initial image will be set by showImage

tk.mainloop()

'''