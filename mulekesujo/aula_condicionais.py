"""Aula dia 13/09/2025"""

"""
Condicionais em Python

- if (se)
- else (senão)
- elif (senão se)

Utilização: Usaremos condicionais semore que nosso código tiver um comportamento para cada situação

Exemplo:

Se o farol estiver 💚:
    avance!
Se não se o farol estiver 💛
    reduza!
Se nao se o farol estiver ❤️‍🔥
    pare!
Se não:
    observe a rua"""

# IF

"""
if condição:
    o que o if faz
"""

# codigo_produto = "#123"
# quantidade_produto = 500
# preco_produto = 4.5
#
# if quantidade_produto < 1000:
#     print("oi")
#     print("Quantidade abaixo do mínimo!")
#     print(f"Comprar {1000 - quantidade_produto} unidades de {codigo_produto}.")
#
# # Exemplo Farol
#
# farol = "verde"
#
# if farol == "verde":
#     print("Siga!")

# IF - ELSE

#

# ELIF

# Exemplo de estoque

# codigo_produto = "#123"
# quantidade_produto = 5000
# preco_produto = 4.5
#
# if 1000 > quantidade_produto >= 0:
#     print("Quantidade abaixo do mínimo!")
#     print(f"Comprar {1000 - quantidade_produto} unidades de {codigo_produto}.")
#
# elif 1000 <= quantidade_produto <= 2500:
#     print("Quantidade ok!")
#
# elif 2500 < quantidade_produto < 5000:
#     print("Quantidade acima do máximo!")
#     print(f"Vender {quantidade_produto - 2500} unidades de {codigo_produto}.")
#
# else:
#     print("Quantidade inválida!")

# Exemplo do farol
#
# farol = "verde"
#
# if farol == "verde": print("Siga!")
#
# elif farol == "amarelo": print("Reduza!")
#
# elif farol == "vermelho": print("Pare!")
#
# else: print("Observe o guarda de transito.")

# Exemplo de estoque

# codigo_produto = input("Código do Produto: ")
# quantidade_produto = int(input("Quantidade do Produto: "))
# preco_produto = 4.5
#
# if codigo_produto == "#123":
#     if quantidade_produto == "opa":
#
#         if 1000 > quantidade_produto >= 0:
#             print("Quantidade abaixo do mínimo!")
#             print(f"Comprar {1000 - quantidade_produto} unidades de {codigo_produto}.")
#
#         elif str():
#             print("Não coloque letras!")
#
#         elif 1000 <= quantidade_produto <= 2500:
#             print("Quantidade ok!")
#
#         elif 2500 < quantidade_produto < 5000:
#             print("Quantidade acima do máximo!")
#             print(f"Vender {quantidade_produto - 2500} unidades de {codigo_produto}.")
#
#         else:
#             print("Quantidade inválida!")
#     else:
#         print("Não coloque letras")
# else:
#     print("Código do produto errouuuu!")

# Match Case

dia_semana = int(input("Digite número do dia da senama, por exemplo 1 - Domingo"))

match dia_semana:

    case 1: print("Domingo")
    case 2: print("Segunda")
    case 3: print("Terça")
    case 4: print("Quarta")
    case 5: print("Quinta")
    case 6: print("Sexta")
    case 7: print("Sábado")
    case _: print("Dia Inválido")