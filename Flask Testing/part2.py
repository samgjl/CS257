from flask import Flask
from flask import render_template
import random
import psycopg2

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")
