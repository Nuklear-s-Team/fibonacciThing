# Copyright 2020 Khang Nguyen and Tim Merrill
# Improved by Luzgog

# Made with the same translate function as the original.

import tkinter as tkinter
from tkinter import messagebox
from tkinter import scrolledtext
from Fibonacci_Encoder import encode, decode, encodeReversed, decodeReversed, randomGen, encodeRandom, generatefromkey, decodeRandom
root = tkinter.Tk(className="Fibonacci Encoder")
help = tkinter.Toplevel(width=90, height=90)
help.withdraw()
translations = tkinter.Toplevel(width=90, height=90)
translations.withdraw()
lol = tkinter.StringVar()
mode = tkinter.StringVar()
lastTranslation = tkinter.StringVar()
key = tkinter.StringVar()
lastTranslation.set("Last Tranlsation: None")
currentTranslation = ""
#root.iconphoto(False, tkinter.PhotoImage(file="icon.png"))
decodeNames = ["de", "decode", "De", "Decode", "d", "D"]
encodeNames = ["en", "encode", "En", "Encode", "e", "E"]


def showHelp():
    help.deiconify()


def closeHelp():
    help.withdraw()


def error():
    messagebox.showerror("Error", "Invalid Input")


def keyMissingError():
    messagebox.showerror("Error", "No Key")


def translate():
    global currentTranslation
    task = lol.get()
    message = T.get()
    version = mode.get()
    getKey = RandomEncode.get()
    global key
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
        elif version == "Random":
            try:
                if getKey == "":
                    randomDict, key2 = randomGen()
                    key.set(key2)
                    key2 = ''
                    totranslate = encodeRandom(message, randomDict)
                    getKey = ""
                    randomDict = {}
                else:
                    totranslate = encodeRandom(message, generatefromkey(getKey))
                    getKey = ""
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
        elif version == "Random":
            if getKey == "":
                keyMissingError()
            else:
                totranslate = decodeRandom(message, generatefromkey(getKey))
    T.insert(tkinter.END, totranslate)
    link.config(state=tkinter.NORMAL)
    keyDisplay.config(state=tkinter.NORMAL)
    link.delete(1.0, tkinter.END)
    keyDisplay.delete(1.0, tkinter.END)
    mode2 = mode.get()
    link.insert(1.0, "Last Translation: (" + mode2 + " Mode) " + message + " <-> " + totranslate)
    currentTranslation = "(" + mode2 + " Mode) " + message + " <-> " + totranslate
    keyDisplay.insert(1.0, str(key.get()))
    key.set("")
    link.config(state=tkinter.DISABLED)
    keyDisplay.config(state=tkinter.DISABLED)


def saveTranslation():
    global currentTranslation
    saves.config(state=tkinter.NORMAL)
    saves.insert(tkinter.END, currentTranslation)
    saves.insert(tkinter.END, "\n\n")
    saves.config(state=tkinter.DISABLED)



def openTrans():
    translations.deiconify()


def closeTrans():
    translations.withdraw()


def copyKey():
    root.clipboard_clear()
    root.clipboard_append(keyDisplay.get(1.0, tkinter.END))


Encode = tkinter.Radiobutton(root, text='Encode', variable=lol, value="Encode", indicatoron=0, width=42, selectcolor="light green").grid(row=1, column=0, sticky=tkinter.W)
Decode = tkinter.Radiobutton(root, text='Decode', variable=lol, value="Decode", indicatoron=0, width=42, selectcolor="light green").grid(row=1, column=1, sticky=tkinter.E)
Regular = tkinter.Radiobutton(root, text='Regular', variable=mode, value="Regular", indicatoron=0, width=42, selectcolor="cyan").grid(row=4, column=0, sticky=tkinter.W)
Reversed = tkinter.Radiobutton(root, text='Reversed', variable=mode, value="Reversed", indicatoron=0, width=42, selectcolor="cyan").grid(row=4, column=1, sticky=tkinter.E)
Random = tkinter.Radiobutton(root, text="Use Random Dictionary", variable=mode, value="Random", indicatoron=0, width=42, selectcolor="gold").grid(row=5, column=0, sticky=tkinter.N)
RandomEncode = tkinter.Entry(root, width=48)
RandomEncode.grid(row=5, column=1)
J = tkinter.Scale(root, state=tkinter.DISABLED, length=600, troughcolor="black", width=1, orient=tkinter.HORIZONTAL, showvalue=0, sliderlength=200, label="--------------------------------------------------------Mode--------------------------------------------------------")
J.set(100)
J.grid(row=0, sticky=tkinter.N, columnspan=2)

