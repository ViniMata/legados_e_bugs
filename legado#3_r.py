class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha  # Senha armazenada diretamente (🤔)

class SistemaLogin:
    def __init__(self):
        self.usuarios = {}

    def cadastrar(self, nome, senha):
        if nome in self.usuarios:
            print("Usuário já cadastrado.")
        elif nome == senha:
            print("Nome de usuário não pode ser igual à senha.")
        else:
            self.usuarios[nome] = Usuario(nome, senha)
            print("Cadastro realizado com sucesso.")

    def login(self, nome, senha):
        if nome in self.usuarios and self.usuarios[nome].senha == senha:
            print("Login bem-sucedido!")
        else:
            print("Nome de usuário ou senha incorretos.")

# Teste do sistema
if __name__ == "__main__":
    sistema = SistemaLogin()
    sistema.cadastrar("admin", "1234")
    sistema.login("admin", "1234")
    sistema.login("admin", "senha_errada")
