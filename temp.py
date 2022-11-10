#         # self.btn_style = ttk.Style()
#         # self.btn_style.configure('Custom.TButton', foreground='black', background='black', font='Arial 14', padding=20)
#
#         # Label styles
#         self.lb_style = ttk.Style()
#         self.lb_style.configure('Custom.TLabel', foreground='black', font='Helvetica 16')
#
#         self.upper_label = ttk.Label(self, text='Software Gestion Escolar', style='Custom.TLabel')
#         self.upper_label.pack(pady=10)
#
#         self.side_label = ttk.Label(self, text='Seleccione una opción: ', style='Custom.TLabel')
#         self.side_label.pack(pady=10)
#
#         # Cuadro de opciones
#         self.combo = ttk.Combobox(self)
#         self.combo['state'] = 'readonly'
#         self.combo['values'] = ['Personal', 'Clases', 'Boletin']
#         self.combo.set('Personal')
#         self.combo.configure(justify='center', font='Helvetica 12')
#         self.combo.bind('<<ComboboxSelected>>', self.selection_changed)
#         self.combo.pack()
#
#         self.pack()
#
#     # Funcion para mostrar seleccion
#     def selection_changed(self, event):
#
#         selection = self.combo.get()
#         messagebox.showinfo(title='seleccion',
#                             message=f'Se ha seleccionado la opcion: {selection}')
#
#
# class EditionFrame(ttk.Frame):
#
#     def __init__(self, container, edition):
#         super().__init__(container)
#
#         self.edition = edition