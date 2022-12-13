import tkinter
from tkinter import ttk

from controllers import ButtonController, RecordController
from frames import MainFrame, CRUDViewFrame, ListViewFrame


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1200x600')
        self.title('School Management System')

        self.frames = {}

        # Instantiate main frame.
        main_frame = MainFrame(self)

        # Instantiate ButtonController. This object holds a reference to the Frame that we will use to display
        # Create and Edit forms.
        controller = ButtonController()
        crud_view_frame = CRUDViewFrame(main_frame, controller)
        controller.parent_frame = crud_view_frame
        crud_view_frame.grid(row=1, column=0)

        objects = ['Alumnos', 'Profesores']

        list_view_data = []

        db_controller = RecordController()
        for o in objects:
            _data = {
                'object': o,
                'initial_data': db_controller.get_record_list(o)
            }
            list_view_data.append(_data)

        list_view_frame = ListViewFrame(main_frame, controller, data=list_view_data)
        list_view_frame.grid(row=0, column=0)


if __name__ == '__main__':
    app = App()
    # frame = MainFrame(app)

    style = ttk.Style()
    # style.theme_use('winnative')
    style.configure('Treeview', background='lightgray', foreground='black',
                    rowheight=25, fieldbackground='lightgray')

    style.configure('TNotebook.Tab', padding=(10, 0, 10, 0), font='Helvetica 12')

    btn_style = ttk.Style()
    btn_style.configure('Custom.TButton', foreground='black', font='Helvetica 10')

    app.mainloop()
