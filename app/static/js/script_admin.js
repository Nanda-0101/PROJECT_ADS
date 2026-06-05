const requiredIds = [
    'page-dashboard', 'page-riwayat', 'page-kelola', 'page-profil', 
    'statTotalMahasiswa', 'statTotalTes', 'statTipeDominan', 
    'kelolaTable', 'riwayatTable', 'btnTambahMahasiswa', 
    'formTambahMahasiswa', 'nimBaru', 'namaBaru', 'passwordBaru', 
    'detailTesBody', 'editProfilBtn', 'formEditProfil', 
    'editUsername', 'editEmail', 'editPassword',
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
function initAdminShell() {
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
}

window.initAdminShell = initAdminShell;

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAdminShell);
} else {
    initAdminShell();
}

// ========== DATA (loaded from backend) ==========
let mahasiswaList = [];
let riwayatTesList = [];
let profilAdmin = {};
let adminSummary = null;
let dashboardChart = null;

async function fetchJSON(url, options) {
    const res = await fetch(url, options);
    if (!res.ok) {
        const txt = await res.text().catch(() => '');
        throw new Error(`HTTP ${res.status} ${res.statusText} - ${txt}`);
    }
    return res.json();
}

function escapeHtml(value) {
    return String(value ?? '')
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');
}

async function loadMahasiswa() {
    try {
        mahasiswaList = await fetchJSON('/api/mahasiswa');
        renderKelolaTable();
        updateStatistik();
    } catch (e) {
        console.error('Gagal memuat mahasiswa:', e);
    }
}

async function loadRiwayat() {
    try {
        // normalize incoming riwayat data to avoid undefined fields
        const raw = await fetchJSON('/api/riwayat');
        riwayatTesList = raw.map(r => {
            return {
                id: Number(r.id ?? r.id_hasil ?? r.ID_Hasil ?? null),
                nim: r.nim ?? r.NIM ?? '-',
                nama: r.nama ?? r.Nama_Mahasiswa ?? '-',
                prodi: r.prodi ?? r.Prodi ?? '-',
                tanggal: r.tanggal ?? r.Tanggal ?? '-',
                skor: r.skor ?? r.Skor ?? '-',
                status: r.status ?? (r.id_jenis ? (r.id_jenis == 1 ? 'Introvert' : (r.id_jenis == 2 ? 'Ekstrovert' : 'Ambivert')) : 'Unknown')
            };
        });
        renderRiwayatTable();
        updateStatistik();
    } catch (e) {
        console.error('Gagal memuat riwayat:', e);
    }
}

async function loadAdminSummary() {
    try {
        adminSummary = await fetchJSON('/api/admin/summary');
        updateStatistik();
        renderDashboardSummaryChart();
    } catch (e) {
        console.error('Gagal memuat ringkasan admin:', e);
    }
}

async function loadAdminProfile() {
    try {
        const raw = await fetchJSON('/api/admin/profile');
        profilAdmin = {
            nama: raw.nama ?? raw.username ?? '-',
            username: raw.username ?? raw.nama ?? '-',
            nip: raw.nip ?? raw.id ?? '-',
            email: raw.email ?? '-',
            fullFakultas: raw.fullFakultas ?? raw.fakultas ?? 'Matematika dan Ilmu Pengetahuan Alam'
        };
        updateProfilUI();
    } catch (e) {
        console.error('Gagal memuat profil admin:', e);
    }
}

// ========== HELPER FUNCTIONS ==========
function updateStatistik() {
    const totalMhsEl = document.getElementById('statTotalMahasiswa');
    const totalTesEl = document.getElementById('statTotalTes');

    const totalMahasiswa = adminSummary && adminSummary.total_mahasiswa !== undefined ? Number(adminSummary.total_mahasiswa) : mahasiswaList.length;
    const totalTes = adminSummary && adminSummary.total_tes !== undefined ? Number(adminSummary.total_tes) : riwayatTesList.length;

    if(totalMhsEl) totalMhsEl.innerText = totalMahasiswa;
    if(totalTesEl) totalTesEl.innerText = totalTes;

    const elDominan = document.getElementById('statTipeDominan');
    if (elDominan) {
        elDominan.innerText = adminSummary && adminSummary.dominant ? adminSummary.dominant : getDominantStatusFromRiwayat();
    }
}

function getDominantStatusFromRiwayat() {
    if (!riwayatTesList.length) return '-';

    const counts = {};
    let dominant = '-';
    let maxCount = 0;

    riwayatTesList.forEach(t => {
        const status = t.status || 'Unknown';
        counts[status] = (counts[status] || 0) + 1;
        if (counts[status] > maxCount) {
            maxCount = counts[status];
            dominant = status;
        }
    });

    return dominant;
}

