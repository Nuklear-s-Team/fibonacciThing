# Copyright 2020 Khang Nguyen and Tim Merrill
# Improved by Luzgog

# Made with the same translate function as the original.

import tkinter as tkinter
from tkinter import messagebox
import time
from Fibonacci_Encoder import encode, decode, encodeReversed, decodeReversed
root = tkinter.Tk(className="Fibonacci Encoder")
lol = tkinter.StringVar()
mode = tkinter.StringVar()
root.iconphoto(False, tkinter.PhotoImage(file="icon.png"))
decodeNames = ["de", "decode", "De", "Decode", "d", "D"]
encodeNames = ["en", "encode", "En", "Encode", "e", "E"]


def error():
    messagebox.showerror("Error", "Invalid Input")


def translate():
    task = lol.get()
    message = T.get()
    version = mode.get()
    T.delete(0, tkinter.END)
    if task in encodeNames:
        if version == "Regular":
            try:
                totranslate= encode(message)
            except BaseException:
                error()
        elif version == "Reversed":
            try:
                totranslate = encodeReversed(message)
            except BaseException:
                error()
    elif task in decodeNames:
        if version == "Regular":
            try:
                totranslate = decode(message)
            except BaseException:
                error()
        elif version == "Reversed":
            try:
                totranslate = decodeReversed(message)
            except BaseException:
                error()
    T.insert(tkinter.END, totranslate)


Encode = tkinter.Radiobutton(root, text='Encode', variable=lol, value="Encode", indicatoron=0, width=42, selectcolor="light green").grid(row=1, column=0, sticky=tkinter.W)
Decode = tkinter.Radiobutton(root, text='Decode', variable=lol, value="Decode", indicatoron=0, width=42, selectcolor="light green").grid(row=1, column=0, sticky=tkinter.E)
Regular = tkinter.Radiobutton(root, text='Regular', variable=mode, value="Regular", indicatoron=0, width=42, selectcolor="cyan").grid(row=3, column=0, sticky=tkinter.W)
Reversed = tkinter.Radiobutton(root, text='Reversed', variable=mode, value="Reversed", indicatoron=0, width=42, selectcolor="cyan").grid(row=3, column=0, sticky=tkinter.E)

J = tkinter.Scale(root, state=tkinter.DISABLED, length=600, troughcolor="black", width=1, orient=tkinter.HORIZONTAL, showvalue=0, sliderlength=200, label="--------------------------------------------------------Mode--------------------------------------------------------")
J.set(100)
J.grid(row=0, sticky=tkinter.N)

R = tkinter.Scale(root, state=tkinter.DISABLED, length=500, troughcolor="black", width=1, orient=tkinter.HORIZONTAL, showvalue=0, sliderlength=200, label="--------------------------------------------Key Sets--------------------------------------------")
R.set(100)
R.grid(row=2, sticky=tkinter.N)

T = tkinter.Entry(root, width=100)
L = tkinter.Scale(root, state=tkinter.DISABLED, length=500, troughcolor="black", width=1, orient=tkinter.HORIZONTAL, showvalue=0, sliderlength=200, label="------------------------------------------Input Below------------------------------------------")
L.set(100)
L.grid(row=5, sticky=tkinter.N)
T.grid(row=6, column=0, sticky=tkinter.W)

X = tkinter.Scale(root, state=tkinter.DISABLED, length=500, troughcolor="black", width=1, orient=tkinter.HORIZONTAL, showvalue=0, sliderlength=200)
X.set(100)
X.grid(row=7, sticky=tkinter.N)

Translate = tkinter.Button(root, text="Translate", command=translate, width=42, activebackground="light green").grid(row=8, column=0, sticky=tkinter.W)
Quit = tkinter.Button(root, text="Quit", command=root.quit, width=42, activebackground="red").grid(row=8, column=0, sticky=tkinter.E)
T.insert(tkinter.END, "")

X = tkinter.Scale(root, state=tkinter.DISABLED, length=600, troughcolor="black", width=1, orient=tkinter.HORIZONTAL, showvalue=0, sliderlength=200)
X.set(100)
X.grid(row=9, sticky=tkinter.N)

tkinter.mainloop()