import qrcode
from qrcode.image.styledpil import StyledPilImage #Pilimage é uma classe que representa uma imagem

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)  # para poder adicionar uma imagem
qr.add_data("https://api.whatsapp.com/send?phone=5522992240688")

imagem = qr.make_image(
    image_factory=StyledPilImage,
    embeded_image_path = "C:\\Users\\horti\\OneDrive\\Documentos\\meusProjetos\\Portf-lio\\imagens\\python.jpg"
,
)

imagem.save("qrcode_logo.png")
