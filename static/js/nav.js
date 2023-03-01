const createNav = () => {
    let nav = document.querySelector('.navbar');

    nav.innerHTML = `
        <div class="nav">
            <img src="{{ url_for('static', filename='images/dark-logo.png')}}" class="brand-logo" alt="">

        <ul class="links-container">
            <li class="link-item"><a href="/home" class="link">home</a></li>
            <li class="link-item"><a href="/women" class="link">women</a></li>
            <li class="link-item"><a href="/men1" class="link">men</a></li>
            <li class="link-item"><a href="/guidelines" class="link">guidelines</a></li>
            <li class="link-item"><a href="/contact" class="link">contact</a></li>
        </ul>
        </div>
    `;
}

createNav();