async function renderUpperTrack(id) {
    let content = document.getElementById("content");
    // Add the id to the URL's parameters:
    let url = new URL(window.location.href);
    url.searchParams.set('id', id);
    window.history.pushState({}, '', url);
    // Fetch the track and its features:
    let track = await fetch(`/track/${id}`).then(response => response.json());
    let features = await fetch(`/audio_features/${id}`).then(response => response.json());
    let trackElement = await buildUpperTrackHTML(track['track'], features['features']);
    content.appendChild(trackElement);
    // Background color:
    getColorAndSetBackground(track);
    // Recommendations:
    let spinner = renderLoadingSpinner()
    content.appendChild(spinner)
    let recommendations = await renderRecommendations(track['track'], features['features']);
    spinner.remove();
    content.appendChild(recommendations);
}

// Get a temporary loading spinner:
function renderLoadingSpinner() {
    let spinner = document.createElement('div');
    spinner.innerHTML = '<div class="lds-facebook"><div></div><div></div><div></div></div>';
    return spinner;
}

function renderSearchbar() {
    let searchbar = document.createElement('div');
    searchbar.className = 'searchbar';
    searchbar.innerHTML = `
        <div class="searchbar-container">
            <h1>Stats and Recommendations</h1>
            <h3>Input your favorite song below and we'll show you its audio features and some similar songs.</h3>
            <div class="searchbar">
                <input class="input" type="text" id="id_entry" placeholder="Paste in the URL of a Spotify track" value="">
                <button class="go" onclick="loadUpperTrack()">Search</button>
            </div>
        </div>`;
    return searchbar;
}

async function loadUpperTrack() {
    // Transfer to loading screen:
    let entry = document.getElementById('id_entry');
    let track_id = entry.value.split('/').pop().split('?')[0];
    entry.parentElement.parentElement.remove();
    let loading = document.querySelector('.lds-facebook');
    loading.style.display = "block";  
    // Render the track:
    renderUpperTrack(track_id);
    // Remove loader:
    loading.style.display = "none";
}

async function renderRecommendations(track, features) {
    let recommendations = document.createElement('div');
    recommendations.className = 'recommendations';
    recommendations.innerHTML = '<h2>Recommendations</h2>';
    let recs = await getRecommendations(track, features);
    for (let i = 0; i < recs.length; i++) {
        let rec = recs[i];
        let trackElement = await buildTrackHTML(rec, rec['audio_features']);
        trackElement.style.height = '66px';
        recommendations.appendChild(trackElement);
    }
    return recommendations;
}

async function getRecommendations(track, features) {
    let recs = await fetch("/recommendations", {
        method: "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify({
            audio_features: features,
            id: track['id'],
        })
    }).then((r) => r.json());
    return recs['recommendations'];
}


