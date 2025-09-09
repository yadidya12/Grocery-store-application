import mysql.connector
from mysql.connector import Error
import os
import pymysql

# Keep a single connection only if valid, else reconnect
__cnx = None

def get_sql_connection():
    connection = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "Yadidya@9676",
        database = "groceryapplication"
    )
    return connection
