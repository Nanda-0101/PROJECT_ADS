let isAdmin = false;

const toggle = document.getElementById("toggleRole");
const title = document.getElementById("title");
const desc = document.getElementById("desc");
const roleTitle = document.getElementById("roleTitle");
const infoText = document.getElementById("infoText");
const forgotLink = document.getElementById("forgotLink");

// TOGGLE ROLE LOGIN
toggle.addEventListener("click", () => {
    isAdmin = !isAdmin;

    if (isAdmin) {
        title.innerHTML = "Halo <br> Administrator FMIPA 👋";
        desc.innerHTML = "Sistem SIPEKA untuk admin mengelola data mahasiswa.";

        roleTitle.innerHTML = "SIPEKA (Administrator)";
        toggle.innerHTML = "Masuk sebagai Mahasiswa";

        infoText.innerHTML = "";

    } else {
        title.innerHTML = "Halo <br> Mahasiswa FMIPA 👋";
        desc.innerHTML = "SIPEKA membantu mahasiswa mengetahui kepribadian mereka.";

        roleTitle.innerHTML = "SIPEKA";
        toggle.innerHTML = "Masuk sebagai Administrator";

        infoText.innerHTML = `
            Belum punya akun? 
            <a href="https://wa.me/6285792764316" target="_blank">
                Hubungi administrator kampus FMIPA.
            </a>
        `;
    }
});

// FORGOT PASSWORD
forgotLink.addEventListener("click", function (e) {
    e.preventDefault();
    alert("Fitur lupa password belum tersedia");
});