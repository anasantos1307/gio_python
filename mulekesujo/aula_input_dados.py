"""
Input de Dados:

- Função input()
    input(argumento do tipo string)
"""

codigo_produto = input("Informe o código do produto: ")
quantidade_produto = int(input(f"Quantidade de {codigo_produto}: "))
preco_produto = float(input(f"Preço de {codigo_produto}: R$"))

# print()
# print(codigo_produto)
# print(quantidade_produto * 2, type(quantidade_produto))

print(f"Código: {codigo_produto}, Quantidade {quantidade_produto}, "
      f"Preço: R$ {preco_produto:.2f}")
valor_final = quantidade_produto * preco_produto
print(f"Valor Total da compra: R${valor_final:.2f}")