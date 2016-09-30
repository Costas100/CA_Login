## Constantine Athanitis
## Work 4: Login

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def start():
    print request.headers
    return render_template('frontEnd.html')

@app.route("/authenticate/" , methods=['POST'])
def auth():
    usr = request.form["user"]
    psw = request.form["pass"]
    if (usr == "Tony" and psw == "Hawk"):
        return "Success! You have now logged in."
    else:
        return "Oh no! You have failed to log in."


if (__name__) == "__main__":
    app.debug = True
    app.run()
        
