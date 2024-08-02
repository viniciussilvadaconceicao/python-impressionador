import qrcode
from qrcode.image.styledpil import StyledPilImage #Pilimage é uma classe que representa uma imagem

qr = qrcode.QRCode()
qr.add_data("https://api.whatsapp.com/send?phone=5522992240688")
qr.make(fit=True)

imagem = qr.make_image(image_factory=StyledPilImage, embeded_image_path="python.png")
imagem.save("qrcode_logo.png")