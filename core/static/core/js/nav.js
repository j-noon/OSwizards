// core/static/core/js/nav.js
document.addEventListener("DOMContentLoaded", () => {
  // ----- Dropdown toggle -----
  const btn = document.querySelector(".nav-toggle");
  const nav = document.querySelector("#site-nav");

  if (!btn || !nav) return;

  const openNav = () => {
    btn.setAttribute("aria-expanded", "true");
    nav.hidden = false;
    requestAnimationFrame(() => nav.classList.add("is-open"));
  };

  const closeNav = () => {
    btn.setAttribute("aria-expanded", "false");
    nav.classList.remove("is-open");

    nav.querySelectorAll("video.lightning").forEach(v => {
      v.pause();
      v.currentTime = 0;
    });

    const onEnd = (e) => {
      if (e.propertyName !== "opacity") return; // pick one property
      nav.hidden = true;
      nav.removeEventListener("transitionend", onEnd);
    };

    nav.addEventListener("transitionend", onEnd);
  };

  // Toggle via button
  btn.addEventListener("click", (e) => {
    e.stopPropagation(); // prevent document click from firing
    const isOpen = btn.getAttribute("aria-expanded") === "true";
    isOpen ? closeNav() : openNav();
  });

  // Prevent clicks inside the scroll from closing it
  nav.addEventListener("click", (e) => {
    e.stopPropagation();
  });

  // Close when clicking anywhere else on the page
  document.addEventListener("click", () => {
    const isOpen = btn.getAttribute("aria-expanded") === "true";
    if (isOpen) closeNav();
  });

  // ----- Lightning overlay: play on hover/focus, stop on leave/blur -----
  const links = document.querySelectorAll(".scroll-link");

  links.forEach((link) => {
    const vid = link.querySelector("video.lightning");
    if (!vid) return;

    vid.muted = true;

    const play = async () => {
      try {
        vid.currentTime = 0;
        await vid.play();
      } catch {}
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