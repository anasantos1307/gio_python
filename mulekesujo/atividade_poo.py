"""EXECICIO"""
"""
Criar uma classe carro que tenha:
Atributos:
- marca
- modelo
- ano
- cor

Métodos:
- __init__
- __repr__
- calcular-ipva() -> float
- avisar_troca_oleo(quilometragem) -> print() avisando se troca ou não óleo
"""

class Carro:
    marca: str
    modelo: str
    ano: int

    def __init__(self, marca: str, modelo: str, ano: int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def calcula_ipva(self, valor: float, ano_atual: int) -> float | None:
        ano_carro = ano_atual - self.ano
        if ano_carro > 20:
            print(f"O carro {self.modelo} tem {ano_carro} anos e está isento de IPVA.")
            return None
        else:
            ipva = valor * 0.04
            print(f"O IPVA do carro {self.modelo} é de R${ipva:,.2f}")
            return ipva

    def troca_oleo(self, quilometragem: float) -> None:
        if quilometragem >= 10000:
            print("O carro precisa de uma troca de óleo!")
        else:
            print("O carro não necessita ainda de um troca de óleo!")

    def __repr__(self):
        return f"Carro: (Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano})"

carro1 = Carro("Toyota", "Corolla", 2022)
carro2 = Carro("Chevrolet", "Opala", 1990)

print(carro1)
print(carro2)
print()

# Calcular IPVA
carro1.calcula_ipva(120000, 2025)
carro2.calcula_ipva(50000, 2025)
print()

# Verificar troca de óleo
carro1.troca_oleo(8000)
carro1.troca_oleo(12000)