# LinkedIn Organic Content Strategy for B2B SaaS

A curated research repository analyzing how top B2B practitioners build organic reach, pipeline, and brand authority on LinkedIn.

---

## Project Objective:

Build a **repeatable, evidence-based LinkedIn organic content strategy** for B2B SaaS — grounded in real practitioner output, not generic advice.

The project answers four questions:

1. **Who** should SaaS teams study on LinkedIn?
2. **What** are they posting, and why does it work?
3. **How** do strategy layers (positioning, distribution, algorithms, attribution) fit together?
4. **Where** can each insight be traced back to a primary source?

---

## Main Deliverables

| Deliverable | Location | Description |
|-------------|----------|-------------|
| Expert profiles | [`research/other/experts/`](research/other/experts/) | 10 profiles with LinkedIn links, source URLs, and selection rationale |
| LinkedIn post analysis | [`research/linkedin-posts/`](research/linkedin-posts/) | 2 annotated posts per expert (date, URL, summary) |
| Source index | [`research/sources.md`](research/sources.md) | Master index linking all experts, posts, and references |

---

## Experts

| Expert | LinkedIn | Lens |
|--------|----------|------|
| Justin Welsh | [Profile](https://www.linkedin.com/in/justinwelsh/) | Post systems & content OS |
| Dave Gerhardt | [Profile](https://www.linkedin.com/in/davegerhardt/) | B2B brand voice & community |
| Ross Simmonds | [Profile](https://www.linkedin.com/in/rosssimmonds/) | Content distribution |
| Amanda Natividad | [Profile](https://www.linkedin.com/in/amandanat/) | Audience research & zero-click content |
| Chris Walker | [Profile](https://www.linkedin.com/in/chriswalker171/) | Dark social & pipeline attribution |
| Kieran Flanagan | [Profile](https://www.linkedin.com/in/kieranjflanagan/) | Scaled SaaS organic + AI workflows |
| Lara Acosta | [Profile](https://www.linkedin.com/in/laraacostar/) | Hooks, carousels & personal branding |
| Richard van der Blom | [Profile](https://www.linkedin.com/in/richardvanderblom/) | LinkedIn algorithm data |
| Daniel Murray | [Profile](https://www.linkedin.com/in/daniel-murray-marketing/) | B2B media brand at scale |
| Alex Lieberman | [Profile](https://www.linkedin.com/in/alex-lieberman/) | Storytelling & content-led growth |

---

## Why These Experts Were Selected

Each expert covers a distinct layer of LinkedIn organic strategy — together spanning **craft, systems, data, distribution, and revenue impact**.

| Expert | Rationale |
|--------|-----------|
| **Justin Welsh** | Built a solo business through daily LinkedIn content; reference for post architecture and content pillars |
| **Dave Gerhardt** | Former Drift CMO; models POV-driven B2B voice and community-led distribution |
| **Ross Simmonds** | Foundation CEO; bridges LinkedIn with SEO, repurposing, and distribution ROI |
| **Amanda Natividad** | SparkToro VP; audience research rigor and on-platform (zero-click) value |
| **Chris Walker** | Refine Labs founder; reframed LinkedIn as a dark-social pipeline channel |
| **Kieran Flanagan** | HubSpot SVP; how large SaaS orgs operationalize organic content at scale |
| **Lara Acosta** | LinkedIn growth practitioner; tactical hooks, carousels, and profile positioning |
| **Richard van der Blom** | Independent algorithm researcher; quantitative backbone for format and timing |
| **Daniel Murray** | Marketing Millennials founder; high-frequency B2B media branding |
| **Alex Lieberman** | Morning Brew co-founder; narrative craft and content-business thinking |

---

## Research Methodology

### Core workflow (LinkedIn-focused)

1. **Select experts** — practitioners with demonstrated LinkedIn results across strategy, craft, data, and distribution
2. **Document profiles** — capture profile links, key sources, and why each expert matters for B2B SaaS
3. **Archive posts** — save 2 recent posts per expert with date, URL, and summary of argument, format, and CTA
4. **Index sources** — maintain a single master index in `research/sources.md` with cross-links to all files

### Annotation standard

Every file answers: *Why does this matter for B2B SaaS LinkedIn strategy?* All entries link back to original sources.

---

## Repository Structure

```
linkedin-organic-content-b2b-saas-research/
├── README.md
├── requirements.txt                   # Python deps (bonus script only)
│
├── research/
│   ├── sources.md                     # Master index
│   ├── linkedin-posts/                # Core: 2 posts per expert
│   ├── other/experts/                 # Core: 10 expert profiles
│   └── youtube-transcripts/           # Bonus: supplementary transcripts
│
└── scripts/
    ├── new-post-note.md               # Template for post annotations
    ├── new-transcript-note.md         # Template for manual transcripts
    └── fetch-youtube-transcript.py    # Bonus: API-based transcript fetcher
```

---

## Bonus: API-Based Research Methodology

> **Supplementary resource** — not a core deliverable.

A Python script ([`scripts/fetch-youtube-transcript.py`](scripts/fetch-youtube-transcript.py)) demonstrates automated content gathering using the `youtube-transcript-api` library. It accepts a YouTube URL, extracts the video ID, downloads captions, and saves timestamped markdown to [`research/youtube-transcripts/`](research/youtube-transcripts/).

This supports deeper research on expert talks and podcasts but is positioned as an **additional technical demonstration** of API-driven workflow automation.

```bash
pip install -r requirements.txt
python scripts/fetch-youtube-transcript.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

---

## Getting Started

1. Open [`research/sources.md`](research/sources.md) for the full index
2. Read expert profiles in [`research/other/experts/`](research/other/experts/)
3. Review post analyses in [`research/linkedin-posts/`](research/linkedin-posts/)
