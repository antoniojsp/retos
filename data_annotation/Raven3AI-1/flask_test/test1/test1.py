from flask import Flask, request, send_file

app = Flask(__name__)

import logging

# Configure logging
# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     filename='qr_server.log')

@app.before_request
def log_request_info():
    logging.info(f'Headers: {request.headers}')
    logging.info(f'Body: {request.get_data()}')

@app.after_request
def log_response(response):
    logging.info(f'Response Status: {response.status}')
    return response


@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    url = request.form.get('url')
    # Validate URL here
    if not validate_url(url):
        return "Invalid URL", 400
    print(url)
    # Generate QR code
    qr_code_path = generate_qr_code(url)
    print(qr_code_path)
    return send_file(qr_code_path, mimetype='image/png')


def validate_url(url):
    # URL validation logic
    import re
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None


import qrcode
from PIL import Image

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
    img_path = f"{url}.png"  # Generate path based on URL
    img.save(img_path)
    print(img_path)
    return img_path


if __name__ == '__main__':
    app.run(debug=True)