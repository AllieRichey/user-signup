from flask import Flask, request, redirect, render_template 
import os #don't think I need this?

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/signup")
def index():
    return render_template('index.html')

@app.route("/signup", methods=['POST'])
def validate_user_input():
    username = request.form['username']
    password = request.form['password']
    password_check = request.form['password-check']
    email = request.form['email']

    username_err = ''
    password_err = ''
    password_check_err = ''
    email_err = ''

    if len(username) == 0 or ((' ' in username) == True) or len(username) < 3 or len(username) > 20:
        username_err = "That's not a valid username"
        username = ''

    if len(password) == 0 or ((' ' in password) == True) or len(password) < 3 or len(password) > 20:
        password_err = "That's not a valid password"
        password = ''

    if password_check!= password:
        password_check_err = "Passwords don't match"
        password_check = ''

    if len(email) == 0:
        pass
    elif (email.count("@") != 1) or (email.count(".") != 1) or ((' ' in email) == True) or len(email) < 3 or len(email) > 20 :
        email_err = " That's not a valid email"
        email = ''

    if not username_err and not password_err and not password_check_err and not email_err:
        return redirect('/welcome?user={0}'.format(username)) # maybe remove .format ?
    else:
        return render_template('index.html', username_err = username_err,
                                      password_err = password_err,
                                      password_check_err = password_check_err,
                                      email_err = email_err,
                                      username = username,
                                      password = password,
                                      password_check = password_check,
                                      email = email)


@app.route("/welcome", methods=['POST', 'GET'])
def welcome():
    username = request.form['username']
    return render_template('welcome.html', username=username)


app.run()