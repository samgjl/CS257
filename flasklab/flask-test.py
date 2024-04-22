import flask

app = flask.Flask(__name__)

#
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
def get_population(place):
    query = f"SELECT state_pop FROM states WHERE state_name = '{place}'"
    

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

if __name__ == '__main__':
    my_port = 5115 # or 5215
    app.run(host='0.0.0.0', port = my_port) 