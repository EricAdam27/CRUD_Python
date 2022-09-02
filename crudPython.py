import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='dbaulacrud'
)

cursor = conexao.cursor()

# CRUD

cursor.close()
conexao.close()
