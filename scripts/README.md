# Scripts

Helper scripts and templates for the research repository.

## Core templates

| File | Purpose |
|------|---------|
| [`new-post-note.md`](new-post-note.md) | Template for annotating a saved LinkedIn post |
| [`new-transcript-note.md`](new-transcript-note.md) | Template for manually adding a transcript |

## Bonus: API-based transcript fetcher

> Supplementary — demonstrates automated content gathering, not a core deliverable.

| File | Purpose |
|------|---------|
| [`fetch-youtube-transcript.py`](fetch-youtube-transcript.py) | Download YouTube captions via `youtube-transcript-api` and save as markdown |

```bash
pip install -r requirements.txt
python scripts/fetch-youtube-transcript.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

Options:

- `-o, --output-dir` — custom output folder (default: `research/youtube-transcripts`)
- `-l, --language` — preferred language code (repeatable)
