CREATE TABLE albums (id text, 
    name text, 
    album_group text, 
    album_type text, 
    release_date bigint, 
    popularity bigint
);

CREATE TABLE artists (
    name text, 
    id text, 
    popularity bigint, 
    followers bigint
);

CREATE TABLE audio_features (
    id text, 
    acousticness real, 
    analysis_url text, 
    danceability real, 
    duration real, 
    energy real, 
    instrumentalness real, 
    key integer, 
    liveness real, 
    loudness real, 
    mode integer,
    speechiness real, 
    tempo real, 
    time_signature integer, 
    valence real
);

CREATE TABLE genres (
    id text
);

CREATE TABLE r_albums_artists (
    album_id text, 
    artist_id text
);

CREATE TABLE r_albums_tracks (
    album_id text, 
    track_id text
);

CREATE TABLE r_artist_genre (
    genre_id text, 
    artist_id text
);

CREATE TABLE r_track_artist (
    track_id text, 
    artist_id text
);

CREATE TABLE tracks (
    id text, 
    disc_number integer, 
    duration integer, 
    explicit integer, 
    audio_feature_id text, 
    name text, 
    preview_url text, 
    track_number integer, 
    popularity bigint, 
    is_playable integer
);
