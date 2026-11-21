(() => {
  const header = document.querySelector(".svs-shell-header");
  if (!header) return;

  const onScroll = () => {
    header.classList.toggle("is-scrolled", window.scrollY > 24);
  };

  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  const toggle = header.querySelector(".svs-nav-toggle");
  const panel =
    header.querySelector(".svs-nav-panel") ||
    document.getElementById("svs-nav-panel");
  if (!toggle || !panel) return;

  const setOpen = (open) => {
    header.classList.toggle("is-nav-open", open);
    panel.classList.toggle("is-open", open);
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    toggle.setAttribute(
      "aria-label",
      open
        ? toggle.getAttribute("data-label-close") || "Close menu"
        : toggle.getAttribute("data-label-open") || "Menu"
    );
    document.body.classList.toggle("svs-nav-locked", open);
  };

  toggle.addEventListener("click", (e) => {
    e.preventDefault();
    e.stopPropagation();
    setOpen(!header.classList.contains("is-nav-open"));
  });

  panel.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => setOpen(false));
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") setOpen(false);
  });

  document.addEventListener("click", (e) => {
    if (!header.classList.contains("is-nav-open")) return;
    if (header.contains(e.target) || panel.contains(e.target)) return;
    setOpen(false);
  });

  window.addEventListener(
    "resize",
    () => {
      if (window.matchMedia("(min-width: 901px)").matches) setOpen(false);
    },
    { passive: true }
  );
})();
