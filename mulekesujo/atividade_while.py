saldo = 1000
while True:
    print("Você quer depositar, sacar ou sair?")
    acao = input()

    if acao == "depositar":
        print("Você quer depositar quantos R$?")
        deposito = float(input("R$ "))
        if deposito < 0:
            print("Você não pode depositar números negativos!")
        else:
            saldo += deposito
            print(f"Você depositou {deposito}")
            print(f"Agora você tem {saldo}")
            continue
    elif acao == "sacar":
        print("Você quer sacar quantos R$?")
        saque = float(input("R$ "))
        if saque > saldo:
            print("Você não pode retirar esse valor")
            continue
        else:
            saldo -= saque
            print(f"Você sacou {saque}")
            print(f"Agora você tem {saldo}")
            continue
    elif acao == "sair":
        print("Você saiu!")
        break
    else:
        print("Coloque uma opção válida!")
        continue

