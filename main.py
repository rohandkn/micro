from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
         url = 'http://text-processing.com/api/phrases/'
         params = {'username': request.form['username'], 'password': request.form['password']}
         r = requests.post(url, data=params)
         error = r.text
    return render_template('login.html', error=error)

   

app.run(host='0.0.0.0')
