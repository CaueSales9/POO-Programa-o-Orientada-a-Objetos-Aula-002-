from ufc import Aluno


class UFC:

    def __init__(self, nome: str):
        self.nome = nome
        self.contas = []

    def cadastrar_conta(self):
        
        print("=== Bem vindo ao sistema da UFC! ===")
        print("=== Realize seu cadastro ===")
        
        #O usuário vai se cadastrar com nome de usuario e senha, o cpf é apenas para uma verificação
        cpf = input("Digite seu CPF:\n> ").strip()
        nome = input("Crie seu nome de usuário:\n> ").strip()
        senha = input("Crie sua senha:\n> ").strip()
        
        ver_campus = self.campus()
        print("\nCampus disponíveis:")
        for campus in ver_campus.keys():
            print(f"- {campus}")
    
        campusT = input('\nQual o seu campus:\n> ').strip().lower()
    
        #Verificação do campus
        if campusT not in ver_campus:
            print("\nCampus não encontrado! Use exatamente os nomes listados acima.\n")
            return
    
        #Mostra os cursos
        print(f"\nCursos disponíveis no {campusT}:")
        for curso in ver_campus[campusT]:
            print(f"- {curso}")
    
        cursoT = input('\nQual o seu curso:\n> ').strip().lower()
    
        #vai verificar se o curso existe no campus
        if cursoT not in ver_campus[campusT]:
            print("\nCurso não encontrado neste campus! Use exatamente os nomes listados acima.\n")
            return
        
        

        cpf_num = ''.join(filter(str.isdigit, cpf))

        #verifica se tem duplicação
        for aluno in self.contas:
            if aluno.cpf == cpf_num:
                print("\nCPF já cadastrado!\n")
                return
            if aluno.nome == nome:
                print("\nNome de usuário já existe!\n")
                return

        aluno = Aluno(nome, senha, cpf_num, campusT, cursoT)

        if not aluno.validar_cpf():
            print("\nCPF inválido!\n")
            return

        self.contas.append(aluno)
        print(f"\nConta criada com sucesso!\nUsuário: {aluno.nome}\nCampus: {campusT}\nCurso: {cursoT}")
        self.menu()
        
        
    def login(self):
        while True:
            nome = input('Digite seu nome de usuário:\n> ')
            senha = input('Digite sua senha:\n> ')
            
            for aluno in self.contas:
                if aluno.nome == nome and aluno.senha == senha:
                    print(f'\nLogin realizado com sucesso! Bem-vindo, {nome}!\n')
                    print('\n1- Ver meu curso\n2 - Trocar de curso\n3 - Trancar curso\n4 - Deletar conta\n5 - Sair')
                    try:
                        menu_login = int(input('O que deseja fazer:\n> '))
                        if menu_login == 1:
                            print(f'\nSeu campus: {aluno.campus}')
                            print(f'Seu curso: {aluno.curso}')
                            
                            
                        #Aqui eu reutilizei alguns comandos do cadastro
                        elif menu_login == 2:
                            ver_campus = self.campus()
                            print("\nCampus disponíveis:")
                            for campus in ver_campus.keys():
                                print(f"- {campus}")

                            campusT = input('\nQual o seu novo campus:\n> ').strip().lower()
    
                            if campusT not in ver_campus:
                                print("\nCampus não encontrado!\n")
                                continue
    
                            print(f"\nCursos disponíveis no {campusT}:")
                            for curso in ver_campus[campusT]:
                                print(f"- {curso}")
        
                            cursoT = input('\nQual o seu curso:\n> ').strip().lower()
    
                            if cursoT not in ver_campus[campusT]:
                                print("\nCurso não encontrado neste campus!\n")
                                continue
    
                            aluno.campus = campusT
                            aluno.curso = cursoT
    
                            print(f"\nCurso trocado com sucesso!")
                            print(f"Novo campus: {campusT}")
                            print(f"Novo curso: {cursoT}")
                            return
                        
                        
                        elif menu_login == 3:
                            confirmar = input('\nTem certeza que deseja trancar seu curso? (s/n):\n> ').strip().lower()
                            if confirmar == 's':
                                aluno.curso = "Curso trancado"
                                print('\nCurso trancado com sucesso!\n')
                            else:
                                print('\nOperação cancelada\n')
                        
                        elif menu_login == 4:
                            confirmar = input('\nTem certeza que deseja deletar sua conta? (s/n):\n> ').strip().lower()
                            if confirmar == 's':
                                self.contas.remove(aluno)
                                print('\nConta deletada com sucesso!\n')
                                return
                            else:
                                print('\nOperação cancelada\n')
                                
                                
                        elif menu_login == 5:
                            self.menu()
                            
                            
                        
                    except ValueError:
                        print('Valor inválido')
                        return
                    
                    
                    
                else:
                    print('\nUsuário ou senha incorreta!\n')
                    break
            
            
            
            
    def campus(self):
            
        return {
        "campus itapaje": ["ads", "ciencia de dados", "seguranca da informacao"],
        
        "campus russas": ["engenharia de software", "ciencia da computacao", 
                         "engenharia civil", "engenharia de producao", "engenharia mecanica"],
        
        "campus quixada": ["design digital", "engenharia de computacao", "redes de computadores",
                          "sistema de informacao", "ciencia da Computacao"],
        
        "campus sobral": ["ciencias economicas", "engenharia eletrica", "financas", "medicina",
                         "musica", "odontologia", "psicologia"]
    }
            
        
        
    def menu(self):
        while True:
            print('=== Bem vindo ao menu da UFC ===')
            print('\n1 - cadastrar conta\n2 - Login\n3 - ver cursos \n')
            try:
                escolha = int(input('O que deseja fazer:\n> '))
                if escolha == 1:
                    self.cadastrar_conta()
                
                elif escolha == 2:
                    self.login()
                    
                elif escolha == 3:
                    
                    #AQui vai listar todos os campus e entrando em um vai mostrar os cursos
                    print(f'1 - UFC Itapajé\n2 - UFC Russas\n3 - UFC Quixadá\n4 - UFC Sobral')
                    cursos = int(input('Qual Campus deseja ver:\n> '))
                    campus_dat = self.campus()
                    
                    if cursos == 1:
                        print(f'\nCursos do campus itapaje:')
                        for curso in campus_dat["campus itapaje"]:
                            print(f'  - {curso}\n')
                            
                    elif cursos == 2:
                        print(f'\nCursos do campus russas:')
                        for curso in campus_dat["campus russas"]:
                            print(f'  - {curso}\n')
                            
                    elif cursos == 3:
                        print(f'\nCursos do campus quixada:')
                        for curso in campus_dat["campus quixada"]:
                            print(f'  - {curso}\n')
                            
                            
                    elif cursos == 4:
                        print(f'\nCursos do campus sobral:')
                        for curso in campus_dat["campus sobral"]:
                            print(f'  - {curso}\n')
                        
                    else:
                        print('\nEscolha inválida')
                        


            except ValueError:
                print('\nOpção incorreta\n')
                continue
            
teste = UFC("Sistema")
teste.menu()