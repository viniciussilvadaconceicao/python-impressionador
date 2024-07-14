'''vendedores = {'João':100, 'Maria':110, 'José':120, 'Ana':125, 'Carlos': 150, 'Pedro': 200, 'Paulo':250,  'Lucas':300,}
for nome in vendedores:
    print(f'vendedor: {nome}, vendeu: {vendedores[nome]}')'''
#se a loja tiver um numero especifico de vendedores usamos o dicionario
meta = 130
nao_bateu = []
bateu = []
cont = 2
print('\n')
print('='*80)      
print('''Bem vindo ao sistema de vendas:
Digite o nome do vendedor e o valor de suas vendas para saber se ele bateu a meta''')
print('='*80)      
for i in range(cont):
    funcionarios = dict()
    funcionarios['vendedor'] = str(input('Nome: ')).upper().strip()
    funcionarios['vendas']= float(input('Vendas: '))
    if funcionarios['vendas'] < meta:
        nao_bateu.append(funcionarios)
    elif funcionarios['vendas'] >= meta:
        bateu.append(funcionarios)
print('\n')        
print('='*44)
print('Os vendedores que não bateram a meta foram:')  
print('='*44)      
for i in nao_bateu:
    print(f'{i["vendedor"]}')
print('\n')
print('='*44)
print('Os vendedores que BATERAM A META!:')  
print('='*44)
for i in bateu:
    print(f'{i["vendedor"]}')
print('\n')