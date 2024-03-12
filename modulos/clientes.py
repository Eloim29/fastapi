from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from config.database import cursor, conexion
from typing import Union


#************************
# OBTENER TODOS LOS CLIENTE
#************************


def getClientes():
    clientes = cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    clientesParseadosAJSON = []

    for cliente in clientes:
        clienteJSON = {
            "id": cliente[0],
            "nombre": cliente[1],
            "direccion": cliente[2],
            "telefono": cliente[3],
            "nit": cliente[4],
            "correo": cliente[5]
        }
        clientesParseadosAJSON.append(clienteJSON)

    return clientesParseadosAJSON

#**********************************
# OBTENER UN CLIENTE POR SU NOMBRE
#**********************************


def cliente_por_nombre(nombre: str):
    clientes = cursor.execute(f"SELECT * FROM clientes WHERE nombre = '{nombre}'")
    clientes = cursor.fetchone()

    if clientes:
        clienteJSON = {
            "id": clientes[0],
            "nombre": clientes[1],
            "direccion": clientes[2],
            "telefono": clientes[3],
            "nit": clientes[4],
            "correo": clientes[5]
        }
        return clienteJSON
    else:
        return {"error": "Cliente no encontrado"}
    

#************************
# AGREGAR UN CLIENTE
#************************


def addClientes(nombre: str, direccion: str, telefono: str, nit: str, correo: str):
    cursor.execute(f"INSERT INTO clientes (nombre, direccion, telefono, nit, correo) VALUES ('{nombre}', '{direccion}', '{telefono}', '{nit}', '{correo}')")
    conexion.commit()
    
    return {"Mensaje": "Cliente Agregado"}


#************************
# ACTUALIZAR TODOS LOS DATOS DE UN CLIENTE
#************************


def update_cliente(id: int, nombre: str, direccion: str, telefono: str, nit: str, correo: str):
    cursor.execute(f"UPDATE clientes SET nombre='{nombre}', direccion='{direccion}', telefono='{telefono}', nit='{nit}', correo='{correo}' WHERE id={id}")
    conexion.commit()
    
    return {"Mensaje": "Cliente Actualizado"}


#************************
# ACTUALIZAR PARCIALMENTE LOS DATOS DE UN CLIENTE
#************************


def partial_update_cliente(id: int, nombre: str = None, direccion: str = None, telefono: str = None, nit: str = None, correo: str = None):
    update_fields = []
    if nombre:
        update_fields.append(f"nombre='{nombre}'")
    if direccion:
        update_fields.append(f"direccion='{direccion}'")
    if telefono:
        update_fields.append(f"telefono='{telefono}'")
    if nit:
        update_fields.append(f"nit='{nit}'")
    if correo:
        update_fields.append(f"correo='{correo}'")

    if not update_fields:
        return {"error": "Ningún campo proporcionado para actualizar"}
    
    set_clause = ", ".join(update_fields)
    cursor.execute(f"UPDATE clientes SET {set_clause} WHERE id={id}")
    conexion.commit()

    return {"Mensaje": "Cliente Actualizado"}
    

#************************
# ELIMINAR UN CLIENTE
#************************


def deleteClientes(id: int):
    clientes = cursor.execute(f"SELECT * FROM  clientes WHERE id={id}")
    clientes = cursor.fetchone()
    if clientes:
        cursor.execute(f"DELETE FORM clientes WHERE id={id}")
        conexion.commit()
        return {"Mensaje": "Cliente eliminado"}
    else:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")