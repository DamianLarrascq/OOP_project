from tkinter import ttk

alumno_data = ['id', 'nombre', 'apellido', 'apellido_2', 'fecha_nacimiento', 'email', 'id_profesores', 'id_directivos', 'id_materias']
directivo_data = ['id', 'nombre', 'apellido', 'apellido_2', 'fecha_nacimiento', 'email', 'cargo', 'fecha_inicio']
profesor_data = ['id', 'nombre', 'apellido', 'apellido_2', 'fecha_nacimiento', 'email', 'id_materia', 'id_directivo']
materias_data = ['id', 'nombre', 'id_profesor']
boletines_data = ['id', 'nombre_alumno', 'materia_1', 'materia_2', 'materia_3', 'materia_4', 'promedio']

buttons = [
    {
        'text':'Agregar',
        'style': 'Custom.TButton',
        'name': 'ag_btn'
    },
    {
        'text': 'Cargar',
        'style': 'Custom.TButton',
        'name': 'cg_btn'
    },
    {
        'text': 'Editar',
        'style': 'Custom.TButton',
        'name': 'ed_btn'
    },
    {
        'text': 'Eliminar',
        'style': 'Custom.TButton',
        'name': 'el_btn'
    }
]


def button_creator(screen, config):
    setattr(screen, config['name'], ttk.Button(text=config['text'], style=config['style'], command=lambda:button_creator(screen, config)))
    getattr(screen, config['name']).pack() # expand=True expands to fill space
    return


def label_creator(screen, config):
    setattr(screen, config['name'], ttk.Label(text=config['text'], style=config['style']))
    getattr(screen, config['name']).pack()


def tab_creator(screen, config):
    setattr(screen, config['name'])
