import requests

#! I'm doing this here to avoid the possibility of thr JavaScript code sharing my client secret.
#! Later, Nathaniel plans to get unique client IDs. Until then...

# Fetch a track from Spotify:
def getTrack(key, track_id):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = {"Authorization": f"Bearer {key}"}
    response = requests.get(url, headers = headers)    
    return {'track': response.json()}

# Fetch the track's audio_features from Spotify
def getAudioFeatures(key, track_id):
    url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    headers = {"Authorization": f"Bearer {key}"}
    response = requests.get(url, headers = headers)
    
    # Parse the audio features into an array:
    f = response.json()
    audio_features = [
        f['acousticness'],
        f['danceability'], 
        f['energy'], 
        f['instrumentalness'],
        f['key'], 
        f['liveness'], 
        f['loudness'], 
        f['mode'],
        f['speechiness'], 
        f['tempo'],
        f['time_signature'],
        f['valence']]
    return {"features": audio_features}
