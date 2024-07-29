import matplotlib.pyplot as plt
import numpy as np

venda = np.random.randint(1000,3000,50)
meses = np.arange(1,51)

plt.figure(1,figsize=(15,3))
plt.subplot(1,3,1)
plt.bar(meses,venda,color='red')
plt.subplot(1,3,2)
plt.scatter(meses,venda,color='green')
plt.subplot(1,3,3)
plt.plot(meses,venda, color='gray')
plt.show()