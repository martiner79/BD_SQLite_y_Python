import sqlite3

def create_database():
    conn = sqlite3.connect("alumnos_db")
    conn.commit()
    conn.close()

def create_Table():
    conn = sqlite3.connect("alumnos_db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE ingreso (
        Nombre TEXT,
        Apellido TEXT,
        Edad NUMERIC,
        CARRERA TEXT
        )"""
   )
    conn.commit()
    conn.close()

def insert_Row(Nombre, Apellido, Edad, CARRERA):
    conn = sqlite3.connect("alumnos_db")
    cursor = conn.cursor()
    ingreso_datos = f"INSERT INTO ingreso VALUES ('{Nombre}','{Apellido}',{Edad},'{CARRERA}')"
    cursor.execute(ingreso_datos)
    conn.commit()
    conn.close()

def read_Row():
    conn = sqlite3.connect("alumnos_db")
    cursor = conn.cursor()
    leer_datos = "SELECT * FROM ingreso"
    cursor.execute(leer_datos)
    leer_datos = cursor.fetchall()
    print(leer_datos)
    conn.commit()
    conn.close()

def insert_many_Rows(lista_datos):
    conn = sqlite3.connect("alumnos_db")
    cursor = conn.cursor()
    ingreso_datos = f"INSERT INTO ingreso VALUES (?,?,?,?)"
    cursor.executemany(ingreso_datos, lista_datos) #Tener en cuenta el "executemany" 
    conn.commit()                                  #para ingresar más de un dato
    conn.close()

def read_specific(dato):
    conn = sqlite3.connect("alumnos_db")
    cursor = conn.cursor()
    leer_datos = f"SELECT * FROM ingreso ORDER BY {dato} DESC"
    cursor.execute(leer_datos)
    leer_datos = cursor.fetchall()
    print(leer_datos)
    conn.commit()
    conn.close()

def search_name(nombre):
    conn = sqlite3.connect("alumnos_db")
    cursor = conn.cursor()
    leer_datos = f"SELECT * FROM ingreso WHERE Nombre LIKE '{nombre}%'" 
    cursor.execute(leer_datos)                                         
    leer_datos = cursor.fetchall()
    print(leer_datos)                                                   #Utilizamos 'LIKE' porque tendríamos
    conn.commit()                                                       #un error con el signo '='. Ya que el mismo
    conn.close()                                                        #usa caracteres ASCI (QUE NO ES KEYSENSITIVE).
                                                                        #Por lo tanto, no podríamos encontrar los
                                                                        #nombres si los buscáramos con minúscula
                                                                        #al principio.
def update_Row(dato1, dato2, dato3, dato4):
    conn = sqlite3.connect("alumnos_db")
    cursor = conn.cursor()
    leer_datos = f"UPDATE ingreso SET {dato1} = {dato2} WHERE {dato3} LIKE {dato4}"
    cursor.execute(leer_datos)
    conn.commit()
    conn.close()

def delete_row(columnaX, valorX):
    conn = sqlite3.connect("alumnos_db")
    cursor = conn.cursor()
    leer_datos = f"DELETE FROM ingreso WHERE {columnaX} = {valorX}"
    cursor.execute(leer_datos)
    conn.commit()
    conn.close()




if __name__ == "__main__":
    #create_database()
    #create_Table()
    #insert_Row("Fulano","Detal",18,"Informática")
    #insert_Row("Pepe","Honguito",21,"Electrónica")
    #read_Row()
    datos = (
        ("Mengano","Vasuez",20,"Informática"),
        ("Sirenita","Dipierro",22,"Química"),
        ("Rapunsel","Sosa",19,"Física")
    )
    #insert_many_Rows(datos)
    #read_specific("Edad")
    #search_name("Pe")
    #update_Row("Edad",35,"Nombre","'Fulano'")
    #update_Row("Nombre","'Brenda'","Nombre","'Pepe'")
    #delete_row("Nombre","'Sirenita'")