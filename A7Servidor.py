"""7.Escreva um programa cliente e servidor sobre UDP em Python que:

    O cliente envia para o servidor o pedido de obtenção da quantidade total e disponível de memória no servidor e espera receber a resposta durante 5s. Caso passem os 5s, faça seu programa cliente tentar novamente mais 5 vezes (ainda esperando 5s a resposta) antes de desistir.
    O servidor repetidamente recebe a requisição do cliente, captura a informação da quantidade total e disponível de memória há no servidor e envia a resposta ao cliente de volta.
"""

import socket,psutil#,time
#porta IP servidor -Receber
socket_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host_name = socket.gethostname()
socket_server.bind((host_name,9991))

print('Esperando receber na porta', 9991)

while True:

    pacote, destino = socket_server.recvfrom(1024)
    cliente_input = pacote.decode('utf-8')
    ack = 'ACK'.encode('ascii')
    #time.sleep(21)
    if cliente_input == 'm':
        infoMemoria = psutil.virtual_memory()
        resposta = "Memoria Total: " + str(infoMemoria.total/1048576) +" Mb     Memoria em livre:" + str(infoMemoria.available/1048576) + " Mb - " + str(100-infoMemoria.percent) + " %"
        ack = resposta.encode('ascii')
    elif cliente_input == 'sair':
        break
    else:
        ack = str('Opção',cliente_input,'não valida').encode('ascii')

    socket_server.sendto(ack,destino)

socket_server.close()
input('Coneção termoinada, pressione qualquer tecla para sair')

"""import socket,psutil
infoMemoria = psutil.virtual_memory()
resposta = "Memoria Total: " + str(infoMemoria.total/1048576) +" Mb     Memoria em livre:" + str(infoMemoria.available/1048576) + " Mb - " + str(100-infoMemoria.percent) + " %"
print(resposta)"""