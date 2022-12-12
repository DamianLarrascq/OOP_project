import tkinter
import sqlite3
from tkinter import ttk


class EditForm(ttk.Frame):
    def __init__(self, frame, record_data):
        super().__init__(self, frame)
        frame = ttk.LabelFrame(frame, text='Records')
        frame.grid(row=2, column=0, sticky='w', padx=25)
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

    @staticmethod
    def open_edit_form(event):
        print('we made it!')
        values = event.widget.item(event.widget.selection())['values']
        print(values)
        print(event.widget)
        id = values[0]
        table_name = event.widget.master.master.tab('current')['text'].lower()
        _frame = event.widget.master.master.master
        # _slaves = _frame.grid_slaves()
        # for item in _slaves:
        #     item.remove()
        _frame.grid(row=1, column=0)

        result = RecordController().get_record(table_name, id)
        edit_form = EditForm(_frame, result)
        return result


class CreateForm(ttk.Frame):
    def __init__(self, frame, record_data):
        super().__init__(self, frame)
        frame = ttk.LabelFrame(frame, text='Records')
        frame.grid(row=2, column=0, sticky='w', padx=25)
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

    @staticmethod
    def open_create_form(tree):
        cols = tree['columns']
        empty_record = {item: '' for item in cols}
        _frame = tree
        _frame.grid(row=1, column=0)
        create_form = CreateForm(_frame.master, record_data=empty_record)
        return create_form


class CRUDView:
    def __init__(self, container, frame, resource_name: str, data: list[dict]):
        container.add(frame, text=resource_name)
        property_name = f'{resource_name.lower()}_tree'

        # Create List view
        setattr(self, property_name, self.create_tree_widget(frame, data))
        tree = getattr(self, property_name)
        self.create_scrollbar(frame, tree)
        tree.grid(row=1, column=0)

        # Create Form Section
        form_section = ttk.LabelFrame(frame, text='Records')
        form_section.grid(row=2, column=0, sticky='w', padx=25)

        # Create buttons
        self.create_operations(frame, tree, form_section)

        return

    def create_scrollbar(self, container, tree):
        v_scroll = ttk.Scrollbar(container, orient='vertical', command=tree.yview)
        v_scroll.grid(row=1, column=1, sticky='nese')
        tree['yscrollcommand'] = v_scroll.set
        # h_scroll = ttk.Scrollbar(container, orient='horizontal', command=tree.xview)
        # h_scroll.grid(row=2, sticky='swse')
        # tree['xscrollcommand'] = v_scroll.set

    def create_operations(self, tab, tree, form_section):
        frame_name = f'lb_frame_1'
        setattr(self, frame_name, ttk.LabelFrame(tab, text='Operaciones'))
        frame = getattr(self, frame_name)
        getattr(self, frame_name).grid(row=0, column=0, sticky='w', padx=25)
        self.create_buttons(frame, [('Create', tree, lambda: CreateForm.open_create_form(tree))])

    def create_buttons(self, frame, btn_list):
        col = 0
        for button in btn_list:
            tree = button[1]

            # Other buttons
            setattr(self, button[0], ttk.Button(frame, text=button[0], command=button[2]))
            btn = getattr(self, button[0])
            btn.grid(row=0, column=col, padx=5, pady=5)

            # Edit
            tree.bind('<<TreeviewSelect>>', EditForm.open_edit_form)

            col += 1

    def create_tree_widget(self, container, record_data: list[dict] = None):
        """
        :param record_data:
        :param container: Surface where widget will load
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


class TabContainer:
    def __init__(self):
        pass


class RecordController:
    def __init__(self):
        conn = sqlite3.connect('colegio.db')
        conn.row_factory = sqlite3.Row
        self.conn = conn.cursor()

    def get_record(self, table_name: str, identifier: int) -> dict:
        """
        Retrieves a single instance of a record
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

    def __init__(self, container, resource_list):
        super().__init__(container)

        self.nb_width = 600
        self.nb_height = 380

        # Notebook
        self.nb = ttk.Notebook(self)
        self.nb.grid(row=1, column=0)

        controller = RecordController()
        for item in resource_list:
            tab_name = f'tab_{item}'
            setattr(self, tab_name, ttk.Frame(self.nb, width=self.nb_width, height=self.nb_height))
            _tab = getattr(self, tab_name)
            items_data = controller.get_record_list(item)
            crud_view = CRUDView(self.nb, _tab, item, items_data)

        # Position of MainFrame
        self.grid(row=0, column=0)


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1200x600')
        self.title('School Management System')

        container = ttk.Frame(self)
        container.grid(row=0, column=0)

        self.frames = {}

        for F in (MainFrame, EditForm, CreateForm):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=1, column=0, sticky='w')

        self.show_frame(MainFrame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


app = App()

resource_list = ['Alumnos', 'Directivos']

MainFrame(app, resource_list)

style = ttk.Style()
# style.theme_use('winnative')
style.configure('Treeview', background='lightgray', foreground='black',
                rowheight=25, fieldbackground='lightgray')

style.configure('TNotebook.Tab', padding=(10, 0, 10, 0), font='Helvetica 12')

btn_style = ttk.Style()
btn_style.configure('Custom.TButton', foreground='black', font='Helvetica 10')

app.mainloop()
