class conta:
    def __init__(self, numero, valorINI=0):
        self.numero = numero
        self.saldo = valorINI
        
        
    def get_numero(self):
        return self.numero
    
    def get_saldo(self):
        return self.saldo
    
    def debitar(self, valor_INI):
        if valor_INI > 0 and valor_INI <= self.saldo:
            self.saldo -= valor_INI
            return True
        else:
            print("Valor inválido para débito ou saldo insuficiente")
            return False
    
    def creditar(self, valor_INI):
        if valor_INI > 0:
            self.saldo += valor_INI
            return True
        else:
            print("Valor inválido para crédito")
            return False


class Banco:
    def __init__(self):
        self.contas = [None] * 100
        self.indice = 0
        
        
        
    def cadastrar(self, conta):
        self.contas[self.indice] = conta
        self.indice += 1
        
        
    def procurar_conta(self, numero):
        i = 0
        achou = False
        while achou is False and i < self.indice:
            if self.contas[i].get_numero() == numero:
                achou = True
            else:
                i += 1
        if achou is True:
            return self.contas[i]
        else:
            return None
        
        
        
    def debitar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.debitar(valor)
        else:
            print("Conta Inexistente!") 
            
            
            
    def creditar(self, numero, valor): #Modifiquei algumas coisas do debitar
        conta = self.procurar_conta(numero)
        if conta:
            conta.creditar(valor)
        else:
            print("Conta Inexistente!") 
        
        
    def saldo(self, numero):
        conta = self.procurar_conta(numero)
        if conta:
            return conta.get_saldo()
        else:
            print('Conta inexistente')
        

        
    def transferir(self, origem, destino, valor):
        contaORI = self.procurar_conta(origem) #Aqui vai fazer uma verificaçao para ver se a origem e o destino existem
        contaDES = self.procurar_conta(destino) #verificação
        
        if contaDES is None or contaORI is None: #verificação
            print('Destino ou Origem inválidos') #verificação
            
        saldo_atual = contaORI.get_saldo() #Criei uma variável para armazenar o saldo e facilitar a transferência
        
        if valor > saldo_atual or valor <= 0: #verificação do valor
            return 'Valor Inválido'
            
        else:
            contaORI.debitar(valor)
            contaDES.creditar(valor)
            
        print(f'Transferência de R$ {valor:.2f} realizada com sucesso!')
        print(f'De: {origem} | Para: {destino}')
        

#Pedi ao chat para testar
banco = Banco()
    
    # Criando e cadastrando contas
conta1 = conta(1001, 1000.00)  # Conta 1001 com R$ 1000,00
conta2 = conta(1002, 500.00)   # Conta 1002 com R$ 500,00
conta3 = conta(1003, 200.00)   # Conta 1003 com R$ 200,00
    
banco.cadastrar(conta1)
banco.cadastrar(conta2)
banco.cadastrar(conta3)
    
print("=== SISTEMA BANCÁRIO INICIADO ===")
print(f"Contas cadastradas: {banco.indice}")
print()
    
    # Testando saldos
print("Saldos iniciais:")
print(f"Conta 1001: R$ {banco.saldo(1001):.2f}")
print(f"Conta 1002: R$ {banco.saldo(1002):.2f}")
print(f"Conta 1003: R$ {banco.saldo(1003):.2f}")
print()
    
    # Testando crédito
print("Realizando crédito na conta 1001:")
banco.creditar(1001, 300.00)
print()
    
    # Testando débito
print("Realizando débito na conta 1002:")
banco.debitar(1002, 100.00)
print()
    
    # Testando transferência
print("Realizando transferência:")
banco.transferir(1001, 1003, 250.00)
print()
    
    # Verificando saldos finais
print("Saldos finais:")
print(f"Conta 1001: R$ {banco.saldo(1001):.2f}")
print(f"Conta 1002: R$ {banco.saldo(1002):.2f}")
print(f"Conta 1003: R$ {banco.saldo(1003):.2f}")
print()