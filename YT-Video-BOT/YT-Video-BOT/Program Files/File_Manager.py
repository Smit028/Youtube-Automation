import qrcode

# Define the data you want to encode in the QR code
data = "https://www.youtube.com/channel/UC8GHSJt71dPiygKGXao1sRQ"  # Replace with the data you want to encode

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # QR code version (1 to 40, higher values have higher capacity)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level (L, M, Q, or H)
    box_size=10,  # Size of each box in the QR code
    border=4,  # Border size around the QR code
)

# Add data to the QR code
qr.add_data(data)

# Make the QR code
qr.make(fit=True)

# Create an Image object to render the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image file
img.save("my_qr_code.png")

# Display the QR code
img.show()
