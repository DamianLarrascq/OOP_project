import sqlite3

con = sqlite3.connect('colegio.db')
cur = con.cursor()

con.execute("CREATE TABLE boletines('id', 'nombre_alumno', 'materia_1', 'materia_2', 'materia_3', 'materia_4', 'promedio')")

con.commit()
