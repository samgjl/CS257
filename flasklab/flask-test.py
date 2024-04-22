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

@app.route("/add/<x>/<y>")
def add(x, y):
    x, y, = float(x), float(y) # cast to floats first in case they're decimal values
    z = x + y
    # is it an int?
    if z.is_integer():
        return int(z)
    return z

if __name__ == '__main__':
    my_port = 4090
    app.run(host='0.0.0.0', port = my_port) 