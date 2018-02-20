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

app.run()
