"""
Dado um vetor A de tamanho N com apenas números inteiros positivos, calcule o fatorial de cada um deles e armazene o resultado em um vetor B
c.usando o módulo multiprocessing com 4 processos.
"""
import multiprocessing,time

def fatorial(n):
  fat = n
  for i in range(n-1,1,-1):
    fat = fat * i
  return(fat)

def funFactorialVectorB(entrada,saida):
  lista = entrada.get()
  for i in range(0,len(lista)):
    lista[i]= fatorial(lista[i])
  saida.put(lista)

if __name__ == "__main__":
    vectorB = []
    #N_processos = int(input("Numero de processos - "))
    N_processos = 4
    #N_processos = 6
    N_processos = 15

    n_valores = int(input('Tamanho do vector - '))
    valores = []
    for i in range(1,n_valores+1):
        valores.append(i)

    fila_entrada = multiprocessing.Queue()
    fila_saida = multiprocessing.Queue()
    tamanho = len(valores)

    time0 = time.time()

    processos = []
    for i in range(N_processos):
        inicio = i*int(tamanho//N_processos)
        fim = (i+1)*int(tamanho//N_processos)
        #print(inicio)
        #print(fim)
        fila_entrada.put(valores[inicio:fim])
        p = multiprocessing.Process(target = funFactorialVectorB,args = (fila_entrada,fila_saida))
        p.start()
        processos.append(p)

    for i in processos:
        i.join()

    lista_final = []
    for i in processos:
        vectorB += fila_saida.get()

    timeFinal = time.time()
    print(vectorB)
    print("Tamanho do vector",n_valores)
    print("Numero de processos",N_processos)
    print('Demorou: ' + str(float(timeFinal) - float(time0)) + ' segundos')
