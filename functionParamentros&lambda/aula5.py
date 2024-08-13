#imposto 
#serviço 0.15
#produto 0.1

def serviço(valor):
    return valor * 0.15

def produto(valor):
    return valor * 0.1

def imposto(imposto):
    return lambda preco: preco * imposto