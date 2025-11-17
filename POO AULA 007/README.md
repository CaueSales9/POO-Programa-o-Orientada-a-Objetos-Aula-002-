Sistema UFC - Gerenciamento de Alunos
Este projeto implementa um sistema de gerenciamento de alunos para a UFC (Universidade Federal do Ceará), permitindo cadastro, login, visualização de cursos e outras funcionalidades relacionadas.

Estrutura do Projeto
text
projeto-ufc/
├── main.py              # Arquivo principal com a classe UFC e menu
├── ufc.py               # Módulo com a classe Aluno
├── README.md            # Este arquivo
└── requirements.txt     # Dependências do projeto (se houver)
Funcionalidades
Cadastro de conta: Permite criar uma conta de aluno com CPF, nome de usuário, senha, campus e curso

Login: Autenticação de usuário com nome e senha

Visualização de cursos: Lista todos os cursos disponíveis por campus

Gerenciamento de conta:

Ver informações do curso atual

Trocar de curso/campus

Trancar curso

Deletar conta

Pré-requisitos
Python 3.6 ou superior

Módulo ufc (deve estar no mesmo diretório ou no PYTHONPATH)

Como Executar
Clone ou baixe o projeto para sua máquina local

Certifique-se de que todos os arquivos estão no mesmo diretório:

main.py (o código fornecido)

ufc.py (contendo a classe Aluno)

Execute o programa:

bash
python main.py
Siga as instruções no terminal:

Digite 1 para cadastrar uma nova conta

Digite 2 para fazer login (se já tiver uma conta)

Digite 3 para visualizar os cursos disponíveis por campus

Estrutura de Código
Classe UFC
__init__: Inicializa o sistema com nome e lista de contas

cadastrar_conta: Realiza o cadastro de novos alunos

login: Autentica usuários e fornece menu de opções

campus: Retorna dicionário com campus e cursos disponíveis

menu: Menu principal do sistema

Fluxo do Programa
O sistema inicia criando uma instância da classe UFC

O menu principal é exibido com 3 opções:

Cadastrar conta

Login

Ver cursos

Dependendo da escolha, o usuário é direcionado para a funcionalidade correspondente

Observações Importantes
O CPF é validado (necessita implementação da validação na classe Aluno)

Não é permitido cadastro com CPF ou nome de usuário duplicados

Os campus e cursos disponíveis estão pré-definidos no código

O sistema mantém os dados apenas em memória (não persiste entre execuções)

Possíveis Melhorias Futuras
Implementar persistência de dados (banco de dados ou arquivos)

Adicionar mais validações nos campos de entrada

Implementar interface gráfica

Adicionar funcionalidades para administradores

Expandir a lista de campus e cursos

Tratamento de Erros
O sistema inclui tratamento básico de erros para:

Entradas numéricas inválidas

Campus ou cursos não encontrados

Tentativas de login com credenciais incorretas
