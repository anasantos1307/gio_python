import time

print("Bem-vindo ao saltos dos atletas")
for i in range(3, 1, -1):
    time.sleep(1)
print("Aqui você coloca as distâncias do seu atleta!")
for i in range(3, 1, -1):
    time.sleep(1)
while True:
    print("Coloque o nome do seu atleta:")
    atleta = input("")
    if atleta == "":
        print("Você saiu!")
        break
    while True:
        salto1 = float(input("Coloque a distância do primeiro salto dele: "))
        if salto1 <= 0 or salto1 == "":
            print("Valor inválido! Coloque novamente.")
            for i in range(2, 1, -1):
                time.sleep(1)
            continue
        else:
            break
    while True:
        salto2 = float(input("Coloque a distância do segundo salto dele: "))
        if salto2 <= 0 or salto2 == "":
            print("Valor inválido! Coloque novamente.")
            for i in range(2, 1, -1):
                time.sleep(1)
            continue
        else:
            break
    while True:
        salto3 = float(input("Coloque a distância do terceiro salto dele: "))
        if salto3 <= 0 or salto3 == "":
            print("Valor inválido! Coloque novamente.")
            for i in range(2, 1, -1):
                time.sleep(1)
            continue
        else:
            break
    while True:
        salto4 = float(input("Coloque a distância do quatro salto dele: "))
        if salto4 <= 0 or salto4 == "":
            print("Valor inválido! Coloque novamente.")
            for i in range(2, 1, -1):
                time.sleep(1)
            continue
        else:
            break
    while True:
        salto5 = float(input("Coloque a distância do quinto salto dele: "))
        if salto5 <= 0 or salto5 == "":
            print("Valor inválido! Coloque novamente.")
            for i in range(2, 1, -1):
                time.sleep(1)
            continue
        else:
            break
