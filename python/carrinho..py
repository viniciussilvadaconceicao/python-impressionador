'''função feita para armazenar produtos em um carrinho de compras e lista'''
def carrinho():    
    produto = []
    print('=='*30)
    print('Adicione produtos no carinho, caso queira encerrar escreva fim. ')
    print('-'*30)
    inserir_produtos = str(input('Digite o nome do produto: ')).upper()
    print('-'*30)
    while inserir_produtos != 'FIM':
        produto.append(inserir_produtos)
        inserir_produtos = str(input('Digite o nome do produto: ')).upper()
        print('-'*30)
    print('=='*30)
    print('Produtos inseridos no carinho:')
    print('-'*30)
    for i in produto:
        print(i)
    print('-'*30)
    print()


vendas = [100,110,120,125, 150, 200, 250, 300]
vendedores = {'João':100, 'Maria':110, 'José':120, 'Ana':125, 'Carlos': 150, 'Pedro': 200, 'Paulo':250,  'Lucas':300,}
meta = 130
nao_bateu = [] 
for venda in vendas:
    for vendedor, valor in vendedores.items():
        if valor == venda and valor < meta:
            nao_bateu.append(vendedor)   
        elif valor== venda and valor >= meta:
            print(f'O vendedor {vendedor} bateu a meta ')

print(f'Vendedores que não bateram a meta: {nao_bateu}')