R = tkinter.Scale(root, state=tkinter.DISABLED, length=500, troughcolor="black", width=1, orient=tkinter.HORIZONTAL, showvalue=0, sliderlength=200, label="--------------------------------------------Key Sets--------------------------------------------")
R.set(100)
R.grid(row=3, sticky=tkinter.N, columnspan=2)

T = tkinter.Entry(root, width=100)
L = tkinter.Scale(root, state=tkinter.DISABLED, length=500, troughcolor="black", width=1, orient=tkinter.HORIZONTAL, showvalue=0, sliderlength=200, label="------------------------------------------Input Below------------------------------------------")
L.set(100)
L.grid(row=6, sticky=tkinter.N, columnspan=2)
T.grid(row=7, column=0, sticky=tkinter.W, columnspan=2)

X = tkinter.Scale(root, state=tkinter.DISABLED, length=500, troughcolor="black", width=1, orient=tkinter.HORIZONTAL, showvalue=0, sliderlength=200)
X.set(100)
X.grid(row=8, sticky=tkinter.N, columnspan=2)

Translate = tkinter.Button(root, text="Translate", command=translate, width=42, activebackground="light green").grid(row=9, column=0, sticky=tkinter.W)
Quit = tkinter.Button(root, text="Quit", command=root.quit, width=85, activebackground="red").grid(row=10, columnspan=2, sticky=tkinter.E)
T.insert(tkinter.END, "")
Help = tkinter.Button(root, text="Help", command=showHelp, width=42, activebackground="blue").grid(row=9, column=1)

X = tkinter.Scale(root, state=tkinter.DISABLED, length=600, troughcolor="black", width=1, orient=tkinter.HORIZONTAL, showvalue=0, sliderlength=200)
X.set(100)
X.grid(row=11, sticky=tkinter.N, columnspan=2)

link = scrolledtext.ScrolledText(root, width=65, height=5, wrap="word", font="consolas", state=tkinter.DISABLED)
link.grid(row=12, sticky=tkinter.W, columnspan=2)

save = tkinter.Button(root, text="Save this translation", command=saveTranslation, width=42, activebackground="light green").grid(row=13, column=0, sticky=tkinter.N)
copy = tkinter.Button(root, text="Copy this key", command=copyKey, width=42, activebackground="light green").grid(row=13, column=1, sticky=tkinter.N)
openTranslations = tkinter.Button(root, text="Open Saved Translations", command = openTrans, width=85, activebackgroun="light green").grid(row=14, column=0, columnspan=2, sticky=tkinter.N)


keyDisplay = scrolledtext.ScrolledText(root, height=0.5, width=73, wrap="word", state=tkinter.DISABLED)
keyDisplay.grid(row=15, sticky=tkinter.W, columnspan=2)

info = tkinter.Label(root, text="Created by Khang Nguyen and Luzgog. Github link: https://github.com/PG-Development/Fibonacci-Encoder")
info.grid(row=16, sticky=tkinter.E, columnspan=2)

# help window below

