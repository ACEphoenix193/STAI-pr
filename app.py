from flask import Flask, render_template, request,jsonify, Response
from flask_cors import CORS
from chat import get_response
import model1 as sqlHandler
app = Flask(__name__)
CORS(app)

@app.get("/")
def index_get():
    return render_template("register.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)
@app.route("/", methods=['GET', 'POST'])
def route():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        sqlHandler.insertUser(username, email, password)
        users = sqlHandler.retrieveUser()
        return render_template("register.html", users=users)
    else:
        return render_template("register.html")

@app.route("/login.html", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = sqlHandler.retrieveUser()

        for i in range(len(users)):
            if users[i][1] == username and users[i][3] == password:
                response = Response(status=200)
                message = f"Welcome, {users[i][1]}"
                loginstat = True
                break
            else:
                response = Response(status=404)
                loginstat = False
                message = "Try Again!!"

        return render_template("login.html",users = users, message = message, loginstat = loginstat), message, loginstat, response, username
    else:
        return render_template("login.html")
@app.route("/base.html", methods=['GET', 'POST'])
def key():
    if request.method == 'POST':
        users = sqlHandler.retrieveUser()
        for i in range(len(users)):
            if users[i][1] == login()[-1]:
                key = users[i][0]
                break
            else:
                continue
        return render_template("base.html", message = login()[1], loginstat = login()[2], key = key)
    else:
        return render_template("base.html")

if __name__ == "__main__":
    app.run(debug =True)