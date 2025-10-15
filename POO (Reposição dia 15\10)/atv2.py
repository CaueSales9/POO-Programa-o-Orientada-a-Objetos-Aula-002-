estoque_comida = {
    "sanduiche": 15,
    "bolo": 10,
    "pizza": 8,
    "hamburguer": 12,
    "batata_frita": 20,
    "salgado": 25,
    "pastel": 18,
    "coxinha": 30,
    "biscoito": 40,
    "chocolate": 22
}

estoque_bebida = {
    "refrigerante": 25,
    "suco": 2,
    "agua": 50,
    "cafe": 30,
    "cha": 15,
    "vitamina": 10,
    "energetico": 8,
    "milkshake": 12,
    "leite": 20,
    "cha_gelado": 6
}

def mostrar_estoque():
    print("=== Estoque de Bebidas ===")
    for produto, qtd in estoque_bebida.items():
        print(f"{produto}: {qtd}")
    print("=== Estoque de Comidas ===")
    for produto, qtd in estoque_comida.items():
        print(f"{produto}: {qtd}")
    print("="*40)


def adicionar_produto():
    while True:
        try:
            pergunta = int(input('Deseja adicionar\n1 - Comida\n2 - Bebida\n> '))
        except ValueError:
            print("Digite um número válido.")
            continue

        if pergunta == 1:
            nome = input('Qual o nome do produto?\n> ').strip()
            quantidade = int(input('Qual a quantidade do produto?\n> '))
            estoque_comida[nome] = estoque_comida.get(nome, 0) + quantidade
            print(f'Produto "{nome}" com quantidade {quantidade} adicionado em Comidas.')
            break

        elif pergunta == 2:
            nome = input('Qual o nome do produto?\n> ').strip()
            quantidade = int(input('Qual a quantidade do produto?\n> '))
            estoque_bebida[nome] = estoque_bebida.get(nome, 0) + quantidade
            print(f'Produto "{nome}" com quantidade {quantidade} adicionado em Bebidas.')
            break

        else:
            print('Opção inválida! Tente novamente.')
            continue


def remover_produto():
    while True:
        try:
            pergunta = int(input('Você deseja remover\n1 - Comida\n2 - Bebida\n> '))
        except ValueError:
            print("Digite um número válido.")
            continue

        if pergunta == 1:
            nome = input('Qual produto deseja remover?\n> ').strip()
            if nome in estoque_comida:
                qtd_remover = int(input(f'Quantidade a remover ({estoque_comida[nome]} disponíveis):\n> '))
                if qtd_remover >= estoque_comida[nome]:
                    del estoque_comida[nome]
                    print(f'Produto "{nome}" removido do estoque de Comidas.')
                else:
                    estoque_comida[nome] -= qtd_remover
                    print(f'Removido {qtd_remover} unidades de "{nome}".')
            else:
                print('Produto não encontrado em Comidas.')
            break

        elif pergunta == 2:
            nome = input('Qual produto deseja remover?\n> ').strip()
            if nome in estoque_bebida:
                qtd_remover = int(input(f'Quantidade a remover ({estoque_bebida[nome]} disponíveis):\n> '))
                if qtd_remover >= estoque_bebida[nome]:
                    del estoque_bebida[nome]
                    print(f'Produto "{nome}" removido do estoque de Bebidas.')
                else:
                    estoque_bebida[nome] -= qtd_remover
                    print(f'Removido {qtd_remover} unidades de "{nome}".')
            else:
                print('Produto não encontrado em Bebidas.')
            break

        else:
            print('Opção inválida!')
            continue



def consultar_produto():
    nome = input('Digite o nome do produto que deseja consultar:\n> ').strip()
    if nome in estoque_comida:
        print(f'{nome} está em Comidas com {estoque_comida[nome]} unidades.')
    elif nome in estoque_bebida:
        print(f'{nome} está em Bebidas com {estoque_bebida[nome]} unidades.')
    else:
        print('Produto não encontrado no estoque.')


def salvar_relatorio():
    with open('POO_Aula.txt', 'w') as f:
        f.write("Relatório de Estoque:\n")
        for item, qtd in estoque_comida.items():
            f.write(f"{item}: {qtd}\n")
        for item, qtd in estoque_bebida.items():
            f.write(f"{item}: {qtd}\n")




def repor_auto():
    global estoque_bebida, estoque_comida

    for nome in estoque_bebida:
        if estoque_bebida[nome] <= 3:
            estoque_bebida[nome] += 5

    for nome in estoque_comida:
        if estoque_comida[nome] <= 3:
            estoque_comida[nome] += 5

    print('Reposição realizada com sucesso')


def menu():
    while True:
        print('=' * 40)
        print('1 - Adicionar produto')
        print('2 - Remover produto')
        print('3 - Consultar produto')
        print('4 - Mostrar estoque')
        print('5 - Salvar arquivo')
        print('6 - Repor automatico')
        print('=' * 40)
        
        try:
            pergunta = int(input('Bem-vindo! O que deseja realizar?\n> '))
        except ValueError:
            print("Digite um número válido.")
            continue

        if pergunta == 1:
            adicionar_produto()
        elif pergunta == 2:
            remover_produto()
        elif pergunta == 3:
            consultar_produto()
        elif pergunta == 4:
            mostrar_estoque()
        elif pergunta == 5:
            salvar_relatorio()
        elif pergunta == 6:
            repor_auto()
        else:
            print('Opção inválida.')

    

menu()
