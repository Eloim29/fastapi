from config.database import cursor, conexion
from fastapi import FastAPI, HTTPException


#************************
# OBTENER TODOS LOS GASTOS
#************************

def get_gastos():
    gastos = cursor.execute("SELECT * FROM gastos")
    gastos = cursor.fetchall()

    gastosParseadosAJSON = []

    for gasto in gastos:
        gastoJSON = {
            "id": gasto[0],
            "nombre": gasto[1],
            "direccion": gasto[2],
            "telefono": gasto[3],
            "nit": gasto[4],
            "correo": gasto[5]
        }
        gastosParseadosAJSON.append(gastoJSON)

    return gastosParseadosAJSON


#**********************************
# OBTENER UN GASTO POR SU ID
#**********************************

def gasto_por_id(id: int):
    gastos = cursor.execute(f"SELECT * FROM gastos WHERE id = '{id}'")
    gastos = cursor.fetchone()

    if gastos:
        gastoJSON = {
            "id": gastos[0],
            "nombre": gastos[1],
            "direccion": gastos[2],
            "telefono": gastos[3],
            "nit": gastos[4],
            "correo": gastos[5]
        }
        return gastoJSON
    else:
        return {"error": "gasto no encontrado"}
    
    
#************************
# AGREGAR UN GASTO
#************************

def add_gasto(cantidad: str, descripcion: str, valor: str):
    cursor.execute(f"INSERT INTO gastos (cantidad, descripcion, valor) VALUES ('{cantidad}', '{descripcion}', '{valor}')")
    conexion.commit()
    
    return {"Mensaje": "Gasto Agregado"}


#************************
# ACTUALIZAR TODOS LOS DATOS DE UN CLIENTE
#************************

def update_gastos(id: int, cantidad: str, descripcion: str, valor: str):
    cursor.execute(f"UPDATE gastos SET cantidad='{cantidad}', descripcion='{descripcion}', valor='{valor}' WHERE id={id}")
    conexion.commit()
    
    return {"Mensaje": "Gasto Actualizado"}


#************************
# ACTUALIZAR PARCIALMENTE LOS DATOS DE UN CLIENTE
#************************

def partial_update_gasto(id: int, cantidad: str = None, descripcion: str = None, valor: str = None):
    update_fields = []
    if cantidad:
        update_fields.append(f"cantidad='{cantidad}'")
    if descripcion:
        update_fields.append(f"descripcion='{descripcion}'")
    if valor:
        update_fields.append(f"valor='{valor}'")
    
    if not update_fields:
        return {"error": "Ningún campo proporcionado para actualizar"}
    
    set_clause = ", ".join(update_fields)
    cursor.execute(f"UPDATE gastos SET {set_clause} WHERE id={id}")
    conexion.commit()

    return {"Mensaje": "Gasto Actualizado"}


#************************
# ELIMINAR UN CLIENTE
#************************

def delete_gastos(id: int):
    gastos = cursor.execute(f"SELECT * FROM  gastos WHERE id={id}")
    gastos = cursor.fetchone()
    if gastos:
        cursor.execute(f"DELETE FORM gastos WHERE id={id}")
        conexion.commit()
        return {"Mensaje": "Gasto eliminado"}
    else:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")