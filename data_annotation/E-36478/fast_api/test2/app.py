from flask import Flask, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Define a route to the home page
@app.route('/')
def home():
    return jsonify(message="Welcome to the Flask Web App!")

# Define another route
@app.route('/items/<int:item_id>')
def get_item(item_id):
    return jsonify(item_id=item_id)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)