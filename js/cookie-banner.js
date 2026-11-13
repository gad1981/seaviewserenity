(function () {
  var KEY = "svs_cookie_consent";
  try {
    if (localStorage.getItem(KEY) === "1") return;
  } catch (e) {}

  var root = document.getElementById("svs-cookie-banner");
  if (!root) return;

  root.hidden = false;

  var accept = root.querySelector("[data-svs-cookie-accept]");
  if (accept) {
    accept.addEventListener("click", function () {
      try {
        localStorage.setItem(KEY, "1");
      } catch (e) {}
      root.hidden = true;
    });
  }
})();
