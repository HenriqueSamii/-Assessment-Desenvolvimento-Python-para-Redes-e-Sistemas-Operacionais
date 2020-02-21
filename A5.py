"""5.Escreva um programa em Python que leia dois arquivos, a.txt e b.txt, como a seguir
"""

import os

filePath =os.path.dirname(os.path.abspath(__file__))
aPath = filePath+"\\a.txt"
bPath = filePath+"\\b.txt"
if os.path.exists(aPath) and os.path.exists(bPath):
    aString = open(aPath, "r").read()
    bString = open(bPath, "r").read()
    aList = aString.split(" ")
    bList = bString.split(" ")

    forLenght = len(aList)
    if len(bList) < len(aList):
        forLenght = len(bList)

    respostaFinal = ""
    for i in range(forLenght):
        respostaFinal = respostaFinal + str(int(aList[i]) + int(bList[i])) + " "

    if len(bList) < len(aList):
        for i in range(forLenght,len(aList)):
            respostaFinal = respostaFinal + aList[i] + " "
    elif len(bList) > len(aList):
        for i in range(forLenght,len(bList)):
            respostaFinal = respostaFinal + bList[i] + " "

    print(respostaFinal)
else:
    if not os.path.exists(aPath):
        print ("a não existe")
    if not os.path.exists(bPath):
        print ("b não existe")