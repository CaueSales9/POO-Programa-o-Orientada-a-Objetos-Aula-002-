🧾 Descrição do Código — Sistema Bancário Simples em Python

O código implementa um sistema bancário básico orientado a objetos, composto por duas classes principais: conta e Banco.
Ele permite cadastrar contas, consultar saldo, realizar depósitos, saques e transferências entre contas.

💳 Classe conta

A classe conta representa uma conta bancária individual, contendo atributos e métodos que controlam o saldo e as operações básicas.

Atributos:

numero: número identificador da conta (único para cada cliente);

saldo: valor atual disponível na conta (inicialmente definido no construtor).

Métodos:

__init__(self, numero, valorINI=0):
Construtor que inicializa uma nova conta com um número e um saldo inicial (padrão é 0).

get_numero(self):
Retorna o número da conta.

get_saldo(self):
Retorna o saldo atual da conta.

debitar(self, valor_INI):
Realiza o saque (débito) de um valor na conta, desde que seja positivo e menor ou igual ao saldo.

Se a operação for válida, o saldo é reduzido e retorna True.

Caso contrário, exibe uma mensagem de erro e retorna False.

creditar(self, valor_INI):
Realiza o depósito (crédito) de um valor na conta, desde que seja positivo.

Se o valor for válido, ele é adicionado ao saldo e retorna True.

Caso contrário, exibe uma mensagem de erro e retorna False.

🏦 Classe Banco

A classe Banco gerencia múltiplas contas bancárias e suas operações conjuntas.

Atributos:

contas: lista com capacidade para armazenar até 100 objetos da classe conta;

indice: controla a quantidade de contas já cadastradas no banco.

Métodos:

__init__(self):
Inicializa o banco com uma lista de contas vazia (100 posições) e índice em 0.

cadastrar(self, conta):
Adiciona uma nova conta na lista de contas do banco e incrementa o índice.

procurar_conta(self, numero):
Percorre a lista de contas cadastradas para encontrar uma conta com o número informado.

Retorna o objeto conta se for encontrado.

Retorna None caso a conta não exista.

debitar(self, numero, valor):
Localiza a conta pelo número e tenta realizar o débito chamando o método debitar da classe conta.

Caso a conta não exista, exibe “Conta Inexistente!”.

creditar(self, numero, valor):
Localiza a conta e realiza um crédito chamando o método creditar.

Caso a conta não exista, também exibe “Conta Inexistente!”.

saldo(self, numero):
Retorna o saldo atual da conta informada, se ela existir.

Caso contrário, imprime “Conta inexistente”.

transferir(self, origem, destino, valor):
Permite transferir dinheiro de uma conta para outra.

Verifica se ambas as contas (origem e destino) existem.

Confere se o valor é válido (maior que 0 e menor ou igual ao saldo da origem).

Se tudo estiver correto, debita o valor da conta de origem e credita na conta de destino.

Exibe uma mensagem de sucesso ao final.


<br />
<br />
    
UML do código:

![image alt](https://github.com/CaueSales9/POO-Programacao-Orientada-a-Objetos-/blob/22cb00958ce90fdc24d3599381c2d245aa2756e4/POO%20AULA%20006/uml%20de%20um%20banco%20e%20conta.png)