async function buildUpperTrackHTML(track, features) {
    let artistsHTML = '';
    for (let i = 0; i < track['artists'].length; i++) {
        artistsHTML += `<a class='a' href="${track['artists'][i]['external_urls']['spotify']}" target="_blank">
                        ${track['artists'][i]['name']}</a>
                        <div class="circle"></div>`;
    }
    // Get the runtime
    let date = new Date(track['duration_ms']);
    let duration = `${date.getMinutes()}:`;
    if (date.getSeconds() < 10) duration += '0';
    duration += date.getSeconds();

    let keys = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"];

    for (let i = 0; i < features.length; i++) {
        try {
            features[i] = parseFloat(features[i]).toFixed(3);
        } catch {
            features[i] = "???";
        }
    }

    let div = document.createElement('div');
    div.className = 'upper-track';
    div.innerHTML = `
        <img class="album-image" src="${track['album']['images'][0]['url']}" alt="Track Image" class="track-image">
        <div class="track-info">
            <a href="${track['external_urls']['spotify']}" target="_blank"><h1 class="a title">${track['name']}</h1></a>
            <div class="info">
                ${artistsHTML}
                <a>${track['album']['release_date'].split('-')[0]}</a>
                <div class="circle"></div>
                <a>${duration}</a>
                <div class="circle"></div>
                <a>Top ${100-track['popularity']}%</a>
            </div>
            <iframe
                style="border-radius:12px; float: center; height: 75px"
                scrolling-attribute: scrolling="no"
                src="https://open.spotify.com/embed/track/${track['id']}?utm_source=generator" 
                width="66%" 
                height="100%" 
                frameBorder="0" 
                allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
                loading="lazy">
            </iframe>
            <div class="audio-features-container">
                <h3>Audio Features</h3>
                <div class="audio-features">
                    <div id='acousticness' class="big-heatmap" style="background-color: hsl(${(1.0 - features[0]) * 360}, 100%, 50%)">
                        <div class="big-popup"><b>Acousticness</b><br>${features[0]}</div>
                    </div>
                    <div id='danceability' class="big-heatmap" style="background-color: hsl(${(1.0 - features[1]) * 360}, 100%, 50%)">
                        <div class="big-popup"><b>Danceability</b><br>${features[1]}</div>
                    </div>
                    <div id='energy' class="big-heatmap" style="background-color: hsl(${(1.0 - features[2]) * 360}, 100%, 50%)">
                        <div class="big-popup"><b>Energy</b><br>${features[2]}</div>
                    </div>
                    <div id='instrumentalness' class="big-heatmap" style="background-color: hsl(${(1.0 - features[3]) * 360}, 100%, 50%)">
                        <div class="big-popup"><b>Instrumentalness</b><br>${features[3]}</div>
                    </div>
                    <div id='key' class="big-heatmap" style="background-color: hsl(${(1.0 - features[4]/11) * 360}, 100%, 50%)">
                        <div class="big-popup"><b>Key</b><br>${keys[parseInt(features[4])]}</div>
                    </div>
                    <div id='liveness' class="big-heatmap" style="background-color: hsl(${(1.0 - features[5]) * 360}, 100%, 50%)">
                        <div class="big-popup"><b>Liveness</b><br>${features[5]}</div>
                    </div>
                    <div id='loudness' class="big-heatmap" style="background-color: hsl(${(1.0 - features[6]/-60) * 360}, 100%, 50%)">
                        <div class="big-popup"><b>Loudness</b><br>${features[6]} DB</div>
                    </div>
                    <div id='mode' class="big-heatmap" style="background-color: hsl(${(1.0 - features[7]/2) * 360}, 100%, 50%)">
                        <div class="big-popup"><b>Mode</b><br>${['Minor', 'Major'][parseInt(features[7])]}</div>
                    </div>
                    <div id='speechiness' class="big-heatmap" style="background-color: hsl(${(1.0 - features[8]) * 360}, 100%, 50%)">
                        <div class="big-popup"><b>Speechiness</b><br>${features[8]}</div>
                    </div>
                    <div id='tempo' class="big-heatmap" style="background-color: hsl(${(1.0 - features[9]/250) * 360}, 100%, 50%)">
                        <div class="big-popup"><b>Tempo</b><br>${features[9]}</div>
                    </div>
                    <div id='time_signature' class="big-heatmap" style="background-color: hsl(${(1.0 - features[10]/7) * 360}, 100%, 50%)">
                        <div class="big-popup"><b>Time Signature</b><br>${parseInt(features[10])}/4</div>
                    </div>
                    <div id='valence' class="big-heatmap" style="background-color: hsl(${(1.0 - features[11]) * 360}, 100%, 50%)">
                        <div class="big-popup"><b>Valence</b><br>${features[11]}</div>
                    </div>
                </div>
            </div>
        </div>`;
    return div;
}

function getBackgroundColor(img) {
    let colorThief = new ColorThief();
    let color = colorThief.getColor(img);
    document.body.style.background = `linear-gradient(0deg, #191414 25%, rgb(${color[0]}, ${color[1]}, ${color[2]}) 50%, rgb(${color[0]}, ${color[1]}, ${color[2]}) 66%, #191414 87.5%)`;
    if (color[0] + color[1] + color[2] >= 383) {
        document.body.style.color = "black";
    }
}

function getColorAndSetBackground(track) {
    let img = document.createElement("img");
    img.src = track['track']['album']['images'][0]['url'];
    img.setAttribute("crossorigin", "anonymous");
    if (img.complete) {
        getBackgroundColor(img);
    } else {
        img.addEventListener('load', () => getBackgroundColor(img));
    }
    img.remove();
}