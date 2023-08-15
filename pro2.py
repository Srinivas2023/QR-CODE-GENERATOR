import qrcode
from PIL import Image

def generate_qr_code(data, filename, scale=5):
    qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=scale,border=4)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="red", back_color="white")
    img = img.convert("RGB")

    img.save(filename)

if __name__ == "__main__":
    data_to_encode = " https://youtu.be/L67njBCJvZY!"
    output_filename = "qrcode3.png"
    generate_qr_code(data_to_encode, output_filename)
    print(f"QR code saved as '{output_filename}'.")
