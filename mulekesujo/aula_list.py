""" 20/09/2025 """

"""
Listas: Uma coleção Python

Características:
- Representação: [item1, item2, ..., itemN]
- São mutáveis;
- Podem ser heterogêneas;
- Listas são interaveis com as outras;
- Listas NÃO são arrayas;
- São indexadas em zero (assim como as trings);
"""

# minha_lista = [1, 2, 3, 4, 5]
# print(minha_lista)
# print(type(minha_lista))
#
# lista_2 = [10, 3.14, "oi", True, [1, 2, 3]]
# print(lista_2)
#
# matriz = [[1, 2, 3],
#           [4, 5, 6]]
#
# for i in lista_2:
#     print(i)

numeros = list(range(51))
print(numeros)

# Índice

# print(numeros(0))
# print(numeros(27))
# print(numeros(10))
# print(numeros(-1))
# print(numeros(54))

# Slicing
print(numeros[0:12])
print(numeros[12:40])
print(numeros[:25])
print(numeros[25:])
print(numeros[::5])
print(numeros[::-5])

# funções
# # Listas no geral
# print(len(numeros))
#
# # Listas numéricos
# print(sum(numeros))
# print(max(numeros))
# print(min(numeros))

frutas = ["laranja", "maça", "banana", "melancia", "uva"]

print("Nossa lista tem", len(frutas))

# Adicionando itens a uma lista

frutas.append("banana")
print(frutas)

# for i in range(3):
#     fruta = input("Fruta: ")
#     print(frutas)

frutas.extend(["morango", "limão"])
print(frutas)

frutas.insert(1, "maracuja")
print(frutas)

# Remover itens de um lista

ultimo_fruta = frutas. pop()
print(ultimo_fruta)
print(frutas)

frutas.remove("morango")
print(frutas)

del frutas[3]
print(frutas)

# Editar
frutas[0] = "pitaya"
print(frutas)

# Encontrando a posição de um lista

print("Melancia está na posição", frutas.index("melância"))
frutas[frutas.index("melancia")] = "carambola"
print(frutas)

# Contando quantas vezes um dado elemento aparece na lista
print(f"Caramba aparece {frutas.count("carambola")} na nossa lista")

# Método ordenar uma lista:
frutas.sort()
print(frutas)