from collections import Counter #Counter é usado para contar a quantidade de elementos em uma lista serve para dict, list, str, tuple, collections, etc
vendas_tecnologias= {'notebooks':3000, 'desktops':2000, 'smartphones':5000, 'tablets':1000 ,'sansung':25000, 'apple':30000, 'motorola':15000, 'lg':10000}

auxiliar = Counter(vendas_tecnologias)
print(auxiliar.most_common(3))#most_common é usado para mostrar os 3 elementos mais comuns da lista