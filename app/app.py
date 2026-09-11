from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "Cloudnexaa DevSecOps Pipeline",
        "status": "running",
        "security": "enabled"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/version")
def version():
    return jsonify({
        "version": "1.0.0",
        "environment": "devsecops"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
