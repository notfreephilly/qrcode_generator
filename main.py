import qrcode
# from qrcode import QRCode

print("Paste your url below:")
user_data = input()

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4
)

qr.add_data(user_data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.show()