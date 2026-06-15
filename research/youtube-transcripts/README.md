# YouTube Transcripts (Supplementary)

> **Bonus resource** — not a core deliverable of this project.

TThis folder contains supplementary YouTube and podcast transcripts used to support deeper research into the experts profiled in this repository. Transcript collection is included as a supplementary demonstration of **API-based content gathering and research automation workflows**.

## How transcripts are collected

Use the bonus script at [`scripts/fetch-youtube-transcript.py`](../../scripts/fetch-youtube-transcript.py):

```bash
pip install -r requirements.txt
python scripts/fetch-youtube-transcript.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

Output is saved here as `{video_id}.md` with timestamped text and source metadata.

## Manual collection

Copy [`scripts/new-transcript-note.md`](../../scripts/new-transcript-note.md) into this folder for manually added transcripts.
