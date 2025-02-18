class Filme:
    def __init__(self, titulo, categoria, duracao):
        self.titulo = titulo
        self.categoria = categoria
        self.duracao = duracao

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.locacoes = []

    def alugar_filme(self, filme):
        self.locacoes.append(filme)
        print(f'{self.nome} alugou "{filme.titulo}"')

    def devolver_filme(self, filme):
        if filme in self.locacoes:
            self.locacoes.remove(filme)
            print(f'{self.nome} devolveu "{filme.titulo}"')
        else:
            print(f'{filme.titulo} não foi alugado por {self.nome}')

class Locadora:
    def __init__(self):
        self.filmes = []
        self.clientes = []

    def adicionar_filme(self, filme):
        self.filmes.append(filme)

    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def locar_filme(self, cliente_nome, filme_titulo):
        cliente = next((c for c in self.clientes if c.nome == cliente_nome), None)
        filme = next((f for f in self.filmes if f.titulo == filme_titulo), None)

        if cliente and filme:
            cliente.alugar_filme(filme)
        else:
            print(f'Filme ou cliente não encontrado.')

    def devolver_filme(self, cliente_nome, filme_titulo):
        cliente = next((c for c in self.clientes if c.nome == cliente_nome), None)
        filme = next((f for f in self.filmes if f.titulo == filme_titulo), None)

        if cliente and filme:
            cliente.devolver_filme(filme)
        else:
            print(f'Filme ou cliente não encontrado.')
