from typing import Dict
import requests

def busca_cep(cep: str) -> Dict:
    """
    Função recebe o CEP e retorna um JSON com as informções
    :param cep: CEP
    :return: JSON com as informações
    """

    req = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}")
    result = req.json()
    return result