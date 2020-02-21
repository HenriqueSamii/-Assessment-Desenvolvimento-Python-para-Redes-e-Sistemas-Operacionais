"""
Dado um vetor A de tamanho N com apenas números inteiros positivos, calcule o fatorial de cada um deles e armazene o resultado em um vetor B
a.sequencialmente (sem concorrência);
"""
import time

def fatorial(n):
  fat = n
  for i in range(n-1,1,-1):
    fat = fat * i
  return(fat)

vectorB = []

def funFactorialVectorB(listaIn):
  for i in listaIn:
    holder = fatorial(i)
    vectorB.append(holder)

numeroLista = int(input("Tamanho do vector - "))

lista = []

for i in range(1,numeroLista+1):
    lista.append(i)

time0 = time.time()

funFactorialVectorB(lista)

timeFinal = time.time()

print(vectorB)
print("Tamanho do vector",numeroLista)
print('Demorou: ' + str(float(timeFinal) - float(time0)) + ' segundos')

#100 # 150# 1000