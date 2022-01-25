#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 09:16:12 2022

@author: harikrishnareddy
"""

from flask import Flask,render_template
from flask import redirect,url_for

app = Flask(__name__) #constructer

@app.route("/<username>")
def hello(username):
    return render_template("index.html",title="Title of the page",user = username)


@app.route("/user/<un>")
def helloUser(un):
    return "Hello " + un + "!"

@app.route("/user/<un>/<int:age>")
def display(un,age):
    return "Username "+un+",Age "+ str(age)


@app.route("/greet/user/<un>")
def greet_user(un):
    return redirect(url_for('evadu kavalira niku ',username=un))




if __name__ == '__main__':
    app.run(debug =True,port = 5001)