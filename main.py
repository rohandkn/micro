from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
         url = '34.214.28.145:5000/auth'
         params = {'username': request.form['username'], 'password': request.form['password']}
         r = requests.post(url, data=params)
         error = r.text
    return render_template('login.html', error=error)

   

app.run(host='0.0.0.0')
