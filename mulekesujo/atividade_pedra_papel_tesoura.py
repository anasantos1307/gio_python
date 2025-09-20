import random
import time

while True:
    print("Jogo: Pedra, Papel e Tesoura!")
    print("Qual você escolhe? Coloque (sair) para sair.")
    escolha = input()
    ia = random.choice("pedra papel tesoura".split())
    if escolha == ia:
        print("Empate!")
        for i in range(3, 1, -1):
            time.sleep(1)
        print("Você quer continuar ou sair?")
        while True:
            pesado = input()
            if pesado == "continuar":
                break
            elif pesado == "sair":
                print("Você saiu!")
                break
            else:
                print("Coloque novamente")
                continue
    elif escolha == "pedra" and ia == "papel":
        print("Você perdeu!")
        for i in range(2, 1, -1):
            time.sleep(1)
        print("Você quer continuar ou sair?")
        while True:
            pesado = input()
            if pesado == "continuar":
                break
            elif pesado == "sair":
                print("Você saiu!")
                break
            else:
                print("Coloque novamente")
                continue
    elif escolha == "papel" and ia == "tesoura":
        print("Você perdeu!")
        for i in range(2, 1, -1):
            time.sleep(1)
        print("Você quer continuar ou sair?")
        while True:
            pesado = input()
            if pesado == "continuar":
                break
            elif pesado == "sair":
                print("Você saiu!")
                break
            else:
                print("Coloque novamente")
                continue
    elif escolha == "pedra" and ia == "tesoura":
        print("Você ganhou!")
        for i in range(2, 1, -1):
            time.sleep(1)
        print("Você quer continuar ou sair?")
        while True:
            pesado = input()
            if pesado == "continuar":
                break
            elif pesado == "sair":
                print("Você saiu!")
                break
            else:
                print("Coloque novamente")
                continue
    elif escolha == "papel" and ia == "pedra":
        print("Você ganhou!")
        for i in range(2, 1, -1):
            time.sleep(1)
        print("Você quer continuar ou sair?")
        while True:
            pesado = input()
            if pesado == "continuar":
                break
            elif pesado == "sair":
                print("Você saiu!")
                break
            else:
                print("Coloque novamente")
                continue
    elif escolha == "tesoura" and ia == "papel":
        print("Você ganhou!")
        for i in range(2, 1, -1):
            time.sleep(1)
        print("Você quer continuar ou sair?")
        while True:
            pesado = input()
            if pesado == "continuar":
                break
            elif pesado == "sair":
                print("Você saiu!")
                break
            else:
                print("Coloque novamente")
                continue
    elif escolha == "tesoura" and ia == "pedra":
        print("Você perdeu!")
        for i in range(2, 1, -1):
            time.sleep(1)
        print("Você quer continuar ou sair?")
        while True:
            pesado = input()
            if pesado == "continuar":
                break
            elif pesado == "sair":
                print("Você saiu!")
                break
            else:
                print("Coloque novamente")
                continue
    elif escolha == "sair":
        break
    else:
        print("Erro. Coloque novamente a sua escolha!")
        for i in range(2, 1, -1):
            time.sleep(1)
        continue
