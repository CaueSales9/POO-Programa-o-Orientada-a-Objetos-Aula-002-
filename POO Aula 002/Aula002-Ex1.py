import math
import random


#calculo para saber se é um triangulo e qual o seu tipo
def formar_com_coor():
    x1 = int(input("Digite o valor de X1\n> "))
    y1 = int(input("Digite o valor de Y1\n> "))
    x2 = int(input("Digite o valor de X2\n> "))
    y2 = int(input("Digite o valor de Y2\n> "))
    x3 = int(input("Digite o valor de X3\n> "))
    y3 = int(input("Digite o valor de Y3\n> "))

    calculo_1 = int(math.sqrt((x2-x1)**2 + (y2-y1)**2))
    calculo_2 = int(math.sqrt((x3-x2)**2 + (y3-y2)**2))
    calculo_3 = int(math.sqrt((x1-x3)**2 + (y1-y3)**2))

    #Verificação
    if (calculo_1 + calculo_2 > calculo_3 and calculo_2 + calculo_3 > calculo_1 and calculo_1 + calculo_3 > calculo_2):
        print('Isso forma um triangulo')
        if calculo_1 == calculo_2 == calculo_3:
            print('Equilatero')
        elif calculo_1 == calculo_2 or calculo_1 == calculo_3 or calculo_2 == calculo_3:
            print('isóceles')
        else:
            print('Escaleno')
    
    else:
        print('isso não forma um triangulo')
        
    escolha = input('Deseja continuar ? (S/N)\n> ').strip().upper()
    if escolha == "S":
        formar_com_coor()
    else:
        Menu()
        
#Escolha aleatoria das coordenadas  
def obter_coor():
    
    escolha_triangulo = int(input('Qual triangulo deseja receber as coordenadas ?\n1 - Triangulo equilatero\n2 - Triangulo Isóceles\n3 - Escaleno\n> '))
    if escolha_triangulo == 1:
        exemplos_equi = [
            ((0, 0), (2, 0), (1, 2)),
            ((2, 2), (6, 2), (4, 6))
        ]
        
        resul_equi = random.choice(exemplos_equi)
        print(resul_equi)
    
    elif escolha_triangulo == 2:
        exemplos_iso = [
            ((0, 0), (4, 0), (2, 3)),
            ((1, 1), (5, 1), (3, 4)),
            ((0, 0), (6, 0), (3, 5))
        ]
    
        resul_iso = random.choice(exemplos_iso)
        print(resul_iso)
        
    elif escolha_triangulo == 3:
        exemplos_esca = [
            ((0, 0), (5, 0), (2, 3)),
            ((1, 2), (4, 5), (7, 3)),
            ((2, 2), (6, 5), (5, 1))
        ]
        
        resul_esca = random.choice(exemplos_esca)
        print(resul_esca)
        
    retorno = input('Deseja retornar ? (S/N)\n> ').strip().upper()
    if retorno == "S":
        obter_coor()
    else:
        Menu()
        
        
def quadrado():
        x1 = int(input("Digite o valor de X1\n> "))
        y1 = int(input("Digite o valor de Y1\n> "))
        x2 = int(input("Digite o valor de X2\n> "))
        y2 = int(input("Digite o valor de Y2\n> "))
        x3 = int(input("Digite o valor de X3\n> "))
        y3 = int(input("Digite o valor de Y3\n> "))
        x4 = int(input("Digite o valor de X4\n> "))
        y4 = int(input("Digite o valor de Y4\n> "))
        
        #lado dos quadrados
        calculo_1 = (x2-x1)**2 + (y2-y1)**2
        calculo_2 = (x3-x2)**2 + (y3-y2)**2
        calculo_3 = (x4-x3)**2 + (y4-y3)**2
        calculo_4 = (x1-x4)**2 + (y1-y4)**2
        
        #diagonais do quadrado
        calculo_5 = (x3-x1)**2 + (y3-y1)**2
        calculo_6 = (x4-x2)**2 + (y4-y2)**2
        
        #Verificação
        if (calculo_1 == calculo_2 == calculo_3 == calculo_4 and calculo_5 == calculo_6):
            print('Quadrado')
        elif calculo_1 == calculo_3 and calculo_2 == calculo_4 and calculo_5 == calculo_6:
            print('Retangulo')
        else:
            print('Quadrilatero qualquer')
        retorno = input('Deseja retornar ? (S/N)\n> ').strip().upper()
        if retorno == "S":
            quadrado()
        else:
            Menu()
    
#menu
def Menu():
    print('='*70)
    print('Olá, o que deseja fazer ?\n1 - Informar coordenadas para formar um triangulo\n2 - Escolher um triangulo e obter suas coordenadas\n3 - Identificar o tipo de geometria a partir de 4 coordenadas')
    print('='*70)
    escolha = int(input('Qual sua escolha ?\n> '))
    
    if escolha == 1:
        formar_com_coor()
    elif escolha == 2:
        obter_coor()
    elif escolha == 3:
        quadrado()
    else:
        Menu()
        
        
        
Menu()