from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def start():
    print request.headers
    return render_template('frontEnd.html')

@app.route("/authenticate/" , methods=['GET','POST'])
def auth():
    print request.form
    print request.form["user"]
    return "OK"

if (__name__) == "__main__":
    app.debug = True
    app.run()
        
