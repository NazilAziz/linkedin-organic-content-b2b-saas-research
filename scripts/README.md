# Scripts

Helper scripts for collecting and organizing research material.

## Available scripts

| Script | Purpose |
|--------|---------|
| `fetch-youtube-transcript.py` | Download a YouTube transcript to markdown |
| `new-post-note.md` | Template for annotating a saved LinkedIn post |
| `new-transcript-note.md` | Template for adding a YouTube/podcast transcript |

## Usage

Copy a template into the appropriate folder and fill it in:

```bash
# Example: save a new post annotation
cp scripts/new-post-note.md research/linkedin-posts/justin-welsh-hooks-2025-06.md
```

### fetch-youtube-transcript.py

```bash
pip install -r requirements.txt
python scripts/fetch-youtube-transcript.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

Options:

- `-o, --output-dir` — custom output folder (default: `research/youtube-transcripts`)
- `-l, --language` — preferred language code (repeatable)

## Planned scripts

- [ ] `fetch-linkedin-post.py` — archive a post URL to markdown (requires manual auth)
- [ ] `index-sources.py` — regenerate sections of `research/sources.md`
