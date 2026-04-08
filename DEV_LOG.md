# F1R3FLY.IO Website — Dev Log
*Last updated: March 30, 2026*

## Project Path
`/Users/hannahadams/Library/CloudStorage/Dropbox/01 ACTIVE WORK/F1R3FLY PROJECTS/02 F1R3FLY Website/08 Website Rebuild/`

## File Structure
- `index.html` — single-page site, all sections
- `css/styles.css` — mobile-first, breakpoints at 768px (tablet) and 1024px (desktop)
- `js/main.js` — scroll animations, accordion logic, mobile menu, parallax
- `images/` — all assets (logo-icon.svg, team photos, partner logos, parallax layers)

---

## Architecture

### Section Template System
- Nav sections (Home, Technology, Developers, Clients, Partners, Blog) use `.section.section-page`
- Fixed height: `calc(85vh - var(--nav-height))` for consistent scroll landing
- **Exception:** Team section uses `.section` only (content too tall for 85vh), with inline `scroll-margin-top: var(--nav-height)`
- `scroll-margin-top: var(--nav-height)` on `.section-page` handles nav offset
- Native browser `scroll-behavior: smooth` (no custom JS scroll)

### Gradient Connector Bands
- `.section-band` sits between nav sections as visual rhythm/connective tissue
- Gradient classes: `.neutral`, `.teal`, `.magenta`, `.green`, `.purple`
- Content inside bands: eyebrow labels, headings, body text, accordions

### FAQ System (Current)
- 4 simple `.section-band` wrappers with accordions (NOT sticky panels — those were removed Feb 23)
- Bands: Core Architecture (neutral), Developer-Focused (teal), Client-Focused (magenta), Partner-Focused (green)
- Accordion scope: `.closest('.section')` in main.js
- Item spacing: 12px padding-bottom/margin-bottom, 8px question padding
- Transition: 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94)

### Contact Form
- Formspree free tier, endpoint: `mreabjwv`
- Sends to: general.manager@f1r3fly.io (Lilia) + hannah.adams.design@gmail.com
- Both emails verified on Formspree account (Hannah Adams login)
- 50 submissions/month limit (sufficient for pre-launch)

### Hero Section
- Logo: `logo-icon.svg` in `.hero-logo` wrapper
- Mobile: max-width 160px | Tablet (768px+): 180px | Desktop (1024px+): 196px
- Subtitle "A Subsidiary of F1R3FLY Industries" breaks into 2 lines on mobile via `<br class="mobile-break">`
- `.mobile-break` hidden at 768px+ via `display: none`

---

## CSS Breakpoint Structure
- **Base (mobile-first):** All default styles
- **768px+ (tablet):** `.mobile-break` hidden, hero-logo 180px, nav adjustments, 2-col grids
- **1024px+ (desktop):** Full nav links visible, hamburger hidden, hero-logo 196px, 3-col grids, 4-col team grid

---

## Known Issues / To-Do

### ✅ RESOLVED: Mobile "Home" nav scroll bug
Fixed in Session 3. All anchor clicks now manually calculate scroll offset accounting for nav height.

### ⚠️ DevTools responsive mode: nav position: fixed glitch
Chrome DevTools responsive emulation breaks `position: fixed` + `backdrop-filter`. Nav scrolls away in emulator but works fine in real narrow browser and on actual devices. Not a real bug — just don't trust DevTools for fixed-position testing.

### 🟡 General mobile fine-tuning
- Just started responsive pass at 400px width
- Need to check all sections at various mobile breakpoints
- Card grids, team photos, partner logos all need mobile review

---

## Session Log

### Feb 23, 2026 — Session 1 (earlier today)
- Removed FAQ sticky panel system (~55 lines CSS)
- Replaced with 4 simple `.section-band` gradient wrappers
- Compressed FAQ item spacing (30px → 12px)
- Updated accordion JS scope
- Team section: removed `.section-page`, added inline scroll-margin-top
- Diana Yevitska photo: `object-position: center 20%` to fix head crop
- Blog section: kept as standalone on black (consistent with other nav sections)

### Feb 23, 2026 — Session 2 (this session)
- Confirmed Formspree contact form routes to general.manager@f1r3fly.io (already set up)
- Hero logo: mobile size reduced 280px → 160px
- Hero subtitle: added mobile line break (`<br class="mobile-break">`)
- Removed `white-space: nowrap` from `.hero-subsidiary` base styles, restored at 768px+
- Identified "Home" mobile nav scroll bug (not yet fixed)

