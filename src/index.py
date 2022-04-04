








from cgitb import text
from threading import currentThread
from tkinter import *
import math
#from tkinter import ttk
#from tkinter import _XYScrollCommand
from tkinter import ttk
from webbrowser import get



root = Tk()
root.option_add('*tearOff', FALSE)
root.title("Taulukkolaskentasovellus")
root.geometry("500x500")
root.configure(background='SteelBlue1')

menubar = Menu(root)
root['menu'] = menubar
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

menu_file = Menu(menubar)
menubar.add_cascade(menu=menu_file, label='Tiedosto')

menu_edit = Menu(menubar)
menubar.add_cascade(menu=menu_edit, label='Muokkkaa')
width = 10

vbar=Scrollbar(root,orient=HORIZONTAL)



gridCanvas = Canvas(root, bg="white", height=250, width=300, xscrollcommand = vbar.set)
#viewPort = Frame(gridCanvas, height=1000, width=1000)
#gridCanvas.create_window(0, 0, window=viewPort)


gridCanvas.grid(column=0, row=0, sticky=W+E+S+N)



vbar.config(command=gridCanvas.xview)

vbar.grid(column=0, row=1, sticky=EW)
columnwidth = 100
columnHeight = 16

def clipToGrid(firstx, firsty):
    x = firstx - firstx % columnwidth
    y = firsty - firsty  % columnHeight
    return (x, y)
def generatePreviewText(text, maxLenght):
    return text.replace("\n", "")[:maxLenght]
    


TextEditorCanvasId = None
TextEditorCanvasWidget = None
DisplayTextToEdit = None
def onclick(event):
    global TextEditorCanvasId
    global cellGridValues
    global DisplayTextToEdit
    global TextEditorCanvasWidget
    virtualCoords = clipToGrid(gridCanvas.canvasx(event.x), gridCanvas.canvasy(event.y))
    screenCoords = clipToGrid(event.x, event.y)
    if TextEditorCanvasId != None and TextEditorCanvasWidget != None and cellGridValues != None and DisplayTextToEdit != None:
        newText = TextEditorCanvasWidget.get("1.0", END)
        gridCanvas.itemconfig(DisplayTextToEdit, text=generatePreviewText(newText, 10))
        cellGridValues[DisplayTextToEdit] = newText
        gridCanvas.delete(TextEditorCanvasId)
        TextEditorCanvasId = None
    
   

    displayTextBoxId = gridCanvas.find_closest(screenCoords[0], screenCoords[1])
    DisplayTextToEdit = displayTextBoxId[0]+1
    textOfDisplayBox = cellGridValues[DisplayTextToEdit]
    TextEditorCanvasWidget = Text(gridCanvas, state=NORMAL)
    TextEditorCanvasWidget.insert("1.0", textOfDisplayBox)
   
    TextEditorCanvasWidget.focus_set()
    TextEditorCanvasId = gridCanvas.create_window(virtualCoords[0], virtualCoords[1],width=columnwidth, height=columnHeight*2, anchor=NW, window=TextEditorCanvasWidget)
    
    



cellGridValues = {}
for column in range(100):
    for row in range(100):
      
    #    EditText = Text(gridCanvas)
        
     #   gridCanvas.create_window(column*columnwidth, row*columnHeight, window=EditText)
       placeholder = "kokeilu"
       newCell = gridCanvas.create_rectangle(column*columnwidth, row*columnHeight, column*columnwidth+columnwidth, row*columnHeight+columnHeight, tags=("clickable"))        
       newCellText = gridCanvas.create_text(column*columnwidth, row*columnHeight+2, text=placeholder, anchor=NW, justify=LEFT, width=columnwidth-5)
       cellGridValues[newCellText] = placeholder
       
    

gridCanvas.configure(scrollregion = [0,0,100*columnwidth, 100*columnHeight])
gridCanvas.bind('<1>', onclick)



root.mainloop()