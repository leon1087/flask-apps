import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Username is: {}'.format(request.values['username'])
    else:
        return '''<form method="post" action="/login">
            <input type="text" name="username" />
            <input type="password" name="password" />
            <p>
            <button type="submit">Submit</button>
            </form>
            '''
    pass
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/')
def index():
    return render_template('hello.html')


if __name__ == "__main__":
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.run(host=host, port=port)