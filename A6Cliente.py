"""6.Escreva um programa cliente e servidor sobre TCP em Python em que:

    O cliente envia para o servidor o nome de um diretório e recebe a lista de arquivos (apenas arquivos) existente nele.
    O servidor recebe a requisição do cliente, captura o nome dos arquivos no diretório em questão e envia a resposta ao cliente de volta.
"""

import socket, pickle

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999

socket_cliente.connect((host, port))
input_dir = input('Diretório - ')
socket_cliente.send(input_dir.encode('ascii'))
data = b""
while True:
    packet = socket_cliente.recv(1024)
    if not packet: break
    data += packet
lista = pickle.loads(data)
print(lista)
socket_cliente.close()