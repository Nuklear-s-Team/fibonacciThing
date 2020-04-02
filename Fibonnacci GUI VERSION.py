# Copyright 2020 Khang Nguyen and Tim Merrill
# Improved by Luzgog

# Made with the same translate function as the original.

import tkinter as tkinter
import time
from Luzgog_Regular import encode, decode, encodeReversed, decodeReversed
root = tkinter.Tk(className="Fibonacci Encoder")
lol = tkinter.StringVar()
mode = tkinter.StringVar()
decodeNames = ["de", "decode", "De", "Decode", "d", "D"]
encodeNames = ["en", "encode", "En", "Encode", "e", "E"]


def translate():
    task = lol.get()
    message = T.get()
    version = mode.get()
    T.delete(0, tkinter.END)
    if task in encodeNames:
        if version == "Regular":
            totranslate= encode(message)
        elif version == "Reversed":
            totranslate = encodeReversed(message)
    elif task in decodeNames:
        if version == "Regular":
            totranslate = decode(message)
        elif version == "Reversed":
            totranslate = decodeReversed(message)
    T.insert(tkinter.END, totranslate)


Encode = tkinter.Radiobutton(root, text='Encode', variable=lol, value="Encode").grid(row=0, sticky=tkinter.W)
Decode = tkinter.Radiobutton(root, text='Decode', variable=lol, value="Decode").grid(row=1, sticky=tkinter.W)
Regular = tkinter.Radiobutton(root, text='Regular', variable=mode, value="Regular").grid(row=0, column=0, sticky=tkinter.E)
Reversed = tkinter.Radiobutton(root, text='Reversed', variable=mode, value="Reversed").grid(row=1, column=0, sticky=tkinter.E)

T = tkinter.Entry(root, width=100)
T.grid(row=2, column=0, sticky=tkinter.W)
tkinter.Button(root, text="Translate", command=translate, width=43).grid(row=3, column=0, sticky=tkinter.W)
tkinter.Button(root, text="Quit", command=root.quit, width=43).grid(row=3, column=0, sticky=tkinter.E)
T.insert(tkinter.END, "")
tkinter.mainloop()