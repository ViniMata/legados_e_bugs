import random
import string

def gerar_senha(tamanho=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print("Bem-vindo ao Gerador de Senhas!")
    tamanho = int(input("Digite o tamanho da senha desejada: "))
    senha = gerar_senha(tamanho)
    print(f"Sua senha gerada é: {senha}")

if __name__ == "__main__":
    main()
