#importando o matplotlib
import matplotlib.pyplot as plt
#importando o numpy
import numpy as np
# o random gera valores aleatórios, randint gera valores inteiros aleatórios
venda = np.random.randint(1000,3000,50)
#arenge gera um vetor de 1 a 50
meses = np.arange(1,51)
plt.axis([0, 50, 0, max(venda)+100])
plt.xlabel('meses')
plt.ylabel('vendas')
plt.plot(meses, venda,color='red') 
plt.show()