import socket
import threading
import time
import queue
from conexao_bd import consultar_disponibilidade, atualizar_disponibilidade

# IP e Porta de destino
ip_destino = input("IP do destino: ")
porta = 12345

# Fila para mensagens recebidas
mensagens_recebidas = queue.Queue()


# Função para receber mensagens
def receber_mensagens():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("10.199.12.234", porta))
    server_socket.listen(1)
    
    conn, addr = server_socket.accept()
    print(f"Conectado com {addr}")
    
    while True:
        mensagem = conn.recv(1024).decode()
        
        if mensagem.lower() == "adeus":
            print("O outro usuário encerrou a comunicação.")
            break
        
        mensagens_recebidas.put(f"---> {mensagem}")
        tratar_mensagem(mensagem, conn)
    
    conn.close()
    server_socket.close()


# Função para tratar mensagens recebidas
def tratar_mensagem(mensagem, conn):
    partes = mensagem.split("|")
    comando = partes[0].upper()
    
    if comando == "CONSULTA":
        modelo = partes[1]
        quantidade = consultar_disponibilidade(modelo)
        if quantidade is not None and quantidade > 0:
            resposta = f"DISPONÍVEL|{modelo}"
        else:
            resposta = f"INDISPONÍVEL|{modelo}"
        conn.send(resposta.encode())
    
    elif comando == "ALUGUEL":
        modelo = partes[1]
        quantidade = consultar_disponibilidade(modelo)
        if quantidade is not None and quantidade > 0:
            atualizar_disponibilidade(modelo, quantidade - 1)
            resposta = f"CONFIRMADO|{modelo}"
        else:
            resposta = f"FALHA|{modelo}"
        conn.send(resposta.encode())


# Função para enviar mensagens
def enviar_mensagens():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        try:
            client_socket.connect((ip_destino, porta))
            print("Pronto para enviar mensagens.")
            break
        except ConnectionRefusedError:
            print("Aguardando o outro computador. Tentando outra vez em 3 segundos.")
            time.sleep(3)
    
    while True:
        mensagem = input(":")
        client_socket.send(mensagem.encode())
        if mensagem.lower() == "adeus":
            break
    
    client_socket.close()


# Função para exibir mensagens recebidas
def exibir_mensagens():
    while True:
        while not mensagens_recebidas.empty():
            print(mensagens_recebidas.get())
        time.sleep(0.1)


# Inicia as threads para execução simultânea
threading.Thread(target=receber_mensagens, daemon=True).start()
threading.Thread(target=enviar_mensagens).start()
threading.Thread(target=exibir_mensagens, daemon=True).start()