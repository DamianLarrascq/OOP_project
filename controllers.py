import sqlite3

from forms import CreateForm, EditForm


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


class ButtonController(object):
    def __init__(self):
        self.parent_frame = None

    def open_create_form(self, tree):
        cols = tree['columns']
        empty_record = {item: '' for item in cols}
        for widget in self.parent_frame.winfo_children():
            widget.destroy()
        create_form = CreateForm(self.parent_frame, record_data=empty_record)
        return create_form

    def select_row(self, event):
        print('we made it!')
        values = event.widget.item(event.widget.selection())['values']
        print(values)
        print(event.widget)
        id = values[0]
        table_name = event.widget.master.master.tab('current')['text'].lower()
        result = RecordController().get_record(table_name, id)
        # self.controller.parent_frame.forget()
        for widget in self.parent_frame.winfo_children():
            widget.destroy()
        edit_form = EditForm(self.parent_frame, result)
        return result

    def delete_row(self, row_id):
        print(f'row {row_id} deleted')
        return
