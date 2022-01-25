#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home page bro !"

#post - used to receivve the data


@app.route("/store", methods=['POST'])
def create_store():
    pass

@app.route("/store/<string:name>", methods=['GET'])
def get_store(name):
    pass

@app.route("/store/", methods=['GET'])
def get_stores(name):
    pass
    
@app.route("/store/<string:name>/item", methods=['GET'])
def get_items_in_store(name):
    pass

@app.route("/store/<string:name>/item", methods=['POST'])
def create_item_in_store():
    pass



#get - 
app.run(port = 5000)