function renderDashboardSummaryChart() {
    const canvas = document.getElementById('chartKepribadianAdmin');
    if (!canvas || typeof Chart === 'undefined') return;

    const labels = ['Introvert', 'Ekstrovert', 'Ambivert'];
    const values = labels.map(label => Number(adminSummary?.by_type?.[label] || 0));
    const hasData = values.some(value => value > 0);

    const countIntrovert = document.getElementById('chartCountIntrovert');
    const countEkstrovert = document.getElementById('chartCountEkstrovert');
    const countAmbivert = document.getElementById('chartCountAmbivert');
    if (countIntrovert) countIntrovert.innerText = values[0];
    if (countEkstrovert) countEkstrovert.innerText = values[1];
    if (countAmbivert) countAmbivert.innerText = values[2];

    const emptyState = document.getElementById('chartEmptyState');
    if (emptyState) {
        emptyState.classList.toggle('d-none', hasData);
    }

    if (dashboardChart) {
        dashboardChart.destroy();
        dashboardChart = null;
    }

    if (!hasData) {
        return;
    }

    dashboardChart = new Chart(canvas.getContext('2d'), {
        type: 'doughnut',
        data: {
            labels,
            datasets: [{
                data: values,
                backgroundColor: ['#36A2EB', '#FF9F40', '#4BC0C0'],
                borderColor: '#ffffff',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '68%',
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        boxWidth: 14,
                        padding: 16,
                        font: {
                            family: 'Poppins, sans-serif',
                            size: 12
                        }
                    }
                }
            }
        }
    });
}

function renderRiwayatTable() {
    let tbody = document.querySelector('#riwayatTable tbody');
    if(!tbody) return;
    
    tbody.innerHTML = '';
    if (!riwayatTesList.length) {
        tbody.innerHTML = `
            <tr>
                <td colspan="8" class="py-4 text-muted">Belum ada data riwayat tes.</td>
            </tr>
        `;
        return;
    }

    riwayatTesList.forEach((item, idx) => {
        let status = item.status || 'Unknown';
        let statusClass = String(status).toLowerCase().replace(/\s+/g, '-');

        let row = `
            <tr>
                <td>${idx+1}</td>
                <td class="col-nim">${escapeHtml(item.nim)}</td>
                <td>${escapeHtml(item.nama)}</td>
                <td>${escapeHtml(item.prodi)}</td>
                <td>${escapeHtml(item.tanggal)}</td>
                <td><strong>${escapeHtml(item.skor)}</strong></td>
                <td><span class="status-badge ${statusClass}">${escapeHtml(status)}</span></td>
                <td class="text-center">
                    <button type="button" class="btn-detail-riwayat btn-lihat-detail" data-id="${item.id}">Detail</button>
                </td>
            </tr>
        `;
        tbody.innerHTML += row;
    });

    document.querySelectorAll('.btn-lihat-detail').forEach(btn => {
        btn.addEventListener('click', async () => {
            let id = parseInt(btn.getAttribute('data-id'));
            let tes = riwayatTesList.find(t => t.id === id);
            if (tes) {
                await loadDetailRiwayat(id, tes);
                let modalDetail = new bootstrap.Modal(document.getElementById('modalDetailTes'));
                modalDetail.show();
            }
        });
    });
}

function formatJawabanRiwayat(idSoal, jawaban) {
    const jawabanStr = String(jawaban ?? '-');
    if (idSoal === 1) {
        return jawabanStr === '1' ? 'Laki-laki' : jawabanStr === '2' ? 'Perempuan' : jawabanStr;
    }
    if (idSoal === 2) {
        return `${jawabanStr} tahun`;
    }

    const labelJawaban = {
        1: 'Sangat Tidak Setuju',
        2: 'Tidak Setuju',
        3: 'Netral',
        4: 'Setuju',
        5: 'Sangat Setuju'
    };

    const label = labelJawaban[Number(jawabanStr)];
    return label ? `${jawabanStr} - ${label}` : jawabanStr;
}

