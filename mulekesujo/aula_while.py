"""
While:
"""

# i = 0
#
# while i < 11:
#     print(i)
#     i += 1
# else:
#     print("Fim da copetição")
""""""
# n = int(input("Número: "))
#
# while n <= 50:
#     if n == 50:
#         print(f"{n} é igual a 50")
#
#     else:
#         print(f"{n} é menor que 50")
#     n = int(input("Número: "))
# print(f"{n} é maior que 50")

# EXEMPLO DE LOGIN

# username = input("Usuário: ")
# senha = input("Senha: ")
#
#
# if username != "admin" and senha != "senha123":
#     print("Usuário e Senha errados")
#     while username = ("Usuário: "):
#
#     senha = input("Senha: ")
#
# elif username != "admin" and senha == "senha123":
#     print("Usuário errado!")
#     username = input("Usuário: ")
#     senha = input("Senha: ")
#
# elif username == "admin" and senha != "senha123":
#     print("Senha errado!")
#     username = input("Usuário: ")
#     senha = input("Senha: ")
#
# else:
#     print(f"Bem-vindo {username}")


"""
continue: retorna até a verificação da condição do while
break: parar o while
"""

import time

tentativa = 0


while True:
    if tentativa < 3:
        user = input("Usuário: ")
        if user == "admin":
            senha = input("Senha: ")
            if senha == "senha123":
                print("Bem-vindo(a)!")
                break
            else:
                print("Senha errada!")
                tentativa += 1
        else:
            print("Usuario errado")
            tentativa += 1
            continue
    else:
        print("Tentativas excedidas!")
        for i in range(10, 0, -1):
            print("\r", end=f"Espere {i} segundos.")
            time.sleep(1)
        print()
        tentativa = 0
        continue