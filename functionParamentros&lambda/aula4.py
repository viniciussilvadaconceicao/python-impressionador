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

#agora queremos apenas os valores que são maiores que 4000

def maiorque4000(item):
    '''função que verifica se o valor é maior que 4000'''
    return item[1] > 4000

produtos_maiorque4000 = list(filter(maiorque4000, preco_tecnologicos.items()))
print(produtos_maiorque4000)