"""Undo word-by-word spacing in scripts that are written without spaces.

Argos (and some other MT engines) emit Thai, Lao, Khmer, Myanmar, Japanese and
Chinese with a space after every token, e.g. "คน เป็น ห่วง ว่า". Read aloud,
TTS treats each space as a pause and the line sounds robotic.

These scripts use spaces only between phrases or sentences, so when a line is
spaced like a word list we join the tokens. Lines that already look natural
(long runs between spaces) are left alone, which keeps real phrase breaks.
"""

from __future__ import annotations

import re

_UNSPACED = (
    "฀-๿"  # Thai
    "຀-໿"  # Lao
    "ក-៿"  # Khmer
    "က-႟"  # Myanmar
    "぀-ヿ"  # Hiragana, Katakana
    "㐀-䶿一-鿿"  # CJK ideographs
)
_RUN = re.compile(f"[{_UNSPACED}]+")
_GAP = re.compile(f"(?<=[{_UNSPACED}]) +(?=[{_UNSPACED}])")

# Natural Thai averages well over 8 characters between spaces; word-by-word
# MT output averages 2-4.
_MAX_AVG_RUN = 5.0
_MIN_GAPS = 3


def tidy_unspaced_script(text: str) -> str:
    if not text:
        return text
    gaps = _GAP.findall(text)
    if len(gaps) < _MIN_GAPS:
        return text
    runs = _RUN.findall(text)
    if not runs:
        return text
    avg = sum(len(r) for r in runs) / len(runs)
    if avg > _MAX_AVG_RUN:
        return text
    return _GAP.sub("", text)
