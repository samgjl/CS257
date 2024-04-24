from flask import Flask
from flask import render_template
import random
import psycopg2

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/person/<fun>')
def rand(fun):
    title = ''
    if fun == '0':
        title = "Too bad!"
        
    name = genName()
    year = random.randint(1000, 2000)
    place = genPlace()
    return render_template("person.html", title = title, randName = name, randYear = year, randCity = place[0], randState = place[1])

def genPlace():
    conn = psycopg2.connect(
        host = "localhost",
        port = 5432,
        database = "johnsonlacosss",
        user = "johnsonlacosss",
        password = "puppy288market"
    )
    cur = conn.cursor()
    
    cur.execute("SELECT city, home_state FROM us_cities ORDER BY RANDOM() LIMIT 1;")
    city = cur.fetchone()
    conn.close()
    return city

def genName():
    names = ['Anna', 'Tanya', 'Amy', 'Josh', 'Tom', 'Matt', 'DLN', 'David', 'Sneha', 'Layla', 'Jeff', 'Anya']
    return random.choice(names)

if __name__ == '__main__':
    my_port = 5115 # or 5215
    app.run(host='0.0.0.0', port = my_port) 
