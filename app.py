from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/add_product", methods=["POST"])
def add_product():
    data = request.json
    # Example logic
    return jsonify({"message": "Product added", "data": data})

if __name__ == "__main__":
    app.run(debug=True)
