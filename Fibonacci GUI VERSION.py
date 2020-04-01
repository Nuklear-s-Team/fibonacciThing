# Copyright 2020 Khang Nguyen and Tim Merrill

# Made with the same translate function as the original.

import tkinter as tkinter
import time
root = tkinter.Tk(className="Fibonacci Encoder")
lol = tkinter.StringVar()


def translate():
    keys = {" ": "|", "a": "2.", "b": "3.", "c": "5.", "d": "8.", "e": "13.", "f": "21.", "g": "34.", "h": "55.",
            "i": "89.", "j": "144.", "k": "233.", "l": "377.", "m": "610.", "n": "987.", "o": "1597.", "p": "2584.",
            "q": "4181.", "r": "6765.", "s": "10946.",
            "t": "17711.", "u": "28657.", "v": "46368.", "w": "75025.", "x": "121393.", "y": "196418.",
            "z": "317811.",
            "!": "!", ",": ",", "?": "?", "'": "'.", "|": "|", ":": ":", "": "", "-": "-."}
    encodeNames = ["en", "encode", "En", "Encode"]
    decodeNames = ["de", "decode", "De", "Decode"]
    dekeys = {v: k for k, v in keys.items()}
    cdekeys = {k.replace('.', ''): v for k, v in dekeys.items()}
    task = lol.get()
    totranslate = T.get()
    T.delete(0, tkinter.END)
    if task in encodeNames:
        totranslate = totranslate.lower()
        totranslate = totranslate.replace(".", "|||")
        for item in totranslate:
            totranslate = totranslate.replace(item, str(keys[item]))
            totranslate = totranslate.replace(".|", "|")
        if totranslate[len(totranslate) - 1] == ".":
            totranslate = totranslate[:len(totranslate) - 1]
    elif task in decodeNames:
        totranslate = totranslate.replace("|||", "~")
        totranslate = totranslate.replace("|", " ")

        translist = totranslate.split(sep=".")
        for item in translist:
            if " " in item:
                index1 = translist.index(item)
                temp = item.split(" ")
                for item in temp:
                    if "~" in item:
                        temp2 = item.replace("~", "")
                        tempIndex = temp.index(item)
                        temp[tempIndex] = temp2
                        temp2 = str(cdekeys[temp2])  # excuse my messy code here
                        temp[tempIndex] = temp2
                        temp2 = temp2 + ". "
                        temp[tempIndex] = temp2
                    else:
                        index2 = temp.index(item)
                        item = str(cdekeys[item])
                        temp[index2] = item

                item = " ".join(temp)
                translist[index1] = item
            elif "~" in item:
                temp = item.replace("~", "")
                temp = str(cdekeys[temp])
                index = translist.index(item)
                item = temp + ". "
                translist[index] = item
            else:
                index = translist.index(item)
                translist[index] = item.replace(item, str(cdekeys[item]))
        totranslate = "".join(translist)
    else:
        pass
    T.insert(tkinter.END, totranslate)


Encode = tkinter.Radiobutton(root, text='Encode', variable=lol, value="Encode").pack(anchor=tkinter.W)
Decode = tkinter.Radiobutton(root, text='Decode', variable=lol, value="Decode").pack(anchor=tkinter.W)


T = tkinter.Entry(root, width=50)
T.pack(side=tkinter.LEFT, fill=tkinter.Y)
tkinter.Button(root, text="Translate", command=translate, width=7).pack()
tkinter.Button(root, text="Quit", command=root.quit, width=7).pack()
T.insert(tkinter.END, "")
tkinter.mainloop()