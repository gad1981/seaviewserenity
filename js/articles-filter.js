(() => {
  const root = document.querySelector("[data-svs-articles-filter]");
  const grid = document.querySelector("[data-svs-articles-grid]");
  if (!root || !grid) return;

  const cards = [...grid.querySelectorAll("[data-svs-article-card]")];
  const searchInput = root.querySelector("[data-svs-articles-search]");
  const topicBtns = [...root.querySelectorAll("[data-svs-topic]")];
  const statusEl = root.querySelector("[data-svs-articles-status]");
  const emptyEl = document.querySelector("[data-svs-articles-empty]");
  let topic = "all";

  const apply = () => {
    const tokens = (searchInput?.value || "")
      .trim()
      .toLowerCase()
      .split(/\s+/)
      .filter(Boolean);
    let visible = 0;
    cards.forEach((card) => {
      const topics = (card.getAttribute("data-topics") || "").split(/\s+/).filter(Boolean);
      const hay = (card.getAttribute("data-search") || card.textContent || "").toLowerCase();
      const topicOk = topic === "all" || topics.includes(topic);
      const searchOk = !tokens.length || tokens.every((t) => hay.includes(t));
      const show = topicOk && searchOk;
      card.hidden = !show;
      card.toggleAttribute("aria-hidden", !show);
      if (show) visible += 1;
    });
    if (statusEl) {
      statusEl.textContent = visible === cards.length ? "" : `${visible} / ${cards.length}`;
    }
    if (emptyEl) emptyEl.hidden = visible !== 0;
    grid.hidden = visible === 0;
  };

  topicBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      topic = btn.getAttribute("data-svs-topic") || "all";
      topicBtns.forEach((b) => {
        const on = b === btn;
        b.classList.toggle("is-active", on);
        b.setAttribute("aria-pressed", on ? "true" : "false");
      });
      apply();
    });
  });

  searchInput?.addEventListener("input", apply);
  apply();
})();
