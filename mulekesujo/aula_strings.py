import string
from importlib.resources import contents
from math import pi

codigo_produto = "#12"
quantidade_produto = 200
preco_produto = 3.5

print(codigo_produto, quantidade_produto, preco_produto)

# Código: #12, Quatidade: 200, Preço: R$ 3.50

"""
Concatenação de strings:
- Como se fosse uma 'soma' de strings:

    str + str = strstr
"""

nome = "Thiago"
sobrenome = "Lima"

nome_completo =  nome + " " + sobrenome
print(nome_completo)

# Exemplo prático

codigo_produto = "#12"
quantidade_produto = 200
preco_produto = 3.50

print(codigo_produto, quantidade_produto, preco_produto)

# Código: #12, Quantidade: 200, Preço: R$3.50

print("Código: " + codigo_produto + ", Quantidade: " + str(quantidade_produto) + ", Preço: R$" + str(preco_produto))

"""
f-string:
Nos permite compor strings com variaveis sem sair da string
    f"Texto {variavel}."
"""


nome = "Thiago"
sobrenome = "Lima"
nome_completo = f"{nome} {sobrenome}"
print(nome_completo)

# Código: #12, Quantidade: 200, Preço: R$3.50

codigo_produto = "#12"
quantidade_produto = 200
preco_produto = 3.50

print()
print(f"Código: {codigo_produto}, Quantidade: {quantidade_produto}"
      f", Preço: R$ {preco_produto:.2f}")

# Forma antiga (.format())
print("Código: {}, Quantidade: {}, Preço: R$ {}".format(codigo_produto, quantidade_produto, preco_produto))

"""
Formatadores:
- Casas decimais: .nf
- Separador de milhares: ,
- Porcentagem: %
"""

print()
print(f"{pi:.5f}")

# - Separador de milhares: ,
n_habitantes_sp = 810729
print(f"{n_habitantes_sp:,}")
dinheiro_meu = 1000.50
print(f"{dinheiro_meu:,.2f}")

# - Porcentagem: %
print()
valor_compra = 100
desconto = .0003
valor_final = valor_compra * (1 - desconto)
print(f"Valor compra: R$ {valor_compra:,.2f}")
print(f"Desconto: R${desconto:.2%}")
print(f"Valor com desconto: R$ {valor_final:,.2f}")

# Strings

# Métodos úteis

# Formatação

texto = "pRoGrAmAçÃo Em EM Em Em PyThOn"

print(texto.upper())
print(texto.lower())
print(texto.title())
print(texto.capitalize())
print(texto.replace("Em", "Com"))

# Exemplo 1
# nome = input("Nome: ")
# ultimo_nome = input("Ultimo nome")
#
# email = nome + "." + ultimo_nome + "@gmail.cu"
# print(email)

# Exemplo 2
# nome = input("Nome e Ultimo Nome:")
# email = nome.lower().replace(" ", ".") + "@gmail.cu"
# print(email)

# Validação

import string

print("Todas as letras", string.ascii_letters)
print("Todos os digitos", string.digits)
print("Todas as pontuações", string.punctuation)

print()
print("João".isalpha()) #Indentifica so letra
print("1199999999".isdigit()) #Indentifica so numero
print("LED200".isalnum()) #Indentifica se tem so numero, so letras ou so letra e numero

# Separando Strings
nome_completo1 = "Gio Gaspar"
print(nome_completo.split())

# Funções
print("Quantos char tem a palavra paralelepipedo?", len("paralelepipedo"))


"""
Strings com interáveis:

- O que é um iterável: é tudo valor o qual eu posso 'percorrer' 
"""

# Indexadas em 0

texto = "Programação em Python"
print("O que está na posição zero da variável texto:", texto[0])

# Índice
print(texto[0])
print(texto[1])
print(texto[2])
print(texto[3])
print(texto[4])
print(texto[5])
print(texto[6])
print(texto[7])

# Slicing
print(texto[0:6])
print(texto[10:11])
print(texto[:6])
print(texto[::10])
print(texto[::-1])