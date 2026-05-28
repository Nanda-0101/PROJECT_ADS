const requiredIds = [
    'page-dashboard', 'page-riwayat', 'page-kelola', 'page-profil', 
    'statTotalMahasiswa', 'statTotalTes', 'statTipeDominan', 
    'kelolaTable', 'riwayatTable', 'btnTambahMahasiswa', 
    'formTambahMahasiswa', 'nimBaru', 'namaBaru', 'passwordBaru', 
    'detailTesBody', 'editProfilBtn', 'formEditProfil', 
    'editNama', 'editUsername', 'editEmail', 'editFakultas', 'editNip',
    'ubahSandiBtn', 'profilNama', 'profilNip', 'profilEmail', 'profilFakultas',
    'logoutBtn', 'confirmLogoutBtn', 'headerNip', 'modalEditProfil', 'modalTambahMahasiswa', 'modalDetailTes', 'logoutModal'
];

requiredIds.forEach(id => {
    if (!document.getElementById(id)) {
        let dummyEl = document.createElement('div');
        dummyEl.id = id;
        dummyEl.style.display = 'none';
        document.body.appendChild(dummyEl);
    }
});

let idMahasiswaYangAkanDihapus = null;
document.addEventListener("DOMContentLoaded", function() {
    const sidebarContainer = document.getElementById('sidebar-container');
    if (sidebarContainer) {
        fetch('/api/navigasi')
            .then(response => response.text())
            .then(html => {
                sidebarContainer.innerHTML = html;
                document.querySelectorAll('.nav-link').forEach(link => {
                    link.addEventListener('click', function(e) {
                        e.stopImmediatePropagation();
                        window.location.href = this.getAttribute('href');
                    });
                });
            })
            .catch(err => console.error('Gagal memuat sidebar:', err));
    }

    function TampilkanHalamanJikaAsli(pageId) {
        let p = document.getElementById(pageId);
        if (p) {
            const apakahDummy = p.parentElement === document.body;
            if (!apakahDummy) {
                p.classList.remove('hidden');
                p.style.display = 'block';
                return true;
            }
        }
        return false;
    }

    if (TampilkanHalamanJikaAsli('page-profil')) {
        console.log('Halaman Profil Aktif');
    } else if (TampilkanHalamanJikaAsli('page-dashboard')) {
        console.log('Halaman Dashboard Aktif');
    } else if (TampilkanHalamanJikaAsli('page-riwayat')) {
        console.log('Halaman Riwayat Aktif');
    } else if (TampilkanHalamanJikaAsli('page-kelola')) {
        console.log('Halaman Kelola Aktif');
    }
});

// ========== DATA DUMMY ==========
let mahasiswaList = [
    { id: 1, nim: "2508561140", nama: "Anak Agung Nanda Aditya", prodi: "Informatika", password: "pass123" },
    { id: 2, nim: "2409123001", nama: "Budi Santoso", prodi: "Matematika", password: "pass123" },
    { id: 3, nim: "2501012004", nama: "Cynthia Dewi", prodi: "Fisika", password: "pass123" },
    { id: 4, nim: "2103124509", nama: "Dian Pramana", prodi: "Kimia", password: "pass123" }
];

let riwayatTesList = [
    { id: 1, nim: "2508561140", nama: "Anak Agung Nanda Aditya", prodi: "Informatika", tanggal: "10 Maret 2025", skor: 85, status: "Introvert" },
    { id: 2, nim: "2409123001", nama: "Budi Santoso", prodi: "Matematika", tanggal: "14 Maret 2025", skor: 78, status: "Introvert" },
    { id: 3, nim: "2501012004", nama: "Cynthia Dewi", prodi: "Fisika", tanggal: "20 Maret 2025", skor: 62, status: "Ambivert" },
    { id: 4, nim: "2103124509", nama: "Dian Pramana", prodi: "Kimia", tanggal: "5 April 2025", skor: 45, status: "Ambivert" },
    { id: 5, nim: "2508561140", nama: "Anak Agung Nanda Aditya", prodi: "Informatika", tanggal: "12 April 2025", skor: 92, status: "Extrovert" }
];

// Data profil admin
let profilAdmin = {
    nama: "Dr. Andhika Pratamuy, S.Kom, M.Cs",
    nip: "198501012010121003",
    email: "andhi.pratam67@unud.ac.id",
    fakultas: "Matematika dan Ilmu Pengetahuan Alam"
};

