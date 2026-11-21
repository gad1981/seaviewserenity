(() => {
  const hero = document.querySelector(".svs-bleed-hero");
  const stage =
    document.querySelector(".svs-bleed-hero__stage") ||
    document.querySelector(".svs-bleed-hero__media");
  if (!hero || !stage) return;

  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
  if (reduce.matches) return;

  let ticking = false;

  const update = () => {
    ticking = false;
    const y = window.scrollY || 0;
    const h = hero.offsetHeight || window.innerHeight;
    const progress = Math.min(Math.max(y / h, 0), 1);
    stage.style.setProperty("--svs-hero-parallax", `${progress * 10}%`);
    stage.style.setProperty("--svs-hero-fade", String(1 - progress * 0.28));
  };

  const onScroll = () => {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(update);
  };

  window.addEventListener("scroll", onScroll, { passive: true });
  update();
})();
