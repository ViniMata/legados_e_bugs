import random
import string

def gerar_senha(tamanho=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print("Bem-vindo ao Gerador de Senhas!")
    while True:
        try:
            tamanho = int(input("Digite o tamanho da senha desejada: "))
            senha = gerar_senha(tamanho)
            print(f"Sua senha gerada é: {senha}")
            break
        except ValueError:
            print("Digite um valor válido.")

if __name__ == "__main__":
    main()