// ========== HELPER FUNCTIONS ==========
function updateStatistik() {
    document.getElementById('statTotalMahasiswa').innerText = mahasiswaList.length;
    document.getElementById('statTotalTes').innerText = riwayatTesList.length;
    
    if (riwayatTesList.length > 0) {
        let counts = {};
        let dominan = "";
        let maxCount = 0;

        riwayatTesList.forEach(t => {
            let status = t.status; // Mengambil "Introvert", "Extrovert", dll
            counts[status] = (counts[status] || 0) + 1;
            
            if (counts[status] > maxCount) {
                maxCount = counts[status];
                dominan = status;
            }
        });

        const elDominan = document.getElementById('statTipeDominan');
        if (elDominan) {
            elDominan.innerText = dominan;
        }
    } else {
        // Jika data tes kosong
        const elDominan = document.getElementById('statTipeDominan');
        if (elDominan) elDominan.innerText = "-";
    }
}

function renderRiwayatTable() {
    let tbody = document.querySelector('#riwayatTable tbody');
    tbody.innerHTML = '';
    riwayatTesList.forEach((item, idx) => {
        let statusClass = '';
        if (item.status === 'Lulus') statusClass = 'status-lulus';
        else if (item.status === 'Gagal') statusClass = 'status-gagal';
        else statusClass = 'status-retest';
        let row = `
            <tr>
                <td>${idx+1}</td>
                <td>${item.nim}</td>
                <td>${item.nama}</td>
                <td>${item.prodi}</td>
                <td>${item.tanggal}</td>
                <td><strong>${item.skor}</strong></td>
                <td><span class="status-badge ${statusClass}">${item.status}</span></td>
                <td class="text-center"><button class="btn btn-sm btn-outline-primary btn-lihat-detail" data-id="${item.id}">Detail</button></td>
            </tr>
        `;
        tbody.innerHTML += row;
    });
    document.querySelectorAll('.btn-lihat-detail').forEach(btn => {
        btn.addEventListener('click', (e) => {
            let id = parseInt(btn.getAttribute('data-id'));
            let tes = riwayatTesList.find(t => t.id === id);
            if (tes) {
                document.getElementById('detailTesBody').innerHTML = `
                    <p><strong>NIM:</strong> ${tes.nim}</p>
                    <p><strong>Nama:</strong> ${tes.nama}</p>
                    <p><strong>Prodi:</strong> ${tes.prodi}</p>
                    <p><strong>Tanggal:</strong> ${tes.tanggal}</p>
                    <p><strong>Skor:</strong> ${tes.skor}</p>
                    <p><strong>Status:</strong> ${tes.status}</p>
                `;
                let modalDetail = new bootstrap.Modal(document.getElementById('modalDetailTes'));
                modalDetail.show();
            }
        });
    });
}

function renderKelolaTable() {
    let tbody = document.querySelector('#kelolaTable tbody');
    tbody.innerHTML = '';
    mahasiswaList.forEach((m, index) => {
        // Format ID menjadi 3 digit (001, 002...)
        let displayId = String(index + 1).padStart(3, '0');
        
        let row = `
            <tr>
                <td>${displayId}</td>
                <td class="col-nim">${m.nim}</td>
                <td>${m.nama}</td>
                <td>
                    <button class="btn-hapus-custom btn-hapus-mhs" data-id="${m.id}">Hapus</button>
                </td>
            </tr>
        `;
        tbody.innerHTML += row;
    });

    document.querySelectorAll('.btn-hapus-mhs').forEach(btn => {
        btn.addEventListener('click', (e) => {
            let id = parseInt(btn.getAttribute('data-id'));
            if (confirm('Yakin ingin menghapus mahasiswa ini?')) {
                mahasiswaList = mahasiswaList.filter(m => m.id !== id);
                renderKelolaTable();
                updateStatistik();
            }
        });
    });
}

function renderRiwayatTable() {
    let tbody = document.querySelector('#riwayatTable tbody');
    tbody.innerHTML = '';
    riwayatTesList.forEach((item, idx) => {
        let row = `
            <tr>
                <td>${idx+1}</td>
                <td class="col-nim">${item.nim}</td>
                <td>${item.nama}</td>
                <td>${item.prodi}</td>
                <td>${item.tanggal}</td>
                <td>${item.skor}</td>
                <td>${item.status}</td>
                <td><button class="btn btn-sm btn-dark btn-lihat-detail" data-id="${item.id}">Detail</button></td>
            </tr>
        `;
        tbody.innerHTML += row;
    });
}

// Tambah mahasiswa
function tambahMahasiswa(nim, nama, password) {
    let newId = mahasiswaList.length > 0 ? Math.max(...mahasiswaList.map(m => m.id)) + 1 : 1;
    mahasiswaList.push({ id: newId, nim, nama, prodi: "Belum diatur", password });
    renderKelolaTable();
    updateStatistik();
}

// ========== NAVIGASI ==========
let currentPage = 'dashboard';

