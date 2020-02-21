import psutil,os
from time import sleep
"""
1.Escreva um programa em Python que:

    obtenha a lista de processos executando no momento, considerando que o processo pode deixar de existir enquanto seu programa manipula suas informações;
    imprima o nome do processo e seu PID;
    imprima também o percentual de uso de CPU e de uso de memória.
"""

def info_processos_do_sistema():
    proList = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name','memory_percent','cpu_percent'])
        except psutil.NoSuchProcess:
            pass
        else:
            proList.append(pinfo)
    
    return proList

if __name__ == "__main__":

    while True:
        os.system('cls||clear')
        proList = info_processos_do_sistema()

        for i in proList:
            print("\nNome: " + i["name"] + " - Pid: " + str(i["pid"]) + "\nUso de CPU: " + str(i["cpu_percent"]) + " %"+ "\nUso de memoria: " + str(i["memory_percent"]) + " %")
        
        sleep(10)