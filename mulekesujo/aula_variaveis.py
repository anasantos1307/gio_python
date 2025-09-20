"""
Variáveis

nome_da_variavel = valor_da_variavel

Vantagens:
- Tornam o código dinâmico;
- Armazenam dados;
- Auxiliam no processamento de informações
"""

a = 10
print(a, id(a))
print(a + 2)
print(a + 3)
print(a + 4)
print(a + 5)

"""
Nomes de variáveis:

✅ Devem dizer exatamente o que aquele valor representa;
✅ Utilizar o '_'(snake_case) para nomear as variaveis
✅ Sempre usamos letras minúsculas (maiúsculas somente para Classes);

Regras:
❌ Não pode ter espaço ' ';
❌ Não pode começar com número;
❌ Não pode ter caracter especial (!@#$%¨&*(), etc)

Informação:
- Python é case sensitive;
"""

#✅ Devem dizer exatamente o que aquele valor representa;
#✅ Utilizar o '_'(snake_case) para nomear as variaveis
a = 27
idade_professor = 27

#❌ Não pode começar com número;
# 1codigo_produto = "#33"
codigo_produto1 = "#33"

#❌ Não pode ter caracter especial (!@#$%¨&*(), etc)
# *quantidade = 100

# - Python é case sensitive;
quantidade = 100
Quantidade = 200
print(quantidade, id(quantidade))
print(Quantidade, id(Quantidade))
