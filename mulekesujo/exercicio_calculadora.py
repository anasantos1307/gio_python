digito1 = float(input("Digite o primeiro número: "))
digito2 = float(input("Digite o segundo número: "))

print("Digite 1 para + (mais)")
print("Digite 2 para - (menos)")
print("Digite 3 para * (multiplicação)")
print("Digite 4 para / (divisão)")
print("Digite 5 para ** (exponenciação)")

formula = int(input("Digite o sinal: "))
match formula:
    case 1: print(f"Valor somado = {digito1 + digito2:.2f}" )
    case 2: print(f"Valor subtraido = {digito1 - digito2:.2f}" )
    case 3: print(f"Valor multiplicado = {digito1 * digito2:.2f}" )
    case 4: print(f"Valor dividido = {digito1 / digito2:.2f}" )
    case 5: print(f"Valor ao expoente = {digito1 ** digito2:.2f}" )
    case _: print("Digite o sinal correto!.")