### Feb 23, 2026 — Session 3
- **Fixed: Mobile "Home" nav scroll bug** — All anchor clicks now use `preventDefault` + manual `scrollTo` with `--nav-height` offset via `requestAnimationFrame`. Fixes both mobile menu (body overflow reflow) and desktop (scrollIntoView not respecting scroll-margin-top).
- **Fixed: Content overlap on mobile** — Changed `.section-page` from `height` to `min-height` at base (mobile) level, so sections grow to fit content. Restored fixed `height: calc(85vh - var(--nav-height))` at 768px+ where content fits.
- **Investigated: Nav scrolling away on mobile** — Confirmed this is a Chrome DevTools responsive emulation bug, NOT a CSS issue. Nav stays fixed in real narrow browser window. `position: fixed` + `backdrop-filter` has known DevTools emulation issues.
- **Removed `overflow-x: hidden` from body** — Was on `body`, removed entirely (hero already contains parallax with its own `overflow: hidden`). Monitor for horizontal scroll on real devices.
- **Client logos: 2-col grid on mobile** — Changed `.client-logo-grid` base from `repeat(4, 1fr)` to `repeat(2, 1fr)`, restores to 4-col at 768px+. Increased logo sizes from 55%/45% to 75%/60%.
- **Client body text: stacked on mobile** — Replaced inline `2fr 1fr` grid with `.client-body-grid` class. Stacks single-column on mobile, 2-col at 768px+.

---

### Mar 16, 2026 — Session 4
- **Typography swap:** Replaced Adobe Typekit (Brandon Grotesque) with Google Fonts (Josefin Sans 100/300/400/600/700 + Source Sans 3 300/400/600/700). Updated `--font-heading` and `--font-body` CSS variables. Zero remaining references to Brandon in codebase.
- **Brand color corrections:** `--color-bg` → `#000000`, `--color-accent` → `#3FA9F5`, `--color-highlight` → `#F3D630`, `--gradient-brand` → `#F3D630 → #8BB999` (Yellow → Sage), `--gradient-developer` → `#007BC4 → #009188`.
- **Logo replacement:** Nav now uses `f1r3fly-io-horizontal-logo.svg` (bug + wordmark baked in) via `.nav-logo-wordmark` class at 40px height. Hero uses `f1r3fly-io-vertical-logo.svg` at 200×178px. Removed separate `<h1>` heading and `.nav-logo-text` span since wordmark is in the SVG.
- **Eyebrow labels:** Changed `.label` from `display: block` to `display: inline-block` so gradient maps to text width, not container width. Removed `display: block` from `.faq-subsection-label`. Gradient now renders Yellow→Sage correctly on all labels.
- **Nav subtitle gradient fix:** Added `width: fit-content` to `.nav-logo-subtitle`. Removed duplicate gradient from child `<a>` — parent gradient now covers entire subtitle. Changed tablet breakpoint from `display: inline` to `display: inline-block`.
- **Card h3 style:** Changed `.card h3` to Source Sans 3 (`--font-body`), 16px, bold (700) — matches body text size.
- **Ticker text:** Changed from gradient text to `color: rgba(255, 255, 255, 0.35)` with `mix-blend-mode: overlay`.
- **Full audit document created:** `F1R3FLY-Website-Audit-2026-03-16.md` — covers content, colors, typography, team roster, technical issues, deployment questions, prioritized fix list.

---

