"""Aula dia 13/09/2025"""

"""
Operadores Lógicos
and ➡️ E
or  ➡️ OU
not ➡️ NEGAÇÃO

Prioridade:
1° ()
2° not
3° and
4° or

Utilização: Usaremosesses operadores sempre que precisarmos unir
duas ou mais comparações lógicas e/ou expressões lógicas mais completas
"""

# AND

print(False and False)
print(False and True)
print(True and False)
print(True and True)

# Exemplo:
# 1 x 1 x 1 x 1 x 1 x 1 x 1 x 0 = 0
print(True and True and True and True and True and True and False)

# Exemplo login

user = input("Seu nomezinho 😒: ")
password = input("Acesso negado?: ")

acesso = user == "admin" and password == "senha123"
print()
print(f"Usuário reconhecido: {user == "admin"}")
print(f"Usuário reconhecido: {password == "senha123"}")
print(f"Acesso liberado: {acesso}")

#  OR

print(False or False)
print(False or True)
print(True or False)
print(True or True)

# Exemplo:
# 0 + 0 + 0 + 0 + 0 + 0 + 1 = 1
print(False or False or False or False or False or True)

# Exemplo para reprovar alguem, seu burro!

media_final = 10
frequencia = .5

reprovar_burro = media_final > 5 or frequencia < .75


print()
print(f"Média Final: {media_final:.2f}")
print(f"Frequência: {frequencia:.2%}")
print(f"Aluno reprovado: {reprovar_burro}")

# NOT

print(not True)
print(not False)

print(not 10 > 2 and 10 % 5 != 0)
print(10 > 2 and 10 % 5 != 0)

# Exemplo Bomba de Água

C = True
B = True
A = True

situacao_1 = not A and not B and not C
situacao_2 = A and not B and not C
situacao_3 = A and B and not C

bomba = situacao_1 or situacao_2 or situacao_3
print(f"Bomba ligada:  {bomba}")
