import qrcode

# Data to be encoded
data = "https://www.google.com"    
# Create QR code instance
qr = qrcode.QRCode( 
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the instance
qr.add_data(data)
qr.make(fit=True)
# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")
# Save the image
img.save("temp/google_qr_code.png")
print("QR Code generated and saved as /temp/google_qr_code.png")  