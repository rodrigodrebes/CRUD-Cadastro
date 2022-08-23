# DesafioCadastro
Desafio de construção de um programa de cadastros.

Para testar a funcionalidade do programa, abra o arquivo em um editor/leitor de código-fonte (como o VScode) e rode o arquivo “ProgramaCadastro.py”. 

Primeiramente, optou-se pela criação de uma classe Pessoa para conter as funções de get e set dos dados recebidos, agilizando o processo no código principal da interface de usuário. 

Uma vez que se trata de um programa onde o conteúdo do objeto não é originado diretamente do código mas sim recebido de uma fonte externa em tempo de execução, prossegui na criação de uma lista global a ser utilizada para o armazenamento dos valores de input. Feito isso, foi dado seguimento na construção das funcionalidades do programa no arquivo Funcoes, por meio da construção de funções específicas para o programa.

A primeira função (inserePessoa) criada foi a que solicita o input dos dados de nome e idade do usuário. O mecanismo de ação dessa função consiste no recebimento desses dados, armazenamento por meio de append à respectiva lista. Inseridos os dados, o usuário recebe uma mensagem informando-o do conteúdo dos dados inseridos e possibilita a ele a exclusão da pessoa cadastrada, em caso de erro de digitação.
A segunda função (exibePessoas) fornece ao usuário uma lista das pessoas adicionadas até o momento.
A terceira função (ordenaNomeCrescente) fornece ao usuário uma lista de nomes em ordem crescente, alfabética. 
A quarta função (ordenaIdadeCrescente) fornece ao usuário uma lista de idade em ordem numérica crescente. A utilização do lambda surge como alternativa da criação de funções específicas, possibilitando um código mais ágil.
A quinta função (exibirPorCategoria) fornece ao usuário uma exibição de todas as pessoas, separadas por faixas etárias. Dentro dessa função foram criadas listas específicas nas quais a função irá armazenar as pessoas adicionadas que se encaixarem nos requisitos. 
A sexta e última função (executarPrograma) cria um menu interativo em while concatenando as funções anteriormente criadas.
