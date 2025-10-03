import socket
from datetime import datetime

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/v1/details")
def details():
    return jsonify(
        {
            "time": datetime.today().strftime("%I:%M:%S %p on %B %d, %Y"),
            "hostname": socket.gethostname(),
            "message": "Hello World",
        }
    )


@app.route("/api/v1/healthz")
def healthz():
    return jsonify({"status": "up"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0")
