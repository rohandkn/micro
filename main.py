from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    url = 'http://text-processing.com/api/phrases/'
    params = {'username': request.form['username'], 'password': request.form['password']}
    r = requests.post(url, data=params)
    return render_template('login.html', error=r.text)

app.run()
