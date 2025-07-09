from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'secret123'  # Required to use sessions

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        session['user'] = username
        return redirect(url_for('profile'))
    return '''
        <h2>Login Page</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Enter your name">
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/profile')
def profile():
    if 'user' in session:
        return f"<h2>Welcome, {session['user']}!</h2><a href='/logout'>Logout</a>"
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
