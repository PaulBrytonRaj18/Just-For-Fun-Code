import qrcode

# Data to be encoded
data = str(input("Enter the data or URL to encode in QR Code: "))


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


# Display the QR code
img.show()

if __name__ == "__main__":
    if data == "":
        print("No data provided to encode.")
    else:
        print("QR Code generation completed.")