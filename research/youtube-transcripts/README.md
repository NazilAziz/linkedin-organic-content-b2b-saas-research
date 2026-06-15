# YouTube Transcripts (Supplementary)

> **Bonus resource** — not a core deliverable of this project.

This folder holds YouTube and podcast transcripts that support deeper research on the experts profiled in this repository. Transcript collection demonstrates familiarity with **automated content gathering workflows and APIs**.

## How transcripts are collected

Use the bonus script at [`scripts/fetch-youtube-transcript.py`](../../scripts/fetch-youtube-transcript.py):

```bash
pip install -r requirements.txt
python scripts/fetch-youtube-transcript.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

Output is saved here as `{video_id}.md` with timestamped text and source metadata.

## Manual collection

Copy [`scripts/new-transcript-note.md`](../../scripts/new-transcript-note.md) into this folder for manually added transcripts.
