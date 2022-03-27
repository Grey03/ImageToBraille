try:
    from tkinter import *
    import tkinter as tk
    from tkinter import filedialog
except:
    crashed = input("tkinter could not import")

import imgttalgo

global FinX
FinX = 0
global FinY
FinY = 0
global filename
global saveLoc

def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("PNGs",
                                                        "*.png*"),
                                                       ("JPGs",
                                                        "*.jpg*")))

    label_file_explorer.configure(text="Selected File: " + filename)

def saveLocation():
    global saveLoc
    saveLoc = filedialog.askdirectory()
    label_save_explorer.configure(text = "Selected File: " + saveLoc)
     
#actual stuff start here
root = Tk()
root.title("Image To Text Generator V2.0")



#-----Buttns n stuffs----

#File Stuff
label_file_explorer = Label(root, text = "Choose Image *")
button_explore = Button(root, text = "Browse Files", command = browseFiles)

label_save_explorer = Label(root, text = "Choose Save Location *")
button_saveLoc = Button(root, text = "Save Location", command = saveLocation)

#Change Dimension Stuff
global ChangeDi
changeDi = IntVar()
changeDiBox = Checkbutton(root, text="Change Dimensions", variable=changeDi)
DimXLabel = Label(root, text = "Enter Desired X")
global DimensionX
DimensionX = Entry(root, text="X")
DimYLabel = Label(root, text = "Enter Desired Y")
global DimensionY
DimensionY = Entry(root, text="Y")

#Invert
global Invert
Invert = IntVar()
InvertBox = Checkbutton(root, text="Invert text", variable=Invert)

#Contrast
contrastLabel = Label(root,text="Contrast Level")
global contrast
contrast = Scale(root, from_=1, to=255, orient=HORIZONTAL)
contrast.set(128)

#Generate Button
#ADDDDDDDDDDDD THE GENERATE FUNCTION HEREERERE!!!
def sendconvert():
    global filename
    global saveLoc
    global changeDi
    global FinX
    global FinY
    global Invert
    global contrast


    if (filename == None):
        browseFiles()
    if (saveLoc == None):
        saveLocation()

    if (changeDi == 1 and FinX == None or FinY == None):
        print ("No X or Y for Changed Dimension")
        changeDi = 0
    else:

        Default = {
        "filename": filename,
        "savelocation": saveLoc,
        "changeDimensions": changeDi.get(),
        "FinalX": DimensionX.get(),
        "FinalY": DimensionY.get(),
        "Invert": Invert.get(),
        "Contrast": contrast.get()
        }
        imgttalgo.ImgToTxt(Default)

Generate = Button(root, text="Generate Text", command=sendconvert)

#----Positions!----
label_file_explorer.grid(row = 0, column = 0)
button_explore.grid(row = 1, column = 0)

label_save_explorer.grid(row = 0, column = 1)
button_saveLoc.grid(row = 1, column = 1)


changeDiBox.grid(row = 2, column = 0)

DimXLabel.grid(row = 3, column = 0)
DimYLabel.grid(row = 3, column = 1)
DimensionX.grid(row = 4, column = 0)
DimensionY.grid(row = 4, column = 1)

InvertBox.grid(row=5, column = 0)

contrastLabel.grid(row=6, column = 0)
contrast.grid(row=7, column = 0)

Generate.grid(row=8, column = 0)

root.mainloop()