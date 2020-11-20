from app.config import mysql

class Api_Poni:

    def __init__(self):
        pass

    # METODO PARA ORDENAR LOS DATOS
    def data_dict(self, data: tuple) -> dict:
        datos = {}
        for key, value in enumerate(data):
            datos_lista = []
            for dat in value:
                datos_lista.append(dat)
            datos[key] = datos_lista
        return datos


    def login(self, codalu: str, pass_alu: str) -> tuple:
        cur = mysql.get_db().cursor()
        cur.execute(
            'SELECT * FROM alumnos WHERE codalu=%s and pass_alu=%s', (codalu, pass_alu)
        )
        data = cur.fetchall()
        return data


    def register(self, datos: tuple):
        db = mysql.get_db()
        cur = db.cursor()
        cur.execute(
            'INSERT INTO alumnos VALUES(null, %s, %s, %s, %s, %s, %s, %s, %s)', datos
        )
        db.commit()
        #cur.close()
        #mysql.connect().close()


    def check_register(self, codalu: str) -> bool:
        cur = mysql.get_db().cursor()
        cur.execute(
            'SELECT * FROM alumnos WHERE codalu=%s', (codalu,)
        )
        data = cur.fetchone()
        if len(data) > 0:
            return False
        return True