### Mar 17, 2026 — Session 5
- **Blog cards built:** 17 expandable article cards injected via JS into `#blogGrid`. Each card: tag (AI & Agents / Compositionality / Developer / Philosophy), title, description, date, expand/collapse with key takeaways, Substack link. Content sourced from Daria's SEO delivery. Hover gradients cycle through purple, teal, magenta, green (6n rotation).
- **Blog card CSS added to styles.css:** `.blog-parent`, `.blog-tag`, `.blog-expand-btn`, `.blog-child-grid`, `.blog-child`, expanded state (`grid-column: 1 / -1`), tag color classes (`.blog-tag-ai` #3FA9F5, `.blog-tag-comp` #F3D630, `.blog-tag-phil` #8BB999, `.blog-tag-dev` #009188).
- **Quote band added** between Blog and Contact sections: Greg Meredith pull quote in `.section-band.neutral`.
- **Bug fix: blog cards invisible (opacity: 0).** Cards were generated with `animate-in from-bottom` class, but IntersectionObserver had already run before JS injected the cards — so observer never fired on them. Cards rendered as transparent boxes. Fix: removed `animate-in from-bottom` from JS card generation (`card.className='blog-parent'`). Cards now render immediately. Fade-in animation can be restored later by re-triggering the observer after injection.
- **Bug fix: section content bleed-through on tablet/desktop.** The 768px+ breakpoint set `.section-page { height: calc(85vh - var(--nav-height)) }` — a fixed height. Any section with content taller than 85vh (blog with 17 cards, plus others Daria flagged) overflowed, and subsequent sections rendered underneath the overflow. Fix: changed `height` to `min-height` at the 768px+ breakpoint, matching the mobile-first rule. The CSS comment already acknowledged this was the correct approach ("Mobile: min-height instead of height to prevent content overflow/overlap") — the tablet override just wasn't following it.
- **Daria's keyword framework reviewed.** Document `key_words_for_the_web_site.docx` — five clusters: Core Intent, Pain Point Hooks, Use Case, Audience-Specific, Brand Differentiators. Directly useful for meta tags, alt text, and content strategy.

---

---

### Mar 20, 2026 — Session 6
- **Individual article pages built:** Per Daria's meeting (March 20 morning call), switched from expandable inline cards to 17 individual article HTML pages. Each page follows Daria's specified structure: H1 title, Substack subtitle link, "In brief" intro, Key Takeaways (bullets), Key Questions (bullets), Why It Matters (prose), Related internal cross-link, Substack link, topic tags.
- **Article file structure:** `articles/` directory with 17 HTML files using keyword-rich slugs from Daria's doc. Generator script (`generate_articles.py`) at website rebuild root — regenerates all 17 from data + template.
- **Article CSS:** `css/article.css` — article-specific styles inheriting base `styles.css`. Width matches site `--container-max` (1400px). H1 at `font-weight: 500` (medium). Eyebrow tags at 16px/400 matching site `.label` spec. Dashed border box (`.article-box`) wraps article content below breadcrumb.
- **Blog section updated on index.html:** Cards changed from expandable `<div>`s to `<a>` link cards pointing to `articles/[slug].html`. Removed expand/collapse JS, detail content, and Substack links from cards. Added `blog-link-card` and `blog-read-more` CSS classes.
- **Page transitions added:** Directional slide transitions between blog grid and article pages. Blog card click → black panel slides right (going deeper). "← Ideas & Research" back link → panel slides left (going back). CSS keyframe animations (`slideRight` / `slideLeft`) on `.page-transition` overlay in `styles.css`. JS in `main.js` intercepts link clicks, plays transition, navigates at midpoint.
- **Smooth scroll conflict fixed:** Back link previously navigated to `index.html#blog`, triggering CSS `scroll-behavior: smooth` which caused a "rush down" animation competing with the slide transition. Fix: back link now navigates to `index.html?scrollto=blog`. JS on page load detects `?scrollto=` param, forces `scrollBehavior: auto` (instant jump), scrolls to target, then cleans URL to `#blog` and restores smooth scroll.
- **Files modified:** `index.html` (blog section JS), `css/styles.css` (transition overlay, link card styles), `css/article.css` (new file, article layout), `js/main.js` (transition logic, scrollto handler), `generate_articles.py` (article generator script), `articles/*.html` (17 generated files).

---

### Mar 22, 2026 — Session 7
- **SPA router built:** Replaced old page-transition overlay (black panel slide) with a proper SPA router using History API. Blog card clicks now fetch article pages via `fetch()`, extract `<main id="app">` content, crossfade swap in place, and push URL to history. No full page reload going forward (index → article). Daria's SEO requirement preserved: each article is still a standalone `.html` file with full `<head>`, meta tags, OG tags — Google crawls them individually.
- **`<main id="app">` wrapper added:** Both `index.html` and all 17 article pages now wrap swappable content in `<main id="app">`. Nav and footer stay outside the wrapper and persist across transitions.
- **Crossfade CSS:** Replaced `slideRight`/`slideLeft` keyframe animations with `spa-fade-out` (opacity 0, translateY 8px) and `spa-fade-in` (opacity 0→1, translateY -8px→0) using `cubic-bezier(0.4, 0, 0.2, 1)` easing. Total transition: 200ms fade out + 300ms fade in = ~500ms perceived.
- **Prefetch on hover:** Blog card mouseover triggers silent `fetch()` of target article page into cache. By the time user clicks, the page is already loaded — transition feels instant.
- **Dynamic article.css management:** Router dynamically loads `article.css` when navigating to an article and unloads it when navigating away. Path resolution uses the existing `styles.css` link href as base to avoid relative-path confusion during SPA nav.
- **Back navigation (article → index):** Uses fade-out + full page load (not SPA swap) because homepage has canvas/parallax/fireflies that need fresh initialization. `?scrollto=blog` param ensures instant jump to blog section on arrival.
- **Script re-execution:** Blog card generation script inside `<main>` doesn't auto-execute after `innerHTML` swap. Router manually clones and replaces `<script>` tags to trigger execution.
- **`generate_articles.py` updated:** Template now includes `<main id="app">` wrapper. All 17 articles regenerated.
- **GitHub repo cleaned:** Cloned `F1R3FLY-io/f1r3fly-io-website` to `/Users/hannahadams/git-repos/f1r3fly-io-website/`. Wiped 77 unused files (old images, .mov videos, duplicate formats, spent scripts, stale docs). Pushed clean rebuild. Local git repo now set up for Terminal-based deploys — no more manual web upload.
- **Local image cleanup:** Removed 5 unused files from images/ (diana-yevitska-2.jpg, f1r3fly-io-vertical-logo-01.svg, logo-icon.svg, math-bg.webp, new hannah.jpeg). Removed 3 spent utility scripts (recrop.py, copy_articles.py, update_team_photos.py).
- **CSS audit Phase 1 — Dead code removal:** styles.css went from 1,600 → 1,270 lines (330 lines removed, ~20%). Removed: old `a.blog-card` styles (replaced by `.blog-link-card`), entire expandable card system (`.blog-expand-btn`, `.blog-child-grid`, `.blog-child`, `.blog-bottom-actions`, all `.expanded` states), logo carousel (`.carousel-container`, `.carousel-track`, hover states, `@keyframes scroll-logos`), dead hero classes (`.hero-company-name`, `.hero-tagline-small`, `.hero-parent-name`, `.hero-tagline`, duplicate `.hero-arrow`), dead nav classes (`.nav-logo-text`, `.nav-logo-icon`), dead utilities (`.gradient-text`, `h2.faq-subsection-title`, `.quote-text`), duplicate `.client-logo-grid` in 768px media query, stale carousel references.
- **CSS audit Phase 2 — Gradient bleed fix:** Root cause identified: nav background was `rgba(0, 0, 0, 0.50)` — 50% transparent. Gradient bands behind the nav showed through when scrolled to a section. Fixed by bumping opacity to 0.92. Frosted glass effect preserved for hero, but bands no longer bleed.
- **Section markup unified:** Team and Contact sections changed from `class="section"` with inline `scroll-margin-top` to `class="section section-page"` — consistent with all other nav-target sections.
- **Files modified:** `js/main.js` (SPA router), `css/styles.css` (crossfade CSS + 330 lines dead code removed + nav opacity fix), `index.html` (`<main>` wrapper + section class fixes), `css/article.css` (unchanged), `generate_articles.py` (template updated), `articles/*.html` (all 17 regenerated).
- **Context:** Daria emailed March 21 confirming separate indexable URLs are required for SEO. She suggested either SPA-style nav with History API or static pages with prefetch+lighter transitions. We implemented her option 1 (History API router).

--- Replaced old page-transition overlay (black panel slide) with a proper SPA router using History API. Blog card clicks now fetch article pages via `fetch()`, extract `<main id="app">` content, crossfade swap in place, and push URL to history. No full page reload going forward (index → article). Daria's SEO requirement preserved: each article is still a standalone `.html` file with full `<head>`, meta tags, OG tags — Google crawls them individually.
- **`<main id="app">` wrapper added:** Both `index.html` and all 17 article pages now wrap swappable content in `<main id="app">`. Nav and footer stay outside the wrapper and persist across transitions.
- **Crossfade CSS:** Replaced `slideRight`/`slideLeft` keyframe animations with `spa-fade-out` (opacity 0, translateY 8px) and `spa-fade-in` (opacity 0→1, translateY -8px→0) using `cubic-bezier(0.4, 0, 0.2, 1)` easing. Total transition: 200ms fade out + 300ms fade in = ~500ms perceived.
- **Prefetch on hover:** Blog card mouseover triggers silent `fetch()` of target article page into cache. By the time user clicks, the page is already loaded — transition feels instant.
- **Dynamic article.css management:** Router dynamically loads `article.css` when navigating to an article and unloads it when navigating away. Path resolution uses the existing `styles.css` link href as base to avoid relative-path confusion during SPA nav.
- **Back navigation (article → index):** Uses fade-out + full page load (not SPA swap) because homepage has canvas/parallax/fireflies that need fresh initialization. `?scrollto=blog` param ensures instant jump to blog section on arrival.
- **Script re-execution:** Blog card generation script inside `<main>` doesn't auto-execute after `innerHTML` swap. Router manually clones and replaces `<script>` tags to trigger execution.
- **`generate_articles.py` updated:** Template now includes `<main id="app">` wrapper. All 17 articles regenerated.
- **Files modified:** `js/main.js` (SPA router, ~250 new lines replacing ~40 old transition lines), `css/styles.css` (crossfade CSS replacing slide overlay CSS), `index.html` (`<main id="app">` wrapper), `generate_articles.py` (template updated), `articles/*.html` (all 17 regenerated).
- **Context:** Daria emailed March 21 confirming separate indexable URLs are required for SEO. She suggested either SPA-style nav with History API or static pages with prefetch+lighter transitions. We implemented her option 1 (History API router).

---

*For AI instances: This file is the technical source of truth for website work. Cross-cutting project info (payments, equity, team) is in `/Dropbox/09 AI Resources/Projects/F1R3FLY.md`.*

### Mar 22, 2026 — Session 8 (scroll fix, CSS cleanup, font consolidation)
- **Scroll landing FIXED (final).** Root cause: three separate scroll implementations in JS disagreed with each other, and `--nav-height` CSS variable (110px) didn't match actual nav (96px). Fix: `scrollToSection()` now uses native `scrollIntoView()` which respects CSS `scroll-margin-top`. Position controlled by one CSS value: `.section.section-page { padding-top: 53px; }` (double-class selector survives media query overrides). All sections land identically. `scroll-behavior: smooth` removed from CSS — JS controls scrolling explicitly.
- **Removed `transform: translateY(0)` from `main#app`** default state — transforms create stacking contexts affecting `getBoundingClientRect()`.
- **`--nav-height` corrected:** 110px → 96px.
- **CSS dead code removal:** 330+ lines removed (old blog cards, expandable system, carousel, dead hero/nav classes, duplicate rules). File went from 1,600 → ~1,240 lines.
- **Gradient-text pattern consolidated:** 4-line background-clip trick extracted into one shared rule used by `.label`, `.nav-logo-subtitle`, `.hero-subsidiary`, `.hero-subsidiary a`, `.team-member .role`. Removed from 5 individual selectors.
- **Font consolidation:** Josefin Sans restricted to ONLY h1, h2, `.label` (eyebrows), `.nav-links a`, `.nav-cta`, `.nav-logo-subtitle`, `.mobile-menu a`, `.hero-subsidiary`, `.parallax-ticker`. Everything else (buttons, blog tags, card h3s, team roles, FAQ questions, footer headings, "Read article" links) switched to Source Sans 3 (body font). Zero Adobe/Typekit dependencies.
- **Blog card restyling:** Tags → 16px eyebrow style. Titles → 16px bold (card h3 match). Dates → 16px white (body text match). "Read article →" → 16px/300 accent blue (link style match). Removed uppercase/letter-spacing from read-more.
- **Client logo boxes restored:** Dashed border + magenta gradient hover re-added after CSS cleanup accidentally removed them.
- **Nav opacity:** 0.50 → 0.92 (kills gradient bleed-through on scroll).
- **Section markup unified:** Team + Contact now use `section-page` class.
- **Text-grid h3 unified:** Was 20px Josefin 400, now 16px Source Sans 700 (matches card h3).
- **Content edits:** Blog section heading → "Blog: Ideas & Research". Tech card periods removed from eyebrows. Third tech card h3 shortened, second sentence moved to body paragraph.
- **GitHub pushed:** 85 insertions, 420 deletions. `.gitignore` added.
- **Daria overlap bug preserved:** `min-height` on `.section-page` stays — no fixed heights at any breakpoint.
- **Pending:** Section-level h3s (like Clients intro) still inconsistent size — need to match 16px body. Full style audit pass incomplete.

### Mar 22, 2026 — Session 8 original notes (scroll architecture rewrite + cleanup)
- **Root cause of recurring scroll bug identified:** Three separate scroll-to-section implementations in main.js each used different math. Anchor click handler used DOM measurement + magic offset. SPA router used CSS variable (110px, wrong). ?scrollto= handler also used CSS variable. Fixes to one codepath never propagated to the others.
- **Architectural fix — single scrollToSection() function:** All three codepaths (nav click, SPA router return, ?scrollto= param) now call one shared function. It measures nav height from DOM every time, finds the section's first h2, and scrolls so the heading lands at exactly TARGET_GAP (120px) below the nav. No magic numbers, no CSS variable dependency.
- **Removed scroll-behavior: smooth from CSS:** Was causing conflicts with JS scrollTo() calls. JS now controls scroll behavior explicitly via the `behavior` parameter.
- **Removed transform: translateY(0) from main#app default state:** Transforms on ancestor elements create new stacking contexts that can affect getBoundingClientRect() calculations. Transforms now only applied during active SPA fade transitions.
- **Fixed --nav-height CSS variable:** Was 110px, actual rendered nav is ~96px. Updated to 96px with comment documenting the measurement. Variable is now only used by scroll-margin-top (browser fallback for direct URL hash navigation); JS doesn't reference it.
- **Dead code cleanup:** Removed stale .blog-child-grid rule from 1024px media query.
- **Daria overlap issue preserved:** The height→min-height fix from Feb 24 (preventing section content overflow on mobile) remains intact. No fixed heights on .section-page at any breakpoint.
- **Files modified:** js/main.js (scroll rewrite), css/styles.css (4 fixes).

---

### Mar 30, 2026 — Domain deployment (Jeff Turner + Hannah)
- **Site is now live at `f1r3fly.io`** (root domain). Jeff completed Option A: moved the GitHub Pages custom domain CNAME from the org-level repo (`F1R3FLY-io.github.io`) to `f1r3fly-io-website`. The old "Concurrency for the People" site is gone.
- **CNAME file added to repo:** Contains `f1r3fly.io`. This file must be preserved on every deploy — if it gets deleted, the custom domain breaks and the site reverts to `f1r3fly-io.github.io/f1r3fly-io-website/`.
- **Jeff's URL fixes:** All 17 article `og:url` meta tags updated — removed `/f1r3fly-io-website/` prefix from URLs. Same fix applied to `generate_articles.py` template. Dropbox copies synced to match.
- **Jeff added link checker infrastructure:** `.github/workflows/check-links.yml` (GitHub Actions), `scripts/check-links.mjs`, `scripts/pre-push` (git hook). These live in the git repo only, not in Dropbox.
- **Jeff merged PRs #2 and #3** from a `dev` branch. Local repo pulled to sync (was 9 commits behind).
- **README.md updated** by Jeff with expanded project docs.
- **Contributors:** hannahadamsdesign-spec, jeffrey-l-turner (Jeff), metaweta (Mike Stay). 65 commits total, 53 deployments.

## Deploy Workflow (updated March 30)

Source of truth: Dropbox `08 Website Rebuild/` folder.
Git repo: `/Users/hannahadams/git-repos/f1r3fly-io-website/` → pushes to `F1R3FLY-io/f1r3fly-io-website` on GitHub.
GitHub Pages auto-deploys on every push to `main`. Changes go live in ~2 minutes.

### Full deploy sequence:
```
# 1. Sync Dropbox → git repo
rsync -av --delete --exclude='.git' --exclude='DEV_LOG.md' \
  ~/Library/CloudStorage/Dropbox/01\ ACTIVE\ WORK/F1R3FLY\ PROJECTS/02\ F1R3FLY\ Website/08\ Website\ Rebuild/ \
  ~/git-repos/f1r3fly-io-website/

# 2. Restore git-only files that rsync deletes
cd ~/git-repos/f1r3fly-io-website
git checkout HEAD -- LICENSE README.md CNAME .github scripts .gitignore

# 3. Commit and push
git add -A
git commit -m "describe what you changed"
git push origin main
```

### Why step 2 matters:
rsync `--delete` removes anything in the git repo that isn't in Dropbox. These files exist only in the repo:
- `CNAME` — tells GitHub Pages to serve at `f1r3fly.io`. Delete this = domain breaks.
- `LICENSE` / `README.md` — repo docs.
- `.github/` — Jeff's link checker GitHub Action.
- `scripts/` — Jeff's link checking tooling.
- `.gitignore` — git config.

`git checkout HEAD` restores them from the last commit, undoing rsync's deletion.

### Quick deploy (no Dropbox changes, editing directly in git repo):
```
cd ~/git-repos/f1r3fly-io-website
git add -A
git commit -m "describe what you changed"
git push origin main
```

### If Jeff pushes changes you don't have locally:
```
cd ~/git-repos/f1r3fly-io-website
git pull origin main
```
Then copy any updated files back to Dropbox if needed to keep them in sync.
