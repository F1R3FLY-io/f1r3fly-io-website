#!/usr/bin/env python3
"""Generate white paper HTML pages for f1r3fly.io"""

import os

BASE = os.path.dirname(os.path.abspath(__file__))
WP_DIR = os.path.join(BASE, 'white-papers')
os.makedirs(WP_DIR, exist_ok=True)

# Template matching existing article pages exactly
def article_template(title, subtitle, tag, tag_class, date, intro, sections, topics, breadcrumb_label, google_doc_url, slug):
    sections_html = ""
    for s in sections:
        sections_html += f"""  <section class="article-section">
    <h2>{s['heading']}</h2>
    <p>{s['body']}</p>
  </section>
"""
    topics_html = "\n    ".join(f"<span>{t}</span>" for t in topics)
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} &mdash; F1R3FLY.IO</title>
  <meta name="description" content="{subtitle}">
  <meta property="og:title" content="{title} &mdash; F1R3FLY.IO">
  <meta property="og:description" content="{subtitle}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://f1r3fly.io/white-papers/{slug}.html">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@100;300;400;600;700&family=Source+Sans+3:wght@300;400;600;700&display=swap">
  <link rel="stylesheet" href="../css/styles.css">
  <link rel="stylesheet" href="../css/article.css">
</head>
<body>
<nav class="site-nav" aria-label="Main navigation">
  <div class="nav-container">
    <div class="nav-logo-area">
      <a href="../index.html#home" class="nav-logo">
        <img src="../images/f1r3fly-io-horizontal-on-dark-with-tag.svg" alt="F1R3FLY.IO &mdash; A Subsidiary of F1R3FLY Industries" class="nav-logo-wordmark">
      </a>
    </div>
    <ul class="nav-links">
      <li><a href="../index.html#home">Home</a></li>
      <li class="nav-divider" aria-hidden="true">|</li>
      <li><a href="../index.html#technology">Technology</a></li>
      <li class="nav-divider" aria-hidden="true">|</li>
      <li><a href="../index.html#developers">Developers</a></li>
      <li class="nav-divider" aria-hidden="true">|</li>
      <li><a href="../index.html#clients">Clients</a></li>
      <li class="nav-divider" aria-hidden="true">|</li>
      <li><a href="../index.html#partners">Partners</a></li>
      <li class="nav-divider" aria-hidden="true">|</li>
      <li><a href="../index.html#team">Team</a></li>
      <li class="nav-divider" aria-hidden="true">|</li>
      <li><a href="../index.html#blog">Blog</a></li>
      <li class="nav-divider" aria-hidden="true">|</li>
      <li><a href="../index.html#brain-candy">Brain Candy</a></li>
      <li class="nav-divider" aria-hidden="true">|</li>
      <li><a href="../index.html#white-papers">White Papers</a></li>
      <li><a href="../index.html#contact" class="nav-cta">Get In Touch</a></li>
    </ul>
    <button class="hamburger" aria-label="Toggle menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>
  <div class="nav-line" aria-hidden="true"></div>
</nav>
<main id="app">
<article class="article-page">
  <div class="article-breadcrumb">
    <a href="../index.html#white-papers">&larr; {breadcrumb_label}</a>
  </div>
  <div class="article-box">
  <span class="article-tag {tag_class}">{tag}</span>
  <h1>{title}</h1>
  <p class="article-subtitle">
    Lucius Gregory Meredith &mdash; {date}
  </p>
  <div class="article-intro">
    <p><strong>Abstract:</strong> {intro}</p>
  </div>
{sections_html}  <div class="article-links">
    <p class="article-substack-link">
      <a href="{google_doc_url}" target="_blank" rel="noopener">Read the full white paper &rarr;</a>
    </p>
  </div>
  <div class="article-topics">
    {topics_html}
  </div>
  </div>
</article>
</main>
<footer class="section-band neutral site-footer" style="margin:0; padding:80px 20px 40px;">
  <div class="footer-grid">
    <div class="footer-brand">
      <div style="display:flex; align-items:center; gap:12px; margin-bottom:20px;">
        <img src="../images/f1r3fly-io-bug-icon.svg" alt="F1R3FLY.IO" width="40" height="40">
        <span style="font-family:var(--font-heading); font-weight:700; font-size:16px; letter-spacing:2px; text-transform:uppercase; color:var(--color-white);">F1R3FLY.IO</span>
      </div>
      <p style="color:rgba(255,255,255,0.5); font-size:14px; line-height:1.6; margin-bottom:24px;">Scalable. Searchable. Secure. Storable.<br>A Digital Evolution in concurrent computing.</p>
    </div>
    <div class="footer-col">
      <h4 class="footer-heading">Europe Office</h4>
      <p class="footer-address">4-5 Langham Place<br>London, W1B 3DG</p>
      <p class="footer-address"><a href="tel:+442034320078">+44 (0)203 432 0078</a></p>
    </div>
    <div class="footer-col">
      <h4 class="footer-heading">US Office</h4>
      <p class="footer-address">Floor 17, 521 Fifth Avenue<br>New York, NY 10175</p>
      <p class="footer-address"><a href="tel:+16464759644">+1 646 475 9644</a></p>
    </div>
  </div>
  <div class="footer-bottom">
    <p>&copy; 2026 F1R3FLY.IO. All rights reserved.</p>
  </div>
