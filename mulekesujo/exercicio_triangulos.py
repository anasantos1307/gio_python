lado1 = int(input("Coloque o número do lado 1: "))
lado2 = int(input("Coloque o número do lado 2: "))
lado3 = int(input("Coloque o número do lado 3: "))

if lado1 + lado2 > lado3 and lado3 + lado2 > lado1 and lado1 + lado3 > lado2:
    print("É possivel fazer um triangulo com esses valores!")
    if lado1 == lado2 and lado3 == lado2 and lado3 == lado1:
        print("Esse é um triangulo equilatero")

    elif lado3 == lado2 or lado1 == lado3 or lado2 == lado1:
        print("Esse é um triangulo isósceles")

    elif lado3 != lado2 and lado1 != lado2 and lado3 != lado1:
        print("Esse é um triangulo escaleno")
    else:
        print("Não foi possivel forma o triangulo!")
else:
    print("Não foi possivel verificar os valores desse triangulo!")