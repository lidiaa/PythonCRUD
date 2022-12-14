#1. instalar o MySQL

#2. instalar o Driver do MySQL: pip install mysql-connector-python

#3. importar o conector do MySQL
import mysql.connector

#CRUD: Create, Read, Update, Delete = inserir, ler, atualizar e deletar registros

#detalhes do banco de dados no arquivo schema.sql

#4.criar a conexao
conexao = mysql.connector.connect(
    host='localhost',
    user='nome_do_seu_usuario_do_bd',
    password='sua_senha_aqui',
    database='python_crud' #nome do bd
)


#5. executar a conexao
cursor = conexao.cursor()


#CREATE
nomePais = "Argentina"
titulos = 2

comando = f'INSERT INTO paises (nome_pais, qtd_titulos) VALUES ("{nomePais}",{titulos})'
cursor.execute(comando)
conexao.commit()


#READ
comando = f'SELECT * FROM paises'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)



#UPDATE
titulos = 6
paisCampeao = "Brasil"

comando = f'UPDATE paises SET qtd_titulos = {titulos} WHERE nome_pais = "{paisCampeao}"'
cursor.execute(comando)
conexao.commit()




#DELETE
deletarPais = "Argentina"

comando = f'DELETE FROM paises WHERE nome_pais = "{deletarPais}"'
cursor.execute(comando)
conexao.commit()



#6. fechar a conexao
cursor.close()
conexao.close()