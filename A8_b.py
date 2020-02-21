"""
Dado um vetor A de tamanho N com apenas números inteiros positivos, calcule o fatorial de cada um deles e armazene o resultado em um vetor B
b.usando o módulo threading com 4 threads;
"""
import threading,time

def fatorial(n):
  fat = n
  for i in range(n-1,1,-1):
    fat = fat * i
  return(fat)

vectorB = []

def funFactorialVectorB(listaIn,inicio,fim):
  for i in range(inicio,fim):
    holder = fatorial(listaIn[i])
    vectorB.append(holder)

#numeroDeThreads = int(input("Numero de threads - "))
numeroDeThreads = 4
#numeroDeThreads = 6
#numeroDeThreads = 15

numeroLista = int(input("Tamanho do vector - "))

lista = []

for i in range(1,numeroLista+1):
    lista.append(i)

tamanho = len(lista)
#print(tamanho)
metade = int(tamanho//numeroDeThreads)

treadList = []

time0 = time.time()

for i in range(numeroDeThreads):
    t0 = threading.Thread(target=funFactorialVectorB,args=(lista,(metade*i),(metade*(i+1))))
    treadList.append(t0)
    t0.start()

for i in treadList:
    i.join()

timeFinal = time.time()

print(vectorB)
print("Tamanho do vector",numeroLista)
print("Numero de treads",numeroDeThreads)
print('Demorou: ' + str(float(timeFinal) - float(time0)) + ' segundos')