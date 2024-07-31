''' 1- Imposto a pagar no Lucro Presumido

- 5% sobre faturamento de ISS (mensal)
- 0,65% de PIS sobre faturamento, (mensal)
- 3% de COFINS sobre faturmaneto, (mensal)
- 4.8% de IR (trimestral)
- 10% de IR Adicional sobre o que ultrapassar 20mil do faturamento (trimestral)
- CSLL: 2,88% sobre faturamento (trimestral)'''

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
    iss = valor_faturamento * 0.05
    niss = valor_faturamento * 0.0065
    cofins = valor_faturamento * 0.03
    imposto_mensal = iss + niss + cofins
    return imposto_mensal

def calcular_imposto_trimestral(valor_faturamento):
    ir = valor_faturamento * 0.048
    csll = valor_faturamento * 2.88
    adicional_ir = 0
    if valor_faturamento > 200000:
        adicional_ir = (valor_faturamento - 200000) * 0.1
    imposto_trimestral = ir + csll + adicional_ir
    return imposto_trimestral

resultado = {}

for mes in faturamento:
    valor_faturamento = transformar_numero(faturamento[mes])
    imposto_mensal = calcular_imposto_mensal(valor_faturamento)
    imposto_trimestral = calcular_imposto_trimestral(valor_faturamento)
    resultado[mes]= (valor_faturamento, imposto_mensal, imposto_trimestral)

print(resultado)