from tkinter import E, HORIZONTAL, N, S, VERTICAL, W, Button, Canvas, Frame, Label, Menu, Scrollbar, Text, Tk
from grid_display import GridDisplay
from graphs.matplotlib_graphs import ChartManager


class SpreadSheetApp:
    def __init__(self):
        self.x_values_for_chart = []
        self.y_values_for_chart = []
        

        self.root = Tk()
        self.root.option_add('*tearOff', False)
        self.root.title("Taulukkolaskentasovellus")
        self.root.geometry("500x500")
        self.root.configure(background='SteelBlue1')
        
    def init_front_end(self):
        

        self.main_canvas_container = Frame( self.root, bg="white")
        self.main_canvas_container.grid(column=0, row=0, sticky=N+W+S+E)
        self.main_canvas_container.columnconfigure(0, weight=1)
        self.main_canvas_container.rowconfigure(0, weight=1)

        self.init_menu_bar()
        self.init_grid_scrollBars()
        self.init_grid()
        self.canvasChartManager = ChartManager(self.gridCanvas)
        self.init_canvas_config_view()
        self.init_bind_events()

        self.root.mainloop()
    
    def handle_clicks(self, event):
        if event.widget.widgetName == "gridCanvas":
            self.spreadSheetView.reset_drag()
            self.spreadSheetView.cancel_cell_edit()
            if event.state != 1:
                self.spreadSheetView.edit_cell(event)
            elif event.state == 1:
                self.spreadSheetView.select(event.x, event.y, "lightblue")
        elif event.widget.widgetName == "chartWidget":
            event.widget.focus_set()

    def handle_movement(self, event):
        if event.state == 257:
            self.spreadSheetView.select(event.x, event.y, "lightblue")

    def handle_x_scroll(self, a_val, b_val):
        self.gridCanvas.xview(a_val, b_val)
        self.canvasChartManager.update_all_charts()

    def handle_y_scroll(self, a_val, b_val):
        self.gridCanvas.yview(a_val,  b_val)
        self.canvasChartManager.update_all_charts()

    def set_x_values_for_next_chart(self):
        self.x_values_for_chart
        self.x_values_for_chart = []
        for key in self.spreadSheetView.drag_selected_values:
            self.x_values_for_chart.append(self.spreadSheetView.cell_grid_values[key])

    def set_y_values_for_next_chart(self):
        self.y_values_for_chart = []
        for key in self.spreadSheetView.drag_selected_values:
            self.y_values_for_chart.append(self.spreadSheetView.cell_grid_values[key])

    def create_new_bar_chart(self):
        self.canvasChartManager.add_new_bar_chart(
            "Hello World", "title of x", "title of y",
            self.x_values_for_chart, self.y_values_for_chart, 20, 10, 50, 500, 500)

    def create_new_pie_chart(self):
        self.canvasChartManager.add_new_pie_chart(
            "Hello World", "title of x", "title of y",
            self.x_values_for_chart, self.y_values_for_chart, 20, 10, 50, 500, 500)

    def setAnswerTextToSum(self):
        answer = self.spreadSheetView.GetSumOfSelection()
        self.sumResultText.config(text = answer)

    def setAnswerTextToAverage(self):
        answer = self.spreadSheetView.GetAverageOfSelection()
        self.averageResultText.config(text = answer)

    def init_grid(self):
        GRID_WIDTH = 100
        GRID_HEIGHT = 100
        CELL_WIDTH = 200
        CELL_HEIGHT = 50
        CELL_DISPLAY_TEXT_OFFSET_PX_X = 1
        CELL_DISPLAY_TEXT_OFFSET_PX_Y = 3
        FONT_SIZE = 12
        MAX_LETTERS_IN_CELL = 20
        
        self.gridCanvas = Canvas(self.main_canvas_container, bg="white",
                            xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        self.gridCanvas.widgetName = "gridCanvas"
        self.gridCanvas.grid(column=0, row=0, sticky=N+W+S+E)
        self.gridCanvas.configure(
            scrollregion=[0, 0, GRID_WIDTH*CELL_WIDTH, GRID_HEIGHT*CELL_HEIGHT])

        self.spreadSheetView = GridDisplay(self.gridCanvas, GRID_WIDTH, GRID_HEIGHT, CELL_WIDTH, CELL_HEIGHT,
                                    CELL_DISPLAY_TEXT_OFFSET_PX_X, CELL_DISPLAY_TEXT_OFFSET_PX_Y,
                                    FONT_SIZE, MAX_LETTERS_IN_CELL)

    def init_grid_scrollBars(self):
        self.hbar = Scrollbar(self.main_canvas_container, orient=HORIZONTAL)
        self.vbar = Scrollbar(self.main_canvas_container, orient=VERTICAL)
      
      
        self.vbar.config(command=self.handle_y_scroll)
        self.vbar.grid(column=1, row=0, sticky=N+S)

        self.hbar.config(command=self.handle_x_scroll)
        self.hbar.grid(column=0, row=1, sticky=E+W)
    
    def init_canvas_config_view(self):
       
        canvasConfigurerView = Frame(self.root, width=300, bg="white")
        canvasConfigurerView.grid(column=2, row=0, sticky=N+W+S+E)

        ChartConfigurerView = Frame(canvasConfigurerView, width=300, bg="lightgray")
        ChartConfigurerView.grid(column=0, row=0, pady=10, padx=10)

        setXValuesForChart = Button(
            ChartConfigurerView, text="aseta valinta kaavion X arvoksi",
            command=self.set_x_values_for_next_chart)
        setXValuesForChart.grid(column=0, row=1)

        setYValuesForChart = Button(
            ChartConfigurerView, text="aseta valinta kaavion Y arvoksi",
            command=self.set_y_values_for_next_chart)
        setYValuesForChart.grid(column=0, row=2)

        addNewBarChartButton = Button(
            ChartConfigurerView, text="Lisaa uusi pylvaskaavio",
            command=self.create_new_bar_chart)
        addNewBarChartButton.grid(column=0, row=3)

        addNewPieChartButton = Button(
            ChartConfigurerView, text="Lisaa uusi piirakkakaavio",
            command=self.create_new_pie_chart)
        addNewPieChartButton.grid(column=0, row=4)

        calculationsView = Frame(canvasConfigurerView, width=300, bg="lightgray")
        calculationsView.grid(column=0, row=2,  sticky=N+W+S+E,  pady=10, padx=10)

        GetSumOfSelectionButton = Button(calculationsView, text="Laske valinnan summa", 
                                            command=self.setAnswerTextToSum)
        GetSumOfSelectionButton.grid(column=0, row=1, sticky=E+W)
        
        self.sumResultText = Label(calculationsView)
        self.sumResultText.grid(column=0, row=2, sticky=E+W)

        GetAverageOfSelectionButton = Button(calculationsView, text="Laske valinnan keskiarvo", 
                                            command=self.setAnswerTextToAverage)
        GetAverageOfSelectionButton.grid(column=0, row=3, sticky=E+W)
        
        self.averageResultText = Label(calculationsView)
        self.averageResultText.grid(column=0, row=4, sticky=E+W)
        
    def init_bind_events(self):
        self.root.bind('<1>', self.handle_clicks)
        self.gridCanvas.bind('<Motion>', self.handle_movement)
        

    def init_menu_bar(self):
        menubar = Menu(self.root)
        self.root['menu'] = menubar
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        menu_file = Menu(menubar)
        menubar.add_cascade(menu=menu_file, label='Tiedosto')

        menu_edit = Menu(menubar)
        menubar.add_cascade(menu=menu_edit, label='Muokkkaa')

    
       
       