</footer>
<script src="../js/main.js" defer></script>
</body>
</html>"""


# ─── Paper 1: Algorithmic Scientists ───
papers = []
papers.append({
    'slug': 'algorithmic-scientists',
    'title': 'Algorithmic Scientists and the Foundations of Machine Intelligence',
    'subtitle': 'A mathematical framework grounding AI in graph-structured lambda theories, where programs discover their world through experimentation and formulate hypotheses in an automatically generated logic.',
    'tag': 'AI &amp; Foundations',
    'tag_class': 'article-tag-ai',
    'date': 'April 2026',
    'google_doc_url': 'https://docs.google.com/document/d/1wRibIEQCNrvPl4jJMQ59d80KERgeaQGCFU8Sq44pWzo/edit',
    'intro': 'This paper presents F1R3FLY&rsquo;s foundational approach to artificial intelligence, grounded in graph-structured lambda theories (GSLTs). GSLTs provide a uniform categorical framework encompassing virtually all known classical models of computation. Within this framework, bisimulation is the finest equivalence any program can learn about its environment; reactive contexts serve as experimental assays; an auto-generated Hennessy&ndash;Milner logic provides a canonical language for reasoning; and structural reflection embeds this language back into the calculus. The result is a class of programs&mdash;algorithmic scientists&mdash;that discover their world through experimentation and formulate hypotheses in a language automatically grounded in bisimulation-based ontology.',
    'sections': [
        {'heading': 'Key argument', 'body': 'The paper develops a four-step argument: (1) computation is ontologically isolated&mdash;programs can only interact with representations internal to their substrate; (2) bisimulation is the finest distinction a program can draw about its environment; (3) reactive contexts derived from Milner, Leifer, and Sewell&rsquo;s work provide algorithmic experimental assays; and (4) an auto-generated Hennessy&ndash;Milner logic gives programs a canonical language for recording and reasoning about experimental results.'},
        {'heading': 'The GSLT framework', 'body': 'A graph-structured lambda theory is a triple &langle;G, E, R&rangle; consisting of a grammar of terms, a set of equations forming the smallest equivalence relation erasing irrelevant syntactic differences, and a set of rewrite rules determining term evolution. Lambda calculus, pi-calculus, rho calculus, and ambient calculus are all instances. GSLTs form a category whose morphisms are bisimulation-preserving maps, ensuring all constructions are functorial.'},
        {'heading': 'MeTTaIL and the execution engine', 'body': 'MeTTaIL (rholang 1.4), F1R3FLY&rsquo;s core language technology, provides the execution engine: defining GSLTs as first-class entities, enforcing spatial-behavioral types that enable semantic search over smart contracts, and supporting evolutionary programming over entire causal models.'},
        {'heading': 'Why it matters', 'body': 'Rather than treating AI as statistical pattern-matching on large datasets, this framework grounds machine intelligence in a precise mathematical account of computation itself. Programs that behave as scientists&mdash;exploring through experimentation, discovering categories through bisimulation, reasoning in automatically generated logic&mdash;represent a fundamentally different approach to the aspects of intelligence that computation can capture.'},
    ],
    'topics': ['graph-structured lambda theories', 'bisimulation', 'rho calculus', 'MeTTaIL', 'algorithmic science', 'OSLF', 'reactive contexts', 'Hennessy-Milner logic'],
})

# ─── Paper 2: Tokenizing Coordination (F1R3Web) ───
papers.append({
    'slug': 'tokenizing-coordination',
    'title': 'Tokenizing Coordination in Mixed Communities of Humans and Agentic AIs',
    'subtitle': 'How phlogiston-metered friction creates value across F1R3FLY web properties by making coordination costs explicit at the points where friction improves outcomes.',
    'tag': 'Platform &amp; Economics',
    'tag_class': 'article-tag-comp',
    'date': 'April 2026',
    'google_doc_url': 'https://docs.google.com/document/d/14z7fCVs2D9fOFJ3j4xZGWlwJh5w1PkkmcGXZ87a7LN8/edit',
    'intro': 'All computation and storage on the F1R3FLY platform is metered using phlogiston (phlo), convertible to the staking token REV. This paper addresses where and how tokens should be introduced into user-facing experiences when migrating Web 2.0 properties onto F1R3FLY infrastructure. The guiding principle: tokenization should be introduced at points where friction creates value&mdash;where the cost of an action serves a coordination function that improves outcomes for participants.',
    'sections': [
        {'heading': 'The principle of valuable friction', 'body': 'In conventional platform design, friction is the enemy. But there is a class of interactions where friction is actively valuable&mdash;where its absence produces coordination failures: spam drowns signal, free-riders consume resources, low-quality contributions dilute high-quality ones. Token-mediated friction makes coordination costs explicit and allocable, directing them to the parties who bear them rather than whoever has the least power to refuse.'},
        {'heading': 'F1R3FLY web properties', 'body': 'The paper develops tokenization designs across four properties: F1R3Sky (social networking with attention-gated feeds and reputation-weighted amplification), F1R3Eats (food delivery with priority ordering and courier reliability bonds), F1R3Tunes (music distribution), and F1R3Docs (collaborative document editing). Each property applies the same question: where is there a coordination cost that is currently externalized?'},
        {'heading': 'The Person of Interest model', 'body': 'High-profile users&mdash;artists, lawyers, physicians&mdash;face enormous demand on their attention. Token-gated access lets them establish feeds where writing privileges require token expenditure. This is not a paywall: tokens can be redistributed, staked into community pools, or burned. The result is attention management that is economically rational and socially legible.'},
        {'heading': 'Agentic AI as participants', 'body': 'The introduction of agentic AI as first-class participants in these communities transforms interface design and economic mechanics. AI agents operating in tokenized environments must manage phlogiston budgets, earn reputation through verifiable behavior, and coordinate with both human and artificial participants under the same economic rules.'},
    ],
    'topics': ['phlogiston', 'tokenization', 'valuable friction', 'F1R3Sky', 'F1R3Eats', 'F1R3Tunes', 'F1R3Docs', 'attention economy', 'agentic AI', 'coordination'],
})

# ─── Paper 3: F1R3Games ───
papers.append({
    'slug': 'f1r3games-collective-intelligence',
    'title': 'F1R3GAMES: Collective Intelligence Through Play',
    'subtitle': 'A suite of on-chain games designed to cultivate collective intelligence through structured, playful collaboration on F1R3FLY shard infrastructure.',
    'tag': 'Games &amp; Collective Intelligence',
    'tag_class': 'article-tag-phil',
    'date': 'April 2026',
    'google_doc_url': 'https://docs.google.com/document/d/1dOgKe4yRB4HsIhidWkgaMYHqdeT5ygBvYR-2j1WJZSY/edit',
    'intro': 'F1R3Games is a suite of interactive, on-chain applications designed to cultivate collective intelligence through structured, playful collaboration. Built on F1R3FLY shard infrastructure, each game explores a distinct modality of group creativity: visual art (F1R3Pix), musical rhythm (F1R3Beat), collective sentiment (F1R3Ink), generative and evolutionary music (F1R3Skein), and collaborative storytelling (F1R3SideChat). All participant actions are stored on-chain via RSpace tuple-space storage, providing a fully decentralized, tamper-evident, and tokenized environment for co-creation.',
    'sections': [
        {'heading': 'Games as instruments of collective intelligence', 'body': 'Games impose constraints that channel creative energy, create shared attention, establish legible rules of interaction, and produce measurable outcomes. F1R3Games treats collective creative processes as first-class activities and records them with the fidelity required for scientific study. A group&rsquo;s collective output is irreducible to any single participant&rsquo;s contribution.'},
        {'heading': 'The game suite', 'body': 'F1R3Pix is collaborative pixel art on a shared canvas. F1R3Beat is collective rhythm sequencing. F1R3Ink captures collective sentiment through anonymous text contribution. F1R3Skein uses evolutionary algorithms to evolve music through group selection. F1R3SideChat is collaborative storytelling where each player controls a character and the narrative emerges from their interactions.'},
        {'heading': 'On-chain as ground truth', 'body': 'Every pixel placed, every beat sequenced, every word written is stored on a F1R3FLY shard. The complete history of every collective creation is immutable, auditable, and owned by the community of participants rather than a centralized platform. On-chain state transforms ephemeral collaboration into a durable, verifiable record, enabling new forms of attribution, governance, and economic participation.'},
        {'heading': 'Token economics and valuable friction', 'body': 'Each game incorporates token mechanics where friction creates value: placement costs in F1R3Pix prevent griefing, contribution staking in F1R3Beat encourages quality, and selective listening costs in F1R3Skein align individual preferences with group evolution. The phlogiston metering layer ensures all game actions have real computational cost, grounding token economics in actual resource consumption.'},
    ],
    'topics': ['F1R3Games', 'collective intelligence', 'F1R3Pix', 'F1R3Beat', 'F1R3Ink', 'F1R3Skein', 'F1R3SideChat', 'on-chain games', 'rholang', 'tokenized play'],
})

# Generate all pages
for p in papers:
    html = article_template(
        title=p['title'], subtitle=p['subtitle'], tag=p['tag'],
        tag_class=p['tag_class'], date=p['date'], intro=p['intro'],
        sections=p['sections'], topics=p['topics'],
        breadcrumb_label='White Papers', google_doc_url=p['google_doc_url'],
        slug=p['slug']
    )
    path = os.path.join(WP_DIR, f"{p['slug']}.html")
    with open(path, 'w') as f:
        f.write(html)
    print(f"  ✓ {path}")

print("\nDone. Generated 3 white paper pages.")
