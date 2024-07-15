def alcoolico(bebidas):
    bebidas = bebidas.upper()
    if 'BEB' in bebidas:
        return True
    else:
        return False



produtos = ['beb1290', 'BEB2340', 'beb5670', 'BEB6780', 'beb8900', 'BEB3030', 'beb4040', 'BEB5050', 'beb6060', 'BEB7070','TAF2112', 'BAB2111']

for produto in produtos:
    if alcoolico(produto):
        print(f'enviar o {produto} para a seção de bebidas alcoólicas')