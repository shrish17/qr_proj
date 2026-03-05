import qrcode

# Ask user for input
data = input("Enter the text or URL to generate QR code: ")

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

# Create image
img = qr.make_image(fill_color="black", back_color="white")

# Save image
filename = "qr_code.png"
img.save(filename)

print(f"✅ QR code generated and saved as {filename}")
img.show()