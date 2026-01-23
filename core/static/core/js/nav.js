// core/static/core/js/nav.js
document.addEventListener("DOMContentLoaded", () => {
  // ----- Dropdown toggle -----
  const btn = document.querySelector(".nav-toggle");
  const nav = document.querySelector("#site-nav");

  if (btn && nav) {
    btn.addEventListener("click", () => {
      const isOpen = btn.getAttribute("aria-expanded") === "true";
      btn.setAttribute("aria-expanded", String(!isOpen));

      if (isOpen) {
        nav.classList.remove("is-open");
        // allow close animation then hide
        setTimeout(() => {
          nav.hidden = true;
        }, 220);
      } else {
        nav.hidden = false;
        requestAnimationFrame(() => nav.classList.add("is-open"));
      }
    });
  }

  // ----- Fire overlay: play on hover/focus, stop on leave/blur -----
  const links = document.querySelectorAll(".scroll-link");

  links.forEach((link) => {
    const vid = link.querySelector("video.fire");
    if (!vid) return;

    // make sure it's muted (required for autoplay in most browsers)
    vid.muted = true;

    const play = async () => {
      try {
        vid.currentTime = 0;
        await vid.play();
      } catch (err) {
        // Some browsers may still block play until user interaction.
        // Hover/click usually counts, so this is mostly just a safe catch.
      }
    };

    const stop = () => {
      vid.pause();
      vid.currentTime = 0;
    };

    // Desktop hover
    link.addEventListener("mouseenter", play);
    link.addEventListener("mouseleave", stop);

    // Keyboard accessibility
    link.addEventListener("focus", play);
    link.addEventListener("blur", stop);

    // Mobile tap (best effort)
    link.addEventListener("touchstart", play, { passive: true });
  });
});