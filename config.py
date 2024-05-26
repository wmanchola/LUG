# config.py
import pyodbc

def get_db_connection():
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=K01LP-72H5ZY2;'  # Cambia 'your_server' por el nombre de tu servidor
        'DATABASE=TIENDA;'     # Nombre de la base de datos
        'UID=sa;'   # Cambia 'your_username' por tu nombre de usuario
        'PWD=K0m4tsu'    # Cambia 'your_password' por tu contraseña
    )
    return connection
