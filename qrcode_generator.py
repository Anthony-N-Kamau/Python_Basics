import qrcode

# url input 
url = input("Enter URL: ").strip()

# file path to save to 
file_path = "/Users/anthonykamau/Desktop/qr_code.png"

# generate qr code
qr = qrcode.QRCode()

# add data to qr code
qr.add_data(url)

# compile the qr code
img = qr.make_image()

# save as image file
img.save(file_path)

print("Qr Code was generated")
