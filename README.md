# Ideal Car — Site Web

Site vitrine statique pour **Ideal Car**, carrosserie à Meyrin-Genève.  
Route du Mandemant 15, 1217 Meyrin · +41 78 965 75 76 · ideal.car76@yahoo.com

---

## Structure des fichiers

```
Ideal Car/
├── index.html               # Page principale — version anglaise
├── index-fr.html            # Page principale — version française
├── mentions-legales.html    # Mentions légales EN
├── mentions-legales-fr.html # Mentions légales FR
├── logo-idealcar-transparent.png
├── Eurostile BoldItalic.ttf
├── Panamera après réparation.jpg
├── Panamera avant réparation.jpg
└── carrosserie-geneve/
    └── static/images/
        └── logo-idealcar.png
```

---

## Architecture

- **100% statique** — aucun serveur, aucune dépendance externe (hors Google Fonts)
- **Bilingue FR / EN** — deux fichiers séparés avec switcher de langue dans le nav
- **Tout inline** — CSS et JS intégrés dans chaque fichier HTML
- **Police de marque** — Eurostile BoldItalic (locale, `font-display: swap`)

---

## Sections (ordre de la page)

| Section | ID | Notes |
|---|---|---|
| Splash screen | — | Animation d'entrée 2.5s, noir + "Ideal Car" |
| Header nav | — | Sticky, glassmorphism, switcher langue |
| Hero | `#hero` | Plein écran, centré verticalement |
| Carrosserie (Bento) | `#expertise` | Grid bento 4 services |
| Services rapides | `#rapides` | Cards compactes |
| Pneus | `#saisonnier` | Section saisonnière |
| À propos | `#about` | Stats + logo watermark |
| Avant / Après | — | Slider interactif |
| Avis clients | `#avis` | Témoignages + bouton Google Review |
| FAQ | `#faq` | Accordéon 3 questions |
| Contact | `#contact` | Formulaire + coordonnées + horaires |
| Rendez-vous | `#rdv` | Système de réservation par onglets |

---

## Fonctionnalités JS

- **Splash screen** — plein écran au chargement, supprimé du DOM après 2.85s
- **Scroll reveal** — Intersection Observer, fade + slide sur les sections
- **FAQ accordéon** — `max-height` CSS + `aria-expanded`
- **Avant/Après slider** — drag souris et touch
- **Cookie banner** — glassmorphism, persistance `localStorage`
- **Header scroll** — classe `.scrolled` au défilement
- **Menu mobile** — hamburger avec nav déroulante
- **Formulaire photo** — drag & drop + preview

---

## Identité visuelle

| Token | Valeur |
|---|---|
| `--accent` | `#D42B2B` (rouge automobile) |
| `--accent-dark` | `#b01f1f` |
| `--bg` | `#F8F9FA` |
| `--dark` | `#000000` |
| `--muted` | `#6b7280` |
| Police corps | Inter (Google Fonts) |
| Police marque | Eurostile BoldItalic (locale) |

**Éléments en rouge :** boutons CTA, labels de section (pole-label), coches ✓, icônes de services, soulignement du titre À propos.

---

## Déploiement

Le site est prévu sur **`www.idealcar-geneve.ch`**.

Canonical URLs déjà configurées dans chaque fichier.  
`mentions-legales` est en `noindex, follow`.

### Checklist avant mise en ligne

- [ ] Remplacer l'URL Google Review par le vrai Place ID : `https://search.google.com/local/writereview?placeid=PLACE_ID`
- [ ] Ajouter les photos de la galerie (section supprimée temporairement, prête à réintégrer)
- [ ] Vérifier le formulaire de contact (action EmailJS ou backend à brancher)
- [ ] Tester le formulaire WhatsApp : `https://wa.me/41789657576`
- [ ] Vérifier l'affichage mobile sur iOS Safari et Android Chrome

---

## À faire / Idées futures

- [ ] Réintégrer la galerie photo avec les vraies réalisations
- [ ] Brancher le formulaire de contact (EmailJS ou Formspree)
- [ ] Ajouter un sitemap XML
- [ ] Optimiser les images en WebP
