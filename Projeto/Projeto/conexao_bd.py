import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",      # Substitua pelo seu usuário do MySQL
        password="",    # Substitua pela sua senha do MySQL
        database="AluguelCarros"
    )

def consultar_disponibilidade(modelo):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT quantidade FROM Veiculos WHERE modelo = %s", (modelo,))
    resultado = cursor.fetchone()
    conexao.close()
    return resultado["quantidade"] if resultado else None

def atualizar_disponibilidade(modelo, nova_quantidade):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE Veiculos SET quantidade = %s WHERE modelo = %s",
        (nova_quantidade, modelo)
    )
    conexao.commit()
    conexao.close()