const SITE = "https://seaviewserenity.gr";
const LOGO = `${SITE}/gallery/Picture%201.png`;
const HERO = `${SITE}/gallery_gen/d9a25b075f62f8d817a4f599e5f5010c_fit.png`;

const AUTO_REPLY = {
  en: {
    subject: "We received your message — Sea View Serenity",
    greeting: (name) => (name ? `Hello ${name},` : "Hello,"),
    lead: "Thank you for contacting Sea View Serenity.",
    body: "Your request has been submitted successfully. Someone from our team will reply as soon as possible.",
    cta: "Visit the website",
    regards: "Warm regards,",
    place: "Delfini Beach, Syros",
  },
  el: {
    subject: "Λάβαμε το μήνυμά σας — Sea View Serenity",
    greeting: (name) => (name ? `Γεια σας ${name},` : "Γεια σας,"),
    lead: "Σας ευχαριστούμε που επικοινωνήσατε με το Sea View Serenity.",
    body: "Το αίτημά σας υποβλήθηκε με επιτυχία. Κάποιος από την ομάδα μας θα σας απαντήσει το συντομότερο δυνατό.",
    cta: "Επισκεφθείτε τον ιστότοπο",
    regards: "Με εκτίμηση,",
    place: "Παραλία Δελφίνι, Σύρος",
  },
  fr: {
    subject: "Nous avons bien reçu votre message — Sea View Serenity",
    greeting: (name) => (name ? `Bonjour ${name},` : "Bonjour,"),
    lead: "Merci d’avoir contacté Sea View Serenity.",
    body: "Votre demande a bien été envoyée. Quelqu’un de notre équipe vous répondra dès que possible.",
    cta: "Visiter le site",
    regards: "Cordialement,",
    place: "Plage de Delfini, Syros",
  },
  de: {
    subject: "Wir haben Ihre Nachricht erhalten — Sea View Serenity",
    greeting: (name) => (name ? `Hallo ${name},` : "Hallo,"),
    lead: "Vielen Dank, dass Sie Sea View Serenity kontaktiert haben.",
    body: "Ihre Anfrage wurde erfolgreich übermittelt. Jemand aus unserem Team meldet sich so bald wie möglich bei Ihnen.",
    cta: "Zur Website",
    regards: "Herzliche Grüße,",
    place: "Delfini Beach, Syros",
  },
  it: {
    subject: "Abbiamo ricevuto il suo messaggio — Sea View Serenity",
    greeting: (name) => (name ? `Buongiorno ${name},` : "Buongiorno,"),
    lead: "Grazie per aver contattato Sea View Serenity.",
    body: "La sua richiesta è stata inviata correttamente. Qualcuno del nostro team le risponderà al più presto.",
    cta: "Visita il sito",
    regards: "Cordiali saluti,",
    place: "Spiaggia di Delfini, Syros",
  },
  he: {
    subject: "קיבלנו את ההודעה שלך — Sea View Serenity",
    greeting: (name) => (name ? `שלום ${name},` : "שלום,"),
    lead: "תודה שפנית ל-Sea View Serenity.",
    body: "הבקשה שלך נשלחה בהצלחה. מישהו מהצוות שלנו יחזור אליך בהקדם.",
    cta: "לאתר",
    regards: "בברכה,",
    place: "חוף דלפיני, סירוס",
    rtl: true,
  },
};

