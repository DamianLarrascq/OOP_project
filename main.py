import tkinter
import sqlite3
from tkinter import ttk
from utils import alumno_data, profesor_data, boletines_data, materias_data, directivo_data


class MainFrame(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)

        self.nb_width = 600
        self.nb_height = 380

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
        self.nb.add(self.tab_4, text='Materias')

        # Creates operations widget for tabs
        for i in range(len(self.nb.tabs())):
            self.create_operations(i)

        # Creates Treeview for tabs
        self.alumnos_tree = self.create_tree_widget(self.tab_0, alumno_data)
        self.alumnos_tree.grid(row=1, column=0)

        self.profesores_tree = self.create_tree_widget(self.tab_1, profesor_data)
        self.profesores_tree.grid(row=1, column=0)

        self.directivos_tree = self.create_tree_widget(self.tab_2, directivo_data)
        self.directivos_tree.grid(row=1, column=0)

        self.boletines_tree = self.create_tree_widget(self.tab_3, boletines_data)
        self.boletines_tree.grid(row=1, column=0)

        self.materias_tree = self.create_tree_widget(self.tab_4, materias_data)
        self.materias_tree.grid(row=1, column=0)

        # Add data from db
        self.add_directivos()
        self.add_alumnos()

        # Scrollbar for tabs
        self.create_scrollbar(self.tab_0, self.alumnos_tree)
        self.create_scrollbar(self.tab_1, self.profesores_tree)
        self.create_scrollbar(self.tab_2, self.directivos_tree)
        self.create_scrollbar(self.tab_3, self.boletines_tree)
        self.create_scrollbar(self.tab_4, self.materias_tree)

        # Record frame for tabs
        self.create_record_frame(self.tab_0, alumno_data)
        self.create_record_frame(self.tab_1, profesor_data)
        self.create_record_frame(self.tab_2, directivo_data)
        self.create_record_frame(self.tab_3, boletines_data)
        self.create_record_frame(self.tab_4, materias_data)

        # Position of MainFrame
        self.grid(row=0, column=0)

    def create_scrollbar(self, container, tree):
        v_scroll = ttk.Scrollbar(container, orient='vertical', command=tree.yview)
        v_scroll.grid(row=1, column=1, sticky='nese')
        tree['yscrollcommand'] = v_scroll.set
        # h_scroll = ttk.Scrollbar(container, orient='horizontal', command=tree.xview)
        # h_scroll.grid(row=2, sticky='swse')
        # tree['xscrollcommand'] = v_scroll.set

    def create_record_frame(self, container, list):
        r_frame = ttk.LabelFrame(container, text='Records')
        r_frame.grid(row=2, column=0, sticky='w', padx=25)
        self.create_entry_labels(r_frame, list)

    def create_operations(self, i):
        tab_num = f'tab_{i}'
        tab = getattr(self, tab_num)
        frame_name = f'lb_frame_{tab_num}'
        setattr(self, frame_name, ttk.LabelFrame(tab, text='Operaciones'))
        frame = getattr(self, frame_name)
        getattr(self, frame_name).grid(row=0, column=0, sticky='w', padx=25)
        self.create_buttons(frame, ['Nuevo', 'Cargar', 'Editar', 'Eliminar', 'Seleccionar'])

    def create_entry_labels(self, frame, lb_list):
        col = 0
        rw = 0
        for label in lb_list:
            lb = label.replace('_',' ').title() + ':'
            setattr(self, label, ttk.Label(frame, text=lb))
            getattr(self, label).grid(row=rw, column=col, padx=5, pady=5, sticky='w')
            entry = label + '_entry'
            setattr(self, entry, ttk.Entry(frame))
            getattr(self, entry).grid(row=(rw+1), column=col, padx=5, pady=5)
            col += 1
            if col == 4:
                rw += 2
                col = 0

    def create_buttons(self, frame, btn_list):
        col = 0
        for button in btn_list:
            setattr(self, button, ttk.Button(frame, text=button))
            getattr(self, button).grid(row=0, column=col, padx=5, pady=5)
            col += 1

    def create_tree_widget(self, container, col_values):
        """
        :param container: Surface where widget will load
        :param col_values: Tuple or list of strings w/o spaces for columns
        :return: Treeview widget
        """
        columns = col_values
        tree = ttk.Treeview(container, columns=columns, show='headings', selectmode='extended')
        for value in range(len(columns)):
            tree.column(columns[value], anchor='center', width=130)
            val = columns[value].replace('_', ' ').title()
            tree.heading(columns[value], text=val)

        return tree

    def add_directivos(self):
        con = sqlite3.connect('colegio.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM directivos')
        records = cur.fetchall()
        for record in records:
            self.directivos_tree.insert('', tkinter.END, values=record)
        con.commit()
        con.close()

    def add_alumnos(self):
        con = sqlite3.connect('colegio.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM alumnos')
        records = cur.fetchall()
        for record in records:
            self.alumnos_tree.insert('', tkinter.END, values=record)
        con.commit()
        con.close()

    def add_profesores(self):
        con = sqlite3.connect('colegio.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM profesores')
        records = cur.fetchall()
        for record in records:
            self.profesores_tree.insert('', tkinter.END, values=record)
        con.commit()
        con.close()

    def add_boletines(self):
        con = sqlite3.connect('colegio.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM boletines')
        records = cur.fetchall()
        for record in records:
            self.boletines_tree.insert('', tkinter.END, values=record)
        con.commit()
        con.close()

    def add_materias(self):
        con = sqlite3.connect('colegio.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM materias')
        records = cur.fetchall()
        for record in records:
            self.materias_tree.insert('', tkinter.END, values=record)
        con.commit()
        con.close()


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1200x600')
        self.title('School Management System')


app = App()

frame = MainFrame(app)

style = ttk.Style()
style.theme_use('winnative')
style.configure('Treeview', background='lightgray', foreground='black',
                     rowheight=25, fieldbackground='lightgray')

style.configure('TNotebook.Tab', padding=(10,0,10,0), font='Helvetica 12')

btn_style = ttk.Style()
btn_style.configure('Custom.TButton', foreground='black', font='Helvetica 10')

app.mainloop()