async function loadDetailRiwayat(idHasil, tesRingkas) {
    const body = document.getElementById('detailTesBody');
    if (!body) return;

    body.innerHTML = '<p class="text-muted mb-0">Memuat detail riwayat...</p>';

    try {
        const detail = await fetchJSON(`/api/riwayat/${idHasil}`);
        if (!detail.length) {
            body.innerHTML = '<p class="text-muted mb-0">Detail riwayat tidak ditemukan.</p>';
            return;
        }

        body.innerHTML = `
            <div class="mb-3">
                <p class="mb-1"><strong>NIM:</strong> ${escapeHtml(tesRingkas.nim)}</p>
                <p class="mb-1"><strong>Nama:</strong> ${escapeHtml(tesRingkas.nama)}</p>
                <p class="mb-1"><strong>Prodi:</strong> ${escapeHtml(tesRingkas.prodi)}</p>
                <p class="mb-1"><strong>Tanggal:</strong> ${escapeHtml(tesRingkas.tanggal)}</p>
                <p class="mb-0"><strong>Status:</strong> ${escapeHtml(tesRingkas.status)}</p>
            </div>
            <div class="table-responsive">
                <table class="table table-sm align-middle">
                    <thead>
                        <tr>
                            <th style="width: 60px;">No</th>
                            <th>Soal</th>
                            <th>Jawaban</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${detail.map((item, index) => `
                            <tr>
                                <td>${item.id_soal ?? index + 1}</td>
                                <td>${escapeHtml(item.pertanyaan)}</td>
                                <td>${escapeHtml(formatJawabanRiwayat(item.id_soal, item.jawaban))}</td>
                            </tr>
                        `).join('')}
                    </tbody>
                </table>
            </div>
        `;
    } catch (error) {
        console.error('Gagal memuat detail riwayat:', error);
        body.innerHTML = '<p class="text-danger mb-0">Gagal memuat detail riwayat.</p>';
    }
}

