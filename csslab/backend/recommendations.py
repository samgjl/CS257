import requests
import backend.connection as connection

#! I'm doing this here to avoid the possibility of thr JavaScript code sharing my client secret.
#! Later, Nathaniel plans to get unique client IDs. Until then...

# Fetch a track from Spotify:
def getTrack(key: str, track_id: str):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = {"Authorization": f"Bearer {key}"}
    response = requests.get(url, headers = headers).json()
    return {'track': response}

# Fetch the track's audio_features from Spotify
def getAudioFeatures(key: str, features_id: str):
    url = f"https://api.spotify.com/v1/audio-features/{features_id}"
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

# Get recommendations based on the track's audio features
def getRecommendations(body: dict):
    af = [float(f) for f in body['audio_features']]
    id = body['id']
    key = connection.getKey()
    _, cur = connection.getConnection()
    cur.execute(f"""
                SELECT audio_feature_id FROM audio_features WHERE
                acousticness BETWEEN {af[0]-0.05} AND {af[0]+0.05} AND
                danceability BETWEEN {af[1]-0.05} AND {af[1]+0.05} AND
                energy BETWEEN {af[2]-0.05} AND {af[2]+0.05} AND
                instrumentalness BETWEEN {af[3]-0.05} AND {af[3]+0.05} AND
                key BETWEEN {af[4]-1} AND {af[4]+1} AND
                liveness BETWEEN {af[5]-0.05} AND {af[5]+0.05} AND
                loudness BETWEEN {af[6]-5} AND {af[6]+5} AND
                mode = {af[7]} AND
                speechiness BETWEEN {af[8]-0.05} AND {af[8]+0.05} AND
                tempo BETWEEN {af[9]-10} AND {af[9]+10} AND
                time_signature = {af[10]} AND
                valence BETWEEN {af[11]-0.05} AND {af[11]+0.05} AND
                audio_feature_id != '{id}'
                LIMIT 10;
                """)
    recs = [r[0] for r in cur.fetchall()]
    
    # If there are no recommendations, get recommendations from Spotify:
    if len(recs) == 0:
        url = f"https://api.spotify.com/v1/recommendations?seed_tracks={id}&limit=10"
        headers = {"Authorization": f"Bearer {key}"}
        response = requests.get(url, headers = headers).json()
        recs = [r['id'] for r in response['tracks']]
    
    tracks = requests.get(
        f"https://api.spotify.com/v1/tracks?ids={','.join(recs)}",
        headers = {"Authorization": f"Bearer {key}"}        
    ).json()
    
    for track in tracks['tracks']:
        feat = requests.get(
            f"https://api.spotify.com/v1/audio-features/{track['id']}",
            headers = {"Authorization": f"Bearer {key}"}
        ).json()
        track['audio_features'] = [
            feat['acousticness'],
            feat['danceability'], 
            feat['energy'], 
            feat['instrumentalness'],
            feat['key'], 
            feat['liveness'], 
            feat['loudness'], 
            feat['mode'],
            feat['speechiness'], 
            feat['tempo'],
            feat['time_signature'],
            feat['valence']
        ]
        
    return {"recommendations": tracks['tracks']}