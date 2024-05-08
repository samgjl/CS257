//+ Playlist Ordering: frontend
/*
    !Probloem: Must be used in conjunction with HTML import for the moment...
    <script src="https://cdnjs.cloudflare.com/ajax/libs/color-thief/2.3.0/color-thief.umd.js"></script>
*/

// import * as ColorThief from "https://cdnjs.cloudflare.com/ajax/libs/color-thief/2.3.0/color-thief.umd.js";

// Request the playlist order from the server
// @param {string} playlist_id - the Spotify ID of the playlist
// @param {string} start_id - the Spotify ID of the starting song
// @return {Promise} - the promise of the request
async function requestPlaylistOrder(playlist_id, start_id) {
    let order = await fetch(`/smart_shuffle/${playlist_id}/${start_id}`);
    let data = await order.json();
    return data;
}

/* Render the ordered playlist
    * @param {HTMLElement} parent - the parent element to which we append the playlist
    * @param {string} playlist_id - the Spotify ID of the playlist
    * @param {string} start_id - the Spotify ID of the starting song
    * @return {void}
*/
function renderOrderedPlaylist(parent, playlist_id, start_id) {
    requestPlaylistOrder(playlist_id, start_id).then( (data) => {
        let order = data.order;
        let playlist = data.playlist;
        let audio_features = data.audio_features;
        let thief = new ColorThief();

        for (let i = 0; i < order.length; i++) {
            // Get track in order:
            let id = order[i];
            buildTrackHTML(playlist[id], audio_features[id]).then((track) => {
                // Color the background
                let temp_img = track.querySelector("img");
                if (temp_img.complete) {
                    let bgkd = thief.getColor(temp_img, 10);
                    track.style.backgroundColor = `rgb(${bgkd[0]}, ${bgkd[1]}, ${bgkd[2]})`;
                    // If the color is too light, make the text black:
                    let text_color = (bgkd[0] + bgkd[1] + bgkd[2] > 500) ? "black" : "white";
                    track.style.color = text_color;
                    parent.appendChild(track);

                } else {
                    temp_img.addEventListener('load', function() {
                        let bgkd = thief.getColor(temp_img, 10);
                        track.style.backgroundColor = `rgb(${bgkd[0]}, ${bgkd[1]}, ${bgkd[2]})`;
                        // If the color is too light, make the text black:
                        let text_color = (bgkd[0] + bgkd[1] + bgkd[2] > 500) ? "black" : "white";
                        track.style.color = text_color;
                        parent.appendChild(track);
                    });
                }
            });
        }
    });
}