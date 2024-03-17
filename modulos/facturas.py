from config.database import cursor, conexion
from fastapi import FastAPI, HTTPException


#************************
# OBTENER TODOS LAS FACTURAS
#************************
def get_facturas():
    facturas = cursor.execute("SELECT * FROM facturas")
    facturas = cursor.fetchall()

    facturasParseadosAJSON = []

    for factura in facturas:
        facturaJSON = {
            "id": factura[0],
            "id_clientes": factura[1],
            "cantidad": factura[2],
            "descripcion": factura[3],
            "valor_unitario": factura[4],
            "subtotal": factura[5],
            "iva": factura[6],
            "descuento": facturas[7],
            "total": factura[8],
            "orden": factura[9],
            "migo": factura[10],
            "fecha": factura[11],
        }
        facturasParseadosAJSON.append(facturaJSON)

    return facturasParseadosAJSON

#**********************************
# OBTENER UNA COTIZACION POR SU ID
#**********************************

def facturas_por_id(id: int):
    facturas = cursor.execute(f"SELECT * FROM facturas WHERE id = '{id}'")
    facturas = cursor.fetchone()

    if facturas:
        facturaJSON = {
            "id": facturas[0],
            "id_clientes": facturas[1],
            "cantidad": facturas[2],
            "descripcion": facturas[3],
            "valor_unitario": facturas[4],
            "subtotal": facturas[5],
            "iva": facturas[6],
            "descuento": facturas[7],
            "total": facturas[8],
            "orden": facturas[9],
            "migo": facturas[10],
            "fecha": facturas[11],
        }
        return facturaJSON
    else:
        return {"error": "factura no encontrada"}
    
    
#************************
# AGREGAR UNA COTIZACION
#************************

def add_factura(id_clientes: int, cantidad: str, descripcion: str, valor_unitario: str, subtotal: str, iva: str, descuento: str, total: str, orden_pedido: str):
    cursor.execute(f"INSERT INTO cotizaciones (id_clientes, cantidad, descripcion, valor_unitario, subtotal, iva, descuento, total) VALUES ('{id_clientes}', {cantidad}', '{descripcion}', '{valor_unitario}, '{subtotal}', '{iva}', '{descuento}', '{total}', '{orden_pedido}')")
    conexion.commit()
    
    return {"Mensaje": "Cotizacion Agregada"}