from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "healthy", "message": "Welcome to the DevSecOps Secure App!"})

@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    # Safe interpolation, avoiding dangerous eval constructs
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == "__main__":
    # Run on port 5000 inside the container
    app.run(host="0.0.0.0", port=5000)
