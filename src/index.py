
from doctest import master
from tkinter import *


from GridDisplay import gridDisplay
from matplotlibGraphs import chartManager
from BarChart import barChart

#help for Tkinter https://tkdocs.com/tutorial/ 
import matplotlib

matplotlib.use('TkAgg')

#help from https://www.pythontutorial.net/tkinter/tkinter-matplotlib/ 
#for creating bar charts and integrating them to tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)

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
      

def handleXScroll(a, b):
    gridCanvas.xview(a, b)
    canvasChartManager.updateAllCharts()  
    return
def handleYScroll(a, b):
    gridCanvas.yview(a, b)
    canvasChartManager.updateAllCharts()
  
    return

if __name__ == "__main__":
    root = Tk()
    root.option_add('*tearOff', False)
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

    MainCanvas = Canvas(root, bg="white")
    MainCanvas.grid(column=0, row=0, sticky=N+W+S+E)
    MainCanvas.columnconfigure(0, weight=1)
    MainCanvas.rowconfigure(0, weight=1)

    gridCanvas = Canvas(MainCanvas, bg="white", xscrollcommand = hbar.set, yscrollcommand=vbar.set)
    gridCanvas.grid(column=0, row=0, sticky=N+W+S+E)
    spreadSheetView = gridDisplay(gridCanvas, gridWidth, gridHeight, cellWidth, cellHeight, cellDisplayTextOffsetpxX, cellDisplayTextOffsetpxY, fontsize, maxLettersInCell)


    vbar.config(command=handleYScroll)
    vbar.grid(column=1, row=0, sticky=N+S)


    hbar.config(command=handleXScroll)
    hbar.grid(column=0, row=1, sticky=E+W)


    
    canvasChartManager = chartManager(gridCanvas)
    chartCanvas = canvasChartManager.addNewBarChart("Hello World", "title of x", "title of y", [1,2,3,4], [10,20,30,40], 6, 4, 50, 500, 500)
   
    gridCanvas.configure(scrollregion = [0, 0, gridWidth*cellWidth, gridHeight*cellHeight])
    gridCanvas.bind('<1>', lambda event: handleclicks(event))
    gridCanvas.bind('<Motion>', lambda event: handleMovement(event))

    root.mainloop()