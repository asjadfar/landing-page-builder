#!/usr/bin/env python3
"""generate_landing_page.py — build a starter 1-page landing page from a brief.

Part of the landing-page-builder Claude skill.
See landing-page-builder/SKILL.md for the full workflow.

What it does:
  Reads a small JSON brief (see --example for the format) and writes a
  single self-contained HTML file: a 1-page landing page with all six
  sections in order (hero, benefits, social proof, offer / CTA, contact
  form, footer), a single-column mobile layout, readable font sizes,
  44 px tap targets, no horizontal scroll, and no external scripts.

  The output is a STARTER page, not a finished page:
    - Replace every [bracketed] placeholder with the owner's approved copy.
    - Replace the placeholder image with the owner's real photo.
    - The social-proof section is EMPTY unless the brief supplies real
      testimonials or real numbers. This script never invents a
      testimonial, a review, a customer name, or a number.
    - The contact form's action must be set to the owner's real form
      endpoint (or their builder's form) before go-live. Until then it
      shows a note instead of submitting anywhere.

Usage:
  python3 generate_landing_page.py brief.json [output.html]
  python3 generate_landing_page.py --example > brief-example.json

  Example:
    python3 generate_landing_page.py --example > brief.json
    python3 generate_landing_page.py brief.json brightclean.html

Requirements: Python 3, standard library only. No credentials, no network.
"""

import html
import json
import sys

# A clearly fictional example brief. Every value here is a placeholder.
EXAMPLE_BRIEF = {
    "business_name": "BrightClean Services",
    "service": "home cleaning",
    "area": "Springfield",
    "headline": "A spotless home, without lifting a finger",
    "subheadline": "Professional home cleaning in Springfield. Book in 2 minutes — we bring everything we need.",
    "cta_text": "Get My Free Quote",
    "cta_target": "#contact",
    "benefits": [
        {"title": "Done in one visit", "text": "Most homes are fully cleaned in a single 2–3 hour visit."},
        {"title": "We bring our own supplies", "text": "Eco-friendly products and equipment included — you provide nothing."},
        {"title": "Weekend slots available", "text": "Book Saturday or Sunday if weekdays do not work for you."},
        {"title": "Free re-clean promise", "text": "Not happy with a room? We come back and clean it again, free."},
    ],
    "testimonials": [],
    "numbers": [],
    "offer": "First clean 20% off — book before the end of the month.",
    "offer_detail": "20% off your first regular home clean. New customers only.",
    "services": ["Regular home clean", "Deep clean", "Move-in / move-out clean"],
    "contact_email": "hello@example.com",
    "contact_phone": "+1 555-0100",
    "reply_time": "within one business day",
    "form_action": "",
}

REQUIRED_FIELDS = ["business_name", "service", "area", "headline", "subheadline"]


def esc(value):
    """HTML-escape a string so brief text cannot break the page."""
    return html.escape(str(value), quote=True)


def validate(brief):
    """Return a list of problems with the brief. Empty list means OK."""
    problems = []
    for field in REQUIRED_FIELDS:
        if not brief.get(field):
            problems.append("Missing required field: %s" % field)
    for i, benefit in enumerate(brief.get("benefits", []), 1):
        if not benefit.get("title") or not benefit.get("text"):
            problems.append("Benefit %d needs both a title and text" % i)
    if len(brief.get("benefits", [])) > 4:
        problems.append("Too many benefits: %d (maximum 4)" % len(brief["benefits"]))
    for i, t in enumerate(brief.get("testimonials", []), 1):
        if not t.get("quote") or not t.get("name"):
            problems.append("Testimonial %d needs both a quote and a name" % i)
    return problems


def social_proof_html(brief):
    """Social proof from real owner-supplied facts only.

    Returns an empty string when the brief has no testimonials and no
    numbers, so the page never shows invented social proof.
    """
    testimonials = brief.get("testimonials", [])
    numbers = brief.get("numbers", [])
    if not testimonials and not numbers:
        return ""
    parts = ['<section id="proof">', "<h2>What our customers say</h2>"]
    for t in testimonials:
        parts.append(
            '<blockquote><p>"%s"</p><cite>— %s</cite></blockquote>'
            % (esc(t["quote"]), esc(t["name"]))
        )
    for n in numbers:
        parts.append(
            '<p class="number"><strong>%s</strong> %s</p>'
            % (esc(n["value"]), esc(n["label"]))
        )
    parts.append("</section>")
    return "\n".join(parts)


def build_html(brief):
    """Build the full starter page from a validated brief."""
    benefits = "\n".join(
        '    <li><strong>%s</strong><br>%s</li>'
        % (esc(b["title"]), esc(b["text"]))
        for b in brief.get("benefits", [])
    )
    services = "\n".join(
        '      <option>%s</option>' % esc(s) for s in brief.get("services", [])
    )
    proof = social_proof_html(brief)
    form_action = brief.get("form_action") or ""
    form_note = ""
    if not form_action:
        form_note = (
            '    <p class="form-note">Form not connected yet — set the form '
            "endpoint (the owner's form service or builder) before go-live.</p>\n"
        )

    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{business} — {service} in {area}</title>
