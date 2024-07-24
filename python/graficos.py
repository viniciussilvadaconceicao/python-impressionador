vendas_meses = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 10000, 7000, 8000, 4000]
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
#plotar um gráfico de forma simples
import matplotlib.pyplot as plt 
plt.plot(meses, vendas_meses)
plt.ylabel('Vendas')
plt.xlabel('Meses')
plt.show()