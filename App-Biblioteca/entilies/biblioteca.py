from os import remove
from typing import List
from uuid import uuid4
uuid4()
class Endereco:

    logradouro: str
    numero: str
    cidade: str
    bairro: str
    estado: str
    cep: str

    def __init__(self, logradouro: str, numero: str, cidade: str, bairro: str, estado: str, cep: str):
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade
        self.bairro = bairro
        self.estado = estado
        self.cep = cep

    def __repr__(self):
        return (f"Endereço: {self.logradouro}, {self.numero}"
                f" - {self.bairro}, {self.cidade} - {self.estado}, {self.cep}")

class Livro:
    titulo: str
    autor: str
    ano: int

    def __init__(self, titulo: str, autor: str, ano: int):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __repr__(self):
        return  f"{self.titulo}, {self.autor} - ({self.ano})"

class Membro:

    id: str
    nome: str
    endereco: Endereco
    livros: List[Livro]

    def __init__(self, nome: str, endereco: Endereco):
        self.id = " - "
        self.nome = nome
        self.endereco = endereco
        self.livros = []

    def __repr__(self):
        return f"ID: {self.id}\nNome: {self.nome}\n{self.endereco}"

class Biblioteca:

    nome: str
    endereco: Endereco
    acervo: List[Livro]
    membros: List[Membro]

    def __init__(self, nome: str, endereco: Endereco) -> None:
        self.nome = nome
        self.endereco = endereco
        self.acervo = []
        self.membros = []

    # Metodos
    def receber_livro(self, livro: Livro) -> None:
        self.acervo.append(livro)

    def cadastrar_membros(self, membro: Membro) -> None:
        membro.id = uuid4().hex
        self.membros.append(membro)

    def emprestar_livro(self, livro: Livro, membro: Membro) -> None:
        if membro in self.membros:
            self.acervo.remove(livro)
            membro.livros.append(livro)
        else:
            print(f"Membro {membro.nome} não cadastrado!")

    def devolver_livro(self, membro: Membro, livro: Livro):
        membro.livros,remove(livro)
        self.acervo.append(livro)


    def __repr__(self):
        return f"Biblioteca: {self.nome}\n {self.endereco}"