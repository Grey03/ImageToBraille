#http://xahlee.info/comp/unicode_braille.html
#https://home.unicode.org/
#https://www.tutorialspoint.com/working-with-images-in-python
#https://www.geeksforgeeks.org/python-pil-getpixel-method/

import math
import os
import os.path

from PIL import Image

    #Needs to take in the file name, dimensions if needed, invert y/n, contrast
    #then does the old algorithm 
    #then opens the txt for you

def ImgToTxt(info):
    filename = (info["filename"])
    savelocation = (info["savelocation"])
    changeDimensions = (info["changeDimensions"])
    finalX = (info["FinalX"])
    finalY = (info["FinalY"])
    global Invert
    Invert = (info["Invert"])
    global ContrastSetting
    ContrastSetting = (info["Contrast"])

    try:
        image = Image.open(filename).convert("L")
    except:
        print ("Invalid File-type")

    #-----FUNCTIONS-----

    #Img Resize
    def correctSize(img):
        while img.size[0] * img.size[1] > 3000000:
            img = img.resize((math.ceil(img.size[0]/2),math.ceil(img.size[1]/2)))
        while (img.size[0]%2 != 0):
            img = img.resize((img.size[0] + 1, img.size[1]))
        while (img.size[1]%3 != 0):
            img = img.resize((img.size[0], img.size[1] + 1))

        return (img)

    def chunkAnalyzer(chunklist):
        global ContrastSetting
        global Invert 
        thelist = [
        chunklist[5],
        chunklist[3],
        chunklist[1],
        chunklist[4],
        chunklist[2],
        chunklist[0]
      ]
        temp = ("")
        for n in range(len(thelist)):
            if thelist[n] >= ContrastSetting:
                thelist[n] = 1 - Invert
            else:
                thelist[n] = 0 + Invert
        for i in range(len(thelist)):
            temp = (str(temp) + str(thelist[i]))
        temp = int(temp,2)
        temp = (temp + 10240)
        return (chr(temp))


    #Chunk Maker
    def mainAlgo(img):  
        temp = []
        temp2 = []
        for y in range(0,img.size[1],3):
            temp.append(temp2)
            temp2 = []
            for x in range(0,img.size[0],2):
                chunk = [
                (img.getpixel((x,y))),
                (img.getpixel((x + 1,y))),
                (img.getpixel((x,y + 1))),
                (img.getpixel((x + 1,y + 1))),
                (img.getpixel((x,y + 2))),
                (img.getpixel((x + 1,y + 2)))
                ]
                temp2.append(chunkAnalyzer(chunk))
        return (temp)

    #-----RUN-----

    #Resize img
    image = correctSize(image) 
    if (finalX != None and finalY != None and int(changeDimensions) == 1):
        print ("RESIZE")
        image = image.resize((int(finalX) * 2, int(finalY) * 3))

        
        

    final = mainAlgo(image)

    final.pop(0)

    #final = (["test","test"],["test","test"])

    with open(str(savelocation) + "/output.txt", "w", encoding='utf-8') as f:
      for y in range(len(final)):
        if y != 0:
          f.write("\n")
        for x in range(len(final[0])):
            f.write((final[y][x]))
    os.startfile(str(savelocation) + "/output.txt")