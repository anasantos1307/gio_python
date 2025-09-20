from errno import errorcode
from os import waitstatus_to_exitcode
from timeit import repeat

nome_do_cliente = input("Informe seu Nome Completo:").title()
idade_do_cliente = int(input("Informe sua Idade:"))
cidade_do_cliente = input("Informe sua Cidade:").title()
estado_do_cliente = input("Informe seu Estado:").upper()

print(f"Nome: {nome_do_cliente}")
print(f"Idade: {idade_do_cliente}")
print(f"Cidade: {cidade_do_cliente}")
print(f"Estado: {estado_do_cliente}")
