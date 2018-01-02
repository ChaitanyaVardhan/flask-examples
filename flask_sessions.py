from flask import Flask, session, request, redirect, url_for

app = Flask(__name__)

users = {'chaitanya', 'cersei', 'tyrion'}

@app.route('/')
def index():
    return '''
        you are not logged in.<br>
        <a href='/login'>Click here to login</a>
    '''        

@app.route('/<user_name>')
def user(user_name):
    if session['logged_in'] == True:
        return "Weclome " + user_name + "<br> \
            <p><a href='/logout'>Click to Log Out</a><p>"
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
            <p><h2>Enter your username to login</h2></p>
            <form method='POST' action='/login'>
                <p><input type='text' name='user_name', value=''></p>
                <p><input type='submit' value='Submit'></p>
            </form>
        '''
    if request.form['user_name'] in users:
        session['logged_in'] = True
        return redirect(url_for('user', user_name=request.form['user_name']))

    return "Please register first"

@app.route('/logout')
def logout():
    if session['logged_in'] == True:
        session['logged_in'] = False
        return "Logged out"
    else:
        return "Hey dude, you weren't logged in to begin with"
            
if __name__ == '__main__':
    app.secret_key = 'very secret key'

    app.run(host='0.0.0.0', port=8080, debug=True)
