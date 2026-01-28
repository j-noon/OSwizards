(function () {
  const STATUS_URL = "/stream/twitch-status/";
  const INTERVAL = 60000; // 60 seconds

  const statusEl = document.querySelector(".stream-status__state");
  if (!statusEl) return;

  function updateStatus() {
    fetch(STATUS_URL)
      .then(res => res.json())
      .then(data => {
        statusEl.classList.toggle("is-online", data.live);
        statusEl.classList.toggle("is-offline", !data.live);

        statusEl.innerHTML = `
          <span class="status-dot" aria-hidden="true"></span>
          ${data.live ? "Online" : "Offline"}
        `;
      })
      .catch(() => {
        // silent fail — don’t spam console
      });
  }

  setInterval(updateStatus, INTERVAL);
})();
