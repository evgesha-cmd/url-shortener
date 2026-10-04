from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({
        "message": "Hello!"
    })


@app.route("/shorten", methods=["POST"])
def shorten():
    data = request.get_json()

    return jsonify({
        "received_url": data["url"],
        "short_code": "abc123"
    })


if __name__ == "__main__":
    app.run(debug=True)