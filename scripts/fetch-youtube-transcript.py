#!/usr/bin/env python3
"""Download a YouTube transcript and save it as markdown."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT_DIR = REPO_ROOT / "research" / "youtube-transcripts"
DEFAULT_LANGUAGES = ["en", "en-US", "en-GB"]


def extract_video_id(url: str) -> str:
    """Extract a YouTube video ID from a URL or bare ID."""
    value = url.strip()

    if re.fullmatch(r"[\w-]{11}", value):
        return value

    parsed = urlparse(value)
    host = (parsed.hostname or "").lower().removeprefix("www.")

    if host == "youtu.be":
        video_id = parsed.path.lstrip("/").split("/")[0]
        if video_id:
            return video_id

    if host in {"youtube.com", "m.youtube.com"}:
        if parsed.path == "/watch":
            query = parse_qs(parsed.query)
            if "v" in query:
                return query["v"][0]

        match = re.match(r"^/(embed|shorts|v|live)/([^/?]+)", parsed.path)
        if match:
            return match.group(2)

    raise ValueError(f"Could not extract video ID from: {url}")


def format_timestamp(seconds: float) -> str:
    total_seconds = int(seconds)
    hours, remainder = divmod(total_seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    if hours:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def fetch_transcript(
    video_id: str, languages: list[str] | None = None
) -> tuple[list[dict], dict[str, str | bool]]:
    """Fetch transcript snippets and metadata."""
    api = YouTubeTranscriptApi()
    fetched = api.fetch(video_id, languages=languages or DEFAULT_LANGUAGES)
    metadata = {
        "language": fetched.language,
        "language_code": fetched.language_code,
        "is_generated": fetched.is_generated,
    }
    return fetched.to_raw_data(), metadata


def build_markdown(
    video_id: str,
    url: str,
    snippets: list[dict],
    metadata: dict[str, str | bool],
) -> str:
    watch_url = f"https://www.youtube.com/watch?v={video_id}"
    generated = "yes" if metadata["is_generated"] else "no"
    lines = [
        f"# YouTube Transcript: {video_id}",
        "",
        f"**URL:** {url if url != video_id else watch_url}",
        f"**Video ID:** {video_id}",
        f"**Language:** {metadata['language']} ({metadata['language_code']})",
        f"**Auto-generated:** {generated}",
        f"**Saved:** {date.today().isoformat()}",
        "",
        "## Transcript",
        "",
    ]

    for snippet in snippets:
        timestamp = format_timestamp(snippet["start"])
        text = snippet["text"].strip()
        if text:
            lines.append(f"**[{timestamp}]** {text}")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def save_transcript(
    video_id: str,
    url: str,
    output_dir: Path,
    languages: list[str] | None = None,
) -> Path:
    snippets, metadata = fetch_transcript(video_id, languages=languages)
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / f"{video_id}.md"
    output_path.write_text(
        build_markdown(video_id, url, snippets, metadata),
        encoding="utf-8",
    )
    return output_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download a YouTube transcript and save it as markdown."
    )
    parser.add_argument("url", help="YouTube URL or 11-character video ID")
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Output directory (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "-l",
        "--language",
        action="append",
        dest="languages",
        help="Preferred transcript language code (repeatable, e.g. en, es)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        video_id = extract_video_id(args.url)
        output_path = save_transcript(
            video_id=video_id,
            url=args.url,
            output_dir=args.output_dir,
            languages=args.languages,
        )
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    except TranscriptsDisabled:
        print("Error: Transcripts are disabled for this video.", file=sys.stderr)
        return 1
    except NoTranscriptFound:
        print("Error: No transcript found for this video.", file=sys.stderr)
        return 1
    except VideoUnavailable:
        print("Error: Video is unavailable.", file=sys.stderr)
        return 1

    print(f"Saved transcript to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
