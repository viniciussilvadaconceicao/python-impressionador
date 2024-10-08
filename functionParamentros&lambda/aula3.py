'''estrutura do lambda:
minha_função = lambda parametros: expressão'''
minha_função = lambda num : num * 2
print(minha_função(5))
print('\n')
# o lambda é uma função anonima, que não precisa de um nome para ser chamada

def minha_função2(num):
    '''função que retorna o dobro'''
    return num * 2
print(minha_função2(5))
print('\n')
# a função acima é a mesma coisa que a de cima, só que com o lambda é mais simples

imposto = 0.3

valor_imposto = lambda valor : valor * (1 + imposto)
print(valor_imposto(100))
print('\n')

def preço_imposto2(valor):
    '''função que retorna o valor com imposto'''
    return valor * (1 + imposto)
print(preço_imposto2(100))
print('\n')
# novamente a função de cima é a mesma coisa que a de baixo só que com o lambda é mais simples