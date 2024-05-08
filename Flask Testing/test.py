from flask import Flask
from flask import render_template
import random
import psycopg2

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/playlist_order')
def playlist_order():
    return render_template("playlist_order.html")


if __name__ == "__main__":
    app.run(debug=True)