from flask import Flask, render_template
from data import *
import json

data = toJson()

data =  json.loads(data)

print (type(data))

app = Flask(__name__)

app.debug = True

@app.route("/")

def index():

    return render_template("index.html")

@app.route("/shapes")

def shapes():

    return render_template("shapes.html")

@app.route("/data")

def data():

	return render_template('data.html')

@app.route("/graph")

def graph():

	return render_template("graph.html", data=data)

if __name__ == '__main__':

    app.run()
