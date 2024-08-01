def gerador_senha(tamanho):
    if tamanho < 4:
        print("Senha muito curta")
    else:
        import random
        import string
        senha = [
            random.choice(string.ascii_letters),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]
        return senha


tamanho = int(input("Digite o tamanho da senha: "))
print(gerador_senha(tamanho))