
#help for Tkinter https://tkdocs.com/tutorial/ 
from tkinter import *
from GridDisplay import gridDisplay
from matplotlibGraphs import chartManager


import matplotlib

matplotlib.use('TkAgg')

#help from https://www.pythontutorial.net/tkinter/tkinter-matplotlib/ 
#for creating bar charts and integrating them to tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)

def handleClicks(event):
    spreadSheetView.resetDrag()
    spreadSheetView.cancelCellEdit()
    if event.widget._name == "gridCanvas":
        if event.state != 1:
            spreadSheetView.editCell(event)
        elif event.state == 1:   
            spreadSheetView.select(event.x, event.y, "lightblue")
    elif event.widget.widgetName == "chartWidget":
         event.widget.focus_set()

def handleMovement(event):
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

def setXValuesForNextChart():
    
    global xValuesForChart
    xValuesForChart = []
    for key in spreadSheetView.dragSelectedValues:
        xValuesForChart.append(spreadSheetView.cellGridValues[key])
        
def setYValuesForNextChart():
    global yValuesForChart
    yValuesForChart = []
    for key in spreadSheetView.dragSelectedValues:
        yValuesForChart.append(spreadSheetView.cellGridValues[key])


def createNewChart():
    global xValuesForChart
    global yValuesForChart
    canvasChartManager.addNewBarChart("Hello World", "title of x", "title of y", xValuesForChart, yValuesForChart, 20, 10, 50, 500, 500)

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


    pointedWidget = None
    gridWidth = 100
    gridHeight = 100
    cellWidth = 200
    cellHeight = 50
    cellDisplayTextOffsetpxX = 1
    cellDisplayTextOffsetpxY = 3
    fontsize = 12
    maxLettersInCell = 20

    MainCanvasContainer = Frame(root, bg="white")
    MainCanvasContainer.grid(column=0, row=0, sticky=N+W+S+E)
    MainCanvasContainer.columnconfigure(0, weight=1)
    MainCanvasContainer.rowconfigure(0, weight=1)
    hbar=Scrollbar(MainCanvasContainer, orient=HORIZONTAL)
    vbar=Scrollbar(MainCanvasContainer, orient=VERTICAL)

    gridCanvas = Canvas(MainCanvasContainer, bg="white", xscrollcommand = hbar.set, yscrollcommand=vbar.set, name="gridCanvas")
    gridCanvas.grid(column=0, row=0, sticky=N+W+S+E)
    spreadSheetView = gridDisplay(gridCanvas, gridWidth, gridHeight, cellWidth, cellHeight, cellDisplayTextOffsetpxX, cellDisplayTextOffsetpxY, fontsize, maxLettersInCell)


    vbar.config(command=handleYScroll)
    vbar.grid(column=1, row=0, sticky=N+S)


    hbar.config(command=handleXScroll)
    hbar.grid(column=0, row=1, sticky=E+W)


    
    canvasChartManager = chartManager(gridCanvas)
  
   
    canvasConfigurerView = Frame(root, width=300, bg="white")
    canvasConfigurerView.grid(column=2, row=0, sticky=N+W+S+E)

    barChartConfigurerView = Frame(canvasConfigurerView)
    barChartConfigurerView.grid(column=0, row=0)

    xValuesForChart = []
    setXValuesForChart = Button(barChartConfigurerView, text="aseta valinta kaavion X arvoksi", command= lambda: setXValuesForNextChart())
    setXValuesForChart.grid(column=0, row=1)
    
    yValuesForChart = []
    setYValuesForChart = Button(barChartConfigurerView, text="aseta valinta kaavion Y arvoksi", command= lambda: setYValuesForNextChart())
    setYValuesForChart.grid(column=0, row=2)
    
    
    addNewBarChartButton = Button(barChartConfigurerView, text="Lisaa uusi pylvaskaavio", command=lambda: createNewChart())
    addNewBarChartButton.grid(column=0, row=3)


    gridCanvas.configure(scrollregion = [0, 0, gridWidth*cellWidth, gridHeight*cellHeight])
    
    root.bind('<1>', lambda event: handleClicks(event))
    gridCanvas.bind('<Motion>', lambda event: handleMovement(event))
    root.mainloop()