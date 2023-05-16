import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview


class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1), weight=1)
        self.pack()


class CRUDViewFrame(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1), weight=1)
        self.controller = controller


class ListViewFrame(ttk.Frame):
    def __init__(self, container, controller, data=None):
        super().__init__(container)
        self.controller = controller
        # self.grid(row=0, column=0)
        self.nb_width = 600
        self.nb_height = 380
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0,1), weight=1)

        # Notebook
        self.nb = ttk.Notebook(self)
        self.nb.grid(row=1, column=0)

        # for i in range(len(data)):


        # Notebook tabs
        # self.tab_0 = ttk.Frame(self.nb, width=self.nb_width, height=self.nb_height)
        # self.tab_1 = ttk.Frame(self.nb, width=self.nb_width, height=self.nb_height)
        # self.tab_2 = ttk.Frame(self.nb, width=self.nb_width, height=self.nb_height)
        # self.tab_3 = ttk.Frame(self.nb, width=self.nb_width, height=self.nb_height)
        # self.tab_4 = ttk.Frame(self.nb, width=self.nb_width, height=self.nb_height)

        # Add tabs to notebook
        # self.nb.add(self.tab_0, text='Alumnos')
        # self.nb.add(self.tab_1, text='Profesores')
        # self.nb.add(self.tab_2, text='Directivos')
        # self.nb.add(self.tab_3, text='Boletines')
        # self.nb.add(self.tab_4, text='Materias')

        # db_controller = RecordController()
        # for item in data:
        #     _data = item['initial_data']
        #     self.create_crud_view(self.tab_0, item['object'], _data)
        # alumnos_data = data
        # self.create_crud_view(self.tab_0, 'Alumnos', alumnos_data)

        # Position of MainFrame
        self.grid(row=0, column=0, sticky='nsew')

    def create_crud_view(self, frame, resource_name: str, data: list[dict]):
        # self.selected_row = {}

        self.nb.add(frame, text='Alumnos')
        property_name = f'{resource_name.lower()}_tree'

        # Create list view
        setattr(self, property_name, self.create_tree_widget(frame, data))
        tree = getattr(self, property_name)
        self.create_scrollbar(frame, tree)
        tree.grid(row=1, column=0)

        # Create buttons
        self.create_operations(frame, tree)

        # # Create Edit View
        # self.create_edit_form(self.create_record_frame(frame), self.selected_row)
        return

    def create_operations(self, tab, tree):
        frame_name = f'lb_frame_1'
        setattr(self, frame_name, ttk.LabelFrame(tab, text='Operaciones'))
        frame = getattr(self, frame_name)
        getattr(self, frame_name).grid(row=0, column=0, sticky='w', padx=25)
        self.create_buttons(
            frame, [
                ('Create', tree, self.controller.open_create_form),
                # ('Delete', tree, self.controller.delete_row)
            ]
        )

    def create_buttons(self, frame, btn_list):
        col = 0
        for button in btn_list:
            tree = button[1]

            setattr(self, button[0],
                    ttk.Button(frame, text=button[0], command=lambda: button[2](tree)))
            btn = getattr(self, button[0])
            btn.grid(row=0, column=col, padx=5, pady=5)

            tree.bind('<<TreeviewSelect>>', self.controller.select_row)

            col += 1

    def create_tree_widget(self, container, record_data: list[dict] = None):
        """
        :param record_data:
        :param container: Surface where widget will load
        :param col_values: Tuple or list of strings w/o spaces for columns
        :return: Treeview widget
        """
        if record_data:
            columns = list(record_data[0].keys())
            tree = ttk.Treeview(container, columns=columns, show='headings', selectmode='extended')

            # create columns
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, anchor='center', width=130)

            # insert record
            for record in record_data:
                tree.insert('', tk.END, values=list(record.values()))
        else:
            return ttk.Treeview(container, columns=[], show='headings', selectmode='extended')
        return tree

    def create_scrollbar(self, container, tree):
        v_scroll = ttk.Scrollbar(container, orient='vertical', command=tree.yview)
        v_scroll.grid(row=1, column=1, sticky='nese')
        tree['yscrollcommand'] = v_scroll.set
        # h_scroll = ttk.Scrollbar(container, orient='horizontal', command=tree.xview)
        # h_scroll.grid(row=2, sticky='swse')
        # tree['xscrollcommand'] = v_scroll.set
