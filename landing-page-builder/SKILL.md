---
name: landing-page-builder
description: Build a complete 1-page business landing page — hero, benefits, social proof, offer/CTA, contact form, footer — mobile-responsive, fast-loading, with copy templates, a delivery checklist and an approval gate before go-live. Modeled on the Basic $80 / 1 page / 3 days website package (Fiverr gig "I will build a modern responsive website for your business"). Use when the user asks to build, design or write a landing page, a one-page business website, or a service page that collects enquiries through a contact form.
---

# Landing Page Builder

## When to use

Use this skill when the user asks to build, design, write or rebuild a 1-page business landing page, a one-page website for a local service or small business, or a page whose job is to turn visitors into enquiries through a contact form. The end result is a complete, ready-to-publish page — copy, sections, mobile layout, speed basics and contact form — not a mockup or a rough draft.

Do not use it for a multi-page site (that is the Standard $180 / 5 pages or Premium $350 / 10 pages package — see "Scope tiers" below), for a Shopify store (use the shopify-store-automation skill), or for an ad or a social post. If the user asks for a landing page and a store, build the page with this skill and the store with the store skill, and keep the two scopes separate.

## Who does what — Claude handles all the work end to end

Claude runs every step of the workflow below — brief, copy, page structure, mobile rules, speed basics, contact form plan, delivery checklist. The owner is involved only at these points:

1. **Business decisions only the owner can make** — business name, service and area served, prices or price range, contact details (email, phone, WhatsApp), the one action the visitor should take (call, WhatsApp, send the form, book a visit), and the real facts behind any benefit, number or testimonial. Claude drafts everything; the owner supplies the facts and approves them.
2. **Accounts, sign-ins and money** — creating or accessing the hosting / website builder account, connecting a domain, entering payment details for hosting or a paid tool, and the form's email destination. These happen on the owner's own device, with the owner's own details. Claude never handles the owner's password or payment credentials.
3. **Approval gates** — the owner approves the page copy, the page look (desktop and mobile), and the final delivery checklist before anything goes live (see Step 7). Nothing is published without that approval.

Two device-bound exceptions, stated honestly so the "end to end" claim is not overstated:

