class CustomFooter extends HTMLElement {
    constructor() {
        super();
        // Add any initialization code here
    }

    connectedCallback() {
        this.innerHTML = `
        <footer>
            
            <div class="column">
                <ul> 
                    <li><a class='left' href="./">Home</a></li>
                    <li><a class='left' href="./search">Search</a></li>
                    <li><a class='left' href="./smart_shuffle">Smart Shuffle</a></li>
                    <li><a class='left' href="./recommendations">Recommendations</a></li>
                    <li><a class='left' href="./about">About</a></li>
                    <li><a class="left" href="https://github.com/nli100/CD257Final">Github <i class="fa fa-external-link"></i></a></li>
                </ul>
            </div>
            <div class="column">
                <ul>
                    <li><button class='open-spotify' onclick="location.href='https://open.spotify.com'"><img src="static/img/spotify_black.png"><span style="font-size: large">Open Spotify</span></button></li>
                </ul>
            </div>
        </footer>
        `;
    }

}

// Define the custom element
customElements.define('custom-footer', CustomFooter);