import tkinter
from tkinter import ttk


class ObjetosEscuela:

    colegio = 'Colegio Estatal Num 77'

    def __init__(self):
        pass

    def crear(self):
        pass

    def cargar(self):
        pass

    def editar(self):
        pass

    def guardar(self):
        pass

    def eliminar(self):
        pass


class Alumno(ObjetosEscuela):
    pass


class Directivo(ObjetosEscuela):
    pass


class Profesor(ObjetosEscuela):
    pass


class Clases(ObjetosEscuela):
    pass


class Boletines(ObjetosEscuela):
    pass


# class Treeview_Creator(ttk.Treeview):
#     def __init__(self, container, column, show, col_values):
#         super().__init__(container)
#     # Treeview columns
#     columns = ('nombre_completo', 'dni', 'fecha_nacimiento', 'email')
#
#     # Treeview
#     tree = ttk.Treeview(container, columns=columns, show='headings')
#
#     # Treeview column config
#     tree.column('nombre_completo', width=200, anchor=tkinter.CENTER)
#     tree.column('dni', width=100, anchor=tkinter.CENTER)
#     tree.column('fecha_nacimiento', width=120, anchor=tkinter.CENTER)
#     tree.column('email', width=200, anchor=tkinter.CENTER)
#
#     # Treeview headings
#     tree.heading('nombre_completo', text='Nombre Completo')
#     tree.heading('dni', text='D.N.I')
#     tree.heading('fecha_nacimiento', text='Fecha Nacimiento')
#     tree.heading('email', text='Email')
#
#     # Generate sample data
#     col_data = []
#     for i in range(20):
#         col_data.append((f'nombre apellido {i}', f'10.100.10{i}',
#                          f'2{i}/02/190{i}', f'email_{i}@email.com'))
#
#     # Add data to the treeview
#     for data in col_data:
#         tree.insert('', tkinter.END, values=data)
