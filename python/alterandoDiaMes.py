import time

tempo_BR = "23/07/2024"
formato = "%d/%M/%Y"
print(tempo_BR)

tempo_EUA = '07/23/2024'
formato = '%M/%d/%Y'
print(tempo_EUA)

struk_tempo = time.localtime()#aqui ele pega o tempo local
print(struk_tempo)

gmt_exemplo = time.gmtime()#aqui ele pega o tempo de greenwich
print(gmt_exemplo)