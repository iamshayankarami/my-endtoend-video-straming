from flask import Flask, request, render_template, session, url_for, redirect
import sysi, json

def find_and_show_error(show_arr, input_in, position):
    return_error=[]
    if position == 'singin':
        if len(input_in['password'])<8:
            return_error.append('short password')
    if position == 'login':
        if [data[user]['password'] for user in json_data() if user==input_in['usrename']] != input_in['password']:
            return_error.append('wronge password')
        if len([user for user in json_data() if user!=input_in['username']])>=len(json_data) and len([data[user]['email'] for user in data if data[user]['email']!=input_in['email']]>=len([data[user]['email'] for user in data]):
            return_error.append('cant find that usrname')

app = Flask(__name__)
app.secret_key = 'shayan13822003'
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        return_data = {'username': request.form["username"], 'password': request.form["password"]}
        session['data'] = username, password
        return redirect(url_for('main_page'))
    return render_template('index.html')


@app.route('/singin', methods=["POST", "GET"])
def singin():
    if request.method == 'POST':
        return_data={'username': request.form['username'], 'name': request.form['name'], 'password': request.form['password'], 'email': requets.form['email']}


if __name__ == '__main__':
    app.run('0.0.0.0')
