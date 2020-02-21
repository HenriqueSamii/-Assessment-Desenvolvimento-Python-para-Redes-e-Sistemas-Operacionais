# -Assessment-Desenvolvimento-Python-para-Redes-e-Sistemas-Operacionais


1. Escreva um programa em Python que:
        
	  a. obtenha a lista de processos executando no momento, considerando que o processo pode deixar de existir enquanto seu programa manipula suas informações;
        
	  b. imprima o nome do processo e seu PID;
        
	  c. imprima também o percentual de uso de CPU e de uso de memória.
2. Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo para executar o programa do sistema Windows bloco de notas (notepad) para abrir o arquivo.
3. Escreva um programa em Python que:
        
	  a. Gere uma estrutura que armazena o nome dos arquivos em um determinado diretório e a quantidade de bytes que eles ocupam em disco. Obtenha o nome do diretório do usuário.
        
	  b. Ordene decrescentemente esta estrutura pelo valor da quantidade de bytes ocupada em disco (pode usar as funções sort ou sorted);
        
	  c. Dere um arquivo texto com os valores desta estrutura ordenados.
    Escreva um programa em Python que leia um arquivo texto e apresente na tela o seu conteúdo reverso. Exemplo (não esqueça de testar se o arquivo existe):

         arquivo.txt

         Bom dia

        Você pode falar agora?

        Resultado na tela:

        ?aroga ralaf edop êcoV

        aid moB

5. Escreva um programa em Python que leia dois arquivos, a.txt e b.txt, como a seguir (não esqueça de testar se os arquivos existem):

        a. txt: 1 15 -42 33 -7 -2 39 8


        b. txt: 19 56 -43 23 -7 -11 33 21 61 9
	  	

	  Seu programa deve somar elemento por elemento de cada arquivo e imprimir o resultado na tela. Isto é, o primeiro elemento de a.txt deve ser somado ao primeiro elemento de b.txt, segundo elemento de a.txt deve ser somado ao segundo elemento de b.txt, e assim sucessivamente. Caso um arquivo tenha mais elementos que o outro, os elementos que sobrarem do maior devem ser somados a zero.

6. Escreva um programa cliente e servidor sobre TCP em Python em que:
        
      a. O cliente envia para o servidor o nome de um diretório e recebe a lista de arquivos (apenas arquivos) existente nele.

      b. O servidor recebe a requisição do cliente, captura o nome dos arquivos no diretório em questão e envia a resposta ao cliente de volta.
    
7. Escreva um programa cliente e servidor sobre UDP em Python que:
        
      a. O cliente envia para o servidor o pedido de obtenção da quantidade total e disponível de memória no servidor e espera receber a resposta durante 5s. Caso passem os 5s, faça seu programa cliente tentar novamente mais 5 vezes (ainda esperando 5s a resposta) antes de desistir.

      b. O servidor repetidamente recebe a requisição do cliente, captura a informação da quantidade total e disponível de memória há no servidor e envia a resposta ao cliente de volta.
8. Escreva 3 programas em Python que resolva o seguinte problema:

      Dado um vetor A de tamanho N com apenas números inteiros positivos, calcule o fatorial de cada um deles e armazene o resultado em um vetor B.

      Para calcular o fatorial, utilize a seguinte função:



        def fatorial(n):
        fat = n
        for i in range(n-1,1,-1):
          fat = fat * i
        return(fat)


      Os modos de desenvolver seu programa devem ser:

          a. sequencialmente (sem concorrência);

          b. usando o módulo threading com 4 threads;

          c. usando o módulo multiprocessing com 4 processos.
