from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_data():
    if request.headers.get('Authorization') == '7281fae460d84fde91d83514240709':
        data = request.get_json()
        # Simulate processing the data
        response = {"message": "Data received", "received_data": data}
        print(response)
        return jsonify(response), 200
    else:
        return jsonify({"error": "Unauthorized"}), 401

if __name__ == "__main__":
    app.run(debug=True)