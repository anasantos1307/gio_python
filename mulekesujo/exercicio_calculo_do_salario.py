salario = float(input("Digite seu Sálario: "))

if salario <= 2000:
    print("Você não paga imposto!")

elif 5000 <= salario:
    print("Você pagará 20% do imposto")

elif 3500 <= salario <= 5000:
    print("Você pagará 15% do imposto")

elif 2000 <= salario <= 3500:
    print("Você pagará 10% do imposto")





else:
    print("erro")
