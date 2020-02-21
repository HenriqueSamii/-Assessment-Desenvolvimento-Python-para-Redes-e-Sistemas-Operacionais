"""2.Escreva um programa que obtenha um nome de um arquivo texto do 
usuário e crie um processo para executar o programa do sistema Windows bloco de notas (notepad) para abrir o arquivo.
"""
import os

filePath =os.path.dirname(os.path.abspath(__file__))
input_arq = input('Arquivo txt para procurar - ')
input_arqSplit = filePath+"\\"+input_arq+".txt"

if os.path.exists(input_arqSplit):
    os.startfile(input_arqSplit)
else:
    print("Não se encontrou nenhum arquivo txt este nome")