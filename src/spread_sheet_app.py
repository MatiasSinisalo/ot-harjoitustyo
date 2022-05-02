from os import stat
from tkinter import E, HORIZONTAL, N, S, VERTICAL, W, Button, Canvas, Frame, Label, Menu, Scrollbar, Text, Tk
from grid_display import GridDisplay
from graphs.matplotlib_graphs import ChartManager
from file_saver import FileSaver

class SpreadSheetApp:
    def __init__(self):
        self.x_values_for_chart = []
        self.y_values_for_chart = []
       
        self.root = Tk()
        self.root.option_add('*tearOff', False)
        self.root.title("Taulukkolaskentasovellus")
        self.root.geometry("500x500")
        self.root.configure(background='SteelBlue1')

        self.filesaver = FileSaver()
    def start(self):
        self.init_front_end()
        
    def init_front_end(self):
        

        self.main_canvas_container = Frame( self.root, bg="white")
        self.main_canvas_container.grid(column=0, row=0, sticky=N+W+S+E)
        self.main_canvas_container.columnconfigure(0, weight=1)
        self.main_canvas_container.rowconfigure(0, weight=1)

        self.init_menu_bar()
        self.init_grid_scrollBars()
        self.init_grid()
        self.canvas_chart_manager = ChartManager(self.grid_canvas)
        self.init_canvas_config_view()
        self.init_bind_events()
        
        self.root.mainloop()
    
    def handle_clicks(self, event):
        if event.widget.widgetName == "gridCanvas":
            self.spread_sheet_view.reset_drag()
            self.spread_sheet_view.cancel_cell_edit()
            if event.state != 1:
                self.spread_sheet_view.edit_cell(event)
            elif event.state == 1:
                self.spread_sheet_view.select(event.x, event.y, "lightblue")
        elif event.widget.widgetName == "chartWidget":
            event.widget.focus_set()

    def handle_movement(self, event):
        if event.state == 257:
            self.spread_sheet_view.select(event.x, event.y, "lightblue")

    def handle_x_scroll(self, a_val, b_val):
        self.grid_canvas.xview(a_val, b_val)
        self.canvas_chart_manager.update_all_charts()

    def handle_y_scroll(self, a_val, b_val):
        self.grid_canvas.yview(a_val,  b_val)
        self.canvas_chart_manager.update_all_charts()

    def set_x_values_for_next_chart(self):
        self.x_values_for_chart
        self.x_values_for_chart = []
        for key in self.spread_sheet_view.drag_selected_values:
            cell_number = self.spread_sheet_view.cell_grid_number_by_text_id[key]
            self.x_values_for_chart.append(self.spread_sheet_view.cell_grid_values[cell_number])

    def set_y_values_for_next_chart(self):
        self.y_values_for_chart = []
        for key in self.spread_sheet_view.drag_selected_values:
            cell_number = self.spread_sheet_view.cell_grid_number_by_text_id[key]
            self.y_values_for_chart.append(self.spread_sheet_view.cell_grid_values[cell_number])

    def create_new_bar_chart(self):
        self.canvas_chart_manager.add_new_bar_chart(
            "Hello World", "title of x", "title of y",
            self.x_values_for_chart, self.y_values_for_chart, 20, 10, 50, 500, 500)

    def create_new_pie_chart(self):
        self.canvas_chart_manager.add_new_pie_chart(
            "Hello World", "title of x", "title of y",
            self.x_values_for_chart, self.y_values_for_chart, 20, 10, 50, 500, 500)

    def set_answer_text_to_sum(self):
        answer = self.spread_sheet_view.get_sum_of_selection()
        self.sum_result_text.config(text = answer)

    def set_answer_text_to_average(self):
        answer = self.spread_sheet_view.get_average_of_selection()
        self.average_result_text.config(text = answer)

    def init_grid(self):
        GRID_WIDTH = 100
        GRID_HEIGHT = 100
        CELL_WIDTH = 200
        CELL_HEIGHT = 50
        CELL_DISPLAY_TEXT_OFFSET_PX_X = 1
        CELL_DISPLAY_TEXT_OFFSET_PX_Y = 3
        FONT_SIZE = 12
        MAX_LETTERS_IN_CELL = 20
        
        self.grid_canvas = Canvas(self.main_canvas_container, bg="white",
                            xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        self.grid_canvas.widgetName = "gridCanvas"
        self.grid_canvas.grid(column=0, row=0, sticky=N+W+S+E)
        self.grid_canvas.configure(
            scrollregion=[0, 0, GRID_WIDTH*CELL_WIDTH, GRID_HEIGHT*CELL_HEIGHT])

        self.spread_sheet_view = GridDisplay(self.grid_canvas, GRID_WIDTH, GRID_HEIGHT, CELL_WIDTH, CELL_HEIGHT,
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
       
        canvas_configurer_view = Frame(self.root, width=300, bg="white")
        canvas_configurer_view.grid(column=2, row=0, sticky=N+W+S+E)

        chart_configurer_view = Frame(canvas_configurer_view, width=300, bg="lightgray")
        chart_configurer_view.grid(column=0, row=0, pady=10, padx=10)

        set_x_values_for_chart = Button(
            chart_configurer_view, text="aseta valinta kaavion X arvoksi",
            command=self.set_x_values_for_next_chart)
        set_x_values_for_chart.grid(column=0, row=1)

        set_y_values_for_chart = Button(
            chart_configurer_view, text="aseta valinta kaavion Y arvoksi",
            command=self.set_y_values_for_next_chart)
        set_y_values_for_chart.grid(column=0, row=2)

        add_new_bar_chart_button = Button(
            chart_configurer_view, text="Lisaa uusi pylvaskaavio",
            command=self.create_new_bar_chart)
        add_new_bar_chart_button.grid(column=0, row=3)

        add_new_pie_chart_button = Button(
            chart_configurer_view, text="Lisaa uusi piirakkakaavio",
            command=self.create_new_pie_chart)
        add_new_pie_chart_button.grid(column=0, row=4)

        calculations_view = Frame(canvas_configurer_view, width=300, bg="lightgray")
        calculations_view.grid(column=0, row=2,  sticky=N+W+S+E,  pady=10, padx=10)

        get_sum_of_selection_button = Button(calculations_view, text="Laske valinnan summa", 
                                            command=self.set_answer_text_to_sum)
        get_sum_of_selection_button.grid(column=0, row=1, sticky=E+W)
        
        self.sum_result_text = Label(calculations_view)
        self.sum_result_text.grid(column=0, row=2, sticky=E+W)

        get_average_of_selection_button = Button(calculations_view, text="Laske valinnan keskiarvo", 
                                            command=self.set_answer_text_to_average)
        get_average_of_selection_button.grid(column=0, row=3, sticky=E+W)
        
        self.average_result_text = Label(calculations_view)
        self.average_result_text.grid(column=0, row=4, sticky=E+W)
        
    def init_bind_events(self):
        self.root.bind('<1>', self.handle_clicks)
        self.grid_canvas.bind('<Motion>', self.handle_movement)
        

    def init_menu_bar(self):
        menubar = Menu(self.root)
        self.root['menu'] = menubar
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        menu_file = Menu(menubar)
        menubar.add_cascade(menu=menu_file, label='Tiedosto')

        menu_edit = Menu(menubar)
        menubar.add_cascade(menu=menu_edit, label='Muokkkaa')

    def saveStateToFile(self):
        self.filesaver.SaveDictToFile("", self.spread_sheet_view.cell_grid_values)
    
    def loadStateFromFile(self):
        state = self.filesaver.readDictFromFile("")
        if state != None:
            self.spread_sheet_view.cell_grid_values = state[0]
        print(self.spread_sheet_view.cell_grid_values)
        
        
    
    
        

        
       
       