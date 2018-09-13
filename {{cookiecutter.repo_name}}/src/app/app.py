from flask import Flask, render_template, request, jsonify
from src.app.predictor import predict


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/text/predict", methods=["POST"])
def text_predict():
    query = request.form['query']

    reply = predict(query=query)

    result = {
        "reply": reply
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)

