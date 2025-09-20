# ATIVIDADE 1
# for i in range(1, 51, +2):
#     print(i)

# ATIVIDADE 2

# n = int(input("Coloque o número da tabuada que você quer: "))
#
#
# for i in range (1, 11):
#     print(f"{n} x {i} = {i * n}")

# ATIVIDADE 3

print()
n_de_compras = int(input("Quantas compras você fez: "))
total = 0

for n in range(n_de_compras):
    valor_da_compra = float(input(f"Valor da {n + 1}ª compra: R$ "))
    total = total + valor_da_compra

print(f"Você comprou {n_de_compras} produtos e gastou R$ {total:,.2f}")