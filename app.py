from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Cofre Digital",
        "env": os.getenv("ENVIRONMENT", "dev")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
