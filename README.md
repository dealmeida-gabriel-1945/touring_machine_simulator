[//]: # (Título e Descrição)
![](docs/images/01_ifmg_formiga_logo.png)
# IFMG - campus Formiga
# Trabalho de Teoria da Computação
## Interpretador de Máquinas de Turing com sub-rotinas e MT somadora de dois numeros inteiros

### Professor: Walace de Almeida Rodrigues

### Aluno: Gabriel Guimarães de Almeida

### Data de conclusão: 03/01/2022

------------------------------------------------------------

[//]: # (Tabela de Conteúdos)
<!--ts-->
* [Enunciado do trabalho](#enunciado-do-trabalho)
* [Requisitos](#requisitos)
* [Como executar o algoritmo](#como-executar-o-algoritmo)
  * [Como executar suas próprias MTs](#como-executar-suas-próprias-mts)
* [Tecnologia e materiais utilizados](#tecnologia-e-materiais-utilizados)
* [Estrutura de pastas](#estrutura-de-pastas)
* [MT para somar dois inteiros](#mt-para-somar-dois-inteiros)
  * [Linha de raciocínio](#linha-de-raciocínio)
<!--te-->

------------------------------------------------------------

Enunciado do trabalho
=========
Para saber mais sobre o enunciado do trabalho verifique o arquivo **docs/instructions.pdf**

Requisitos
=========
* [Python 3](https://docs.python.org/3/) - linguagem obrigatória para o trabalho

Como executar o algoritmo
=========
Para executar o programa deve-se, na pasta raiz do projeto, inserir um comando o qual deve seguir o seguinte padrão:
>python3 simturing.py path_da_mt [-resume | -r] [-verbose | -v] [-s < n > | -step < n >] [-head "< h >" | -h "< h >"]

* **path_da_mt**
* **[-resume | -r]** flags para informar o programa para não apresentar logs durante sua execução, apenas no final 
da execução mostrando como a fita está no final
* **[-verbose | -v]** flags para informar o programa para apresentar logs durante sua execução. Tais logs mostram o 
bloco de comando que a máquina se encontra, o estado dentro do bloco e parte da fita em volta do cabeçote
* **[-s < n > | -step < n >]** flag para informar o programa a quantidade de passos que ele pode execudar antes de 
solicitar novos comandos
  * **n:** número de passos entre estados que o programa poderá executar antes de realizar a pausa para inserção de 
novos comandos
* **[-head "< h >" | -h "< h >"]** flag para informar o programa quais caracteres aparecerão para simbolizar o cabeçote.
É necessário o uso de aspas
  * **h:** par de caracteres que vão compor a representção visual do cabeçote da máquina de Turing

Como executar suas próprias MTs
=========
Para submeter suas próprias MTs ao programa basta gerar um arquivo .txt e dentro adicionar as linhas de código que 
regerá a MT. Vale salientar que deve-se estar atento à sintaxe, a qual pode ser encontrada no item 4 do documento do
enunciado do trabalho, e que para adicionar breakpoints, os quais são usado para pausar a execução do programa durante
o processamento de uma palavra w, basta adicionar um ponto de exclamação no final do comando desejado.

Vale salientar que o uso da correto da sintaxe da MT é de completa responsabilidade da pessoa que a criou! O uso
correto, em questão da sintaxe e semântica, de "palavras reservadas", tais como "pare" e "retorne", e o respeito à
estrutura padrão dos comandos, blocos e comentários é necessário para o bom funcionamento do interpretador de MTs. 

Tecnologia e materiais utilizados
=========

* [Python 3](https://docs.python.org/3/) - linguagem obrigatória para o trabalho

Estrutura de pastas
=========
Foi decidido a fragmentação das responsabilidades em arquivos python, os quais estão alocados em diferentes pastas
para uma melhor navegação. Cada pasta/arquivo e suas responsabilidades se encontram abaixo:

* *docs/* -> pasta para armazenamento de arquivos para a documentação do projeto
  * */images* -> pasta para armazenamento de arquivos de imagens para a documentação do projeto
  * *instructions.pdf* -> arquivo .pdf contendo o enunciado do trabalho
* */model* -> pasta que armazena algumas classes python, as quais representam as próprias máquinas de Turing, os blocos
de comando e os próprios comandos
* */examples* -> pasta que armazena os arquivos de texto que contém alguns exemplos de MTs as quais podem ser 
reconhecidas por este interpretador
* */util* -> pasta que armazena arquivos python, os quais contêm funções úteis para a leitura dos arquivos de texto e
tratamento das flags
* *parameters.py* -> arquivo python contendo variáveis globais as quais são consumidas e consultadas durante todo o programa
* *simturing.py* -> arquivo python contendo o ponto de partida da execução do código

MT para somar dois inteiros
=========
Esta seção é focada em apresentar a linha de raciocínio da segunda parte do trabalho, a qual consta em a elaboração de
uma máquina de Turing. 

Linha de raciocínio
=========
A linha de raciocínio adotada para realizar a montagem de tal é a mesma que se aplica à crianças quando se deseja
ensiná-las a operação de soma:

* Primeiro devemos somar as unidades
* Depois as dezenas
* Depois as centenas
* E assim por diante...

E, quando a soma entre os numerais resulta em um número maior ou igual a 10, devemos reservar uma unidade de valor para
a integrar na soma da "casa" seguinte.

Para realizar a administração de tais valores foi resolvido separar a palavra submetida em setores:

>Z#A+B=RXE
> 
> onde:
> 
> **Z** é a ala onde fica a marcação do valor que é levado entre as casas, o qual é gerado após uma soma se resultar em 
> um valor maior ou igual a 10
> 
> **A** é a ala onde fica o primeiro número, o qual pode variar de zero até n, onde n é um número que o computador 
> consegue aguentar
> 
> **B** é a ala onde fica o primeiro número, o qual pode variar de zero até n, onde n é um número que o computador
> consegue aguentar
> 
> **R** é onde fica o número resultante da soma, mas este pé gerado inversamente. Exemplo: a soma resultou em 1003, na 
> ala R é armazenado 3001
> 
> **!!!ATENÇÃO!!!** Os valores de A e B são substituidos por letras, cada uma simboliza um uníco numeral. Isso é feito
> para que, ao final da execução, a palavra original poder ser mostrada. 
> 
> **X** é um caractere marcador que é adicionado à fita apenas depois da soma ter sido conluída e ele é usado para
> indicar onde começará a área onde será reescrito o valor em R invertido.
> 
> **E** é onde fica o número correto resultante da soma (inverso do valor armazenado em R). Exemplo: a soma resultou 
> em 1003, na ala R é armazenado 3001, já na ala E é armazenado 1003. Vale salientar que quando tal ala é gerada, a ala
> R é removida assim como o símbolo marcador X.

Caso o usuário insira uma palavra que não respeite o padrão da MT, a fita será apagada e substituída por uma com o 
valor "ERRO"

