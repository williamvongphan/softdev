import flask
from flask import session, render_template, request, redirect, url_for

app = flask.Flask(__name__)
app.secret_key = 'super secret key (this is very strong and can be used in production, yes I know it is extremely secure, over 9000)'

USERNAME = 'QR Code Generators'
PASSWORD = 'strong password'

@app.route('/')
def index():
    # Check if the user is logged in
    print(session)
    if 'username' in session:
        return render_template('response.html', response="Hello, " + session['username'] + "!")
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Check if the user is already logged in
    if 'username' in session:
        return redirect(url_for('index'))
    # else, check if the user is trying to login
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            if username != USERNAME:
                return render_template('login.html', error='Bad username')
            elif password != PASSWORD:
                return render_template('login.html', error='Bad password')
            else:
                return render_template('login.html', error='Bad juju')
    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # Check if the user is logged in
    if 'username' in session:
        session.pop('username', None)
        return redirect(url_for('index'))
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
