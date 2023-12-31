from flask import Flask, render_template, request,jsonify, Response
from flask_cors import CORS
from chat import get_response

app = Flask(__name__)
CORS(app)

@app.get("/")
def index_get():
    return render_template("index.html")

@app.get("/about")
def about():
    return render_template("about.html")

@app.get("/whyge")
def whyge():
    return render_template("why.html")

@app.get("/ethical")
def ethical():
    return render_template("ethical.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug =True)