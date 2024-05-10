from flask import Flask, request, render_template, jsonify
import backend.connection as connection
import backend.recommendations as get_track

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

@app.route("/recommendations/", methods=["POST"])
def recommendations():
    body = request.get_json()
    return get_track.getRecommendations(body)

if __name__ == '__main__':
    my_port = 5215
    app.run(host='0.0.0.0', port = my_port, debug=True)
