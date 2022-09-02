import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='dbaulacrud'
)

cursor = conexao.cursor()

# CREATE
"""nomeProduto = 'Chocolate'
valorProduto = 7
comando = f'insert into vendas(nomeProduto, valorProduto) values ("{nomeProduto}", {valorProduto})'
cursor.execute(comando)
conexao.commit()"""

# READ
"""comando = 'select * from vendas'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)"""

# UPDATE
nomeProduto = 'Toddy'
valorProduto = 5
comando = f'update vendas set valorProduto = {valorProduto} where nomeProduto = "{nomeProduto}"'
cursor.execute(comando)
conexao.commit()

# DELETE

cursor.close()
conexao.close()