const crypto = require("crypto");

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

function apiKey() {
  return process.env.Resend_API_Key_SVS || process.env.RESEND_API_KEY || "";
}

function verifySvix(payload, headers, secret) {
  if (!secret) return true;
  const id = headers["svix-id"];
  const timestamp = headers["svix-timestamp"];
  const signatureHeader = headers["svix-signature"];
  if (!id || !timestamp || !signatureHeader) return false;

  const age = Math.abs(Date.now() / 1000 - Number(timestamp));
  if (!Number.isFinite(age) || age > 60 * 5) return false;

  const secretPart = secret.startsWith("whsec_") ? secret.slice(6) : secret;
  const key = Buffer.from(secretPart, "base64");
  const signedContent = `${id}.${timestamp}.${payload}`;
  const expected = crypto.createHmac("sha256", key).update(signedContent).digest("base64");

  return String(signatureHeader)
    .split(" ")
    .some((part) => {
      const [version, sig] = part.split(",");
      if (version !== "v1" || !sig) return false;
      try {
        return crypto.timingSafeEqual(Buffer.from(expected), Buffer.from(sig));
      } catch {
        return false;
      }
    });
}

function extractEmail(value) {
  const raw = String(value || "").trim();
  const match = raw.match(/<([^>]+)>/);
  return (match ? match[1] : raw).toLowerCase();
}

async function resendFetch(path, options = {}) {
  const response = await fetch(`https://api.resend.com${path}`, {
    ...options,
    headers: {
      Authorization: `Bearer ${apiKey()}`,
      "Content-Type": "application/json",
      ...(options.headers || {}),
    },
  });
  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    const err = new Error(data?.message || data?.error || `Resend ${response.status}`);
    err.status = response.status;
    err.data = data;
    throw err;
  }
  return data;
}

module.exports = async (req, res) => {
  if (req.method !== "POST") {
    return json(res, 405, { ok: false, error: "Method not allowed" });
  }

  if (!apiKey()) {
    return json(res, 500, { ok: false, error: "Email service is not configured" });
  }

  try {
    const payload = await readBody(req);
    const headers = Object.fromEntries(
      Object.entries(req.headers || {}).map(([k, v]) => [String(k).toLowerCase(), v])
    );

    const secret = process.env.RESEND_WEBHOOK_SECRET || "";
    if (secret && !verifySvix(payload, headers, secret)) {
      return json(res, 401, { ok: false, error: "Invalid signature" });
    }

    const event = JSON.parse(payload || "{}");
    if (event.type !== "email.received") {
      return json(res, 200, { ok: true, ignored: true });
    }

    const meta = event.data || {};
    const emailId = meta.email_id;
    if (!emailId) {
      return json(res, 400, { ok: false, error: "Missing email_id" });
    }

    const fromAddr = extractEmail(meta.from);
    const forwardTo = (process.env.CONTACT_TO_EMAIL || "gad1981@gmail.com").toLowerCase();
    const fromIdentity =
      process.env.RESEND_FROM_EMAIL || "Sea View Serenity <info@seaviewserenity.gr>";

    // Avoid loops from our own outbound / auto-forward mail
    if (fromAddr.endsWith("@seaviewserenity.gr") || fromAddr === forwardTo) {
      return json(res, 200, { ok: true, skipped: "loop_guard" });
    }

    const email = await resendFetch(`/emails/receiving/${emailId}`);
    const attachmentsResp = await resendFetch(
      `/emails/receiving/${emailId}/attachments`
    ).catch(() => ({ data: [] }));

    const attachments = [];
    for (const item of attachmentsResp.data || []) {
      if (!item.download_url) continue;
      const fileRes = await fetch(item.download_url);
      if (!fileRes.ok) continue;
      const buffer = Buffer.from(await fileRes.arrayBuffer());
      attachments.push({
        filename: item.filename || "attachment",
        content: buffer.toString("base64"),
        content_type: item.content_type || undefined,
      });
    }

    const subject = email.subject || meta.subject || "(no subject)";
    const textParts = [
      `Forwarded inbound mail to info@seaviewserenity.gr`,
      `From: ${email.from || meta.from}`,
      `To: ${(email.to || meta.to || []).join(", ")}`,
      `Subject: ${subject}`,
      "",
      email.text || "(no text body)",
    ];

    await resendFetch("/emails", {
      method: "POST",
      body: JSON.stringify({
        from: fromIdentity,
        to: [forwardTo],
        reply_to: fromAddr || undefined,
        subject: `[info@] ${subject}`,
        text: textParts.join("\n"),
        html: email.html || undefined,
        attachments: attachments.length ? attachments : undefined,
      }),
    });

    return json(res, 200, { ok: true, forwarded: true });
  } catch (err) {
    console.error("inbound forward error", err?.message || err, err?.data || "");
    return json(res, 500, { ok: false, error: "Forward failed" });
  }
};
