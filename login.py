## Constantine Athanitis
## Work 4: Login

from flask import Flask, render_template, request, url_for, session, redirect
import hashlib

app = Flask(__name__)
app.secret_key = "RANDOM STRING"

data = open("data/userpass.csv","a")
data.close()

@app.route("/")
def root():
    if "username" in session:
        return redirect(url_for("welc"))
    else:
        return redirect(url_for("start"))


@app.route("/welcome")
def welc():
    return render_template("welcome.html")

@app.route("/logout")
def logout():
    if "Lo" in request.form["submit"]:
        session.pop("username")
        return render.template("logout.html")

@app.route("/logreg")
def start():
    return render_template('frontEnd.html')

@app.route("/authenticate" , methods=['POST'])
def auth():
    usr = request.form["user"]
    psw = request.form["pass"]

    if "Register" in request.form["submit"]:
        return reg(usr, psw)
    else:
        return log(usr, psw)


def reg(User, Pass):
    data = open("data/userpass.csv","r")
    list = data.readlines()
    data.close()
    for i in list:
        x = i.split(",")
        if (x[0] == User):
            text = "Oops! That username already exists. Try another one."
            return render_template("Msg.html", m=text)

     
    data = open("data/userpass.csv","a")
    Pass = hashlib.sha224(Pass).hexdigest()
    data.write(User+","+Pass+"\n")
    data.close()
    text = "Congratulations! Your account was created."
    return render_template("frontEnd.html", m = text)



def log(User, Pass):        
    data = open("data/userpass.csv","r")
    list = data.readlines()
    data.close()
    
    good = "You sucessfully logged in!"
    badP = "Password doesn't match the username. Try again."
    badU = "Username doesn't match the password. Try again."
    bad = "Username and password can't be found. Try again."
    
    Pass = hashlib.sha224(Pass).hexdigest()

    for i in list:
        x = i.split(",")
        x[1] = x[1][:-1]
        if (x[0] == User):
            if (x[1] == Pass):
                session["username"] = User
                return render_template("Msg.html", m=good)
            else:
                return render_template("Msg.html", m=badP)
        else:
            if (x[1] == Pass):
                return render_template("Msg.html", m=badU)
    return redirect(url_for("/welcome"))

            
if (__name__) == "__main__":
    app.debug = True
    app.run()
        
