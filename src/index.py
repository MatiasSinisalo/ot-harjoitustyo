
# help for Tkinter https://tkdocs.com/tutorial/

from tkinter import E, HORIZONTAL, N, S, VERTICAL, W, Button, Canvas, Frame, Label, Menu, Scrollbar, Text, Tk
from grid_display import GridDisplay
from matplotlib_graphs import ChartManager


def handle_clicks(event):
    if event.widget.widgetName == "gridCanvas":
        spreadSheetView.reset_drag()
        spreadSheetView.cancel_cell_edit()
        if event.state != 1:
            spreadSheetView.edit_cell(event)
        elif event.state == 1:
            spreadSheetView.select(event.x, event.y, "lightblue")
    elif event.widget.widgetName == "chartWidget":
        event.widget.focus_set()


def handle_movement(event):
    if event.state == 257:
        spreadSheetView.select(event.x, event.y, "lightblue")


def handle_x_scroll(a_val, b_val):
    gridCanvas.xview(a_val, b_val)
    canvasChartManager.update_all_charts()


def handle_y_scroll(a_val, b_val):
    gridCanvas.yview(a_val,  b_val)
    canvasChartManager.update_all_charts()


def set_x_values_for_next_chart():

    global x_values_for_chart
    x_values_for_chart = []
    for key in spreadSheetView.drag_selected_values:
        x_values_for_chart.append(spreadSheetView.cell_grid_values[key])


def set_y_values_for_next_chart():
    global y_values_for_chart
    y_values_for_chart = []
    for key in spreadSheetView.drag_selected_values:
        y_values_for_chart.append(spreadSheetView.cell_grid_values[key])


def create_new_chart():
    canvasChartManager.add_new_bar_chart(
        "Hello World", "title of x", "title of y",
        x_values_for_chart, y_values_for_chart, 20, 10, 50, 500, 500)

def setAnswerTextToSum():
    answer = spreadSheetView.GetSumOfSelection()
    sumResultText.config(text = answer)

def setAnswerTextToAverage():
    answer = spreadSheetView.GetAverageOfSelection()
    averageResultText.config(text = answer)

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

    

    main_canvas_container = Frame(root, bg="white")
    main_canvas_container.grid(column=0, row=0, sticky=N+W+S+E)
    main_canvas_container.columnconfigure(0, weight=1)
    main_canvas_container.rowconfigure(0, weight=1)
    hbar = Scrollbar(main_canvas_container, orient=HORIZONTAL)
    vbar = Scrollbar(main_canvas_container, orient=VERTICAL)


    POINTED_WIDGET = None
    GRID_WIDTH = 100
    GRID_HEIGHT = 100
    CELL_WIDTH = 200
    CELL_HEIGHT = 50
    CELL_DISPLAY_TEXT_OFFSET_PX_X = 1
    CELL_DISPLAY_TEXT_OFFSET_PX_Y = 3
    FONT_SIZE = 12
    MAX_LETTERS_IN_CELL = 20
    gridCanvas = Canvas(main_canvas_container, bg="white",
                        xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    gridCanvas.widgetName = "gridCanvas"
    gridCanvas.grid(column=0, row=0, sticky=N+W+S+E)
    spreadSheetView = GridDisplay(gridCanvas, GRID_WIDTH, GRID_HEIGHT, CELL_WIDTH, CELL_HEIGHT,
                                  CELL_DISPLAY_TEXT_OFFSET_PX_X, CELL_DISPLAY_TEXT_OFFSET_PX_Y,
                                  FONT_SIZE, MAX_LETTERS_IN_CELL)
    
    gridCanvas.configure(
        scrollregion=[0, 0, GRID_WIDTH*CELL_WIDTH, GRID_HEIGHT*CELL_HEIGHT])

    vbar.config(command=handle_y_scroll)
    vbar.grid(column=1, row=0, sticky=N+S)

    hbar.config(command=handle_x_scroll)
    hbar.grid(column=0, row=1, sticky=E+W)

    canvasChartManager = ChartManager(gridCanvas)

    canvasConfigurerView = Frame(root, width=300, bg="white")
    canvasConfigurerView.grid(column=2, row=0, sticky=N+W+S+E)

    barChartConfigurerView = Frame(canvasConfigurerView, width=300, bg="lightgray")
    barChartConfigurerView.grid(column=0, row=0, pady=10, padx=10)

    x_values_for_chart = [0]
    setXValuesForChart = Button(
        barChartConfigurerView, text="aseta valinta kaavion X arvoksi",
        command=lambda: set_x_values_for_next_chart())
    setXValuesForChart.grid(column=0, row=1)

    y_values_for_chart = [0]
    setYValuesForChart = Button(
        barChartConfigurerView, text="aseta valinta kaavion Y arvoksi",
        command=lambda: set_y_values_for_next_chart())
    setYValuesForChart.grid(column=0, row=2)

    addNewBarChartButton = Button(
        barChartConfigurerView, text="Lisaa uusi pylvaskaavio",
        command=lambda: create_new_chart())
    addNewBarChartButton.grid(column=0, row=3)

    calculationsView = Frame(canvasConfigurerView, width=300, bg="lightgray")
    calculationsView.grid(column=0, row=2,  sticky=N+W+S+E,  pady=10, padx=10)

    GetSumOfSelectionButton = Button(calculationsView, text="Laske valinnan summa", 
                                        command=setAnswerTextToSum)
    GetSumOfSelectionButton.grid(column=0, row=1, sticky=E+W)
    
    sumResultText = Label(calculationsView)
    sumResultText.grid(column=0, row=2, sticky=E+W)

    GetAverageOfSelectionButton = Button(calculationsView, text="Laske valinnan keskiarvo", 
                                        command=setAnswerTextToAverage)
    GetAverageOfSelectionButton.grid(column=0, row=3, sticky=E+W)
    
    averageResultText = Label(calculationsView)
    averageResultText.grid(column=0, row=4, sticky=E+W)
    

    
  
    root.bind('<1>', handle_clicks)
    gridCanvas.bind('<Motion>', handle_movement)
    root.mainloop()
