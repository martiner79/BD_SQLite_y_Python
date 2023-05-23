

import sqlite3

# Creamos la conexión a la base de datos "database_example" (Si no existe la crea).
conn = sqlite3.connect("database_example")

# Creamos el cursor el cual nos ayudará a realizar las consultas
cursor = conn.cursor()

# Guardamos los cambios. Esto lo haremos con cada consulta
conn.commit()



#(1) Creamos la tabla "clientes" con sus respectivas columnas (id, nombre, contacto) y tipos de datos

cursor.execute("CREATE TABLE clientes (id NUMERIC AUTO INCREMENT, nombre TEXT, contacto TEXT)")
conn.commit()


#Agregamos los Registros

clientes = (

    (1, "Lucas", "lucas@mail.com"),
    (2, "Romina", "romina@mail.com"),
    (3, "Brenda", "brenda@mail.com"),
)

for id, nombre, contacto in clientes:
    cursor.execute("INSERT INTO clientes VALUES (?,?,?)", (id, nombre, contacto))

conn.commit()



#(2) Creamos la tabla productos con sus respectivos valores

cursor.execute("CREATE TABLE productos (id NUMERIC AUTO INCREMENT, tipo TEXT, marca TEXT)")
conn.commit()


#Agregamos los Registros

productos = (

    (1, "celular", "Motorola"),
    (2, "televisor", "Sonic"),
    (3, "parlante", "Philips"),
)

for id, tipo, marca in productos:
    cursor.execute("INSERT INTO productos VALUES (?,?,?)", (id, tipo, marca))

conn.commit()


#(3) Creamos la tabla facturas

cursor.execute("CREATE TABLE facturas (id NUMERIC AUTO INCREMENTE, tipo TEXT, monto FLOAT, fecha_emision TEXT)")
conn.commit()

#Agregamos los Registros

facturas = (
    (1, "A", 15.34, "15/05/2023"),
    (2, "B", 17.44, "17/06/2023"),
    (3, "C", 23.83, "30/07/2023"),
)

for id, tipo, monto, fecha_emision in facturas:
    cursor.execute("INSERT INTO facturas VALUES (?,?,?,?)", (id, tipo, monto, fecha_emision))

conn.commit()


#El siguiente código lo puede desmarcar para visualizar los registros de las tablas.
'''
cursor.execute("SELECT * FROM clientes")
clientes = cursor.fetchall()
print(clientes)

conn.commit()
conn.close()
'''