# P&S Associates — Concept Website

A pitch/concept website for **P&S Associates Roofing · Gutters · Masonry** (Elizabeth, NJ),
built by Annica Elevation Agency to show the owner (Walter Lozano) what a custom site could look like.

- **Live preview:** open `index.html` in any browser (double-click it). No build step, no
  internet, no dependencies — one self-contained file.
- **Design:** an "architect's blueprint meets premium build" theme — futuristic but grounded in
  the actual craft. The hero has an **interactive blueprint** of a house: tap/hover Roofing,
  Gutters, Masonry, Siding, Windows or Decks to light up that system.
- **Fully responsive** (looks great on phones — includes a sticky tap-to-call bar on mobile).

---

## What's real vs. placeholder

**Verified & real** (from the Google listing + public records):
- Business name, services, and 5.0 ★ rating (13 reviews)
- Phone **(908) 966-5507**, address **740 Pennington St, Elizabeth, NJ 07202**
- Owner **Walter Lozano**, in business since **2012**
- NJ Home Improvement Contractor license **13VH06724100**
- The two testimonials (Marco Borga, John Rubio) are real, lightly trimmed Google reviews
- Facebook page link is the real one

**Placeholder — swap after the client signs:**
- All imagery is custom blueprint-style **illustration** (no stock photos). Once P&S sends real
  project photos, they drop straight into the hero, the "Recent work" gallery, and the About section.
- The quote form is a front-end demo (shows a success message). To make it send real leads, wire it
  to Formspree / Netlify Forms / a mailbox — ~15 min.

**Please confirm with Walter before going live:**
- **Business hours** — the Google card shows "7:00 AM – 8:00 PM" without listing days, so the site
  says "7:00 AM – 8:00 PM / call anytime." Confirm the actual open days.
- **Service-area towns** — the listed towns are typical Union County coverage; confirm which he serves.
- **Email address** — none is shown publicly, so the site leads with Call + Facebook + the form.
  Recommend setting up `info@` or `walter@` on the new domain (see below).

---

## Domain availability & cost

> ⚠️ **Method & caveat.** An authoritative WHOIS/RDAP registration lookup was blocked by network
> policy in the build environment, so availability below is based on a **DNS check** — none of the
> "available" domains resolve to any live website or server. Since P&S currently has **no web
> presence**, these brand domains are very likely truly unregistered. **Confirm with one click** at
> a registrar before buying (links below do a live check).

### ✅ Appear available — recommended
| Domain | Why |
|---|---|
| **pandsassociates.com** ⭐ | Exact brand name — the one to grab. `.net`, `.co`, `.us` also appear open. |
| **pandsroofing.com** ⭐ | Short, memorable, keyword-rich — great for SEO & word-of-mouth. |
| pandsassociatesnj.com | Brand + state; strong local SEO signal. |
| pandsroofingnj.com | Service + state. |
| psassociatesnj.com | Shorter "PS" variant. |
| pandsassociatesroofing.com | Fully descriptive. |
| pandsroofingandmasonry.com / pandsroofingmasonry.com | Describes the two headline trades. |
| pandsmasonry.com | If masonry is the growth focus. |
| pandsexteriors.com / pandshomeimprovement.com | Broader, if he wants to expand beyond roofing. |

### ❌ Appear taken / already in use
- **psassociates.com** — resolves to a server (generic acronym; heavily contested).
- **pandscontractors.com** — resolves to a server.

### 💰 Typical .com pricing (2026) & where to buy
| Registrar | 1st year | Renewal | Notes |
|---|---|---|---|
| **Cloudflare** | ~$10.44 | ~$10.44 | At-cost, no markup, free privacy. Cheapest long-term. |
| **Porkbun** | ~$11 | ~$13 | Great value, free privacy + email forwarding. |
| **Namecheap** | ~$6–10 (promo) | ~$15 | Easiest for beginners, free privacy. |
| **GoDaddy** | ~$12–20 | ~$22 | Most upsells; fine if he already uses it. |
| **Squarespace Domains** | ~$20 | ~$20 | Simple if he wants site + domain in one place. |

**Recommendation:** register **pandsassociates.com** (primary) and grab **pandsroofing.com** as a
short redirect. Budget **~$25–35/year** total for both on Cloudflare or Porkbun, plus a free/low-cost
email forward like `info@pandsassociates.com → Walter's inbox`.

**One-click availability checks:**
- Namecheap: `https://www.namecheap.com/domains/registration/results/?domain=pandsassociates.com`
- Cloudflare: `https://dash.cloudflare.com/?to=/:account/registrar` (search inside)
- Porkbun: `https://porkbun.com/checkout/search?q=pandsassociates.com`

---

## Hosting (once approved)
Because it's a single static file, it hosts anywhere for free/cheap:
**Netlify** or **Cloudflare Pages** (free, drag-and-drop, connects the domain in minutes),
**Vercel**, or standard cPanel hosting. Point the domain, drop in `index.html`, done.
