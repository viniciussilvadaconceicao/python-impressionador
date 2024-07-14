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