<meta name="description" content="{subheadline}">
<style>
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; font-family: system-ui, -apple-system, sans-serif;
         font-size: 17px; line-height: 1.6; color: #222; }}
  section, footer {{ padding: 2rem 1.25rem; max-width: 720px; margin: 0 auto; }}
  h1 {{ font-size: 32px; line-height: 1.2; margin: 0 0 0.75rem; }}
  h2 {{ font-size: 26px; line-height: 1.25; margin: 0 0 1rem; }}
  img {{ max-width: 100%; height: auto; display: block; }}
  .cta {{ display: block; width: 100%; min-height: 48px; padding: 14px 20px;
         background: #0b6e4f; color: #fff; text-align: center; font-size: 18px;
         font-weight: bold; text-decoration: none; border: none; border-radius: 8px;
         cursor: pointer; }}
  ul {{ padding-left: 1.25rem; }}
  li {{ margin-bottom: 1rem; }}
  blockquote {{ margin: 1rem 0; padding: 1rem; background: #f4f4f4;
               border-left: 4px solid #0b6e4f; }}
  blockquote p {{ margin: 0 0 0.5rem; }}
  .number {{ font-size: 20px; }}
  label {{ display: block; font-weight: bold; margin: 1rem 0 0.25rem; }}
  input, select, textarea {{ width: 100%; padding: 12px; font-size: 17px;
         border: 1px solid #999; border-radius: 6px; }}
  textarea {{ min-height: 120px; }}
  button.cta {{ margin-top: 1.25rem; }}
  footer {{ background: #222; color: #fff; max-width: none; }}
  footer .inner {{ max-width: 720px; margin: 0 auto; }}
  footer a {{ color: #fff; }}
  .form-note {{ background: #fff3cd; padding: 0.75rem; border-radius: 6px; }}
</style>
</head>
<body>

<section id="hero">
  <h1>{headline}</h1>
  <p>{subheadline}</p>
  <a class="cta" href="{cta_target}">{cta_text}</a>
</section>

<section id="benefits">
  <h2>Why choose {business}</h2>
  <ul>
{benefits}
  </ul>
</section>

{proof}

<section id="offer">
  <h2>{offer}</h2>
  <p>{offer_detail}</p>
  <a class="cta" href="{cta_target}">{cta_text}</a>
</section>

<section id="contact">
  <h2>Get in touch</h2>
  <p>Email: <a href="mailto:{email}">{email}</a><br>
  Phone: <a href="tel:{phone}">{phone}</a></p>
  <form action="{form_action}" method="post">
    <label for="name">Your name</label>
    <input id="name" name="name" type="text" required autocomplete="name">
    <label for="email">Email or phone</label>
    <input id="email" name="email" type="text" required autocomplete="email">
    <label for="service">Service needed</label>
    <select id="service" name="service" required>
{services}
    </select>
    <label for="message">Message (optional)</label>
    <textarea id="message" name="message"></textarea>
    <button class="cta" type="submit">Send my enquiry</button>
  </form>
{form_note}  <p>We reply {reply_time}.</p>
</section>

<footer>
  <div class="inner">
    <p><strong>{business}</strong> — {service} in {area}</p>
    <p>Email: <a href="mailto:{email}">{email}</a> &middot;
    Phone: <a href="tel:{phone}">{phone}</a></p>
    <p>&copy; 2026 {business}. All rights reserved.</p>
  </div>
</footer>

</body>
</html>
""".format(
        business=esc(brief["business_name"]),
        service=esc(brief["service"]),
        area=esc(brief["area"]),
        headline=esc(brief["headline"]),
        subheadline=esc(brief["subheadline"]),
        cta_text=esc(brief.get("cta_text", "Get in touch")),
        cta_target=esc(brief.get("cta_target", "#contact")),
        benefits=benefits,
        proof=proof,
        offer=esc(brief.get("offer", "")),
        offer_detail=esc(brief.get("offer_detail", "")),
        email=esc(brief.get("contact_email", "")),
        phone=esc(brief.get("contact_phone", "")),
        services=services,
        form_action=esc(form_action),
        form_note=form_note,
        reply_time=esc(brief.get("reply_time", "within one business day")),
    )


def main(argv):
    if len(argv) == 2 and argv[1] == "--example":
        print(json.dumps(EXAMPLE_BRIEF, indent=2))
        return 0
    if len(argv) < 2 or len(argv) > 3:
        print("Usage: generate_landing_page.py brief.json [output.html]", file=sys.stderr)
        print("       generate_landing_page.py --example", file=sys.stderr)
        return 2

    brief_path = argv[1]
    output_path = argv[2] if len(argv) == 3 else "landing-page.html"

    try:
        with open(brief_path, "r", encoding="utf-8") as f:
            brief = json.load(f)
    except FileNotFoundError:
        print("FAIL: brief file not found: %s" % brief_path, file=sys.stderr)
        return 1
    except json.JSONDecodeError as e:
        print("FAIL: brief is not valid JSON: %s" % e, file=sys.stderr)
        return 1

    problems = validate(brief)
    if problems:
        print("FAIL: brief has %d problem(s):" % len(problems), file=sys.stderr)
        for p in problems:
            print("  - %s" % p, file=sys.stderr)
        return 1

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(build_html(brief))

    print("PASS: wrote %s" % output_path)
    if not brief.get("testimonials") and not brief.get("numbers"):
        print("NOTE: no testimonials or numbers supplied — social-proof "
              "section left out. Add real ones from the owner, never invented ones.")
    if not brief.get("form_action"):
        print("NOTE: form_action is empty — connect the form endpoint before go-live.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
