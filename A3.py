"""3.Escreva um programa em Python que:

    gere uma estrutura que armazena o nome dos arquivos em um determinado diretório e a quantidade de bytes que eles ocupam em disco. 
    Obtenha o nome do diretório do usuário.
    Ordene decrescentemente esta estrutura pelo valor da quantidade de bytes ocupada em disco (pode usar as funções sort ou sorted);
    gere um arquivo texto com os valores desta estrutura ordenados.
"""
import os

input_arq = input('O caminho absoluto do arquivo para procurar - ')

if os.path.exists(input_arq):
    arrayDeDir = []

    listDirectorio = os.listdir(input_arq)
    for file in listDirectorio:
        filePath = input_arq+"\\"+file
        if os.path.isfile(filePath):
            bytesR = os.path.getsize(filePath)
            dicNovo = {"nome":file,"tamanho":bytesR}
            arrayDeDir.append(dicNovo)
    
    arrayDeDir = sorted(arrayDeDir, key=lambda k: k['tamanho'], reverse=True) 
    nomeArquivo = input_arq.split("\\")
    novoTxt = open('ArquivosDoDirectorio'+nomeArquivo[len(nomeArquivo)-1]+'.txt','w')
    for dicArq in arrayDeDir:
        itemString = 'Arquivo '+ dicArq["nome"] + " tem " + str(dicArq["tamanho"]) + " bytes\n"
        novoTxt.write(itemString)
    novoTxt.close()
else:
    print("Não se encontrou nenhum arquivo txt este nome")