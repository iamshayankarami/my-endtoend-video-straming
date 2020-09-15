from flask import Flask, request, render_template, session, url_for, redirect
app = Flask(__name__)
app.secret_key = 'shayan13822003'
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        session['data'] = username, password
        return redirect(url_for('main_page'))
    return render_template('index.html')

@app.route('/main_page')
def main_page():
    return render_template("main.html")

if __name__ == '__main__':
    app.run('0.0.0.0')
