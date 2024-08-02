import qrcode
from qrcode.image.styledpil import StyledPilImage #Pilimage é uma classe que representa uma imagem

rede_sociais = {
    "whatsapp":"https://api.whatsapp.com/send?phone=5522992240688",
    "email" :"mailto:viniscdeza@gmail.com",
    "instagram": "https://www.instagram.com/vinicsilvcon?igsh=eTUxYm81bmJqMDN5&utm_source=qr",
    "linkedin" :"https://www.linkedin.com/in/vinicius-silva-sc"
}
for rede_sociais, url in rede_sociais.items():
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)  # para poder adicionar uma imagem
    qr.add_data("url")

    imagem = qr.make_image(
    image_factory=StyledPilImage,
    embeded_image_path = "C:\\Users\\horti\\OneDrive\\Documentos\\meusProjetos\\Portf-lio\\imagens\\python.jpg"

    )

    imagem.save(f"qrcode_logo.png")
