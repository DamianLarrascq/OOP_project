import tkinter
import sqlite3
from tkinter import ttk
from utils import alumno_data, profesor_data, boletines_data, materias_data, directivo_data


class EditForm:
    def __init__(self, frame, record_data):
        col = 0
        rw = 0
        for col_name, value in record_data.items():
            # label
            lb = col_name.replace('_', ' ').title() + ':'
            setattr(self, col_name, ttk.Label(frame, text=lb))
            getattr(self, col_name).grid(row=rw, column=col, padx=5, pady=5)

            # entry
            entry = col_name + '_entry'
            setattr(self, entry, ttk.Entry(frame))
            _entry = getattr(self, entry)
            _entry.grid(row=(rw + 1), column=col, padx=5, pady=5)
            _entry.insert(0, value)
            col += 1
            if col == 4:
                rw += 2
                col = 0


class CreateForm:
    def __init__(self, frame, record_data):
        col = 0
        rw = 0
        for col_name, value in record_data.items():
            # label
            lb = col_name.replace('_', ' ').title() + ':'
            setattr(self, col_name, ttk.Label(frame, text=lb))
            getattr(self, col_name).grid(row=rw, column=col, padx=5, pady=5)

            # entry
            entry = col_name + '_entry'
            setattr(self, entry, ttk.Entry(frame))
            _entry = getattr(self, entry)
            _entry.grid(row=(rw + 1), column=col, padx=5, pady=5)
            # _entry.insert(0, value)
            col += 1
            if col == 4:
                rw += 2
                col = 0


