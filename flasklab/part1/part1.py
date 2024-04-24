import flask
import psycopg2

app = flask.Flask(__name__)

@app.route('/')
def hi():
    return "Hello World!"

# This is only here because I don't know if you want it to be:
@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Red">' + word1 + '</h1>'

@app.route('/pop/<place>')
def get_population(place: str):
    if len(place) > 2:
        return f"<h1 style='color:Red'> Query too long: <span style='color:Gray'>{place}</span><br></br> Please use a 2-letter US state code."
    conn, cur = getConnection()
    # Make our query:
    query = f"SELECT state, state_pop FROM us_states WHERE code = '{place.upper()}'"
    cur.execute(query)
    # return str(cur.fetchall()) #? <-- I did this here to see if I could do SQL injection!
    result = cur.fetchone()
    # Check if the state is legal:
    if result == None:
        return f"<h1>State code <span style='color:Red'>{place.upper()}</span> is invalid. <br></br> Please use a 2-letter US state code.</h1>"
    # Make our result readable:
    pop = str(result[1])
    for i in range(len(pop)-3, 0, -3):
        pop = pop[:i] + "," + pop[i:]
    # We're good! Return:
    conn.close()
    return f"<h1> {result[0]} has a population of {pop}.</h1>"
    

@app.route("/add/<x>/<y>")
def add(x, y):
    # Convert to numbers:
    x = float(x) if '.' in x else int(x)
    y = float(y) if '.' in y else int(y)
    z = x + y
    # is our result an int?
    if z.is_integer():
        z = int(z)
    # Return with fun colors:
    return f"<h1> <span style='color:Red'>{x}</span> + <span style='color:Green'>{y}</span> = <span style='color:Blue'>{z}</span> </h1>"

#+ Database Functions +#
def getConnection():
    conn = psycopg2.connect(
        host = "localhost",
        port = 5432,
        database = "johnsonlacosss",
        user = "johnsonlacosss",
        password = "puppy288market"
    )
    if not conn:
        print("Oops, we don't have a connection!")
        exit(1)
        
    cur = conn.cursor()
    return conn, cur

if __name__ == '__main__':
    my_port = 5115 # or 5215
    app.run(host='0.0.0.0', port = my_port) 