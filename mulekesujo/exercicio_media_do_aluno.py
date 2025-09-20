nota1 = float(input("Coloque a nota 1 do aluno: "))
nota2 = float(input("Coloque a nota 2 do aluno: "))
media = (nota1 + nota2) / 2

print(f"Nota da média: {media:.1f}")
if media == 10:
    print("Aprovado com Distinção")

elif 7 >= media:
    print("Reprovado")

elif media > 10:
    print("Aprovado com Distinção")

elif media >= 7:
    print("Aprovado")

else:
    print("erro")