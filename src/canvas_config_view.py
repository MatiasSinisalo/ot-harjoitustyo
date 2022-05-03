from tkinter import N,W,S,E, Button, Entry, Frame, Label


class CanvasConfigView:
    def __init__(self, app, root) -> None:
        self.root = root
        self.app = app
        canvas_configurer_view = Frame(self.root, width=300, bg="white")
        canvas_configurer_view.grid(column=2, row=0, sticky=N+W+S+E)

        chart_configurer_view = Frame(canvas_configurer_view, width=300, bg="lightgray")
        chart_configurer_view.grid(column=0, row=0, pady=10, padx=10)

        set_x_values_for_chart = Button(
            chart_configurer_view, text="aseta valinta kaavion X arvoksi",
            command=app.set_x_values_for_next_chart)
        set_x_values_for_chart.grid(column=0, row=1)

        set_y_values_for_chart = Button(
            chart_configurer_view, text="aseta valinta kaavion Y arvoksi",
            command=app.set_y_values_for_next_chart)

        set_y_values_for_chart.grid(column=0, row=2)


        label_for_chart_title = Label(chart_configurer_view, text="aseta taulukon otsikko")
        label_for_chart_title.grid(column=0, row=3)
        set_x_title_entry = Entry(chart_configurer_view, textvariable=self.app.next_chart_title)
        set_x_title_entry.grid(column=0, row=4)
        
        label_for_x_title = Label(chart_configurer_view, text="aseta taulukon x otsikko")
        label_for_x_title.grid(column=0, row=5)
        set_x_title_entry = Entry(chart_configurer_view, textvariable=self.app.next_chart_x_title)
        set_x_title_entry.grid(column=0, row=6)


        label_for_y_title = Label(chart_configurer_view, text="aseta taulukon y otsikko")
        label_for_y_title.grid(column=0, row=7)
        set_y_title_entry = Entry(chart_configurer_view, textvariable=self.app.next_chart_y_title)
        set_y_title_entry.grid(column=0, row=8)

        add_new_bar_chart_button = Button(
            chart_configurer_view, text="Lisaa uusi pylvaskaavio",
            command=app.create_new_bar_chart)
        add_new_bar_chart_button.grid(column=0, row=9)

        add_new_pie_chart_button = Button(
            chart_configurer_view, text="Lisaa uusi piirakkakaavio",
            command=app.create_new_pie_chart)
        add_new_pie_chart_button.grid(column=0, row=10)

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
   
    def set_answer_text_to_sum(self):
        answer = self.app.spread_sheet_view.get_sum_of_selection()
        self.sum_result_text.config(text = answer)

    def set_answer_text_to_average(self):
        answer = self.app.spread_sheet_view.get_average_of_selection()
        self.average_result_text.config(text = answer)