class NavBar extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        this.innerHTML = `
        <nav class="navbar">
            <a id="index" href="./"> <img src="static/img/schiller_logo.png"><span>Schillify</span> </a>
            <a id="search" class='nav-item' href="./search">Search</a>
            <a id="smart_shuffle" class='nav-item' href="./smart_shuffle">Smart Shuffle</a>
            <a id="recommendations" class='nav-item' href="./recommendations">Recommendations</a>
            <a id="about" class='nav-item' href="./about">About </a>
            <a id="github" class='nav-item' href="https://github.com/nli00/CS257Final" target="_blank">GitHub <i class="fa fa-external-link" style="font-size:16px"></i></a>
            <button id="connect" class='connect' href="./login"> <img src="static/img/spotify_black.png"> <span style="font-size: large">Connect Spotify</span></button>
        </nav>`;
    }
}

customElements.define('nav-bar', NavBar);