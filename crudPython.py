import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='dbaulacrud'
)

cursor = conexao.cursor()

# CREATE
nomeProduto = 'Chocolate'
valorProduto = 7
comando = f'insert into vendas(nomeProduto, valorProduto) values ("{nomeProduto}", {valorProduto})'
cursor.execute(comando)
conexao.commit()

# READ

# UPDATE

# DELETE

cursor.close()
conexao.close()