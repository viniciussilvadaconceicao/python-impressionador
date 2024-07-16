def eh_da_categoria(bebidas, categoria):
    '''pega os elementos da lista e verifica se é da categoria informada'''
    bebidas = bebidas.upper()
    if categoria in bebidas:
        return True
    else:
        return False



produtos = ['beb1290', 'BEB2340', 'beb5670', 'BEB6780', 'beb8900', 'BEB3030', 'beb4040', 'BEB5050', 'beb6060', 'BEB7070','bab2112', 'BAB2111']

for produto in produtos:
    if eh_da_categoria(produto, 'BEB'):
        print(f'enviar o {produto} para a seção de bebidas alcoólicas')
    elif eh_da_categoria(produto,'BAB'):
        print(f'enviar o {produto} para a seção de bebidas não alcoólicas')