import os
from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        #return "User {} logged in".format(request.form['username'])
        valid = True if request.form['username'] == request.form['password'] else False
        print(valid)
        if valid:
            flash("Successfully Logged in.")
            flash("Welcome!")
            #return "Welcome back " + request.form['username']
            return redirect(url_for('welcome', 
            username=request.form['username']))
        else:
            error = "Incorrect username and password."
        pass
    return render_template('login.html', error = error)
        
@app.route('/welcome/<username>')
def welcome(username):
    return render_template('welcome.html', username=username)

if __name__ == "__main__":
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.secret_key = "SuperKey1"
    app.run(host=host, port=port)