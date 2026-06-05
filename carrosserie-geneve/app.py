"""
Carrosserie Pro Genève — app.py
SSR Flask : CSS inliné + JSON-LD Schema.org pour PageSpeed 100/100
"""

import json
import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates", static_folder="static")

ROOT = os.path.dirname(__file__)


def _load_data() -> dict:
    with open(os.path.join(ROOT, "data.json"), encoding="utf-8") as fh:
        return json.load(fh)


def _load_css() -> str:
    css_path = os.path.join(ROOT, "static", "css", "style.css")
    with open(css_path, encoding="utf-8") as fh:
        return fh.read()


def _build_schema(data: dict) -> str:
    b = data["business"]
    seo = data["seo"]

    schema = {
        "@context": "https://schema.org",
        "@type": "AutoRepair",
        "name": b["name"],
        "description": seo["description"],
        "url": b["website"],
        "telephone": b["phone"],
        "email": b["email"],
        "image": b["website"] + seo["og_image"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": b["address"]["streetAddress"],
            "addressLocality": b["address"]["addressLocality"],
            "postalCode": b["address"]["postalCode"],
            "addressCountry": b["address"]["addressCountry"],
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": b["geo"]["latitude"],
            "longitude": b["geo"]["longitude"],
        },
        "openingHoursSpecification": [
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": spec["dayOfWeek"],
                "opens": spec["opens"],
                "closes": spec["closes"],
            }
            for spec in b["schema_opening_hours"]
        ],
        "priceRange": b["priceRange"],
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": b["aggregate_rating"]["value"],
            "reviewCount": b["aggregate_rating"]["count"],
        },
        "hasMap": (
            f"https://www.google.com/maps/search/"
            f"{b['address']['streetAddress'].replace(' ', '+')}"
            f"+{b['address']['postalCode']}+{b['address']['addressLocality']}"
        ),
    }
    return json.dumps(schema, ensure_ascii=False, indent=2)


@app.route("/")
def index():
    data = app.config["SITE_DATA"]
    return render_template(
        "index.html",
        **data,
        schema=_build_schema(data),
        inline_css=app.config["INLINE_CSS"],
        canonical_path="/",
        current_year=datetime.now().year,
    )


@app.route("/contact", methods=["POST"])
def contact():
    """Point d'entrée du formulaire — à connecter à un service mail (ex: Flask-Mail)."""
    name    = request.form.get("name", "").strip()
    phone   = request.form.get("phone", "").strip()
    email   = request.form.get("email", "").strip()
    service = request.form.get("service", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not phone:
        return redirect(url_for("index") + "#contact")

    # TODO : envoyer l'email via Flask-Mail ou un service SMTP
    # mail.send_message(subject=f"Devis — {name}", ...)

    return redirect(url_for("index") + "#contact?sent=1")


@app.route("/robots.txt")
def robots():
    data = app.config["SITE_DATA"]
    content = (
        "User-agent: *\n"
        "Allow: /\n"
        f"Sitemap: {data['business']['website']}/sitemap.xml\n"
    )
    return content, 200, {"Content-Type": "text/plain"}


@app.route("/sitemap.xml")
def sitemap():
    data = app.config["SITE_DATA"]
    base = data["business"]["website"]
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f'  <url><loc>{base}/</loc><changefreq>monthly</changefreq><priority>1.0</priority></url>\n'
        '</urlset>'
    )
    return xml, 200, {"Content-Type": "application/xml"}


def create_app():
    data = _load_data()
    css  = _load_css()
    app.config["SITE_DATA"]  = data
    app.config["INLINE_CSS"] = css
    return app


if __name__ == "__main__":
    create_app().run(debug=True, host="0.0.0.0", port=5000)