- **Publishing:** Claude produces the finished page (HTML file, or copy + layout plan for the owner's builder). Publishing it to the owner's domain or builder account happens on the owner's device, or in a browser session the owner approves. Claude never logs in as the owner.
- **Photos and logos:** Claude writes the image plan (which image goes where, with what alt text). The photos and logo themselves come from the owner. Claude never invents a business photo and never uses a photo that shows a different business, service or person.

Everything else — research, copywriting, section structure, mobile and speed rules, form plan, checklists — is Claude's work. Do not hand any of it back to the owner as homework.

## Page facts — the package this skill is modeled on (do not invent others)

The Basic website package this skill models is a 1-page landing page: mobile responsive, with a contact form, delivered in 3 days, unlimited revisions. The seller is Asjad Farooq, Shopify Store Designer — Fiverr gig https://www.fiverr.com/s/L34yBpA (Shopify store design) and the website gig "I will build a modern responsive website for your business". His live reference store is Fragrance Empire (https://fragranceempire.my) — Shopify, 155 products, 18 brands, Malaysia market.

## Hard limits — state them honestly, do not work around them

- **No credentials in the skill.** Never put an API key, password, access token, bank detail or secret in a skill file, in chat, or in a repo. Logins and payments happen on the owner's own device.
- **Approval gates are mandatory.** Nothing is published until the owner approves the exact copy, the page look (desktop and mobile), and the delivery checklist. A changed headline, price, photo or form needs fresh approval.
- **Never invent facts about the business.** Every business name, service, price, area served, phone number and email comes from the owner. If a fact is missing, ask — do not fill it in.
- **Never write fake testimonials, fake reviews, or fake numbers.** Social proof comes only from the real business owner — real customer words (with the customer's permission), real counts (years in business, jobs done, rating from a real listing), or real logos of real partners. If the business has no testimonials yet, the page says so honestly (for example "New customers welcome — first booking discount") or leaves the testimonial block out until the owner supplies one. Claude may draft wording only when a real customer asked for help with the wording and agrees with the text.
- **Never claim a service, qualification, guarantee or result the owner did not confirm.** "Licensed", "insured", "guaranteed", "same-day" and similar claims go on the page only when the owner confirms them in writing.
- **One page, one job.** A landing page has one clear action (the CTA). Do not add a second competing action, a shop, a blog or a booking system to a 1-page build without agreeing a bigger scope with the owner first.
- **Do not promise a ranking, a traffic number, or a conversion rate.** Basic SEO (page title, meta description, headings, alt text) is included; a Google ranking or a number of enquiries is not promised.
- **Paid tools need the owner's approval.** Never buy hosting, a domain, a form service or a paid plugin without the owner approving the exact price first. Free options only unless approved.

## Scope tiers — ask which one before starting

Mirror the seller's real website packages. This skill builds the Basic tier. Ask the owner which tier the build is, and do not build a bigger scope than the tier covers without agreement.

| Tier | Pages | Includes | Delivery | Revisions |
|---|---|---|---|---|
| Basic | 1 | 1-page landing page, mobile responsive, contact form | 3 days | Unlimited |
| Standard | Up to 5 | Up to 5 pages, contact form, basic SEO | 5 days | Unlimited |
| Premium | Up to 10 | Up to 10 pages, extra sections | 7 days | Unlimited |

Prices: Basic $80, Standard $180, Premium $350. If the owner asks for more than 1 page, stop and agree the tier (and price) before building — do not quietly build 5 pages on a Basic budget.

## The page structure — sections in order

Every landing page built with this skill has these six sections, in this order. Do not skip one and do not reorder them without the owner's agreement.

1. **Hero** — headline, subheadline, one clear CTA button. The visitor must understand what the business does, for whom, and what to do next, within 5 seconds.
2. **Benefits** — 3–4 benefits, outcome-focused (what the customer gets), not a feature list.
3. **Social proof** — testimonials, numbers, or logos. Real ones only, supplied by the owner (see Hard limits).
4. **Offer / CTA** — the offer restated plainly (what, how much, how long it lasts) plus the same CTA again.
5. **Contact form** — name, email or phone, message, service needed. Plus the business's real contact details next to it.
6. **Footer** — business name, contact details, service area, links (privacy, terms if the owner has them), copyright year.

## Workflow

### Step 1 — Brief (decisions first, no building before this)

Collect and write down, in `templates/delivery-checklist.md`:

1. Business name, service, and area served (city / region).
2. Who the customer is and what problem the business solves for them.
3. The one action the visitor should take (call, WhatsApp, send the form, book a visit). Pick one — the same CTA appears in the hero and in the offer section.
4. Services offered and prices (or price range, or "free quote"). Only prices the owner confirms.
5. Benefits: 3–4 outcomes the customer gets (for example: cleaned in one visit, no harsh chemicals, weekend slots). Each benefit must be a fact the owner confirms.
6. Social proof the owner can actually supply: real testimonials (customer words + first name only, with permission), real numbers (years in business, jobs completed), real logos. If none, record "none yet" and plan the page without a testimonial block.
7. Contact details for the form and the footer: email, phone / WhatsApp, and the email address form submissions go to.
8. Photos and logo: what the owner has, and what is still missing. No photo is used until the owner supplies it.
9. Tier (Basic / Standard / Premium) and the delivery date.
10. Anything the owner explicitly does NOT want (for example: no prices on the page, no testimonials yet, no WhatsApp button).

Do not start Step 2 until the brief is filled in and the owner has confirmed it. A missing price, phone number or CTA is a blocker, not something to guess.

### Step 2 — Copy (one section at a time, from the templates)

Write the copy from `templates/section-copy-templates.md`. Rules for every section:

- **Headline formulas:** use the formulas in the template (for example "[Service] in [Area] — [Outcome] in [Time]"). Fill in the brackets with the owner's real facts. Never write a headline that promises something the owner did not confirm.
- **One idea per section.** The hero sells the outcome; benefits prove it; social proof backs it; the offer asks for the action. Do not repeat the same sentence in three sections.
- **Short lines, plain words.** Headline under 10 words where possible. Benefit bullets one line each. No jargon, no superlatives the business cannot back up ("best", "number one", "guaranteed" only when the owner confirms them).
- **CTA button text:** use the templates (for example "Get My Free Quote", "Book My Cleaning", "Call Now"). The button text must name the action, not just say "Click here" or "Submit".
- **Social proof:** copy the owner's real testimonials word for word (fixing only spelling, and only with the owner's approval). Never invent a customer name, a star rating, or a number. If the owner supplies a number ("over 200 homes cleaned"), write it exactly as given and note the source in the checklist.

### Step 3 — Page structure (layout, from the sample outline)

Build the page from `templates/sample-page-outline.md` — the full sample for the fictional "BrightClean Services" shows what a finished outline looks like for every section. For the owner's real business:

1. List the six sections in order, with the approved copy under each.
2. Note the image or logo for each section that needs one, with its alt text (see Step 5). Sections with no owner-supplied photo use a plain colour block or a text layout — never a stock photo that shows a different business.
3. Keep the page to one screen of scrolling per section where possible. A landing page that takes ten screens to read is not a landing page.
4. The CTA button appears twice: once in the hero, once in the offer section. Both buttons do the same thing (scroll to the contact form, or open the call / WhatsApp link the owner chose).
5. The contact form sits directly above the footer, with the business's phone and email beside it so a visitor who does not want to fill in a form can still reach the business.

### Step 4 — Mobile-responsive rules (mobile first, because most visitors are on a phone)

Check every rule below on a real phone width (360–414 px) before the owner approves the page. Fragrance Empire's store sees about 90% of customers on mobile — assume a landing page is the same.

1. **Single column on mobile.** All sections stack into one column. No side-by-side columns, no text next to an image, below 768 px width.
2. **No horizontal scroll.** Nothing on the page is wider than the screen. Test by scrolling sideways — if anything moves, fix it before approval.
3. **Readable font sizes.** Body text at least 16 px, headings at least 24 px (hero headline 32 px or larger) on mobile. Never set body text below 16 px — small text is unreadable and browsers zoom it.
4. **Tap targets.** Buttons and links at least 44 × 44 px, with at least 8 px of space between tappable items. The CTA button is full-width on mobile.
5. **Hero fits one screen.** On mobile the hero headline, subheadline and CTA button are all visible without scrolling where possible; the hero image (if any) never pushes the CTA below the fold.
6. **Form works on a phone keyboard.** Email field opens the email keyboard, phone field opens the number keyboard, message field is tall enough to type in (at least 4 lines). Labels stay visible above each field.
7. **Images scale.** Every image is 100% width of its container at most, with height auto. No fixed pixel widths on images.
8. **Test on a real phone, not just a resized desktop window.** Check the hero, benefits, form and footer on an actual phone before the owner approves.

### Step 5 — Speed basics (a slow page loses the visitor)

1. **Image sizes:** every image under 200 KB where possible, never over 500 KB. Resize images to the size they are shown at (a hero image shown at 800 px wide does not need to be 4000 px wide). Use JPG for photos, PNG only for logos / graphics with transparency, WebP where the builder supports it.
2. **Alt text on every image:** name what the image shows (for example "BrightClean cleaner wiping a kitchen counter"). Alt text is also the SEO text for the image.
3. **No heavy embeds above the fold.** No video player, map, chat widget or social feed in the hero. If the owner wants a map or a video, it goes below the form or in the footer.
4. **Minimal scripts:** no more than the builder / hosting needs plus the form. No extra trackers, pop-ups or chat widgets unless the owner explicitly asks for them — and then record each one in the checklist.
5. **One font family, two weights at most.** Do not load four font families and six weights for one page.
6. **Check before approval:** load the page on a phone on a mobile connection and note how long the hero takes to appear. If it takes more than about 3 seconds, shrink the hero image first — that is the usual cause.

### Step 6 — Contact form (fields, and what happens after submit)

Fields — exactly these, no more without the owner's agreement:

| Field | Type | Required? |
|---|---|---|
| Name | Text | Yes |
| Email or phone | Email / tel (at least one of the two) | Yes — one of them |
| Service needed | Dropdown or radio (the owner's service list) | Yes |
| Message | Text area | No (optional) |

After submit, all three of these must happen:

1. **Confirmation message on screen** — the visitor sees it immediately, for example: "Thank you, [Name]. We received your message and will reply within one business day." The message must state the real reply time the owner confirms (for example "within 24 hours", "by the next business day") — never promise "within an hour" unless the owner confirms it.
2. **Owner notified** — the submission goes to the email address the owner gave in the brief (or to the form service the owner chose). Test this with a real submission before go-live: fill in the form once, confirm the email arrives, then delete the test submission.
3. **No dead end** — the confirmation screen also shows the business phone / WhatsApp so a visitor who needs an urgent answer can call instead of waiting.

Form rules:

- The form's email destination is the owner's real email, set on the owner's device. Claude never enters the owner's email password or form-service login.
- Do not add fields the owner did not ask for (no date of birth, no address, no payment details on a landing page form).
- Spam protection: use the builder's built-in option (for example a honeypot or reCAPTCHA) if available. Do not add a paid anti-spam service without the owner's approval.
- If the form is a third-party embed, the embed goes below the offer section and the page still loads fast (see Step 5, rule 3).

### Step 7 — Delivery checklist + approval gate

Complete `templates/delivery-checklist.md` for the page. Then stop and get the owner's approval for: the page copy, the page look (desktop and mobile), the form (tested with a real submission), and the checklist itself.

Go live only after approval. The go-live steps:

1. Publish the page (owner's device / approved browser session) to the agreed domain or builder.
2. Open the live page on a phone and on a desktop: hero, benefits, social proof, offer, form, footer — all six sections present, in order.
3. Fill in the live form once with a test message, confirm the owner receives it, then delete the test submission.
4. Click every link on the live page (CTA buttons, phone / email links, footer links). A link that goes nowhere is a launch blocker.
5. Return the live page URL to the owner, with the tier delivered and anything still pending (for example a photo the owner still has to send).

### Step 8 — After go-live (first week)

1. Ask the owner whether any enquiries came through the form, and whether the notification email arrived each time.
2. Fix any broken link, wrong price, wrong phone number or missing image the owner reports, and re-verify live after each fix.
3. Do not change copy, prices, offers or the form without the owner's approval.
4. Record what was delivered (page URL, tier, sections, form destination) in the checklist so the next page starts from a known state.

## How to run one landing page build

1. Fill in the brief (Step 1) and get the owner to confirm it.
2. Write the copy from `templates/section-copy-templates.md` (Step 2).
3. Build the page structure from `templates/sample-page-outline.md` (Step 3), apply the mobile rules (Step 4) and the speed basics (Step 5).
4. Set up the contact form and test it with a real submission (Step 6).
5. Fill in `templates/delivery-checklist.md` and get the owner's approval at the gate (Step 7).
6. Go live (Step 7), then do the first-week checks (Step 8).

## Starter page generator

`scripts/generate_landing_page.py` builds a starter HTML file from the section templates — a single-column, mobile-responsive skeleton with all six sections, the copy placeholders filled in from a small JSON brief, and the speed and mobile rules already applied. Run it to get a working first draft, then replace the placeholder copy with the owner's approved copy and the placeholder images with the owner's real photos. It never writes fake testimonials: the social-proof section is left empty unless the brief supplies real ones.
