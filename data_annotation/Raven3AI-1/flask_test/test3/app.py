from flask import Flask, request, jsonify, send_file
import qrcode
import os
import sqlite3

app = Flask(__name__)


# Database setup
def init_db():
    with sqlite3.connect('qrcode.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS qr_table (url TEXT PRIMARY KEY, qr_path TEXT)''')
        conn.commit()


# QR Code generation
def generate_qr_code(url):
    img = qrcode.make(url)
    img_path = f"{url.replace('://', '_').replace('/', '_')}.png"
    img.save(img_path)
    return img_path


# Main route to handle POST requests
@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json
    url = data.get('url')
    print("url")

    # Validate URL
    if not url or not url.startswith(('http://', 'https://')):
        return jsonify({"error": "Invalid URL"}), 400
    with sqlite3.connect('qrcode.db') as conn:
        c = conn.cursor()
        c.execute('SELECT qr_path FROM qr_table WHERE url = ?', (url,))
        result = c.fetchone()

        if result:
            img_path = result[0]
        else:
            img_path = generate_qr_code(url)
            c.execute('INSERT INTO qr_table (url, qr_path) VALUES (?, ?)', (url, img_path))
            conn.commit()

    return send_file(img_path, mimetype='image/png')


if __name__ == '__main__':
    init_db()
    app.run(port=5000, debug=True)
