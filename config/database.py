import mysql.connector

config = {
    "user": "root",
    "password": "Eloimadmin29",
    "host": "localhost",
    "port": "3307",
    "database": "sistemacontable"
}

conexion = mysql.connector.connect(
    user=config["user"],
    host=config["host"],
    password=config["password"],
    database=config["database"],
    port=config["port"]
)

cursor = conexion.cursor()

