import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request, render_template, redirect, url_for, flash, session
import pymysql

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        #return "User {} logged in".format(request.form['username'])
        #valid = True if request.form['username'] == request.form['password'] else False
        valid = valid_login(request.form['username'], request.form['password'])
        print(valid)
        if valid:
            flash("Successfully Logged in.")
            flash("Welcome!")
            #return "Welcome back " + request.form['username']
            session['username'] = request.form['username']
            return redirect(url_for('welcome'))
        else:
            error = "Incorrect username and password."
            app.logger.warning("Incorrect username and password for user (%s).", request.form['username'])
            
    return render_template('login.html', error = error)
    
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))
    
def valid_login(username, password):
    #mysql
    MYSQL_DATABASE_HOST= os.getenv('IP', '0.0.0.0')
    MYSQL_DATABASE_USER = 'hehemama00'
    MYSQL_DATABASE_PASSWORD = ''
    MYSQL_DATABASE_DB = 'my_flask_app'
    conn = pymysql.connect(host = MYSQL_DATABASE_HOST,
    user = MYSQL_DATABASE_USER,
    password = MYSQL_DATABASE_PASSWORD,
    db = MYSQL_DATABASE_DB
        )
        
    cursor = conn.cursor()
    cursor.execute("select * from user where username='{}' and password='{}'"\
    .format(username, password))
    data = cursor.fetchone()
        
    if data:
        return True
    else:
        return False
        
@app.route('/')
def welcome():
    if session['username']:
        return render_template('welcome.html', username=session['username'])
    else:
        return redirect(url_for('login'))

if __name__ == "__main__":
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.secret_key = '\xad\xa5N\xaf\x8e\x19\x9cn}\x03\xb6[\xbbE\xbb\x1aYf\xd5\x96\x14\x9f\xe1\x81'
    #logging
    handler = RotatingFileHandler("error.log", maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host=host, port=port)