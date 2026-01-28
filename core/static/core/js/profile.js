document.addEventListener("DOMContentLoaded", () => {
  const openBtns = document.querySelectorAll("[data-profile-open]");
  const modal = document.querySelector("[data-profile-modal]");
  const closeBtn = document.querySelector("[data-profile-close]");

  const editOpen = document.querySelector("[data-edit-open]");
  const editPanel = document.querySelector("[data-edit-panel]");
  const editClose = document.querySelector("[data-edit-close]");

  if (!openBtns.length || !modal) return;

  const open = () => {
    modal.hidden = false;
    document.body.style.overflow = "hidden";

    // Always show edit panel when opening via banner / profile
    if (editPanel) editPanel.hidden = false;
  };

  const close = () => {
    modal.hidden = true;
    document.body.style.overflow = "";
    if (editPanel) editPanel.hidden = true;
  };

  /* =========================
     OPEN MODAL (ALL TRIGGERS)
     ========================= */
  openBtns.forEach((btn) => {
    btn.addEventListener("click", open);
  });

  /* =========================
     CLOSE MODAL
     ========================= */
  closeBtn?.addEventListener("click", (e) => {
    e.stopPropagation();
    close();
  });

  modal.addEventListener("click", (e) => {
    if (e.target === modal) close();
  });

  const card = modal.querySelector(".pm-card");
  card?.addEventListener("click", (e) => e.stopPropagation());

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && !modal.hidden) close();
  });

  /* =========================
     EDIT PANEL TOGGLE
     ========================= */
  editOpen?.addEventListener("click", (e) => {
    e.stopPropagation();
    if (editPanel) editPanel.hidden = false;
  });

  editClose?.addEventListener("click", (e) => {
    e.stopPropagation();
    if (editPanel) editPanel.hidden = true;
  });

  /* =========================
     FILE UPLOAD UX
     ========================= */
  const fileTrigger = document.querySelector("[data-file-trigger]");
  const fileInput = document.getElementById("avatar-input");
  const fileName = document.querySelector("[data-file-name]");

  fileTrigger?.addEventListener("click", () => {
    fileInput?.click();
  });

  fileInput?.addEventListener("change", () => {
    fileName.textContent =
      fileInput.files[0]?.name || "No file chosen";
  });
});