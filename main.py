from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def alive():
    return jsonify(message="🚀 Hello, I’m alive and 100 % deployed by Railway!")

if __name__ == "__main__":
    # Railway injects PORT env-var; fallback for local test
    port = int(os.getenv("PORT", 8000))
    app.run(host="0.0.0.0", port=port)