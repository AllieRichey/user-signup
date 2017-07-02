from flask import Flask, request, redirect, render_template # do I need all of these?
import cgi
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('index.html')



@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']
    return render_template('welcome.html', username=username)


app.run()