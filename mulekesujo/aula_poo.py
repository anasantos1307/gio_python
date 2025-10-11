"""Aula 11/10/2025"""

"""
Programação Orientada a Objeto

Definição: é um paradigma de programalçao onde o objetio central do desenvolvimento são as entidades da aplicação,
por exemplo se estamos trabalhando com um sistema de banco as entidades seriam, Cliente, Gerente, etc.

Sintaxe:
class NomeClass:
    atributos
    métodos
    
Padrões:
- Nomes das classes são em PascalCase

Conceitos importantes:
- Classe
- Instância
- Atributos
- Métodos
- Herança
- Polimorfismo
- Encapsulamento
"""

class ClienteBanco:
    # Listagem: tipagem dos atributos
    nome: str
    n_conta: str
    saldo: float

    # Construtor
    def __init__(self, nome: str, conta: str, saldo: float):
        self.nome = nome
        self.conta = conta
        self.saldo = saldo

    def consultar_saldo(self) -> None:
        print(f"{self.nome}, seu saldo é: R$ {self.saldo:,.2f}")

    def depositar(self, valor: float) -> None:
        self.saldo += valor

    def sacar(self, valor: float) -> None:
        if valor > self.saldo:
            print("Saldo insuficiente")
        self.saldo -= valor

    # Representação
    def __repr__(self):
        return f"Cliente=(Nome: {self.nome!r}, Conta: {self.conta!r}, Saldo: {self.saldo:.2f})"

class ClientePrata(ClienteBanco):

    pontos: float

    def __init__(self,  nome: str, conta: str, saldo: float):
        super().__init__(nome, conta, saldo)
        self.pontos = saldo // 5

    def pegar_emprestimo(self, valor: float) -> None:
        if self.saldo > 0:
            self.saldo += valor
        else:
            print("Recusado")

"""
Implemetar uma classe CLienteOuro
* Mudança livre
"""
class ClienteOuro(ClientePrata):

    def __init__(self,  nome: str, conta: str, saldo: float):
        super().__init__(nome, conta, saldo)

    def ir_investir(self, investir2: float) :
        if self.saldo >= 0:
            self.saldo -= investir2
            investimento = investir2 * 0.05
            print(f"Você investiu R${investir2} e o retorno será de R${investimento:,.2f}")
            self.saldo += investimento + investir2
            print(f"Seu saldo após o investimento é de: R${self.saldo}")
        else:
            print("Recusou")




joao = ClienteBanco("João", "1", 2000.0)
print(joao)
joao.consultar_saldo()
joao.depositar(1000)
joao.sacar(500)
joao.consultar_saldo()

ana = ClienteBanco("Ana", "2", 2500)
print(ana)
ana.consultar_saldo()
ana.depositar(1250)
ana.sacar(250)
ana.consultar_saldo()

maria = ClientePrata( "Maria", "3", 10000)
maria.pegar_emprestimo(1000)
maria.consultar_saldo()

gustavo = ClienteOuro( "Gustavo", "4", 5000)
gustavo.ir_investir(100)
gustavo.consultar_saldo()