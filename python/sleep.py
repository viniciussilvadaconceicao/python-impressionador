import time

for cont in range (10,0,-1):
    print(cont ,end=' \r')# o \r faz com que o cursor volte para o inicio da linha
    time.sleep(1)
print('Feliz ano novo!!!')