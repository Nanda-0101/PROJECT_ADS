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
        fetch('/admin/admin_navigasi.html')
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

let profilAdmin = {
    nama: "Dr. Andhika Pratamuy, S.Kom, M.Cs",
    nip: "198501012010121003",
    email: "andhi.pratam67@unud.ac.id",
    fullFakultas: "Matematika dan Ilmu Pengetahuan Alam"
};

// ========== HELPER FUNCTIONS ==========
function updateStatistik() {
    const totalMhsEl = document.getElementById('statTotalMahasiswa');
    const totalTesEl = document.getElementById('statTotalTes');
    
    if(totalMhsEl) totalMhsEl.innerText = mahasiswaList.length;
    if(totalTesEl) totalTesEl.innerText = riwayatTesList.length;
    
    if (riwayatTesList.length > 0) {
        let counts = {};
        let dominan = "";
        let maxCount = 0;

        riwayatTesList.forEach(t => {
            let status = t.status;
            counts[status] = (counts[status] || 0) + 1;
            
            if (counts[status] > maxCount) {
                maxCount = counts[status];
                dominan = status;
            }
        });

        const elDominan = document.getElementById('statTipeDominan');
        if (elDominan) elDominan.innerText = dominan;
    } else {
        const elDominan = document.getElementById('statTipeDominan');
        if (elDominan) elDominan.innerText = "-";
    }
}

