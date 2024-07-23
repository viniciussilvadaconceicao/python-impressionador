import time 
tempo = time.localtime()
print(tempo)
print(time.strftime("%d %B %Y " , tempo)) # %d dia, %B mês por extenso, %Y ano
print(time.strftime("%H:%M:%S" , tempo)) # %H hora, %M minuto, %S segundo