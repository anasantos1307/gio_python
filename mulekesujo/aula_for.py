""""""

"""
Em python 2 tipos de loopings:

- for: criar estruturas de repetição contadas;
- while:  criar estruturas de repetição condicionais;

Utilização: sempre que eu precisar repetir uma estrutura de código
Danese o numero de vezes. A quantida de loops pode ser baseada em: ranges, string. listas, etc

Sintaxe:

for i in iterável:
    bloco do for
"""

# numeros = [1, 2, 3, 4, 5]
#
# for i in numeros:
#     print(i)

# a = 1
# numeross = [a, 2, 3, 5]
#
# for numero in numeross:
#     print(numero)

# numeros = [1, 2]
# for _ in numeros:
#     nome = input("Nome: ")
#     print(f"Bem-vindo(a) {nome}!")
#
# for letra in "Olá mundo!":
#     print(letra.lower())

"""
Range()

1° Forma: range(stop)

[ 0 , 10 [
"""

# sequancia = range(10)
# print(sequancia)
# print(*sequancia)
#
# for i in range(10):
#     print(i)

# for n in range(5):
#     nome = input("Nome: ")
#     n1 = float(input("Nota 1: "))
#     n2 = float(input("Nota 2: "))
#     media = (n1 + n2) / 2
#     print(f"{nome}, sua média é {media:.2f}")
#
#     if media == 10:
#         print("A+")
#     elif media < 9.9 and media >= 7:
#         print("B")
#     elif media < 7:
#         print("F")

"""
2° Forma: range(star, stop)
"""

# for i in range(5, 11):
#     print(f"O quadrado de {i} é {i ** 2}")
#
# idade = int(input("Idade: "))
#
# if idade in range(14, 25):
#     print("Pode fazer o CAI")
# elif idade in range(0, 13):
#     print("Você não pode fazer nenhum ainda!")
#     input()
# else:
#     print("Faça um técnico.")

"""
3° Forma: range(star., stop, step)
"""

# for n in range(0, 110, 10):
#     print(n)

"""
Exemplo: cálculo de comissão para um vendedor de carros
"""
print()
n_carros = int(input("Quantos carros você vendeu no mês de Agosto: "))
total = 0

for n in range(n_carros):
    valor_da_venda = float(input(f"Valor da {n + 1} venda: R$ "))
    total = total + valor_da_venda

comissao = total * .07

print(f"Você vendeu {n_carros} carros e a empresa ganhou R$ {total:,.2f}.")
print(f"Sua comissão foi de R$ {comissao:.2f}")