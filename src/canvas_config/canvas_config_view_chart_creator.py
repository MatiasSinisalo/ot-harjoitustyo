from tkinter import N,W,S,E, Button, Entry, Frame, Label, StringVar


class CanvasChartCreatorView:
    """Class responsible for the chart creation UI"""
    def __init__(self, root, app):
        """Inits the UI for creating charts"""
        self.root = root
        self.app = app
        #help for stringvars: https://www.pythontutorial.net/tkinter/tkinter-stringvar/
        self.next_chart_x_title = StringVar()
        self.next_chart_y_title = StringVar()
        self.next_chart_title = StringVar()

        chart_configurer_view = Frame(self.root, width=300, bg="lightgray")
        chart_configurer_view.grid(column=0, row=0, pady=10, padx=10)

        set_x_values_for_chart = Button(
            chart_configurer_view, text="aseta valinta kaavion X arvoksi",
            command=self.set_x_values_for_next_chart)
        set_x_values_for_chart.grid(column=0, row=1)

        set_y_values_for_chart = Button(
            chart_configurer_view, text="aseta valinta kaavion Y arvoksi",
            command=self.set_y_values_for_next_chart)

        set_y_values_for_chart.grid(column=0, row=2)


        label_for_chart_title = Label(chart_configurer_view, text="aseta taulukon otsikko")
        label_for_chart_title.grid(column=0, row=3)
        set_x_title_entry = Entry(chart_configurer_view, textvariable=self.next_chart_title)
        set_x_title_entry.grid(column=0, row=4)
        
        label_for_x_title = Label(chart_configurer_view, text="aseta taulukon x otsikko")
        label_for_x_title.grid(column=0, row=5)
        set_x_title_entry = Entry(chart_configurer_view, textvariable=self.next_chart_x_title)
        set_x_title_entry.grid(column=0, row=6)


        label_for_y_title = Label(chart_configurer_view, text="aseta taulukon y otsikko")
        label_for_y_title.grid(column=0, row=7)
        set_y_title_entry = Entry(chart_configurer_view, textvariable=self.next_chart_y_title)
        set_y_title_entry.grid(column=0, row=8)

        add_new_bar_chart_button = Button(
            chart_configurer_view, text="Lisaa uusi pylvaskaavio",
            command=self.create_new_bar_chart)
        add_new_bar_chart_button.grid(column=0, row=9)

        add_new_pie_chart_button = Button(
            chart_configurer_view, text="Lisaa uusi piirakkakaavio",
            command=self.create_new_pie_chart)
        add_new_pie_chart_button.grid(column=0, row=10)
    
    def set_x_values_for_next_chart(self):
        """Sets the x values for the next chart"""
        self.x_values_for_chart = []
        for key in self.app.spread_sheet_view.drag_selected_values:
            cell_number = self.app.spread_sheet_view.cell_grid_number_by_text_id[key]
            self.x_values_for_chart.append(self.app.spread_sheet_view.cell_grid_values[cell_number])

    def set_y_values_for_next_chart(self):
        """Sets the y values for the next chart"""
        self.y_values_for_chart = []
        for key in self.app.spread_sheet_view.drag_selected_values:
            cell_number = self.app.spread_sheet_view.cell_grid_number_by_text_id[key]
            self.y_values_for_chart.append(self.app.spread_sheet_view.cell_grid_values[cell_number])

    def create_new_bar_chart(self):
        """Calls the chart canvas manager to create a new bar chart"""
        self.app.canvas_chart_manager.add_new_bar_chart(
           self.next_chart_title.get(), self.next_chart_x_title.get(), self.next_chart_y_title.get(),
            self.x_values_for_chart, self.y_values_for_chart, 20, 10, 50, 500, 500)

    def create_new_pie_chart(self):
        """Calls the chart canvas manager to create a new pie chart"""
        self.app.canvas_chart_manager.add_new_pie_chart(
             self.next_chart_title.get(), self.next_chart_x_title.get(), self.next_chart_y_title.get(),
            self.x_values_for_chart, self.y_values_for_chart, 20, 10, 50, 500, 500)

   