faturamento = {
    'janeiro': 'R$95.659,25',
    'fevereiro': 'R$98.130,32',
    'março': 'R$60.100,50',
    'abril': 'R$70.200,34',
    'maio': 'R$98.340,67',
    'junho': 'R$95.780,98',
    'julho': 'R$98.433,49',
    'agosto': 'R$101.090,56',
    'setembro': 'R$90.508,77',
    'outubro': 'R$98.800,23',
    'novembro': 'R$95.430,13',
    'dezembro': 'R$71.129,80'
}
#voce precisa inserir no sistema um dicionário no formato :
'''resultado = {
'mes':(faturamento, imposto_mensal, imposto_trimetral)
}'''

#passo a passo
#para cada mes de faturamento
#transformar o valor do faturamento em um numero
#calcular o imposto mensal
#calcular o imposto trimestral
#adicionar o faturamento , imposto mensal e trimestral ao dicionario resultado
def transformar_numero(texto):
    texto = texto.replace('R$', '')
    texto = texto.replace('.', '')
    texto = texto.replace(',', '.')
    valor = float(texto)
    return valor

def calcular_imposto_mensal(valor_faturamento):
    pass

def calcular_imposto_trimestral(valor_faturamento):
    pass

for mes in faturamento:
    valor_faturamento = transformar_numero(faturamento[mes])
    imposto_mensal = calcular_imposto_mensal(valor_faturamento)
    imposto_trimestral = calcular_imposto_trimestral(valor_faturamento)