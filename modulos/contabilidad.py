from config.database import cursor, conexion
from fastapi import FastAPI, HTTPException


#************************
# OBTENER TODOS LOS GASTOS
#************************

def get_contabilidad():
    contabilidad = cursor.execute("SELECT * FROM contabilidad")
    contabilidad = cursor.fetchall()

    contabilidadParseadosAJSON = []

    for custom in contabilidad:
        customJSON = {
            "id": custom[0],
            "nombre": custom[1],
            "direccion": custom[2],
            "telefono": custom[3],
            "nit": custom[4],
            "correo": custom[5]
        }
        contabilidadParseadosAJSON.append(customJSON)

    return contabilidadParseadosAJSON
