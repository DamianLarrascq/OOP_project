import tkinter
from tkinter import ttk


class MainFrame(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)

        self.nb_width = 600
        self.nb_height = 380

        # Notebook style
        self.nb_style = ttk.Style()
        self.nb_style.configure('TNotebook.Tab', font='Helvetica 14', padding=(10,0,10,0))

        # Notebook
        self.nb = ttk.Notebook(self)
        self.nb.grid(row=1, column=0)

        # Notebook tabs
        self.tab_0 = ttk.Frame(self.nb, width=self.nb_width, height=self.nb_height)
        self.tab_1 = ttk.Frame(self.nb, width=self.nb_width, height=self.nb_height)
        self.tab_2 = ttk.Frame(self.nb, width=self.nb_width, height=self.nb_height)
        self.tab_3 = ttk.Frame(self.nb, width=self.nb_width, height=self.nb_height)
        self.tab_4 = ttk.Frame(self.nb, width=self.nb_width, height=self.nb_height)

        # Add tabs to notebook
        self.nb.add(self.tab_0, text='Alumnos')
        self.nb.add(self.tab_1, text='Profesores')
        self.nb.add(self.tab_2, text='Directivos')
        self.nb.add(self.tab_3, text='Boletines')
        self.nb.add(self.tab_4, text='Clases')

        # print(self.nb.tabs()) # retorna lista de ventanas

        for i in range(len(self.nb.tabs())):
            self.create_operations(i)

        # Frame for buttons
        # self.lb_frame = ttk.LabelFrame(self.tab_0, text='Operaciones')
        # self.lb_frame.grid(row=0, column=0)
        #
        # self.btn_create = ttk.Button(self.lb_frame, text='Nuevo')
        # self.btn_create.grid(row=0, column=1)

        # self.btn_load = ttk.Button(self.lb_frame, text='Cargar')
        # self.btn_load.grid(row=0, column=2)
        #
        # self.btn_edit = ttk.Button(self.lb_frame, text='Editar')
        # self.btn_edit.grid(row=0, column=3)
        #
        # self.btn_del = ttk.Button(self.lb_frame, text='Eliminar')
        # self.btn_del.grid(row=0, column=4)

        self.alumnos_tree = self.create_tree_widget(self.tab_0, ('Nombre_Completo', 'D.N.I', 'Email'))
        self.alumnos_tree.grid(row=1, column=0)

        self.profesores_tree = self.create_tree_widget(self.tab_1, ('Nombre_Completo', 'D.N.I', 'Email', 'Materias'))
        self.profesores_tree.grid(row=1, column=0)

        self.directivos_tree = self.create_tree_widget(self.tab_2, ('Nombre_Completo', 'D.N.I', 'Email', 'Cargo'))
        self.directivos_tree.grid(row=1, column=0)

        self.boletines_tree = self.create_tree_widget(self.tab_3, ('Nombre_Alumno', 'Materia_1', 'Materia_2', 'Promedio'))
        self.boletines_tree.grid(row=1, column=0)

        self.clases_tree = self.create_tree_widget(self.tab_4, ('Nombre', 'Horarios', 'Cantidad_alumnos', 'Profesor', 'alguna mierda'))
        self.clases_tree.grid(row=1, column=0)

        self.grid(row=0, column=0)

    def create_operations(self, i):
        tab_num = f'tab_{i}'
        tab = getattr(self, tab_num)
        frame_name = f'lb_frame_{tab_num}'
        button_name = f'btn_frame_{tab_num}'
        setattr(self, frame_name, ttk.LabelFrame(tab, text='Operaciones'))
        frame = getattr(self, frame_name)
        getattr(self, frame_name).grid(row=0, column=0, sticky='w', padx=25)
        setattr(self, button_name, ttk.Button(frame, text='Nuevo'))
        getattr(self, button_name).grid(row=0, column=1, padx=5)
        setattr(self, button_name, ttk.Button(frame, text='Cargar'))
        getattr(self, button_name).grid(row=0, column=2, padx=5)
        setattr(self, button_name, ttk.Button(frame, text='Editar'))
        getattr(self, button_name).grid(row=0, column=3, padx=5)
        setattr(self, button_name, ttk.Button(frame, text='Eliminar'))
        getattr(self, button_name).grid(row=0, column=4, padx=5)

    # def create_button(self, button_name, frame):
    #     setattr(self, button_name, ttk.Button(frame, text='Nuevo'))
    #     getattr(self, button_name).grid(row=0, column=1)

    def create_tree_widget(self, container, col_values):
        """
        :param container: Surface where widget will load
        :param col_values: Tuple of strings w/o spaces for columns
        :return: Treeview widget
        """
        columns = col_values
        tree = ttk.Treeview(container, columns=columns, show='headings')

        for value in range(len(columns)):
            tree.column(columns[value])
            val = columns[value].replace('_', ' ')
            tree.heading(columns[value], text=val)

        # Generate sample data
        # col_data = []
        # for i in range(20):
        #     col_data.append((f'nombre apellido {i}', f'10.100.10{i}',
        #                           f'2{i}/02/190{i}', f'email_{i}@email.com'))
        #
        # Add data to the treeview
        # for data in col_data:
        #     tree.insert('', tkinter.END, values=data)

        return tree


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x400')
        self.title('School Management System')


app = App()

frame = MainFrame(app)

btn_style = ttk.Style()
btn_style.configure('Custom.TButton', foreground='black', font='Helvetica 10')

app.mainloop()
