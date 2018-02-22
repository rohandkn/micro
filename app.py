from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            error = 'Login Successful'
    return error
@app.route("/")
def hello():
    return "Hey I'm using Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)
