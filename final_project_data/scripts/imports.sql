\copy albums FROM './csv/albums.csv' DELIMITER ';' CSV
\copy artists FROM './csv/artists.csv' DELIMITER ';' CSV
\copy audio_features FROM './csv/audio_features.csv' DELIMITER '|' CSV
\copy genres FROM './csv/genres.csv' DELIMITER '|' CSV
\copy r_albums_artists FROM './csv/r_albums_artists.csv' DELIMITER '|' CSV
\copy r_albums_tracks FROM './csv/r_albums_tracks.csv' DELIMITER '|' CSV
\copy r_track_artist FROM './csv/r_track_artist.csv' DELIMITER '|' CSV
\copy tracks FROM './csv/tracks.csv' DELIMITER '|' CSV