# LinkedIn Organic Content Strategy for B2B SaaS

A structured research repository for studying how leading B2B marketers build organic reach, pipeline, and brand authority on LinkedIn.

---

## Project Objective

This project exists to turn scattered LinkedIn marketing advice into a **repeatable, evidence-based content strategy** for B2B SaaS companies.

Rather than chasing trends or copying viral formats blindly, the repository:

- Curates practitioners who have demonstrated results on LinkedIn
- Archives real posts, transcripts, and source material
- Annotates *why* each source matters for B2B SaaS organic growth
- Separates strategy (positioning, distribution, attribution) from craft (hooks, formats, algorithms)

The end goal is a practical playbook: what to post, how to structure it, how to measure influence on pipeline, and how to operationalize content across founders, executives, and marketing teams.

---

## Expert List

| Expert | LinkedIn | Primary lens |
|--------|----------|--------------|
| Justin Welsh | [justinwelsh](https://www.linkedin.com/in/justinwelsh/) | Repeatable post systems & content OS |
| Dave Gerhardt | [davegerhardt](https://www.linkedin.com/in/davegerhardt/) | B2B brand voice & community-led marketing |
| Ross Simmonds | [rosssimmonds](https://www.linkedin.com/in/rosssimmonds/) | Content distribution & repurposing |
| Amanda Natividad | [amandanat](https://www.linkedin.com/in/amandanat/) | Audience research & zero-click content |
| Chris Walker | [chriswalker171](https://www.linkedin.com/in/chriswalker171/) | Dark social & pipeline attribution |
| Kieran Flanagan | [kieranjflanagan](https://www.linkedin.com/in/kieranjflanagan/) | Scaled SaaS organic + AI workflows |
| Lara Acosta | [laraacostar](https://www.linkedin.com/in/laraacostar/) | Hooks, carousels & personal branding |
| Richard van der Blom | [richardvanderblom](https://www.linkedin.com/in/richardvanderblom/) | LinkedIn algorithm data & systems |
| Daniel Murray | [daniel-murray-marketing](https://www.linkedin.com/in/daniel-murray-marketing/) | B2B media brand at scale |
| Alex Lieberman | [alex-lieberman](https://www.linkedin.com/in/alex-lieberman/) | Storytelling & content-led growth |

Detailed profiles with source links live in [`research/other/experts/`](research/other/experts/).

---

## Why These Experts Were Selected

Each expert covers a distinct layer of LinkedIn organic strategy. Together they span **craft, systems, data, distribution, and revenue impact**.

| Expert | Why selected |
|--------|--------------|
| **Justin Welsh** | Built a multi-million-dollar solo business through daily LinkedIn content. Best reference for post architecture, content pillars, and converting attention into newsletter and product revenue. |
| **Dave Gerhardt** | Former Drift CMO and Exit Five founder. Models strong POV-driven B2B voice and community-led distribution — how SaaS leaders should sound human, not corporate. |
| **Ross Simmonds** | Foundation CEO focused on content distribution ROI. Bridges LinkedIn with SEO and repurposing — answers how social fits into a full organic engine. |
| **Amanda Natividad** | SparkToro VP and zero-click content thinker. Brings audience research rigor and on-platform value delivery — critical for quality over click-bait. |
| **Chris Walker** | Refine Labs founder who reframed LinkedIn as a dark-social pipeline channel. Connects organic activity to revenue economics SaaS leadership cares about. |
| **Kieran Flanagan** | HubSpot SVP and Marketing Against the Grain co-host. Represents how large SaaS orgs operationalize organic and AI-enabled content without losing authenticity. |
| **Lara Acosta** | LinkedIn growth practitioner for founders. Tactical expert on hooks, carousels, profile positioning, and comment-to-DM conversion mechanics. |
| **Richard van der Blom** | Independent LinkedIn algorithm researcher. Annual Algorithm Insights report provides the quantitative backbone for format, timing, and systems decisions. |
| **Daniel Murray** | The Marketing Millennials founder. Demonstrates high-frequency B2B media branding — staying visible in crowded feeds with personality and consistency. |
| **Alex Lieberman** | Morning Brew co-founder. Content-business thinking and narrative craft — treating LinkedIn as a media channel, not a bulletin board. |

---

## Collection Methodology

Research is gathered in layers, each with a consistent annotation standard.

### 1. Expert profiling
Each expert gets a dedicated markdown file with profile links, key sources (podcasts, blogs, courses, reports), selection rationale, and a collection checklist.

### 2. LinkedIn post archiving
Two recent posts per expert are saved in `research/linkedin-posts/` with:
- Post date and original URL
- Summary of core argument, format, and CTA pattern
- Implicit notes on applicability to B2B SaaS

### 3. Transcript collection
YouTube and podcast transcripts are stored in `research/youtube-transcripts/` using `scripts/fetch-youtube-transcript.py` or manual templates. Each file includes source URL, language metadata, and timestamped text.

### 4. Source indexing
`research/sources.md` acts as the master index — linking experts to profile files, categorizing material types, and tracking priority sources still to collect.

### 5. Annotation standard
Every new file should answer: *Why does this matter for B2B SaaS LinkedIn strategy?* Files are named descriptively (`expert-topic-YYYY-MM.md`) and link back to original sources.

---

## Repository Structure

```
linkedin-organic-content-b2b-saas-research/
├── README.md                          # Project overview (this file)
├── requirements.txt                   # Python dependencies for scripts
│
├── research/
│   ├── sources.md                     # Master source index
│   ├── linkedin-posts/                # Archived LinkedIn posts (2 per expert)
│   ├── youtube-transcripts/           # Video/podcast transcripts
│   └── other/
│       └── experts/                   # One profile per expert (10 files)
│
└── scripts/
    ├── README.md                      # Script documentation
    ├── fetch-youtube-transcript.py    # Download YouTube transcripts to markdown
    ├── new-post-note.md               # Template for post annotations
    └── new-transcript-note.md         # Template for manual transcripts
```

---

## Getting Started

1. Read [`research/sources.md`](research/sources.md) for the full source index.
2. Browse expert profiles in [`research/other/experts/`](research/other/experts/).
3. Review archived posts in [`research/linkedin-posts/`](research/linkedin-posts/).
4. Pull transcripts with:

```bash
pip install -r requirements.txt
python scripts/fetch-youtube-transcript.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

---

## Contributing

When adding material:

- Link to the original source URL
- Add a short annotation on B2B SaaS relevance
- Use consistent naming: `expert-topic-YYYY-MM.md`
- Update `research/sources.md` when adding priority sources