function renderRiwayatTable() {
    let tbody = document.querySelector('#riwayatTable tbody');
    if(!tbody) return;
    
    tbody.innerHTML = '';
    riwayatTesList.forEach((item, idx) => {
        let statusClass = item.status.toLowerCase(); 
        
        let row = `
            <tr>
                <td>${idx+1}</td>
                <td class="col-nim">${item.nim}</td>
                <td>${item.nama}</td>
                <td>${item.prodi}</td>
                <td>${item.tanggal}</td>
                <td><strong>${item.skor}</strong></td>
                <td><span class="status-badge ${statusClass}">${item.status}</span></td>
                <td class="text-center">
                    <button type="button" class="btn-detail-riwayat btn-lihat-detail" data-id="${item.id}">Detail</button>
                </td>
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
    if(!tbody) return;
    
    tbody.innerHTML = '';
    mahasiswaList.forEach((m, index) => {
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

    // Event listener untuk tombol yang digambar dinamis oleh JS
    document.querySelectorAll('.btn-hapus-mhs').forEach(btn => {
        btn.addEventListener('click', (e) => {
            bukaModalHapusStatis(btn.getAttribute('data-id'));
        });
    });
} 

function bukaModalHapusStatis(idMahasiswa) {
    idMahasiswaYangAkanDihapus = parseInt(idMahasiswa);
    
    const modalTitle = document.querySelector('#logoutModal .modal-title');
    const modalBody = document.querySelector('#logoutModal .modal-body');
    const confirmBtn = document.getElementById('confirmLogoutBtn');
    
    if(modalTitle) modalTitle.innerText = "Konfirmasi Hapus";
    if(modalBody) modalBody.innerText = "Apakah Anda yakin ingin menghapus data mahasiswa ini?";
    if(confirmBtn) {
        confirmBtn.innerText = "Hapus";
        confirmBtn.className = "btn btn-danger";
    }
    
    let modalElement = document.getElementById('logoutModal');
    if (modalElement) {
        let modalHapus = new bootstrap.Modal(modalElement);
        modalHapus.show();
    }
}

// Tambah mahasiswa
function tambahMahasiswa(nim, nama, password) {
    let newId = mahasiswaList.length > 0 ? Math.max(...mahasiswaList.map(m => m.id)) + 1 : 1;
    mahasiswaList.push({ id: newId, nim, nama, prodi: "Informatika", password });
    renderKelolaTable();
    updateStatistik();
}

// ========== NAVIGASI ==========
let currentPage = 'dashboard';

function showPage(pageId) {
    document.querySelectorAll('[id^="page-"]').forEach(el => el.classList.add('hidden'));
    const targetPage = document.getElementById(`page-${pageId}`);
    if(targetPage) targetPage.classList.remove('hidden');
    
    currentPage = pageId;

    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('data-page') === pageId) link.classList.add('active');
    });

    if (pageId === 'riwayat') renderRiwayatTable();
    if (pageId === 'kelola') renderKelolaTable();
    if (pageId === 'dashboard') updateStatistik();
    if (pageId === 'profil') updateProfilUI();
}

function updateProfilUI() {
    if(document.getElementById('profilNama')) document.getElementById('profilNama').innerText = profilAdmin.nama;
    if(document.getElementById('profilNip')) document.getElementById('profilNip').innerText = profilAdmin.nip;
    if(document.getElementById('profilEmail')) document.getElementById('profilEmail').innerText = profilAdmin.email;
    if(document.getElementById('profilFakultas')) document.getElementById('profilFakultas').innerText = profilAdmin.fullFakultas;
    if(document.getElementById('headerNip')) document.getElementById('headerNip').innerText = `NIP ${profilAdmin.nip}`;
}

function editProfil(nama, nip, email, fakultas) {
    profilAdmin.nama = nama;
    profilAdmin.nip = nip;
    profilAdmin.email = email;
    profilAdmin.fullFakultas = fakultas;
    updateProfilUI();
}

// ========== EVENT LISTENERS ==========
document.addEventListener('DOMContentLoaded', () => {
    renderKelolaTable();
    renderRiwayatTable();
    showPage('dashboard');

    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            let page = link.getAttribute('data-page');
            if (page) showPage(page);
        });
    });

    document.querySelectorAll('.btn-action').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            let page = btn.getAttribute('data-page');
            if (page) showPage(page);
        });
    });

    const btnTambahMhs = document.getElementById('btnTambahMahasiswa');
    if(btnTambahMhs) {
        btnTambahMhs.addEventListener('click', () => {
            document.getElementById('nimBaru').value = '';
            document.getElementById('namaBaru').value = '';
            document.getElementById('passwordBaru').value = '';
            let modal = new bootstrap.Modal(document.getElementById('modalTambahMahasiswa'));
            modal.show();
        });
    }

   const formTambahMhs = document.getElementById('formTambahMahasiswa');
if(formTambahMhs) {
    formTambahMhs.addEventListener('submit', (e) => {
        e.preventDefault();
        let nim = document.getElementById('nimBaru').value.trim();
        let nama = document.getElementById('namaBaru').value.trim();
        let password = document.getElementById('passwordBaru').value.trim();
        if (nim && nama && password) {
            tambahMahasiswa(nim, nama, password);
            formTambahMhs.classList.add('d-none');
            const successBox = document.getElementById('successBox');
            if(successBox) {
                successBox.classList.remove('d-none');
            }
            
            formTambahMhs.reset();
        } else {
            alert('Semua field harus diisi!');
        }
    });
}

const modalTambahMhsElement = document.getElementById('modalTambahMahasiswa');
if(modalTambahMhsElement) {
    modalTambahMhsElement.addEventListener('hidden.bs.modal', () => {
        if(formTambahMhs) formTambahMhs.classList.remove('d-none');
        const successBox = document.getElementById('successBox');
        if(successBox) successBox.classList.add('d-none');
    });
}

    // Edit profil admin
    const editProfilBtn = document.getElementById('editProfilBtn');
    if(editProfilBtn) {
        editProfilBtn.addEventListener('click', () => {
            document.getElementById('editNama').value = profilAdmin.nama;
            document.getElementById('editNip').value = profilAdmin.nip;
            document.getElementById('editEmail').value = profilAdmin.email;
            document.getElementById('editFakultas').value = profilAdmin.fullFakultas;
            let modal = new bootstrap.Modal(document.getElementById('modalEditProfil'));
            modal.show();
        });
    }

    const formEditProfil = document.getElementById('formEditProfil');
    if(formEditProfil) {
        formEditProfil.addEventListener('submit', (e) => {
            e.preventDefault();
            let nama = document.getElementById('editNama').value.trim();
            let nip = document.getElementById('editNip').value.trim();
            let email = document.getElementById('editEmail').value.trim();
            let fakultas = document.getElementById('editFakultas').value.trim();
            if (nama && nip && email && fakultas) {
                editProfil(nama, nip, email, fakultas);
                let modal = bootstrap.Modal.getInstance(document.getElementById('modalEditProfil'));
                if(modal) modal.hide();
                alert('Profil berhasil diperbarui!');
            } else {
                alert('Semua field harus diisi!');
            }
        });
    }

    const ubahSandiBtn = document.getElementById('ubahSandiBtn');
    if (ubahSandiBtn) {
        ubahSandiBtn.addEventListener('click', function(e) {
            e.preventDefault();
            const iosModalElement = document.getElementById('modalUbahSandiIos');
            const iosModal = new bootstrap.Modal(iosModalElement);
            document.getElementById('iosNewPassword').value = '';
            iosModal.show();
        });
    }

    const btnSimpanSandiIos = document.getElementById('btnSimpanSandiIos');
    if (btnSimpanSandiIos) {
        btnSimpanSandiIos.addEventListener('click', function() {
            const passwordBaru = document.getElementById('iosNewPassword').value;
            if (passwordBaru.trim() === "") {
                alert("Kata sandi tidak boleh kosong!");
                return;
            }
            const iosModalElement = document.getElementById('modalUbahSandiIos');
            const modalInstance = bootstrap.Modal.getInstance(iosModalElement);
            if (modalInstance) modalInstance.hide();
            
            setTimeout(() => {
                const suksesModalElement = document.getElementById('modalSuksesSandiIos');
                const suksesModal = new bootstrap.Modal(suksesModalElement);
                suksesModal.show();
            }, 400);
        });
    }

    const logoutBtn = document.getElementById('logoutBtn');
    if(logoutBtn) {
        logoutBtn.addEventListener('click', () => {
            idMahasiswaYangAkanDihapus = null; 
            const modalTitle = document.querySelector('#logoutModal .modal-body h5');
            if(modalTitle) modalTitle.innerText = "Apakah Anda yakin ingin melakukan logout?";
            
            let modal = new bootstrap.Modal(document.getElementById('logoutModal'));
            modal.show();
        });
    }

    const confirmLogoutBtn = document.getElementById('confirmLogoutBtn');
    if(confirmLogoutBtn) {
        confirmLogoutBtn.addEventListener('click', () => {
            if (idMahasiswaYangAkanDihapus !== null) {
                mahasiswaList = mahasiswaList.filter(m => m.id !== idMahasiswaYangAkanDihapus);
                
                renderKelolaTable();
                updateStatistik();
                
                let modalElement = document.getElementById('logoutModal');
                let modalInstance = bootstrap.Modal.getInstance(modalElement);
                if(modalInstance) modalInstance.hide();
                idMahasiswaYangAkanDihapus = null;
            } else {
                window.location.href = "/logout"; 
            }
        });
    }
});