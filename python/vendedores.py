vendas = [100,110,120,125, 150, 200, 250, 300]
vendedores = {'João':100, 'Maria':110, 'José':120, 'Ana':125, 'Carlos': 150, 'Pedro': 200, 'Paulo':250,  'Lucas':300,}
meta = 130
nao_bateu = [] 
print()
print('=-'*30)
for venda in vendas:
    for vendedor, valor in vendedores.items():
        if valor == venda and valor < meta:
            nao_bateu.append(vendedor)   
        elif valor== venda and valor >= meta:
            print(f'O vendedor {vendedor} bateu a meta ')
print('=-'*30)
print()
print('-'*70)
print(f'Vendedores que não bateram a meta: {nao_bateu}')
print('-'*70)
print('\n')