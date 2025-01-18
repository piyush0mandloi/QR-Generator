from flask import Flask, request, send_file,render_template
import qrcode
import io
import urllib.parse

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr/<path:data>', methods=['GET'])
def generate_qr(data):
    # Decode the URL-encoded string
    decoded_data = urllib.parse.unquote(data)

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(decoded_data)
    qr.make(fit=True)

    # Create an in-memory image of the QR code
    img = qr.make_image(fill='black', back_color='white')

    # Save the image to a BytesIO object
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    # Send the image as a response
    return send_file(img_io, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)


# https://wa.me/918357955178?text=Hi%2C%20I%20want%20enquiry%20regarding%20wifi%20in%20Kishan%20Vintage


# # Data you want to encode in the QR code
# data = "https://wa.me/918357955178?text=Hi%2C%20I%20want%20enquiry%20regarding%20wifi%20in%20Kishan%20Vintage"  # You can change this to any URL or text
# qr = qrcode.QRCode(
#     version=1,  # Version controls the size of the QR code (1 is the smallest)
#     error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
#     box_size=10,  # Size of each box in the QR code
#     border=4,  # Thickness of the border
# )
# qr.add_data(data)
# qr.make(fit=True)

# # Create an image from the QR code instance
# img = qr.make_image(fill='black', back_color='white')

# # Save the image to a file
# img.save("qrcode_example2.png")

# # Optionally, display the image (if you are using a graphical interface)
# img.show()