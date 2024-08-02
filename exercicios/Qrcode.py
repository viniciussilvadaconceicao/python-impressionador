#primeiro instalar pip install qrcode
#segundo instalar pip install Pillow
import qrcode

imagem = qrcode.make("https://api.whatsapp.com/send?phone=5522992240688")#crio uma variavel para receber o qrcode
imagem.save("qrcode.png")#salvo o qrcode em um arquivo png