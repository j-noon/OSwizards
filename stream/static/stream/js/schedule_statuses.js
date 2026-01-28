(function () {
  const URL = "/stream/schedule-statuses/";
  const INTERVAL = 10000; // 10 seconds

  function pillHtml(status) {
    if (status === "live") return `<span class="sched-pill is-live">LIVE NOW</span>`;
    if (status === "cancelled") return `<span class="sched-pill is-cancelled">CANCELLED</span>`;
    if (status === "past") return `<span class="sched-pill is-past">PAST</span>`;
    return `<span class="sched-pill is-upcoming">UPCOMING</span>`;
  }

  function update() {
    fetch(URL)
      .then(r => r.json())
      .then(data => {
        const map = new Map((data.items || []).map(x => [String(x.id), x.status]));

        document.querySelectorAll(".schedule-grid[data-item-id]").forEach(row => {
          const id = row.getAttribute("data-item-id");
          const status = map.get(String(id));
          if (!status) return;

          const target = row.querySelector(".js-sched-status");
          if (!target) return;

          // Only update if changed (avoids flicker)
          const current = target.getAttribute("data-status");
          if (current === status) return;

          target.innerHTML = pillHtml(status);
          target.setAttribute("data-status", status);
        });
      })
      .catch(() => {
        // silent fail
      });
  }

  // run once quickly, then poll
  update();
  setInterval(update, INTERVAL);
})();