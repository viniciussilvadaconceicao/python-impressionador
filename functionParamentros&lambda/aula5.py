#imposto 
#serviço 0.15
#produto 0.1

def serviço(valor):
    return valor * 0.15

def produto(valor):
    return valor * 0.1

def imposto(imposto):
    return lambda preco: preco * (1 + imposto)

calcular_serviço = imposto(0.15)
calcular_produto = imposto(0.1)
calcular_imposto = imposto(0.3)

print(calcular_serviço(100))