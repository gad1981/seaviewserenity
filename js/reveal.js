(() => {
  const items = [...document.querySelectorAll(".svs-reveal")];
  if (!items.length) return;

  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce) {
    items.forEach((el) => el.classList.add("is-in"));
    return;
  }

  if (!("IntersectionObserver" in window)) {
    items.forEach((el) => el.classList.add("is-in"));
    return;
  }

  const io = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        const el = entry.target;
        const delay = Number(el.getAttribute("data-reveal-delay") || 0);
        window.setTimeout(() => {
          el.classList.add("is-in");
        }, Math.max(0, delay) * 1000);
        io.unobserve(el);
      }
    },
    { root: null, rootMargin: "0px 0px -8% 0px", threshold: 0.12 }
  );

  items.forEach((el) => io.observe(el));
})();
