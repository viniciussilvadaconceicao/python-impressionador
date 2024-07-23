import time 
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')# mudar a linguagem para português
tempo = time.localtime()

print(tempo)
print(time.strftime("%d %B %Y " , tempo)) # %d dia, %B mês por extenso, %Y ano
print(time.strftime("%H:%M:%S" , tempo)) # %H hora, %M minuto, %S segundo

tempo = time.strftime("%A, %d de %B %Y, %H:%M:%S" , tempo)# %A dia da semana 
print("tempo formatado: ", tempo) 