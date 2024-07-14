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
vendedores = ['João', 'Maria', 'José', 'Ana', 'Carlos', 'Pedro', 'Paulo', 'Lucas']
meta = 130
nao_bateu = [] 
for venda in vendas:
    if venda < meta:
       nao_bateu.append(venda)
print(f'Vendedores que não bateram a meta: {nao_bateu}')