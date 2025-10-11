"""Aula 11/10/2025"""
from http import HTTPStatus

from pyexpat.errors import messages

"""
Tratamento de Exceções

Finalidade: Tratamos as exceções para que nossas aplicações não "quebram" durante a experiência dos usuários

Palavras Python:
- try
- except
- finally

Sintaxe:

try:
    código principal
    
except Exception:
    
    Tratamento da exception

finally:

    bloco finally
"""

def soma(a: int, b: int) -> int:
    """
    Soma
    :param a: número
    :param b: número
    :return:  soma de a e b
    """
    try:
        soma = a + b
        return soma
    except TypeError:
        return "Não podemos somar string ou int, apenas int e int"

# print(soma(10, 15))
# print(soma(10, "15"))
#
# print("Próximo passo")

def divisao(a: int, b: int) -> float | str:
    try:
        res = a/b
        return res
    except TypeError:
        return "Não podemos dividir um int por uma string, apenas int pot int"
    except ZeroDivisionError:
        return "Não podemos dividir um número por 0 (zero)"

# print(divisao(10, 15))
# print(divisao(10, "2"))
# print(divisao(10, 0))

"""
Exemplo de Tratamento de Exceções de uma API

@app.route("/user/<int:user_id>")
def get_user_by_id(user_id):
    
    try:
        user = achar(user_id)
        return {"user": user}, HTTPStatus.OK
    except ValueError as e:
        return {"message": "Não achamos"}, HTTPStatus.NOT_FOUND
"""

