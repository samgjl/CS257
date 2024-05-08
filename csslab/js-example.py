from flask import Flask
from flask import render_template
import connection
import track as get_track

app = Flask(__name__)

@app.route('/')
def welcome():
    message = "Welcome to My Example Webpage."
    message = message + " This text was produced by concatenating strings in Python!"
    return render_template("homepage.html", someText = message)


@app.route("/track")
def track():
    return render_template("track.html")

@app.route("/track/<track_id>")
def getTrack(track_id):
    key = connection.getKey()
    return get_track.getTrack(key, track_id)

@app.route("/audio_features/<track_id>")
def getAudioFeatures(track_id):
    key = connection.getKey()
    return get_track.getAudioFeatures(key, track_id)


if __name__ == '__main__':
    my_port = 5115
    app.run(host='0.0.0.0', port = my_port, debug=True)
