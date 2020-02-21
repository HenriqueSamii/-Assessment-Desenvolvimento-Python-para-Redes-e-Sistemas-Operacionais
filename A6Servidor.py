"""6.Escreva um programa cliente e servidor sobre TCP em Python em que:

    O cliente envia para o servidor o nome de um diretório e recebe a lista de arquivos (apenas arquivos) existente nele.
    O servidor recebe a requisição do cliente, captura o nome dos arquivos no diretório em questão e envia a resposta ao cliente de volta.
"""

import socket,os, pickle
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999

socket_servidor.bind((host, port))
socket_servidor.listen()
print("escutando na porta", port)
while True:
    (cliente, cliente_addr) = socket_servidor.accept()
    print("conectado ao", str(cliente_addr))
    mensagem = cliente.recv(1024)
    pathS = mensagem.decode('ascii')

    try:
        arr = os.listdir(pathS)
        lista_resposta = []
        for i in arr:
            #os.path.join(dir_atual, i)
            if os.path.isfile(pathS + "\\" +i):
                lista_resposta.append(i)

        #retornar a cliente lista_resposta
        bytes_resp = pickle.dumps(lista_resposta)
        cliente.send(bytes_resp)
    except Exception as erro:
        print(str(erro))
    
    cliente.close()