from flask import Flask, request, send_file
import qrcode
import os
import logging
import hashlib

app = Flask(__name__)
#
# logging.basicConfig(filename='app.log', level=logging.INFO,
#                     format='%(asctime)s:%(levelname)s:%(message)s')


def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    temp_path = "temp_qrcode.png"
    img.save(temp_path)
    return temp_path


def store_qr_code(file_path, qr_code_path):
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
    os.rename(qr_code_path, file_path)


def validate_url(url):
    # Simple URL validation (you might want to use a more robust method)
    print(url)
    return url.startswith("http://") or url.startswith("https://")


@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    url = request.form.get('url').lower().strip()
    print(type(url))
    print(validate_url(url))
    if not validate_url(url):
        return "Invalid URL", 400

    logging.info(f"Request received for URL: {url}")

    url_hash = hashlib.md5(url.encode()).hexdigest()
    file_path = f"qr_codes/{url_hash}.png"

    if os.path.exists(file_path):
        logging.info(f"QR code found in cache: {file_path}")
        return send_file(file_path, mimetype='image/png')

    temp_path = generate_qr_code(url)
    store_qr_code(file_path, temp_path)
    logging.info(f"QR code generated and stored: {file_path}")

    return send_file(file_path, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)