def somatorio(*args):
    '''podemos passar quantos argumentos quisermos
    e a função irá somar todos eles'''
    soma = 0
    for numero in args:
        soma += numero
    return soma

print(somatorio(1,4,5,10,100))

# (*args) é usado para passar um número variável de argumentos muitos dão o nome de args
#(**kwargs) é usado para passar como dict um número variável de argumentos muitos dão o nome de kwargs