"""7.Escreva um programa cliente e servidor sobre UDP em Python que:

    O cliente envia para o servidor o pedido de obtenção da quantidade total e disponível de memória no servidor e espera receber a resposta durante 5s. Caso passem os 5s, faça seu programa cliente tentar novamente mais 5 vezes (ainda esperando 5s a resposta) antes de desistir.
    O servidor repetidamente recebe a requisição do cliente, captura a informação da quantidade total e disponível de memória há no servidor e envia a resposta ao cliente de volta.
"""

import socket
#porta IP servidor - Enviar
host = socket.gethostname()
port = 9991
socket_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
dest = (host,port)
socket_server.settimeout(5)

while True:
    mesagem = input('Degite "m" para receber quantidade total e disponível de memoria - ')
    socket_server.sendto(mesagem.encode('ascii'),dest)
    if mesagem == 'sair':
        break
    else:
        veses = 0
        while True:
            try:
                ack_mensagem,address = socket_server.recvfrom(1024)
                print(ack_mensagem.decode('ascii'))
                break
            except socket.timeout:
                if veses < 4:
                    veses += 1
                    print("Tentanto de novo")
                else:
                    print("Numero de Timouts ultrapasou limite, programa terminado")
                    break

socket_server.close()