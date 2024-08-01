def gerador_senha(tamanho):
    if tamanho < 4:
        print("Senha muito curta")
    


tamanho = int(input("Digite o tamanho da senha: "))
print(gerador_senha(tamanho))