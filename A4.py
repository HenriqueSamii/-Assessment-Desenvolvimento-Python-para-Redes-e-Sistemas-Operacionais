"""4.Escreva um programa em Python que leia um arquivo texto e apresente na tela o seu conteúdo reverso
"""

import os

filePath =os.path.dirname(os.path.abspath(__file__))

input_arqSplit = filePath+"\\teste.txt"

if os.path.exists(input_arqSplit):
    f = open(input_arqSplit, "r")
    fText = f.read().split("\n")
    for s in reversed(fText):
        print(s[::-1])

else:
    print("Não se encontrou nenhum o txt teste")