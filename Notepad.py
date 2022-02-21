import tkinter
from tkinter.filedialog import *
import tkinter as tk

def saveFile():
    new_file = asksaveasfile(mode='w', filetype=[('text files', '.txt')])
    if new_file is None:
        return
    import tkinter
    text = str(entry.get(1.0, tkinter.END))
    new_file.write(text)
    new_file.close()

def openFile():
    file = askopenfile(mode='r', filetype=[('text files', '.txt')])
    if file is None:
        content = file.read()
    entry.insert(tkinter.INSERT, content)

def clearFile():
    entry.delete(1.0, tkinter.END)

canvas = tk.Tk()
canvas.geometry("400x600")
canvas.title("Notepad")
canvas.config(bg = "white")
top = tkinter.Frame(canvas)
top.pack(padx = 10, pady = 5, anchor = 'nw')

b1 = tkinter.Button(canvas, text="Open", bg ="white", command = openFile)
b1.pack(in_ = top, side =tkinter.LEFT)

b2 = tkinter.Button(canvas, text="Save", bg ="white", command = saveFile)
b2.pack(in_ = top, side =tkinter.LEFT)

b3 = tkinter.Button(canvas, text="Clear", bg ="white", command = clearFile)
b3.pack(in_ = top, side =tkinter.LEFT)

b4 = tkinter.Button(canvas, text="Exit", bg ="white", command = exit)
b4.pack(in_ = top, side=tkinter.LEFT)

entry = tkinter.Text(canvas, wrap =tkinter.WORD, bg ='#F9DDA4', font = ("poppins", 15))
entry.pack(padx = 10, pady = 5, expand = True, fill =tkinter.BOTH)

canvas.mainloop()