function showPage(pageId) {
    document.querySelectorAll('[id^="page-"]').forEach(el => el.classList.add('hidden'));
    document.getElementById(`page-${pageId}`).classList.remove('hidden');
    currentPage = pageId;

    // Update active menu
    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('data-page') === pageId) link.classList.add('active');
    });

    // Render konten spesifik
    if (pageId === 'riwayat') renderRiwayatTable();
    if (pageId === 'kelola') renderKelolaTable();
    if (pageId === 'dashboard') updateStatistik();
    if (pageId === 'profil') updateProfilUI();
}

function updateProfilUI() {
    document.getElementById('profilNama').innerText = profilAdmin.nama;
    document.getElementById('profilNip').innerText = profilAdmin.nip;
    document.getElementById('profilEmail').innerText = profilAdmin.email;
    document.getElementById('profilFakultas').innerText = profilAdmin.fakultas;
    document.getElementById('headerNip').innerText = `NIP ${profilAdmin.nip}`;
}

function editProfil(nama, nip, email, fakultas) {
    profilAdmin.nama = nama;
    profilAdmin.nip = nip;
    profilAdmin.email = email;
    profilAdmin.fakultas = fakultas;
    updateProfilUI();
}

document.querySelectorAll('.nav-link, .btn-action').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        const targetPage = this.getAttribute('data-page');
        
        // Sembunyikan semua halaman
        document.querySelectorAll('main > div').forEach(div => {
            div.classList.add('hidden');
        });
        
        // Tampilkan halaman yang dipilih
        const activePage = document.getElementById('page-' + targetPage);
        if (activePage) {
            activePage.classList.remove('hidden');
        }
    });
});

// ========== EVENT LISTENERS ==========
document.addEventListener('DOMContentLoaded', () => {
    showPage('dashboard');

    // Navigasi menu
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            let page = link.getAttribute('data-page');
            if (page) showPage(page);
        });
    });

    // Tombol action di dashboard card
    document.querySelectorAll('.btn-action').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            let page = btn.getAttribute('data-page');
            if (page) showPage(page);
        });
    });

    // Tombol tambah mahasiswa
    document.getElementById('btnTambahMahasiswa').addEventListener('click', () => {
        document.getElementById('nimBaru').value = '';
        document.getElementById('namaBaru').value = '';
        document.getElementById('passwordBaru').value = '';
        let modal = new bootstrap.Modal(document.getElementById('modalTambahMahasiswa'));
        modal.show();
    });

    // Form tambah mahasiswa
    document.getElementById('formTambahMahasiswa').addEventListener('submit', (e) => {
        e.preventDefault();
        let nim = document.getElementById('nimBaru').value.trim();
        let nama = document.getElementById('namaBaru').value.trim();
        let password = document.getElementById('passwordBaru').value.trim();
        if (nim && nama && password) {
            tambahMahasiswa(nim, nama, password);
            let modal = bootstrap.Modal.getInstance(document.getElementById('modalTambahMahasiswa'));
            modal.hide();
            alert('Mahasiswa berhasil ditambahkan!');
        } else {
            alert('Semua field harus diisi!');
        }
    });

    // Edit profil
    document.getElementById('editProfilBtn').addEventListener('click', () => {
        document.getElementById('editNama').value = profilAdmin.nama;
        document.getElementById('editNip').value = profilAdmin.nip;
        document.getElementById('editEmail').value = profilAdmin.email;
        document.getElementById('editFakultas').value = profilAdmin.fakultas;
        let modal = new bootstrap.Modal(document.getElementById('modalEditProfil'));
        modal.show();
    });

    document.getElementById('formEditProfil').addEventListener('submit', (e) => {
        e.preventDefault();
        let nama = document.getElementById('editNama').value.trim();
        let nip = document.getElementById('editNip').value.trim();
        let email = document.getElementById('editEmail').value.trim();
        let fakultas = document.getElementById('editFakultas').value.trim();
        if (nama && nip && email && fakultas) {
            editProfil(nama, nip, email, fakultas);
            let modal = bootstrap.Modal.getInstance(document.getElementById('modalEditProfil'));
            modal.hide();
            alert('Profil berhasil diperbarui!');
        } else {
            alert('Semua field harus diisi!');
        }
    });

    // Ubah sandi (simulasi)
    document.getElementById('ubahSandiBtn').addEventListener('click', () => {
        let newPass = prompt('Masukkan kata sandi baru:');
        if (newPass && newPass.length >= 6) {
            alert('Kata sandi berhasil diubah (simulasi).');
        } else if (newPass) {
            alert('Kata sandi minimal 6 karakter.');
        }
    });

    // SHOW MODAL
    document.getElementById('logoutBtn').addEventListener('click', () => {
        let modal = new bootstrap.Modal(document.getElementById('logoutModal'));
        modal.show();
    });

    // CONFIRM LOGOUT
    document.getElementById('confirmLogoutBtn').addEventListener('click', () => {
        window.location.href = "/logout"; 
    });
});
