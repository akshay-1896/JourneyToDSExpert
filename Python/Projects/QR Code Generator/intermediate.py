import qrcode
from PIL import Image, ImageOps

qr = qrcode.QRCode(version=1,
               error_correction=qrcode.constants.ERROR_CORRECT_H,
               box_size=10,
               border=4)

qr.add_data("https://www.youtube.com/@GuptVrindavanDham")
qr.make(fit=True)

img = qr.make_image(fill_color="slateblue", back_color="white")

border_color = "slateblue"
border_width = 30

new_img = ImageOps.expand(img, border= border_width, fill= border_color)
new_img.save("Gupt_Vrindavan_Dham.png")