class RecordController:
    def __init__(self):
        conn = sqlite3.connect('colegio.db')
        conn.row_factory = sqlite3.Row
        self.conn = conn.cursor()

    def get_record(self, table_name: str, identifier: int) -> dict:
        """
        Retrieves a single instance of a record.

        :param table_name:
        :param identifier:
        :return:
        """
        query_al = f"""
        SELECT * FROM {table_name.lower()}
        WHERE id = {identifier}
        """
        res = self.conn.execute(query_al)
        item = self.conn.fetchall()[0]
        result = {k: item[k] for k in item.keys()}
        return result

    def get_record_list(self, table_name: str) -> list[dict]:
        """
        """
        query_al = f"SELECT * FROM {table_name.lower()}"
        res = self.conn.execute(query_al)
        result = self.conn.fetchall()
        list_accumulator = []
        for item in result:
            list_accumulator.append({k: item[k] for k in item.keys()})
        print(list_accumulator)
        return list_accumulator

    def update_record(self, table_name: str, record_data: dict) -> dict:
        """

        :param table_name:
        :param record_data:
        :return:
        """
        pass

    def delete_record(self, table_name: str, identifier: dict) -> dict:
        """
        """
        pass

    def create_record(self, table_name: str, record_data: dict) -> dict:
        """
        """
        pass


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
        # self.nb.add(self.tab_0, text='Alumnos')
        self.nb.add(self.tab_1, text='Profesores')
        self.nb.add(self.tab_2, text='Directivos')
        self.nb.add(self.tab_3, text='Boletines')
        self.nb.add(self.tab_4, text='Materias')

        # Creates operations widget for tabs
        # for i in range(len(self.nb.tabs())):
        #     self.create_operations(i)

        # Creates Treeview for tabs
        # self.alumnos_tree = self.create_tree_widget(self.tab_0, alumno_data)
        # self.alumnos_tree.grid(row=1, column=0)

        # self.profesores_tree = self.create_tree_widget(self.tab_1, profesor_data)
        # self.profesores_tree.grid(row=1, column=0)
        #
        # self.directivos_tree = self.create_tree_widget(self.tab_2, directivo_data)
        # self.directivos_tree.grid(row=1, column=0)
        #
        # self.boletines_tree = self.create_tree_widget(self.tab_3, boletines_data)
        # self.boletines_tree.grid(row=1, column=0)
        #
        # self.materias_tree = self.create_tree_widget(self.tab_4, materias_data)
        # self.materias_tree.grid(row=1, column=0)

        # Load data from db
        self.load_data()

        # Scrollbar for tabs
        # self.create_scrollbar(self.tab_0, self.alumnos_tree)
        # self.create_scrollbar(self.tab_1, self.profesores_tree)
        # self.create_scrollbar(self.tab_2, self.directivos_tree)
        # self.create_scrollbar(self.tab_3, self.boletines_tree)
        # self.create_scrollbar(self.tab_4, self.materias_tree)

        # Record frame for tabs
        # self.create_entry_labels(self.create_record_frame(self.tab_0), alumno_data)
        # self.create_entry_labels(self.create_record_frame(self.tab_1), profesor_data)
        # self.create_entry_labels(self.create_record_frame(self.tab_2), directivo_data)
        # self.create_entry_labels(self.create_record_frame(self.tab_3), boletines_data)
        # self.create_entry_labels(self.create_record_frame(self.tab_4), materias_data)

        controller = RecordController()
        alumnos_data = controller.get_record_list('Alumnos')
        self.create_crud_view(self.tab_0, 'Alumnos', alumnos_data)

        # Position of MainFrame
        self.grid(row=0, column=0)

    def create_scrollbar(self, container, tree):
        v_scroll = ttk.Scrollbar(container, orient='vertical', command=tree.yview)
        v_scroll.grid(row=1, column=1, sticky='nese')
        tree['yscrollcommand'] = v_scroll.set
        # h_scroll = ttk.Scrollbar(container, orient='horizontal', command=tree.xview)
        # h_scroll.grid(row=2, sticky='swse')
        # tree['xscrollcommand'] = v_scroll.set

    def create_record_frame(self, container):
        r_frame = ttk.LabelFrame(container, text='Records')
        r_frame.grid(row=2, column=0, sticky='w', padx=25)
        return r_frame

    def create_operations(self, tab, tree):
        frame_name = f'lb_frame_1'
        setattr(self, frame_name, ttk.LabelFrame(tab, text='Operaciones'))
        frame = getattr(self, frame_name)
        getattr(self, frame_name).grid(row=0, column=0, sticky='w', padx=25)
        self.create_buttons(frame, [('Create', tree)])

    def select_row(self, event):
        print('we made it!')
        values = event.widget.item(event.widget.selection())['values']
        print(values)
        print(event.widget)
        id = values[0]
        table_name = event.widget.master.master.tab('current')['text'].lower()
        result = RecordController().get_record(table_name, id)
        edit_form = EditForm(self.create_record_frame(frame), result)
        return result

    def open_create_form(self, tree):
        cols = tree['columns']
        empty_record = {item: '' for item in cols}
        create_form = CreateForm(self.create_record_frame(frame), record_data=empty_record)
        return create_form

    def create_buttons(self, frame, btn_list):
        col = 0
        for button in btn_list:
            tree = button[1]

            setattr(self, button[0], ttk.Button(frame, text=button[0], command=lambda: self.open_create_form(tree)))
            btn = getattr(self, button[0])
            btn.grid(row=0, column=col, padx=5, pady=5)

            tree.bind('<<TreeviewSelect>>', self.select_row)

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
                tree.insert('', tkinter.END, values=list(record.values()))
        return tree

    def load_data(self):
        con = sqlite3.connect('colegio.db')
        cur = con.cursor()
        query_al = "SELECT * FROM alumnos"
        query_dir = "SELECT * FROM directivos"
        query_prof = "SELECT * FROM profesores"
        query_bol = "SELECT * FROM boletines"
        query_mat = "SELECT * FROM materias"
        cur.execute(query_al)
        records_al = cur.fetchall()
        # for record in records_al:
        #     self.alumnos_tree.insert('', tkinter.END, values=record)

        cur.execute(query_dir)
        records_dir = cur.fetchall()
        # for record in records_dir:
        #     self.directivos_tree.insert('', tkinter.END, values=record)
        #
        # cur.execute(query_prof)
        # records_prof = cur.fetchall()
        # for record in records_prof:
        #     self.directivos_tree.insert('', tkinter.END, values=record)
        #
        # cur.execute(query_bol)
        # records_bol = cur.fetchall()
        # for record in records_bol:
        #     self.boletines_tree.insert('', tkinter.END, values=record)
        #
        # cur.execute(query_mat)
        # records_mat = cur.fetchall()
        # for record in records_mat:
        #     self.materias_tree.insert('', tkinter.END, values=record)

        con.commit()
        con.close()

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


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1200x600')
        self.title('School Management System')


app = App()

frame = MainFrame(app)

style = ttk.Style()
# style.theme_use('winnative')
style.configure('Treeview', background='lightgray', foreground='black',
                rowheight=25, fieldbackground='lightgray')

style.configure('TNotebook.Tab', padding=(10, 0, 10, 0), font='Helvetica 12')

btn_style = ttk.Style()
btn_style.configure('Custom.TButton', foreground='black', font='Helvetica 10')

app.mainloop()