function escHtml(value) {
  return String(value || "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function buildAutoReplyText(copy, name) {
  return [
    copy.greeting(name),
    "",
    copy.lead,
    copy.body,
    "",
    copy.regards,
    "Sea View Serenity",
    copy.place,
    SITE,
  ].join("\n");
}

function buildAutoReplyHtml(copy, name, lang) {
  const dir = copy.rtl ? "rtl" : "ltr";
  const align = copy.rtl ? "right" : "left";
  const greeting = escHtml(copy.greeting(name));
  const home = lang === "en" ? `${SITE}/en/` : `${SITE}/${lang}/`;

  return `<!DOCTYPE html>
<html lang="${escHtml(lang)}" dir="${dir}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>${escHtml(copy.subject)}</title>
</head>
<body style="margin:0;padding:0;background:#e8f1fa;color:#333c44;font-family:'Open Sans','Helvetica Neue',Arial,sans-serif;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:linear-gradient(180deg,#e8f1fa 0%,#f3f6f9 45%,#ffffff 100%);background-color:#e8f1fa;">
    <tr>
      <td align="center" style="padding:28px 16px;">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:560px;background:#ffffff;border:1px solid #d9e2ec;overflow:hidden;">
          <tr>
            <td style="padding:0;line-height:0;font-size:0;">
              <img src="${HERO}" alt="Sea View Serenity terrace at sunset, Syros" width="560" style="display:block;width:100%;max-width:560px;height:auto;border:0;" />
            </td>
          </tr>
          <tr>
            <td style="padding:28px 28px 8px ${align === "right" ? "28px" : "28px"};text-align:${align};">
              <img src="${LOGO}" alt="Sea View Serenity" width="56" height="56" style="display:block;width:56px;height:56px;border-radius:50%;border:0;margin:0 0 18px;" />
              <h1 style="margin:0 0 10px;font-family:Roboto,'Helvetica Neue',Arial,sans-serif;font-size:24px;line-height:1.25;font-weight:700;color:#13161a;">
                Sea View Serenity
              </h1>
              <p style="margin:0 0 18px;font-size:13px;letter-spacing:0.08em;text-transform:uppercase;font-weight:700;color:#3d6fa8;">
                ${escHtml(copy.place)}
              </p>
              <p style="margin:0 0 12px;font-size:16px;line-height:1.6;color:#13161a;">
                ${greeting}
              </p>
              <p style="margin:0 0 12px;font-size:16px;line-height:1.7;color:#333c44;">
                ${escHtml(copy.lead)}
              </p>
              <p style="margin:0 0 24px;font-size:16px;line-height:1.7;color:#5c6670;">
                ${escHtml(copy.body)}
              </p>
              <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 28px;">
                <tr>
                  <td style="background:#3d6fa8;">
                    <a href="${home}" style="display:inline-block;padding:12px 18px;font-family:Roboto,'Helvetica Neue',Arial,sans-serif;font-size:14px;font-weight:700;color:#ffffff;text-decoration:none;">
                      ${escHtml(copy.cta)}
                    </a>
                  </td>
                </tr>
              </table>
              <p style="margin:0 0 4px;font-size:15px;line-height:1.6;color:#13161a;">
                ${escHtml(copy.regards)}
              </p>
              <p style="margin:0 0 2px;font-family:Roboto,'Helvetica Neue',Arial,sans-serif;font-size:15px;font-weight:700;color:#13161a;">
                Sea View Serenity
              </p>
              <p style="margin:0;font-size:14px;line-height:1.6;color:#5c6670;">
                ${escHtml(copy.place)}<br />
                <a href="${SITE}/" style="color:#3d6fa8;text-decoration:none;">seaviewserenity.gr</a>
                &nbsp;·&nbsp;
                <a href="mailto:info@seaviewserenity.gr" style="color:#3d6fa8;text-decoration:none;">info@seaviewserenity.gr</a>
              </p>
            </td>
          </tr>
          <tr>
            <td style="padding:18px 28px 24px;border-top:1px solid #d9e2ec;background:#f7fbff;text-align:${align};">
              <p style="margin:0;font-size:12px;line-height:1.55;color:#5c6670;">
                Sea View Serenity · Delfini Beach, Ano Syros 81400, Syros, Greece
              </p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>`;
}

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
      text: buildAutoReplyText(reply, name),
      html: buildAutoReplyHtml(reply, name, lang),
    });

    return json(res, 200, { ok: true });
  } catch (err) {
    console.error("contact form error", err?.message || err, err?.data || "");
    return json(res, 502, { ok: false, error: "Failed to send message" });
  }
};
