
from tkinter import *
from gridDisplay import gridDisplay

#Tkinterin käyttöön otettua apua https://tkdocs.com/tutorial/ 

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

gridCanvas.configure(scrollregion = [0, 0, gridWidth*cellWidth, gridHeight*cellHeight])
gridCanvas.bind('<1>', lambda event: spreadSheetView.onClick(event))
gridCanvas.bbox("all")


root.mainloop()