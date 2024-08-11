preco_tecnologicos = {'asus': 4000, 'samsung': 7000, 'apple': 6000 , 'xaomi':5000}

def imposto(valor):
    '''Função que calcula o imposto de um produto'''
    return valor * (1 + 0.3)

preco_imposto = list(map(imposto,preco_tecnologicos.values()))#map(função, lista) ele pega a função e aplica na lista	
print(preco_imposto)
print('\n')

# Função lambda
preco_imposto2 = list(map(lambda valor: valor * ( 1 + 0.3) ,preco_tecnologicos.values()))#map(lambda, lista)
print(preco_imposto2)
