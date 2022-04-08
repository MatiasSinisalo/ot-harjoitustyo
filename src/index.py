
from tkinter import *
from GridDisplay import gridDisplay
from matplotlibGraphs import chartManager
from CustomEvent import event
#help for Tkinter https://tkdocs.com/tutorial/ 

root = Tk()
root.option_add('*tearOff', FALSE)
root.title("Taulukkolaskentasovellus")
root.geometry("500x500")
root.configure(background='SteelBlue1')

menubar = Menu(root)
root['menu'] = menubar
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

def handleclicks(event):
    if event.state != 1:
        spreadSheetView.editCell(event)
    elif event.state == 1:
        spreadSheetView.deselect()
        spreadSheetView.select(event.x, event.y, "lightblue")

def handleMovement(event):
    #event.state = 257 
    if event.state == 257:
        spreadSheetView.select(event.x, event.y, "lightblue")
       

menu_file = Menu(menubar)
menubar.add_cascade(menu=menu_file, label='Tiedosto')

menu_edit = Menu(menubar)
menubar.add_cascade(menu=menu_edit, label='Muokkkaa')


hbar=Scrollbar(root, orient=HORIZONTAL)
vbar=Scrollbar(root, orient=VERTICAL)

gridWidth = 100
gridHeight = 100
cellWidth = 200
cellHeight = 50
cellDisplayTextOffsetpxX = 1
cellDisplayTextOffsetpxY = 3
fontsize = 12
maxLettersInCell = 20
gridCanvas = Canvas(root, bg="white", height=250, width=300, xscrollcommand = hbar.set, yscrollcommand=vbar.set)
gridCanvas.grid(column=0, row=0, sticky=W+E+S+N)
spreadSheetView = gridDisplay(gridCanvas, gridWidth, gridHeight, cellWidth, cellHeight, cellDisplayTextOffsetpxX, cellDisplayTextOffsetpxY, fontsize, maxLettersInCell)


vbar.config(command=gridCanvas.yview)
vbar.grid(column=1, row=0, sticky=N+S)


hbar.config(command=gridCanvas.xview)
hbar.grid(column=0, row=1, sticky=E+W)



canvasChartManager = chartManager(gridCanvas)
chartCanvas = canvasChartManager.addNewBarChart("Hello World", "title of x", "title of y", [1,2,3,4], [10,20,30,40], 6, 4, 100)
chartCanvas.grid(row=2, column=0)



gridCanvas.configure(scrollregion = [0, 0, gridWidth*cellWidth, gridHeight*cellHeight])
gridCanvas.bind('<1>', lambda event: handleclicks(event))
gridCanvas.bind('<Motion>', lambda event: handleMovement(event))

root.mainloop()