function renderKelolaTable() {
    let tbody = document.querySelector('#kelolaTable tbody');
    if(!tbody) return;
    
    tbody.innerHTML = '';
    if (!mahasiswaList.length) {
        tbody.innerHTML = `
            <tr>
                <td colspan="5" class="py-4 text-muted">Belum ada data mahasiswa.</td>
            </tr>
        `;
        return;
    }

    mahasiswaList.forEach((m, index) => {
        let displayId = String(index + 1).padStart(3, '0');
        let row = `
            <tr>
                <td>${displayId}</td>
                <td class="col-nim">${escapeHtml(m.nim)}</td>
                <td>${escapeHtml(m.nama)}</td>
                <td>${escapeHtml(m.prodi || '-')}</td>
                <td>
                    <button class="btn-edit btn-edit-mhs" data-id="${m.id}">Edit</button>
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
    // edit buttons
    document.querySelectorAll('.btn-edit-mhs').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const id = Number(btn.getAttribute('data-id'));
            const m = mahasiswaList.find(x => x.id === id);
            if (!m) return alert('Data mahasiswa tidak ditemukan');
            // reuse the tambah modal for editing
            document.getElementById('nimBaru').value = m.nim || '';
            document.getElementById('namaBaru').value = m.nama || '';
            const prodiInput = document.getElementById('prodiBaru');
            if (prodiInput) prodiInput.value = m.prodi || '';
            document.getElementById('passwordBaru').value = '';
            // store edit id on the form element
            const form = document.getElementById('formTambahMahasiswa');
            if (form) form.dataset.editId = String(id);
            const modal = new bootstrap.Modal(document.getElementById('modalTambahMahasiswa'));
            modal.show();
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
async function tambahMahasiswa(nim, nama, prodi, password) {
    await fetchJSON('/api/mahasiswa', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            NIM: nim,
            Nama_Mahasiswa: nama,
            Prodi: prodi,
            Password_Mahasiswa: password
        })
    });

    await loadMahasiswa();
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
    if (pageId === 'dashboard') {
        updateStatistik();
        loadAdminSummary();
    }
    if (pageId === 'profil') updateProfilUI();
}

function updateProfilUI() {
    if(document.getElementById('profilNama')) document.getElementById('profilNama').innerText = profilAdmin.username || profilAdmin.nama || '-';
    if(document.getElementById('profilUsername')) document.getElementById('profilUsername').innerText = profilAdmin.username || profilAdmin.nama || '-';
    if(document.getElementById('profilNip')) document.getElementById('profilNip').innerText = profilAdmin.nip || '-';
    if(document.getElementById('profilEmail')) document.getElementById('profilEmail').innerText = profilAdmin.email || '-';
    if(document.getElementById('profilFakultas')) document.getElementById('profilFakultas').innerText = profilAdmin.fullFakultas || 'Matematika dan Ilmu Pengetahuan Alam';
    if(document.getElementById('headerNip')) document.getElementById('headerNip').innerText = `Akun Admin: ${profilAdmin.username || '-'}`;
}

async function editProfil(username, email, password) {
    await fetchJSON('/api/admin/profile', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username,
            email,
            ...(password ? { password } : {})
        })
    });

    await loadAdminProfile();
}

// ========== EVENT LISTENERS ==========
document.addEventListener('DOMContentLoaded', () => {
    (async () => {
        await loadMahasiswa();
        await loadRiwayat();
        await loadAdminProfile();
        await loadAdminSummary();
    })();

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
            const prodiInput = document.getElementById('prodiBaru');
            if (prodiInput) prodiInput.value = '';
            document.getElementById('passwordBaru').value = '';
            const form = document.getElementById('formTambahMahasiswa');
            if (form && form.dataset.editId) delete form.dataset.editId;
            let modal = new bootstrap.Modal(document.getElementById('modalTambahMahasiswa'));
            modal.show();
        });
    }

   const formTambahMhs = document.getElementById('formTambahMahasiswa');
if(formTambahMhs) {
        formTambahMhs.addEventListener('submit', async (e) => {
        e.preventDefault();
        let nim = document.getElementById('nimBaru').value.trim();
        let nama = document.getElementById('namaBaru').value.trim();
        let prodi = document.getElementById('prodiBaru') ? document.getElementById('prodiBaru').value.trim() : '';
        let password = document.getElementById('passwordBaru').value.trim();
        if (!nim || !nama) {
            alert('NIM dan Nama harus diisi!');
            return;
        }
        const editId = formTambahMhs.dataset.editId ? Number(formTambahMhs.dataset.editId) : null;
        if (editId) {
            // update flow
            try {
                await fetchJSON(`/api/mahasiswa/${editId}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ NIM: nim, Nama_Mahasiswa: nama, Prodi: prodi || undefined, Password_Mahasiswa: password || undefined })
                });
                delete formTambahMhs.dataset.editId;
                formTambahMhs.reset();
                let modal = bootstrap.Modal.getInstance(document.getElementById('modalTambahMahasiswa'));
                if (modal) modal.hide();
                await loadMahasiswa();
                alert('Mahasiswa berhasil diperbarui');
            } catch (err) {
                console.error('Gagal memperbarui mahasiswa:', err);
                alert('Gagal memperbarui mahasiswa. Silakan coba lagi.');
            }
        } else {
            // create flow
            if (password.trim() === '') {
                alert('Password harus diisi saat menambah mahasiswa baru');
                return;
            }
            try {
                await tambahMahasiswa(nim, nama, prodi, password);
                formTambahMhs.classList.add('d-none');
                const successBox = document.getElementById('successBox');
                if(successBox) {
                    successBox.classList.remove('d-none');
                }
                formTambahMhs.reset();
            } catch (err) {
                console.error('Gagal menambah mahasiswa:', err);
                alert('Gagal menambah mahasiswa. Silakan coba lagi.');
            }
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
            document.getElementById('editUsername').value = profilAdmin.username || profilAdmin.nama || '';
            document.getElementById('editEmail').value = profilAdmin.email || '';
            const editPassword = document.getElementById('editPassword');
            if (editPassword) editPassword.value = '';
            let modal = new bootstrap.Modal(document.getElementById('modalEditProfil'));
            modal.show();
        });
    }

    const formEditProfil = document.getElementById('formEditProfil');
    if(formEditProfil) {
        formEditProfil.addEventListener('submit', async (e) => {
            e.preventDefault();
            let username = document.getElementById('editUsername').value.trim();
            let email = document.getElementById('editEmail').value.trim();
            let password = document.getElementById('editPassword') ? document.getElementById('editPassword').value.trim() : '';
            if (!username || !email) {
                alert('Username dan email harus diisi!');
                return;
            }

            try {
                await editProfil(username, email, password);
                let modal = bootstrap.Modal.getInstance(document.getElementById('modalEditProfil'));
                if(modal) modal.hide();
                alert('Profil berhasil diperbarui!');
            } catch (err) {
                console.error('Gagal memperbarui profil admin:', err);
                alert('Gagal memperbarui profil admin. Silakan coba lagi.');
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
        confirmLogoutBtn.addEventListener('click', async () => {
            if (idMahasiswaYangAkanDihapus !== null) {
                try {
                    await fetchJSON(`/api/mahasiswa/${idMahasiswaYangAkanDihapus}`, {
                        method: 'DELETE'
                    });
                    await loadMahasiswa();

                    let modalElement = document.getElementById('logoutModal');
                    let modalInstance = bootstrap.Modal.getInstance(modalElement);
                    if(modalInstance) modalInstance.hide();
                    idMahasiswaYangAkanDihapus = null;
                } catch (err) {
                    console.error('Gagal menghapus mahasiswa:', err);
                    alert('Gagal menghapus mahasiswa. Silakan coba lagi.');
                }
            } else {
                window.location.href = "/logout"; 
            }
        });
    }
});