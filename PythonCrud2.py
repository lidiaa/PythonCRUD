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

print("CRUD em Python - Copa do Mundo 2022\n")

print("1-Inserir um país")
print("2-Ler registros")
print("3-Atualizar quantidade de títulos")
print("4-Deletar um país")

opcao=int(input("Digite uma opção: "))

if opcao == 1:
    #CREATE
    nomePais = input("digite o nome do pais: ")
    titulos = int(input("Digite a quantidade de títulos: "))
    comando = f'INSERT INTO paises (nome_pais, qtd_titulos) VALUES ("{nomePais}",{titulos})'
    cursor.execute(comando)
    conexao.commit()


elif opcao == 2:
    #READ
    comando = f'SELECT * FROM paises'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)
        

elif opcao == 3:
    #UPDATE
    paisCampeao = input("Digite o nome do pais para atualizar: ")
    titulos = int(input("Digite a nova quantidade de títulos: "))
    comando = f'UPDATE paises SET qtd_titulos = {titulos} WHERE nome_pais = "{paisCampeao}"'
    cursor.execute(comando)
    conexao.commit()


elif opcao == 4:
    #DELETE
    deletarPais = input("Digite o nome do pais para deletar: ")
    comando = f'DELETE FROM paises WHERE nome_pais = "{deletarPais}"'
    cursor.execute(comando)
    conexao.commit()


else:
    print("Opção inválida")


#6. fechar a conexao
cursor.close()
conexao.close()