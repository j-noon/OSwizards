document.addEventListener("DOMContentLoaded", () => {
  const openBtn = document.querySelector("[data-profile-open]");
  const modal = document.querySelector("[data-profile-modal]");
  const closeBtn = document.querySelector("[data-profile-close]");

  const editOpen = document.querySelector("[data-edit-open]");
  const editPanel = document.querySelector("[data-edit-panel]");
  const editClose = document.querySelector("[data-edit-close]");

  if (!openBtn || !modal) return;

  const open = () => {
    modal.hidden = false;
    document.body.style.overflow = "hidden";
  };

  const close = () => {
    modal.hidden = true;
    document.body.style.overflow = "";
    if (editPanel) editPanel.hidden = true;
  };

  // Open modal
  openBtn.addEventListener("click", open);

  // Close via X button
  closeBtn?.addEventListener("click", (e) => {
    e.stopPropagation();
    close();
  });

  // Close when clicking outside the card
  modal.addEventListener("click", (e) => {
    if (e.target === modal) {
      close();
    }
  });

  // Prevent clicks inside the card from bubbling
  const card = modal.querySelector(".profile-card");
  card?.addEventListener("click", (e) => {
    e.stopPropagation();
  });

  // Close with ESC
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && !modal.hidden) {
      close();
    }
  });

  // Open edit panel
  editOpen?.addEventListener("click", (e) => {
    e.stopPropagation();
    if (editPanel) editPanel.hidden = false;
  });

  // Close edit panel
  editClose?.addEventListener("click", (e) => {
    e.stopPropagation();
    if (editPanel) editPanel.hidden = true;
  });
});