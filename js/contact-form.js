(() => {
  const form = document.querySelector("[data-contact-form]");
  if (!form) return;

  const status = form.querySelector("[data-contact-status]");
  const submit = form.querySelector('[type="submit"]');
  const idleLabel = submit ? submit.textContent : "";

  const setStatus = (tone, message) => {
    if (!status) return;
    status.hidden = !message;
    status.textContent = message || "";
    status.dataset.tone = tone || "";
  };

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    if (form.dataset.busy === "1") return;

    const data = new FormData(form);
    const payload = {
      name: String(data.get("name") || "").trim(),
      email: String(data.get("email") || "").trim(),
      phone: String(data.get("phone") || "").trim(),
      dates: String(data.get("dates") || "").trim(),
      guests: String(data.get("guests") || "").trim(),
      message: String(data.get("message") || "").trim(),
      company: String(data.get("company") || "").trim(),
      lang: String(data.get("lang") || document.documentElement.lang || "en").trim(),
    };

    form.dataset.busy = "1";
    if (submit) {
      submit.disabled = true;
      submit.textContent = form.dataset.sending || idleLabel;
    }
    setStatus("", "");

    try {
      const response = await fetch("/api/contact", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      const result = await response.json().catch(() => ({}));
      if (!response.ok || !result.ok) {
        throw new Error(result.error || "send_failed");
      }
      form.reset();
      setStatus("ok", form.dataset.success || "OK");
    } catch (err) {
      setStatus("err", form.dataset.error || "Error");
    } finally {
      form.dataset.busy = "0";
      if (submit) {
        submit.disabled = false;
        submit.textContent = idleLabel;
      }
    }
  });
})();
