(function () {
  function closeOthers(except) {
    document.querySelectorAll("details.svs-lang-dd[open]").forEach(function (el) {
      if (el !== except) el.removeAttribute("open");
    });
  }

  document.addEventListener("click", function (e) {
    var dd = e.target.closest && e.target.closest("details.svs-lang-dd");
    if (!dd) {
      closeOthers(null);
      return;
    }
    closeOthers(dd);
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closeOthers(null);
  });
})();
