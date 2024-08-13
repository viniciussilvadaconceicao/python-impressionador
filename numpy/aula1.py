import numpy as np 
#numpy seu foco maior é para operações matemáticas
def arry():
    '''Criando um array com numpy'''
    arry = np.array([1,2, 3, 4, 5, 6, 7, 8, 9, 10])
    lista = [1, "dois", 3.0]
    print(arry)
    print(lista)
    for elemento in lista:
        print(type(elemento))
def soma_lista():
    '''somando na lista'''
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nova_lista = []
    for num in lista:
        nova_lista.append(num + 1)
    print(nova_lista)

def somando_arry():
    '''somando arrays'''
    arry = np.array([1,2, 3, 4, 5, 6, 7, 8, 9, 10])
    arry_soma = arry + 1 
    print(arry_soma)
print(somando_arry())