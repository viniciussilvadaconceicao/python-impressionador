produtos = ['Iphone 11','Ipad','Iphone 15', 'airpods','macbook','apple watch','apple tv','mac mini','mac pro','mac air']
produtos.sort(key= str.casefold)
print(produtos)	

vendas_produtos = {'iphone':400,'ipad':550,'sansung':1000,'pc':18000}

def segundo_elemento(tupla):
    return tupla[1]

vendas_produtos = list(vendas_produtos.items())
