
// Makes an HTML element from the song ID
// @param {string} track_id - the Spotify ID of the song
// @return {HTMLElement} - the HTML element of the song
async function embedSpotifyPlayer(track_id) {
    let iframe = document.createElement('div');
    iframe.innerHTML = `
        <iframe class="spotify-embed" 
            style="border-radius:12px; float: center;"
            scrolling-attribute: scrolling="no"
            src="https://open.spotify.com/embed/track/${track_id}?utm_source=generator" 
            width="50%" 
            height="75" 
            frameBorder="0" 
            allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
            loading="lazy">
        </iframe>
    `;
    return iframe;
}

function getTrackColor(img, div) {
    let colorThief = new ColorThief();
    let color = colorThief.getColor(img);
    if (color[0] + color[1] + color[2] >= 450) {
        div.querySelector(".track").style.color = "black";
        div.querySelector(".artist").style.color = "black";
    }
    // div.style.backgroundColor = `rgb(${color[0]}, ${color[1]}, ${color[2]})`;
    div.style.background = `linear-gradient(90deg, 
        rgb(${color[0]}, ${color[1]}, ${color[2]}) 0%, 
        rgb(${color[0]}, ${color[1]}, ${color[2]}) 50%, 
        #191414 80%)`;
    return color;
}

/* Build a track manually (no embedding)
    * @param {Object} track - the track object
    * @param {array} audio_features - the audio features object
    * @return {HTMLElement} - the HTML element of the track

*/
async function buildTrackHTML(track, features) {
    let name = track.name;
    let artist = track.artists[0].name;
    let image_src = track.album.images[0].url;
    let div = document.createElement('div');
    let keys = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"];

    for (let i = 0; i < features.length; i++) {
        try {
            features[i] = parseFloat(features[i]).toFixed(3);
        } catch {
            features[i] = "???";
        }
    }

    div.setAttribute('class', 'spotify-embed');
    div.innerHTML = `
        <img src="${image_src}" class="spotify-logo" crossorigin='anonymous'>
        <div class="track-artist">
            <a class="track" href="/track?id=${track['id']}">${name}</a>
            <a class="artist" href="${track.artists[0].external_urls.spotify}" target="_blank">${artist}</a>
        </div>
        <div class="audio_features">
            <div class="heatmap" id="acousticness" style="background-color: hsl(${(1.0 - features[0]) * 360}, 100%, 50%)">
                <div class="popup">
                    <b>Acousticness</b><br>${features[0]}
                </div>
            </div>
            <div class="heatmap" id="danceability" style="background-color: hsl(${(1.0 - features[1]) * 360}, 100%, 50%)">
                <div class="popup">
                    <b>Danceability</b><br>${features[1]}
                </div>
            </div>
            <div class="heatmap" id="energy" style="background-color: hsl(${(1.0 - features[2]) * 360}, 100%, 50%)">
                <div class="popup">
                    <b>Energy</b><br>${features[2]}
                </div>
            </div>
            <div class="heatmap" id="instrumentalness" style="background-color: hsl(${(1.0 - features[3]) * 360}, 100%, 50%)">
                <div class="popup">
                    <b>Instrumentalness</b><br>${features[3]}
                </div>
            </div>
            <div class="heatmap" id="key" style="background-color: hsl(${(1.0 - features[4]/11) * 360}, 100%, 50%)">
                <div class="popup">
                    <b>Key</b><br>${keys[parseInt(features[4])]}
                </div>
            </div>
            <div class="heatmap" id="liveliness" style="background-color: hsl(${(1.0 - features[5]) * 360}, 100%, 50%)">
                <div class="popup">
                    <b>Liveliness</b><br>${features[5]}
                </div>
            </div>
            <div class="heatmap" id="loudness" style="background-color: hsl(${(1.0 - features[6]/-60) * 360}, 100%, 50%)">
                <div class="popup">
                    <b>Loudness</b><br>${features[6]} DB
                </div>
            </div>
            <div class="heatmap" id="mode" style="background-color: hsl(${(1.0 - features[7]/2) * 360}, 100%, 50%)">
                <div class="popup">
                    <b>Mode</b><br>${["Minor", "Major"][parseInt(features[7])]}
                </div>
            </div>
            <div class="heatmap" id="speechiness" style="background-color: hsl(${(1.0 - features[8]) * 360}, 100%, 50%)">
                <div class="popup">
                    <b>Speechiness</b><br>${features[8]}
                </div>
            </div>
            <div class="heatmap" id="tempo" style="background-color: hsl(${(1.0 - features[9]/250) * 360}, 100%, 50%)">
                <div class="popup">
                    <b>Tempo</b><br>${features[9]} BPM
                </div>
            </div>
            <div class="heatmap" id="time_signature" style="background-color: hsl(${(1.0 - features[10]/7) * 360}, 100%, 50%)">
                <div class="popup">
                    <b>Time Signature</b><br>${parseInt(features[10])}/4
                </div>
            </div>
            <div class="heatmap" id="valence" style="background-color: hsl(${(1.0 - features[11]) * 360}, 100%, 50%)">
                <div class="popup">
                    <b>Valence</b><br>${features[11]}
                </div>
            </div>
        </div>`;

        // Set up a dummy image to grab color:
        let img = div.querySelector("img");
        img.src = track['album']['images'][0]['url'];
        img.setAttribute("crossorigin", "anonymous");
        if (img.complete) {
            getTrackColor(img, div);
        } else {
            img.addEventListener('load', () => getTrackColor(img, div));
        }

    return div;
}