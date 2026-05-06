let isAdmin = false;

const toggle = document.getElementById("toggleRole");
const title = document.getElementById("title");
const desc = document.getElementById("desc");
const roleTitle = document.getElementById("roleTitle");
const infoText = document.getElementById("infoText");
const forgotLink = document.getElementById("forgotLink");

// =====================
// TOGGLE ROLE
// =====================
toggle.addEventListener("click", () => {
    isAdmin = !isAdmin;

    if (isAdmin) {
        title.innerHTML = "Halo <br> Administrator FMIPA 👋";
        desc.innerHTML = "SIPEKA adalah Sistem Informasi Kepribadian Mahasiswa yang dirancang khusus untuk mahasiswa FMIPA Universitas Udayana. Melalui platform ini, mahasiswa dapat mengenali tipe kepribadian diri mereka, apakah termasuk Extrovert, Introvert, atau Ambivert secara mudah, cepat, dan akurat.";

        roleTitle.innerHTML = "SIPEKA (Administrator)";
        toggle.innerHTML = "Masuk sebagai Mahasiswa";

        // HILANGKAN TEXT
        infoText.innerHTML = "";

    } else {
        title.innerHTML = "Halo <br> Mahasiswa FMIPA 👋";
        desc.innerHTML = "SIPEKA adalah Sistem Informasi Kepribadian Mahasiswa yang dirancang khusus untuk mahasiswa FMIPA Universitas Udayana. Melalui platform ini, mahasiswa dapat mengenali tipe kepribadian diri mereka, apakah termasuk Extrovert, Introvert, atau Ambivert secara mudah, cepat, dan akurat.";

        roleTitle.innerHTML = "SIPEKA";
        toggle.innerHTML = "Masuk sebagai Administrator";

        // KEMBALIKAN TEXT + WA
        infoText.innerHTML = `
            Belum punya akun? 
            <a href="https://wa.me/62812312414" target="_blank" class="bold-text admin-link">
                Hubungi administrator kampus FMIPA.
            </a>
        `;
    }
});


forgotLink.addEventListener("click", function(e){
    e.preventDefault();
    alert("Fitur lupa password belum tersedia");
});