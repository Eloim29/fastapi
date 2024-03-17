from config.database import cursor, conexion
from fastapi import FastAPI, HTTPException


#************************
# OBTENER TODOS LAS COTIZACIONES
#************************

def get_cotizaciones():
    cotizaciones = cursor.execute("SELECT * FROM cotizaciones")
    cotizaciones = cursor.fetchall()

    cotizacionesParseadosAJSON = []

    for cotizacion in cotizaciones:
        cotizacionJSON = {
            "id": cotizacion[0],
            "id_clientes": cotizacion[1],
            "cantidad": cotizacion[2],
            "descripcion": cotizacion[3],
            "valor_unitario": cotizacion[4],
            "subtotal": cotizacion[5],
            "iva": cotizacion[6],
            "descuento": cotizacion[7],
            "total": cotizacion[8],
            "orden_pedido": cotizacion[9],
            "fecha": cotizacion[10],
        }
        cotizacionesParseadosAJSON.append(cotizacionJSON)

    return cotizacionesParseadosAJSON


#**********************************
# OBTENER UNA COTIZACION POR SU ID
#**********************************

def cotizacion_por_id(id: int):
    cotizaciones = cursor.execute(f"SELECT * FROM cotizaciones WHERE id = '{id}'")
    cotizaciones = cursor.fetchone()

    if cotizaciones:
        cotizacionJSON = {
            "id": cotizaciones[0],
            "id_clientes": cotizaciones[1],
            "cantidad": cotizaciones[2],
            "descripcion": cotizaciones[3],
            "valor_unitario": cotizaciones[4],
            "subtotal": cotizaciones[5],
            "iva": cotizaciones[6],
            "descuento": cotizaciones[7],
            "total": cotizaciones[8],
            "orden_pedido": cotizaciones[9],
            "fecha": cotizaciones[10],
        }
        return cotizacionJSON
    else:
        return {"error": "Cotizacion no encontrada"}
    
    
#************************
# AGREGAR UNA COTIZACION
#************************

def add_cotizacion(id_clientes: int, cantidad: str, descripcion: str, valor_unitario: str, subtotal: str, iva: str, descuento: str, total: str, orden_pedido: str):
    cursor.execute(f"INSERT INTO cotizaciones (id_clientes, cantidad, descripcion, valor_unitario, subtotal, iva, descuento, total) VALUES ('{id_clientes}', {cantidad}', '{descripcion}', '{valor_unitario}, '{subtotal}', '{iva}', '{descuento}', '{total}', '{orden_pedido}')")
    conexion.commit()
    
    return {"Mensaje": "Cotizacion Agregada"}


#************************
# ACTUALIZAR TODOS LOS DATOS DE UNA COTIZACION
#************************

def update_cotizaciones(id: int, id_clientes: int, cantidad: str, descripcion: str, valor_unitario: str, subtotal: str, iva: str, descuento: str, total: str, orden_pedido: str):
    cursor.execute(f"UPDATE cotizaciones SET id_clientes='{id_clientes}', cantidad='{cantidad}', descripcion='{descripcion}', valor_unitario='{valor_unitario}', subtotal='{subtotal}', iva='{iva}', descuento='{descuento}', total='{total}', orden_pedido= '{orden_pedido}' WHERE id={id}")
    conexion.commit()
    
    return {"Mensaje": "Cotizacion Actualizada"}


#************************
# ACTUALIZAR PARCIALMENTE LOS DATOS DE UNA COTIZACION
#************************

def partial_update_cotizacion(id: int, id_clientes: int, cantidad: str = None, descripcion: str = None, valor_unitario: str = None,
                              subtotal: str = None, iva: str = None, descuento: str = None, total: str = None, orden_pedido: str = None):
    update_fields = []
    if cantidad:
        update_fields.append(f"cantidad='{cantidad}'")
    if descripcion:
        update_fields.append(f"descripcion='{descripcion}'")
    if valor_unitario:
        update_fields.append(f"valor_unitario='{valor_unitario}'")
    if subtotal:
        update_fields.append(f"subtotal='{subtotal}'")
    if iva:
        update_fields.append(f"iva='{iva}'")
    if descuento:
        update_fields.append(f"descuento='{descuento}'")
    if total:
        update_fields.append(f"total='{total}'")
    if orden_pedido:
        update_fields.append(f"orden_pedido='{orden_pedido}'")
    
    if not update_fields:
        return {"error": "Ningún campo proporcionado para actualizar"}
    
    set_clause = ", ".join(update_fields)
    cursor.execute(f"UPDATE cotizaciones SET {set_clause} WHERE id={id}")
    conexion.commit()

    return {"Mensaje": "Cotizacion Actualizada"}


#************************
# ELIMINAR UNA COTIZACION
#************************

def delete_cotizacion(id: int):
    cotizaciones = cursor.execute(f"SELECT * FROM  cotizaciones WHERE id={id}")
    cotizaciones = cursor.fetchone()
    if cotizaciones:
        cursor.execute(f"DELETE FORM cotizaciones WHERE id={id}")
        conexion.commit()
        return {"Mensaje": "Cotizacion eliminada"}
    else:
        raise HTTPException(status_code=404, detail="Cotizacion no encontrada")