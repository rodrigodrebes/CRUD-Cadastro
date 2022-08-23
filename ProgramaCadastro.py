from Funcoes import *

def executar():
   print("Bem vindo!")
   continuar = True
   while(continuar):
      escolha = int(input("O que você deseja fazer? \n 1 - Cadastrar nova pessoa \n 2 - Consultar pessoas cadastradas \n 3 - Exibir lista de pessoas, ordenadas por ordem alfabética crescente \n 4 - Exibir lista de pessoas ordenadas por Idade crescente \n 5 - Exibir lista de pessoas por categoria \n 6 - Sair do Programa\n"))
      if escolha == 1:
         inserePessoa()
      elif escolha == 2:
         exibePessoas(listaPessoas)
      elif escolha == 3:
         ordenaNomeCrescente()
      elif escolha == 4:
         ordenaIdadeCrescente()
      elif escolha == 5:
         exibirPorCategoria()
      elif escolha == 6:
         print("\nAdeus! Obrigado por utilizar nosso programa :)\n")
         continuar = False
      else:
         print('\nOps! Escolha inexistente. Tente novamente.\n')

executar()