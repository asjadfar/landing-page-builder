# Landing Page Builder Skill

A Claude skill for building a complete 1-page business landing page, built from Asjad's real website work. Claude handles all the work end to end — brief, copy, page structure, mobile rules, speed basics, contact form and delivery checklist — with the owner involved only for the decisions, accounts/sign-ins/money and approval gates. It is modeled on the Basic $80 / 1 page / 3 days website package, and on the live store Fragrance Empire as the reference for mobile-first, fast-loading pages.

## What it does

Takes a landing page from brief to go-live in one repeatable workflow:

1. **Brief** — business name, service, area served, the one action the visitor should take, prices, benefits, social proof the owner can actually supply, contact details, tier. No building before the brief is confirmed.
2. **Copy** — headline formulas, benefit bullets, CTA button text, offer wording, form confirmation message — from `templates/section-copy-templates.md`.
3. **Page structure** — the six sections in order: hero, benefits, social proof, offer / CTA, contact form, footer. A full sample outline for a fictional cleaning service shows what a finished page looks like.
4. **Mobile-responsive rules** — single column on mobile, no horizontal scroll, readable font sizes, tap targets at least 44 × 44 px, form that works on a phone keyboard, tested on a real phone.
5. **Speed basics** — image sizes, no heavy embeds above the fold, minimal scripts, one font family.
6. **Contact form** — name, email/phone, service needed, message; confirmation message on screen, owner notified by email, tested with a real submission before go-live.
7. **Delivery checklist + approval gate** — nothing goes live until the owner approves the exact copy, the page look on desktop and mobile, and the checklist.
8. **First week** — enquiry check, fixes, delivery record.

## Who does what — Claude handles all the work end to end

Claude runs every step — brief, copy, structure, mobile and speed rules, form plan, checklist. The owner is involved only at three points: (1) business decisions only the owner can make (name, service, area, prices, contact details, the CTA, and the real facts behind any benefit, number or testimonial); (2) accounts, sign-ins and money (hosting / builder account, domain, form email destination, paid tools — all on the owner's own device); and (3) approval gates (page copy, page look on desktop and mobile, final delivery checklist). The two device-bound exceptions are publishing (owner's device or an approved browser session) and photos / logo (Claude plans them; the images come from the owner). Everything else is Claude's work — do not hand it back to the owner as homework.

## The live example store

- **Store:** Fragrance Empire — https://fragranceempire.my
- **Platform:** Shopify, Basic plan, Horizon theme, currency MYR, timezone Asia/Kuala_Lumpur, market Malaysia
- **Catalog:** 155 products = 142 single products + 13 bundles, 18 brands, 28 collections
- **Mobile:** about 90% of customers order by mobile — pages are built mobile-first and checked on a real phone
- **Built by:** Asjad Farooq, Shopify Store Designer — Fiverr gig https://www.fiverr.com/s/L34yBpA

## Service tiers (the seller's real website packages)

| Tier | Pages | Includes | Delivery | Revisions |
|---|---|---|---|---|
| Basic | 1 | 1-page landing page, mobile responsive, contact form | 3 days | Unlimited |
| Standard | Up to 5 | Up to 5 pages, contact form, basic SEO | 5 days | Unlimited |
| Premium | Up to 10 | Up to 10 pages, extra sections | 7 days | Unlimited |

Prices: Basic $80, Standard $180, Premium $350. Ask the owner which tier the build is before starting, and do not build a bigger scope than the tier covers without agreement. This skill builds the Basic 1-page tier.

## Files

```
landing-page-builder/
├── README.md                                  # this file
└── landing-page-builder/
    ├── SKILL.md                               # the Claude skill — the workflow itself
    ├── scripts/
    │   └── generate_landing_page.py           # builds a starter HTML page from a JSON brief
    └── templates/
        ├── section-copy-templates.md          # headline formulas, benefit bullets, CTA text, form copy
        ├── sample-page-outline.md             # full sample page outline (fictional "BrightClean Services")
        └── delivery-checklist.md              # brief + pre-launch checklist + approval gate
```

## Setup

### 1. Get the brief first

Fill in `templates/delivery-checklist.md` (Step 1 of `SKILL.md`) with the owner: business name, service, area served, the one CTA, prices, benefits, social proof, contact details, tier. Do not start building until the owner confirms the brief.

### 2. Choose the publishing route (one of these)

**Route A — Website builder (recommended to start).** The owner signs in to their builder (for example Wix, Squarespace, WordPress, or a Shopify page) on their own device and approves each step, or approves a browser session. Claude prepares everything (copy, section plan, image plan, form plan) and the owner applies it in the builder. No credentials needed.

**Route B — Static HTML file.** Claude generates a starter page with `scripts/generate_landing_page.py`, the owner approves the copy and look, and the owner uploads the finished HTML file to their hosting on their own device.

Do not use any other route. Do not paste passwords or credentials into the skill files, into chat, or into a repo — credentials live only in the owner's secure storage.

### 3. Photos and logo

Photos and the logo come from the owner. Claude writes the image plan (which image goes where, with what alt text) and never uses a photo that shows a different business, service or person. If a photo cannot be identified with certainty, it stays unused and is flagged for the owner.

### 4. Use in Claude

Copy the `landing-page-builder/` folder into a Claude skills directory (for example a Claude Code skills folder, or a repo Claude is pointed at), or keep this whole repo and point Claude at `landing-page-builder/SKILL.md`. Then ask Claude to run the workflow, for example: "Build a 1-page landing page for my cleaning business using the landing-page-builder skill. Tier: Basic."

## Honest limits — read before using

- **No direct hosting connection.** Claude does not have a built-in connection to the owner's hosting or builder. Publishing goes through the browser (owner's sign-in + approval) or by uploading a file the owner approves. Never claim direct auto-publishing without one of those.
- **No credentials in the skill.** No passwords, API keys, access tokens, bank details or secrets are stored in these files. If a step needs a login or a payment detail, the owner does it on their own device.
- **Approval gate is mandatory.** No copy, price, photo or form is published until the owner approves the exact final version. A changed headline, price, image or form needs fresh approval.
- **Never invent business facts, testimonials, reviews or numbers.** Every business name, service, price, area, phone number and email comes from the owner. Social proof comes only from real customers, in their own words, with their permission. If the business has no testimonials yet, the page leaves that block out or says so honestly.
- **Never claim a qualification, guarantee or result the owner did not confirm.** "Licensed", "insured", "guaranteed" and "same-day" go on the page only when the owner confirms them.
- **Do not promise a ranking, traffic number or conversion rate.** Basic SEO (page title, meta description, headings, alt text) is included; a Google ranking or a number of enquiries is not promised.
- **Paid tools need approval.** Never buy hosting, a domain, a form service or a paid plugin without the owner approving the exact price first.

## How to run one landing page build

1. Fill in the brief in `templates/delivery-checklist.md` and get the owner to confirm it.
2. Write the copy from `templates/section-copy-templates.md`.
3. Build the page structure from `templates/sample-page-outline.md`, apply the mobile rules and speed basics in `SKILL.md` Steps 4–5.
4. Set up the contact form (Step 6) and test it with a real submission.
5. Fill in the delivery checklist and get the owner's approval at the gate (Step 7).
6. Go live (Step 7), then do the first-week checks (Step 8).
