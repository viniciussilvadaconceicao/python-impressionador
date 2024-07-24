from collections import Counter
vendas_tecnologias= {'notebooks':3000, 'desktops':2000, 'smartphones':5000, 'tablets':1000 ,'sansung':25000, 'apple':30000, 'motorola':15000, 'lg':10000}

auxiliar = Counter(vendas_tecnologias)
print(auxiliar.most_common(3))