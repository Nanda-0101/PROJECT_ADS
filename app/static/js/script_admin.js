document.addEventListener("DOMContentLoaded", () => {

    // ==========================
    // LOAD SIDEBAR
    // ==========================
    const sidebarContainer = document.getElementById("sidebar-container");

    if (sidebarContainer) {
        fetch("/api/navigasi")
            .then(res => res.text())
            .then(html => {
                sidebarContainer.innerHTML = html;
            })
            .catch(err => console.error(err));
    }

    // ==========================
    // MODAL TAMBAH ADMIN
    // ==========================
    const modalTambah = document.getElementById("modalTambahMahasiswa");
    const formTambah = document.getElementById("formTambahMahasiswa");

    const btnTambah = document.getElementById("btnTambahMahasiswa");

    if (btnTambah) {
        btnTambah.addEventListener("click", () => {

            formTambah.reset();

            const successBox = document.getElementById("successBox");
            if (successBox) {
                successBox.classList.add("d-none");
            }

            formTambah.classList.remove("d-none");

            const modal = new bootstrap.Modal(modalTambah);
            modal.show();
        });
    }

    // ==========================
    // TAMBAH ADMIN
    // ==========================
    if (formTambah) {

        formTambah.addEventListener("submit", async (e) => {

            e.preventDefault();

            const username =
                document.getElementById("nimBaru").value.trim();

            const email =
                document.getElementById("namaBaru").value.trim();

            const password =
                document.getElementById("passwordBaru").value.trim();

            if (!username || !email || !password) {
                alert("Semua field wajib diisi.");
                return;
            }

            try {

                const response = await fetch(
                    "/admin/kelola-admin/tambah",
                    {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            username: username,
                            email: email,
                            password: password
                        })
                    }
                );

                const result = await response.json();

                if (!response.ok) {
                    throw new Error(result.detail);
                }

                formTambah.classList.add("d-none");

                document
                    .getElementById("successBox")
                    .classList
                    .remove("d-none");

                setTimeout(() => {
                    window.location.reload();
                }, 1200);

            }
            catch (err) {

                alert(err.message);

            }

        });

    }

    // ==========================
    // HAPUS ADMIN
    // ==========================
    let idAdmin = null;

    document.querySelectorAll(".btn-hapus-admin")
        .forEach(btn => {

            btn.addEventListener("click", () => {

                idAdmin = btn.dataset.id;

                const modalTitle =
                    document.querySelector("#logoutModal .modal-title");

                const modalBody =
                    document.querySelector("#logoutModal .modal-body");

                const confirmBtn =
                    document.getElementById("confirmLogoutBtn");

                modalTitle.textContent =
                    "Konfirmasi Hapus";

                modalBody.textContent =
                    "Apakah Anda yakin ingin menghapus admin ini?";

                confirmBtn.textContent =
                    "Hapus";

                confirmBtn.className =
                    "btn btn-danger";

                const modal =
                    new bootstrap.Modal(
                        document.getElementById("logoutModal")
                    );

                modal.show();

            });

        });

    // ==========================
    // KONFIRMASI HAPUS
    // ==========================
    const confirmBtn =
        document.getElementById("confirmLogoutBtn");

    if (confirmBtn) {

        confirmBtn.addEventListener("click", async () => {

            if (!idAdmin) {
                window.location.href = "/logout";
                return;
            }

            try {

                const response =
                    await fetch(
                        `/admin/kelola-admin/hapus/${idAdmin}`,
                        {
                            method: "POST"
                        }
                    );

                const result =
                    await response.json();

                if (!response.ok) {
                    throw new Error(result.detail);
                }

                window.location.reload();

            }
            catch (err) {

                alert(err.message);

            }

        });

    }

    // ==========================
    // LOGOUT
    // ==========================
    const logoutBtn =
        document.getElementById("logoutBtn");

    if (logoutBtn) {

        logoutBtn.addEventListener("click", () => {

            idAdmin = null;

            const modalTitle =
                document.querySelector("#logoutModal .modal-title");

            const modalBody =
                document.querySelector("#logoutModal .modal-body");

            const confirmBtn =
                document.getElementById("confirmLogoutBtn");

            modalTitle.textContent =
                "Konfirmasi Logout";

            modalBody.textContent =
                "Apakah Anda yakin ingin logout?";

            confirmBtn.textContent =
                "Logout";

            confirmBtn.className =
                "btn btn-danger";

            const modal =
                new bootstrap.Modal(
                    document.getElementById("logoutModal")
                );

            modal.show();

        });

    }

});