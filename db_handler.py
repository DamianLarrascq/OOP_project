import sqlite3

con = sqlite3.connect('colegio.db')
cur = con.cursor()

data = [
    (1, 'Daniel', 'Sáez', 'Vega', 20022001, 'email1@email.com', 1, 1, 2),
    (2, 'Juan', 'Gómez', 'López', 22022002, 'email2@email.com', 1, 2, 2),
    (3, 'Diego', 'Flores', 'Salas', 10122000, 'email3@email.com', 2, 1, 2),
    (4, 'Marta', 'Herrera', 'Gil', 20062003, 'email4@email.com', 2, 1, 2),
    (5, 'Antonio', 'Carretero', 'Ortega', 23082001, 'email5@email.com', 1, 1, 1),
    (6, 'Manuel', 'Domínguez', 'Hernández', 20022002, 'email6@email.com', 1, 2, 1),
    (7, 'Antonio', 'Vega', 'Hernández', 12032002, 'email7@email.com', 1, 2, 1),
    (8, 'Alfredo', 'Ruiz', 'Flores', 16042002, 'email8@email.com', 1, 1, 1),
    (9, 'Carlos', 'Calvo', 'Silva', 17042003, 'email9@email.com', 1, 1, 1),
    (10, 'Fredo', 'Flores', 'Martínez', 12052001, 'email10@email.com', 1, 1, 1),
    (11, 'Pepe', 'Ruiz', 'Hernández', 11062005, 'email11@email.com', 1, 1, 1),
    (12, 'Nicolás', 'Martínez', 'Herrera', 27082004, 'email12@email.com', 1, 1, 1),
    (13, 'Facundo', 'Perez', 'Vega', 29092003, 'email13@email.com', 1, 1, 1),
    (14, 'Eladio', 'Gómez', 'Plantas', 21022002, 'email14@email.com', 1, 1, 1)
]

cur.executemany("INSERT INTO alumnos VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", data)

con.commit()

con.close()