title = tkinter.Label(help, text="Help Menu").grid(row=0, sticky=tkinter.N)
helpText = scrolledtext.ScrolledText(help, width=65, height=20, wrap="word")
helpText.grid(row=1, sticky=tkinter.N)
helpText.insert(1.0, "Thanks for downloading this encoder! My team and I have worked hard on it. \n \n"
                     "Important: When you want to close this, do NOT press the x at the top right. Press the exit help menu button at the bottom.\n \n"
                     "When you download this repository, you should have gotten 2 .py files: the Fibonacci_Encoder, and the Fibonacci GUI Version file. "
                     "Make sure they are in the same folder. The GUI Version is the much more convenient version of this program, but it uses the same functions. "
                     "When you open up the GUI file, you should see a small window pop up on your screen. This is the main application window, built with tkinter. "
                     "You select your mode at the top, choosing from either Encode, Decode, or Decode from Random. To encode from a random, select Encode from random in the keysets. "
                     "Below those, you should see keysets. You have regular, reversed, and encode from random. Next to both of the random choices you see inputs. "
                     "Below the modes and keysets you see an input, to place your text inside, and this is where the message will come out. \n \n"
                     "Regular Mode\n"
                     "Regular mode is the base mode of this encoder. It uses a set dictionary of keys and items, to encode your message. "
                     "To use this mode, simply choose the \"Encode\" mode and the \"Regular\" Keyset. Once you press translate, your message will be replaced "
                     "by the encoded version. Below your output, there is a last translation box which shows you the original. "
                     "To decode, just switch your mode to decode, and input the code you received from your friend into the box. "
                     "It should change before your very eyes into comprehensible text.\n\n"
                     "Reversed Mode\n"
                     "Reversed mode is a separate, different keyset then the regular mode. It takes the code for a letter, and switches it around to the opposite letter. "
                     "For example, the code for a is now the code for z, and the code for b is now the code for y. This means the code for z is now the code for a, and so on. "
                     "To use this keyset, choose which mode you want, and then instead of selecting the \"Regular\" keyset, choose the \"Reversed\" keyset.\n\n"
                     "Random Mode\n"
                     "Random Mode scrambles the codes for the letters to random locations. The total number of possible dictionaries is 403,291,461,126,605,635,584,000,000, aka 403 septillion. "
                     "That's a lot of possible combinations! And every time you use it, it generates a random choice. Now, that's cool, but say you want to retrieve an already generated "
                     "dictionary. That's easy! You see, whenever you generate a new dictionary, a key will appear in the lower text box. Just press the \"Copy this key\" buttton "
                     "to copy the key.\n\n"
                     "To encode using this mode, you first select the \"Encode\" Button. Then select the \"Use Random Dictionary\" choice. If you already have a key, put it in the "
                     "entry box next to the button. If you do not have a key, simply leave the box blank. Then press translate. You should get a result and a key. If you want to now encode "
                     "more messages using the same key, just copy the key and put it in the box. When you send messages to someone else, send them the key privately, so then you can"
                     " send them the message in public and other people will get gibberish.\n\n"
                     "To decode using this mode, you must have a key, or else you will get an error. Put the key in the box next to \"Use Random Dictionary\". Then select \"Decode\" "
                     "and \"Use Random Dictionary\". Finally, put in the message in the lower entry box. When you press Translate, you should get a good message.")
helpText.tag_add("important", "3.0", "3.9")
helpText.tag_add("regularTag", "7.0", "7.12", "10.0", "10.13", "13.0", "13.12")
helpText.tag_config("important", foreground="red", font=("Consolas", 13, "bold", "italic"))
helpText.tag_config("regularTag", foreground="blue", font=("Consolas", 12, "bold", "italic"))
helpText.config(state=tkinter.DISABLED)
closeHelpButton = tkinter.Button(help, text="Exit Help Menu", command=closeHelp, activebackground="red").grid(row=2, sticky=tkinter.N)

# saved translations below

titleTrans = tkinter.Label(translations, text="Saved Translations").grid(row=0, sticky=tkinter.N)
saves = scrolledtext.ScrolledText(translations, width=65, height=20, wrap="word")
saves.grid(row=1, sticky=tkinter.N)
saves.config(state=tkinter.DISABLED)
closeTransButton = tkinter.Button(translations, text="Exit Saved Translations", command=closeTrans, activebackground="red").grid(row=2, sticky=tkinter.N)

tkinter.mainloop()