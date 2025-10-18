from entilies.biblioteca import Endereco, Livro, Membro, Biblioteca
from utils.cep import busca_cep

cep = "09435470"
numero = "181" # sempre vai ser esse numero q vc definiu
informacoes_de_endereco = busca_cep(cep=cep)

# Instanciando Endereço
e1 = Endereco(
    logradouro=informacoes_de_endereco["address"],
    numero=numero,
    bairro=informacoes_de_endereco["district"],
    cidade=informacoes_de_endereco["city"],
    estado=informacoes_de_endereco["state"],
    cep=cep
)

print(e1)
print()

# Instanciando Livros
iracema = Livro("Iracema", "José de Alencar", 1865)
revolucao_dos_bichos = Livro("Revolução dos Bichos", "George Orwell", 1945)
o_pianista = Livro("O Pianista", "Wladyslw Szpilman", 1946)

print(iracema)
print(revolucao_dos_bichos)
print(o_pianista)

# Instanciando Membros
joao = Membro("Joao", e1)
ana = Membro("Ana", e1)
print(joao)
print(ana)
print()

# Instaciar Biblioteca
biblioteca = Biblioteca("Biblioteca Senai", e1)

# Adicionar livros
biblioteca.receber_livro(iracema)
biblioteca.receber_livro(revolucao_dos_bichos)
biblioteca.receber_livro(o_pianista)
print(biblioteca.acervo)

# Cadastrar Membro
biblioteca.cadastrar_membros(joao)
biblioteca.cadastrar_membros(ana)
print(joao)
print(ana)
print()

# Emprestar Livros
biblioteca.emprestar_livro(iracema, joao)
print("Acervo", biblioteca.acervo)
print("João", joao.livros)
biblioteca.emprestar_livro(revolucao_dos_bichos, ana)
print("Acervo", biblioteca.acervo)
print("Ana", ana.livros)

# Devolver Livros
biblioteca.devolver_livro(joao, iracema)
biblioteca.devolver_livro(ana, revolucao_dos_bichos)
print("Acervo", biblioteca.acervo)
print("João", joao.livros)
print("Ana", ana.livros)