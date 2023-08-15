import qrcode
data = "https://youtu.be/bC36d8e3bb0"
qr = qrcode.QRCode(version = 6.7,box_size = 12, border = 5)
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save('qrcode2.png')