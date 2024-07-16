def somatorio(*args):
    '''podemos passar quantos argumentos quisermos
    e a função irá somar todos eles'''
    soma = 0
    for numero in args:
        soma += numero
    return soma

print(somatorio(1,4,5,10,100))
print('\n'*5)

# (*args) é usado para passar um número variável de argumentos muitos dão o nome de args
#(**kwargs) é usado para passar como dict um número variável de argumentos muitos dão o nome de kwargs

def preco_final(preco, **kwargs):
    '''calcula o preço final de um produto pasando o argumento dentro de um dict'''
    print(kwargs)#para ver o que está sendo passado em dict
    if 'desconto' in kwargs:
        preco = preco - kwargs['desconto']
    if 'garantia_extra' in kwargs:
        preco = preco + kwargs['garantia_extra']
    if 'frete' in kwargs:
        preco = preco + kwargs['frete']
    if 'imposto' in kwargs:
        preco = preco + kwargs['imposto']
        return preco

print(preco_final(2000, desconto = 0.5, garantia_extra = 100, frete = 50, imposto = 0.1))