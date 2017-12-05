import os
from flask import Flask, url_for

app = Flask(__name__)

@app.route("/hello")
def hello():
    #for Cloud9 only, this is for step tracing.
    #import pdb; pdb.set_trace()
    
    return "Hello World!"

@app.route("/")
def index():
    #return "Index Page"
    return url_for('show_user_profile', username='Leon')


@app.route("/username/<username>")
def show_user_profile(username):
    return "Hello {}".format(username)
    
    
@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "Post {}".format(post_id)
    
    
if __name__ == "__main__":
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.run(host=host, port=port)