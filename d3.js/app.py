from flask import Flask, render_template
from data import *
import json

freq = totalFrequency(callee())

freq = json.loads(freq)
#print (freq)

freql = []

for item in freq[0].keys():

	freql.append(freq[0][item])

print (freql)

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

	return render_template('data.html', frequency=freql)

if __name__ == '__main__':

    app.run()
