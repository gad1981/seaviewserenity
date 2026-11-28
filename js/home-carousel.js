(() => {
  const root = document.querySelector("[data-svs-carousel]");
  if (!root) return;

  const track = root.querySelector(".svs-carousel__track");
  const slides = [...root.querySelectorAll(".svs-carousel__slide")];
  const prevBtn = root.querySelector("[data-svs-carousel-prev]");
  const nextBtn = root.querySelector("[data-svs-carousel-next]");
  const dots = [...root.querySelectorAll("[data-svs-carousel-dot]")];
  const indexEl = root.querySelector("[data-svs-carousel-index]");
  if (!track || slides.length < 2) return;

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const intervalMs = Number(root.getAttribute("data-interval") || 3000);
  let index = 0;
  let timer = 0;

  const go = (next) => {
    index = (next + slides.length) % slides.length;
    // Track is forced LTR in CSS so negative X always advances forward
    track.style.transform = `translate3d(-${index * 100}%, 0, 0)`;
    slides.forEach((slide, i) => {
      slide.setAttribute("aria-hidden", i === index ? "false" : "true");
    });
    dots.forEach((dot, i) => {
      dot.classList.toggle("is-active", i === index);
      dot.setAttribute("aria-current", i === index ? "true" : "false");
    });
    if (indexEl) indexEl.textContent = String(index + 1);
  };

  const stop = () => {
    if (timer) {
      clearInterval(timer);
      timer = 0;
    }
  };

  const start = () => {
    if (reduceMotion) return;
    stop();
    timer = window.setInterval(() => go(index + 1), intervalMs);
  };

  prevBtn?.addEventListener("click", () => {
    go(index - 1);
    start();
  });
  nextBtn?.addEventListener("click", () => {
    go(index + 1);
    start();
  });
  dots.forEach((dot, i) => {
    dot.addEventListener("click", () => {
      go(i);
      start();
    });
  });

  root.addEventListener("mouseenter", stop);
  root.addEventListener("mouseleave", start);
  root.addEventListener("focusin", stop);
  root.addEventListener("focusout", (e) => {
    if (!root.contains(e.relatedTarget)) start();
  });

  go(0);
  start();
})();
