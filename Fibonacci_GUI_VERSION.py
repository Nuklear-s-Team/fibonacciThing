# Copyright 2020 Khang Nguyen and Tim Merrill

# Made with the same translate function as the original.

import tkinter as tkinter
import time
from Fibonacci_Encoder import encode, decode
root = tkinter.Tk(className="Fibonacci Encoder")
lol = tkinter.StringVar()
decodeNames = ["de", "decode", "De", "Decode", "d", "D"]
encodeNames = ["en", "encode", "En", "Encode", "e", "E"]

def translate():
    task = lol.get()
    message = T.get()
    T.delete(0, tkinter.END)
    if task in encodeNames:
        totranslate= encode(message)
    elif task in decodeNames:
        totranslate= decode(message)
    T.insert(tkinter.END, totranslate)


Encode = tkinter.Radiobutton(root, text='Encode', variable=lol, value="Encode").pack(anchor=tkinter.W)
Decode = tkinter.Radiobutton(root, text='Decode', variable=lol, value="Decode").pack(anchor=tkinter.W)


T = tkinter.Entry(root, width=50)
T.pack(side=tkinter.LEFT, fill=tkinter.Y)
tkinter.Button(root, text="Translate", command=translate, width=7).pack()
tkinter.Button(root, text="Quit", command=root.quit, width=7).pack()
T.insert(tkinter.END, "")
tkinter.mainloop()