from Pessoa import Pessoa
listaPessoas = []

def inserePessoa():
   nome = str(input("Insira o nome: "))
   idade = int(input("Insira a idade: "))
   pessoaAdicionada = Pessoa(nome, idade)
   listaPessoas.append(pessoaAdicionada)
   print("\nNova pessoa criada:\n" + "\nNome: " + listaPessoas[-1].getNome() + "\nIdade: " + str(listaPessoas[-1].getIdade()) + "\n")

def exibePessoas(lista):
   if len(lista) == 0:
      print("\nNão há pessoas cadastradas.\n")
   else:
    for pessoa in lista:
      print(pessoa.toString())

def ordenaNomeCrescente():
   pessoasOrdemCrescente = listaPessoas.copy()
   pessoasOrdemCrescente.sort(key=lambda x: x.nome)
   exibePessoas(pessoasOrdemCrescente)

def ordenaIdadeCrescente():
   pessoasIdadeCrescente = listaPessoas.copy()
   pessoasIdadeCrescente.sort(key=lambda x: x.idade)
   exibePessoas(pessoasIdadeCrescente)

def exibirPorCategoria():
   listaCriancas = []
   listaAdolescentes = []
   listaAdultos = []
   listaIdosos = []
   for pessoa in listaPessoas:
      if pessoa.getIdade() > 0 and pessoa.getIdade() < 12:
         listaCriancas.append(pessoa)
      elif pessoa.getIdade() >= 12 and pessoa.getIdade() < 20:
         listaAdolescentes.append(pessoa)
      elif pessoa.getIdade() >= 20 and pessoa.getIdade() < 65:
         listaAdultos.append(pessoa)
      elif pessoa.getIdade() > 65:
         listaIdosos.append(pessoa)

   print("Lista de Crianças: ")
   exibePessoas(listaCriancas)
   print("Lista de Adolescentes: ")
   exibePessoas(listaAdolescentes)
   print("Lista de Adultos: ")
   exibePessoas(listaAdultos)
   print("Lista de Idosos: ")
   exibePessoas(listaIdosos)
