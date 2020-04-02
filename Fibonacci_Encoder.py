#Copyright 2019 by Khang Nguyen and Timothy Merrill

#How to use:
#Run the program.
#It will ask you to decode or encode.
#Type de for decode, and en for encode.
#Then type your message. While encoding,
#you can use most punctuation except an
#apostrophe. You can use commas and other
#punctuation. While decoding, you just paste
#the message you got in the prompt.

#When you try to encode an apostrophe, it works as expected.
#However the decoder will not work if there is one.
#This is being fixed soon.

#Please credit me as the original author if you are making something using this.
#Thanks! :)

keys = {" ": "|", "a": "2.", "b": "3.", "c": "5.", "d": "8.", "e": "13.", "f": "21.", "g": "34.", "h": "55.","i": "89.", "j": "144.", "k": "233.", "l": "377.", "m": "610.", "n": "987.", "o": "1597.", "p": "2584.","q": "4181.", "r": "6765.", "s": "10946.","t": "17711.", "u": "28657.", "v": "46368.", "w": "75025.", "x": "121393.", "y": "196418.", "z": "317811.","!": "!", ",": ",", "?": "?", "'": "'.", "|": "|", ":": ":", "": "", "-": "-."}
dekeys = {v: k for k, v in keys.items()}
cdekeys = {k.replace('.', ''): v for k, v in dekeys.items()}

def encode(message):
    totranslate = message.lower()
    totranslate = totranslate.replace(".", "|||")
    for item in totranslate:
        totranslate = totranslate.replace(item, str(keys[item]))
        totranslate = totranslate.replace(".|", "|")
    if totranslate[-1] == ".":
        totranslate = totranslate[:len(totranslate) - 1]
    return totranslate
def decode(message):
    totranslate = message.replace("|||", "~")
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
    return "".join(translist)
if __name__ == '__main__': #executed only if you use the file directly and not by importing it
    complete = False
    decodeNames = ["de", "decode", "De", "Decode", "d", "D"]
    encodeNames = ["en", "encode", "En", "Encode", "e", "E"]
    while complete == False:
        task = str(input("Decode or encode?"))
        if task in encodeNames:
            print("Give me your message")
            message = str(input(""))
            print(encode(message))
    
        elif task in decodeNames:
            print("Give me your message")
            message = str(input(""))
            print(decode(message))
      
        else:
            print("You did not choose a valid action.")
        print("Another task? Y or N")
        again = input()
        if again in ["No","N", "n", "no"]:
            complete= True
