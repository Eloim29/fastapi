from typing import Union
from fastapi import FastAPI, HTTPException
from config.database import cursor, conexion
from fastapi.middleware.cors import CORSMiddleware
from modulos.cotizaciones import get_cotizaciones, cotizacion_por_id, add_cotizacion, partial_update_cotizacion, update_cotizaciones, delete_cotizacion
from modulos.clientes import get_clientes
from modulos.facturas import get_facturas

origins = [
    
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/cotizaciones")
def cotizaciones():
    return get_cotizaciones()

@app.get("/cotizaciones/{id}")
def cotizaciones_id(id: int):
    return cotizacion_por_id(id)

@app.post("/cotizaciones")
def agregar_cotizacion(id_clientes: int, cantidad: str, descripcion: str, valor_unitario: str, subtotal: str, iva: str, descuento: str, total: str, orden_pedido: str):
    return add_cotizacion(id_clientes, cantidad, descripcion,valor_unitario, subtotal, iva, descuento, total, orden_pedido )

@app.put("/cotizaciones/{id}")
def actualizar_cotizaciones(id: int, id_clientes: int, cantidad: str, descripcion: str, valor_unitario: str, subtotal: str, iva: str, descuento: str, total: str, orden_pedido: str):
    return update_cotizaciones(id, id_clientes, cantidad, descripcion, valor_unitario, subtotal, iva, descuento, total, orden_pedido)

@app.patch("/cotizaciones/{id}")
def patch_cotizaciones(id: int, id_clientes: int, cantidad: str, descripcion: str, valor_unitario: str,
                              subtotal: str, iva: str, descuento: str , total: str, orden_pedido: str):
    return partial_update_cotizacion(id, id_clientes, cantidad, descripcion, valor_unitario, subtotal, iva, descuento, total, orden_pedido)

@app.delete("/cotizacioines/{id}")
def eliminar_cotizacion(id: int):
    return delete_cotizacion(id)


@app.get("/clientes")
def clientes():
    return get_clientes()





# #************************
# # OBTENER TODOS LOS CLIENTE
# #************************

# @app.get("/clientes")
# def get_clientes():
#     clientes = cursor.execute("SELECT * FROM clientes")
#     clientes = cursor.fetchall()

#     clientesParseadosAJSON = []

#     for cliente in clientes:
#         clienteJSON = {
#             "id": cliente[0],
#             "nombre": cliente[1],
#             "direccion": cliente[2],
#             "telefono": cliente[3],
#             "nit": cliente[4],
#             "correo": cliente[5]
#         }
#         clientesParseadosAJSON.append(clienteJSON)

#     return clientesParseadosAJSON

# #************************
# # OBTENER UN CLIENTE POR SU NOMBRE
# #************************

# @app.get("/clientes/{nombre}")
# def getUserByName(nombre: str):
#     clientes = cursor.execute(f"SELECT * FROM clientes WHERE nombre = '{nombre}'")
#     clientes = cursor.fetchone()

#     if clientes:
#         clienteJSON = {
#             "id": clientes[0],
#             "nombre": clientes[1],
#             "direccion": clientes[2],
#             "telefono": clientes[3],
#             "nit": clientes[4],
#             "correo": clientes[5]
#         }
#         return clienteJSON
#     else:
#         return {"error": "Cliente no encontrado"}
    

# #************************
# # AGREGAR UN CLIENTE
# #************************

# @app.post("/clientes")
# def addClientes(nombre: str, direccion: str, telefono: str, nit: str, correo: str):
#     cursor.execute(f"INSERT INTO clientes (nombre, direccion, telefono, nit, correo) VALUES ('{nombre}', '{direccion}', '{telefono}', '{nit}', '{correo}')")
#     conexion.commit()
    
#     return {"Mensaje": "Cliente Agregado"}


# #************************
# # ACTUALIZAR TODOS LOS DATOS DE UN CLIENTE
# #************************

# @app.put("/clientes/{id}")
# def update_cliente(id: int, nombre: str, direccion: str, telefono: str, nit: str, correo: str):
#     cursor.execute(f"UPDATE clientes SET nombre='{nombre}', direccion='{direccion}', telefono='{telefono}', nit='{nit}', correo='{correo}' WHERE id={id}")
#     conexion.commit()
    
#     return {"Mensaje": "Cliente Actualizado"}


# #************************
# # ACTUALIZAR PARCIALMENTE LOS DATOS DE UN CLIENTE
# #************************

# @app.patch("/clientes/{id}")
# def partial_update_cliente(id: int, nombre: str = None, direccion: str = None, telefono: str = None, nit: str = None, correo: str = None):
#     update_fields = []
#     if nombre:
#         update_fields.append(f"nombre='{nombre}'")
#     if direccion:
#         update_fields.append(f"direccion='{direccion}'")
#     if telefono:
#         update_fields.append(f"telefono='{telefono}'")
#     if nit:
#         update_fields.append(f"nit='{nit}'")
#     if correo:
#         update_fields.append(f"correo='{correo}'")

#     if not update_fields:
#         return {"error": "Ningún campo proporcionado para actualizar"}
    
#     set_clause = ", ".join(update_fields)
#     cursor.execute(f"UPDATE clientes SET {set_clause} WHERE id={id}")
#     conexion.commit()

#     return {"Mensaje": "Cliente Actualizado"}
    

# #************************
# # ELIMINAR UN CLIENTE
# #************************

# @app.delete("/cliente/{id}")
# def deleteClientes(id: int):
#     clientes = cursor.execute(f"SELECT * FROM  clientes WHERE id={id}")
#     clientes = cursor.fetchone()
#     if clientes:
#         cursor.execute(f"DELETE FORM clientes WHERE id={id}")
#         conexion.commit()
#         return {"Mensaje": "Cliente eliminado"}
#     else:
#         raise HTTPException(status_code=404, detail="Cliente no encontrado")