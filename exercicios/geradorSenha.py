def gerador_senha(tamanho):
    if tamanho < 4:
        print("Senha muito curta")
    else:
        import random
        import string
        senha = [
            random.choice(string.ascii_letters),#letras maiusculas e minusculas
            random.choice(string.digits),#numeros
            random.choice(string.punctuation)#caracteres especiais
        ]
        random.shuffle(senha)#embaralha a senha
        return senha


tamanho = int(input("Digite o tamanho da senha: "))
print(gerador_senha(tamanho))