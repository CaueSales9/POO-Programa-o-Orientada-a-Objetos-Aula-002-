while True:
    n1 = int(input('Digite um número que 5 dígitos\n> '))
    conversao_str = str(n1)
    conv = conversao_str[::-1]
    if len(conversao_str) < 5:
        print('Os números devem ser maiores que 5 dígitos')
        continue
    if conversao_str == conv:
        print("=" * 20)
        print('É um palíndromo')
        print("=" * 20)
    else:
        print('Não é um palindromo')
    pergunta = input('Deseja continuar ? (S/N)\n> ').strip().upper()
    if pergunta == "S":
        continue
    else:
        break