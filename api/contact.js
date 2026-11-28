const AUTO_REPLY = {
  en: {
    subject: "We received your message — Sea View Serenity",
    text: (name) =>
      `Hello${name ? ` ${name}` : ""},\n\nThank you for contacting Sea View Serenity. Your request has been submitted successfully.\n\nSomeone from our team will reply as soon as possible.\n\nWarm regards,\nSea View Serenity\nDelfini Beach, Syros\nhttps://seaviewserenity.gr/`,
  },
  el: {
    subject: "Λάβαμε το μήνυμά σας — Sea View Serenity",
    text: (name) =>
      `Γεια σας${name ? ` ${name}` : ""},\n\nΣας ευχαριστούμε που επικοινωνήσατε με το Sea View Serenity. Το αίτημά σας υποβλήθηκε με επιτυχία.\n\nΚάποιος από την ομάδα μας θα σας απαντήσει το συντομότερο δυνατό.\n\nΜε εκτίμηση,\nSea View Serenity\nΠαραλία Δελφίνι, Σύρος\nhttps://seaviewserenity.gr/`,
  },
  fr: {
    subject: "Nous avons bien reçu votre message — Sea View Serenity",
    text: (name) =>
      `Bonjour${name ? ` ${name}` : ""},\n\nMerci d’avoir contacté Sea View Serenity. Votre demande a bien été envoyée.\n\nQuelqu’un de notre équipe vous répondra dès que possible.\n\nCordialement,\nSea View Serenity\nPlage de Delfini, Syros\nhttps://seaviewserenity.gr/`,
  },
  de: {
    subject: "Wir haben Ihre Nachricht erhalten — Sea View Serenity",
    text: (name) =>
      `Hallo${name ? ` ${name}` : ""},\n\nvielen Dank, dass Sie Sea View Serenity kontaktiert haben. Ihre Anfrage wurde erfolgreich übermittelt.\n\nJemand aus unserem Team meldet sich so bald wie möglich bei Ihnen.\n\nHerzliche Grüße\nSea View Serenity\nDelfini Beach, Syros\nhttps://seaviewserenity.gr/`,
  },
  it: {
    subject: "Abbiamo ricevuto il suo messaggio — Sea View Serenity",
    text: (name) =>
      `Buongiorno${name ? ` ${name}` : ""},\n\nGrazie per aver contattato Sea View Serenity. La sua richiesta è stata inviata correttamente.\n\nQualcuno del nostro team le risponderà al più presto.\n\nCordiali saluti,\nSea View Serenity\nSpiaggia di Delfini, Syros\nhttps://seaviewserenity.gr/`,
  },
  he: {
    subject: "קיבלנו את ההודעה שלך — Sea View Serenity",
    text: (name) =>
      `שלום${name ? ` ${name}` : ""},\n\nתודה שפנית ל-Sea View Serenity. הבקשה שלך נשלחה בהצלחה.\n\nמישהו מהצוות שלנו יחזור אליך בהקדם.\n\nבברכה,\nSea View Serenity\nחוף דלפיני, סירוס\nhttps://seaviewserenity.gr/`,
  },
};

function json(res, status, body) {
  res.statusCode = status;
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  res.setHeader("Cache-Control", "no-store");
  res.end(JSON.stringify(body));
}

function readBody(req) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    req.on("data", (c) => chunks.push(c));
    req.on("end", () => resolve(Buffer.concat(chunks).toString("utf8")));
    req.on("error", reject);
  });
}

function clean(value, max = 2000) {
  return String(value || "")
    .replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/g, "")
    .trim()
    .slice(0, max);
}

function isEmail(value) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value) && value.length <= 254;
}

async function sendResend(apiKey, payload) {
  const response = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${apiKey}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });
  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    const message = data?.message || data?.error || `Resend ${response.status}`;
    const err = new Error(message);
    err.status = response.status;
    err.data = data;
    throw err;
  }
  return data;
}

module.exports = async (req, res) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");

  if (req.method === "OPTIONS") {
    res.statusCode = 204;
    return res.end();
  }

  if (req.method !== "POST") {
    return json(res, 405, { ok: false, error: "Method not allowed" });
  }

  const apiKey = process.env.Resend_API_Key_SVS || process.env.RESEND_API_KEY;
  const from =
    process.env.RESEND_FROM_EMAIL || "Sea View Serenity <info@seaviewserenity.gr>";
  const to = process.env.CONTACT_TO_EMAIL || "gad1981@gmail.com";

  if (!apiKey) {
    return json(res, 500, { ok: false, error: "Email service is not configured" });
  }

  try {
    const raw = await readBody(req);
    let body;
    try {
      body = JSON.parse(raw || "{}");
    } catch {
      return json(res, 400, { ok: false, error: "Invalid JSON" });
    }

    // Honeypot
    if (clean(body.company, 80)) {
      return json(res, 200, { ok: true });
    }

    const name = clean(body.name, 120);
    const email = clean(body.email, 254).toLowerCase();
    const phone = clean(body.phone, 60);
    const dates = clean(body.dates, 120);
    const guests = clean(body.guests, 40);
    const message = clean(body.message, 4000);
    const lang = clean(body.lang, 8).toLowerCase() || "en";
    const reply = AUTO_REPLY[lang] || AUTO_REPLY.en;

    if (!name || !email || !message) {
      return json(res, 400, { ok: false, error: "Missing required fields" });
    }
    if (!isEmail(email)) {
      return json(res, 400, { ok: false, error: "Invalid email" });
    }

    const notifyText = [
      "New booking enquiry from seaviewserenity.gr",
      "",
      `Language: ${lang}`,
      `Name: ${name}`,
      `Email: ${email}`,
      phone ? `Phone: ${phone}` : null,
      dates ? `Dates: ${dates}` : null,
      guests ? `Guests: ${guests}` : null,
      "",
      "Message:",
      message,
    ]
      .filter(Boolean)
      .join("\n");

    await sendResend(apiKey, {
      from,
      to: [to],
      reply_to: email,
      subject: `Enquiry from ${name} (${lang})`,
      text: notifyText,
    });

    await sendResend(apiKey, {
      from,
      to: [email],
      reply_to: "info@seaviewserenity.gr",
      subject: reply.subject,
      text: reply.text(name),
    });

    return json(res, 200, { ok: true });
  } catch (err) {
    console.error("contact form error", err?.message || err, err?.data || "");
    return json(res, 502, { ok: false, error: "Failed to send message" });
  }
};
