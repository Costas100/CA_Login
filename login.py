## Constantine Athanitis
## Work 4: Login

from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

data = open("data/userpass.csv","a")
data.close()

@app.route("/")
def start():
    print request.headers
    return render_template('frontEnd.html')

@app.route("/authenticate/" , methods=['POST'])
def auth():
    usr = request.form["user"]
    psw = request.form["pass"]

    if "Register" in request.form["submit"]:
        return reg(usr, psw)
    else:
        return log(usr, psw)


def reg(User, Pass):
    '''  return check(User)
     The following code does what check() should do.
     However, i am getting a return function error, so i made it part of the reg() code'''
    
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


'''def check(User):
    data = open("data/userpass.csv","r")
    list = data.readlines()
    data.close()
    for i in list:
        x = i.split(",")
        if (x[0] == User):
            text = "Oops! That username already exists. Try another one."
            return render_template("Msg.html", m=text)
    return
'''

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
        '''Checks
        print User
        print Pass
        print x[0]
        print x[1]
        '''
        if (x[0] == User):
            if (x[1] == Pass):
                return render_template("Msg.html", m=good)
            else:
                return render_template("Msg.html", m=badP)
        else:
            if (x[1] == Pass):
                return render_template("Msg.html", m=badU)
    return render_template("Msg.html", m=bad)

            
if (__name__) == "__main__":
    app.debug = True
    app.run()
        
