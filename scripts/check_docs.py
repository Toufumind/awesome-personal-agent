#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# This original script only is MIT-licensed; see scripts/LICENSE.
"""Offline checks for this repository's Markdown conventions (Python 3.9+).

Checks inline Markdown links/images, reference definitions, HTML href/src,
explicit HTML anchors and ordinary ATX headings. Not a general Markdown renderer:
prefer explicit anchors for complex headings; exotic Markdown needs manual review.
Does not fetch external URLs, change files, judge translation quality, or evaluate
agents. Run from any directory: python3 scripts/check_docs.py [repository-root].
"""

import html
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

# Existing documents containing both languages in one file, not missing translations.
BILINGUAL_SINGLE_FILES = {
    "docs/LICENSE.md", "fixtures/t03/SMOKE-RESULTS.md",
    ".github/pull_request_template.md",  # GitHub uses one bilingual default template.
}
EXCLUDED_DIRS = {".git", ".venv", "node_modules", "__pycache__"}
INLINE_LINK = re.compile(r'!?\[[^\]\n]*\]\(\s*(<[^>\n]*>|(?:[^\s()]|\([^()]*\))+)'
                         r'(?:\s+["\'][^\n]*["\'])?\s*\)')
REFERENCE = re.compile(r'^ {0,3}\[[^\]]+\]:\s*(<[^>]+>|\S+)', re.MULTILINE)


class Tags(HTMLParser):
    def __init__(self):
        super().__init__()
        self.anchors = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if value is None:
                continue
            if name == "id" or (tag == "a" and name == "name"):
                self.anchors.append(value)
            if name in {"href", "src"}:
                self.links.append(value)


def visible_text(text):
    """Remove fenced examples/comments; retain newlines for heading boundaries."""
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    result, fence = [], None
    for line in text.splitlines():
        match = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if fence:
            if (match and match[1][0] == fence[0] and len(match[1]) >= len(fence)
                    and not line[match.end():].strip()):
                fence = None
            result.append('')
        elif match:
            fence = match[1]
            result.append('')
        else:
            result.append(line)
    return '\n'.join(result)


def escaped(text, position):
    """An odd run of backslashes escapes the opening bracket; even runs do not."""
    preceding = text[:position]
    return (len(preceding) - len(preceding.rstrip('\\'))) % 2 == 1


def parse(text):
    text = visible_text(text)
    # Inline code is not an HTML tag or a Markdown link.
    no_code = re.sub(r'(`+).*?\1', '', text)
    tags = Tags()
    tags.feed(no_code)
    anchors = set(tags.anchors)
    generated = set()
    for heading in re.findall(r'^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$', text, re.MULTILINE):
        heading = re.sub(r'!?\[([^]]*)\]\([^)]*\)', r'\1', heading)
        heading = html.unescape(re.sub(r'<[^>]+>', '', heading)).lower()
        # Repository uses simple headings; complex Unicode/symbol slugs should use IDs.
        slug = re.sub(r'[^\w\- ]', '', heading).replace(' ', '-')
        candidate, number = slug, 0
        while candidate in generated:
            number += 1
            candidate = f'{slug}-{number}'
        generated.add(candidate)
    anchors.update(generated)
    links = tags.links + [m[1].strip('<>') for m in INLINE_LINK.finditer(no_code)
                         if not escaped(no_code, m.start() + (m[0][0] == '!'))]
    links += [m[1].strip('<>') for m in REFERENCE.finditer(no_code)]
    duplicates = sorted({a for a in tags.anchors if tags.anchors.count(a) > 1})
    return anchors, links, duplicates


def check(root):
    root = Path(root).resolve()
    files = sorted(p for p in root.rglob('*.md')
                   if not any(part in EXCLUDED_DIRS for part in p.relative_to(root).parts))
    errors, parsed = [], {}
    for path in files:
        if path.is_symlink():
            errors.append(f'{path.relative_to(root)}: symlink Markdown is unsupported')
            continue
        parsed[path] = parse(path.read_text(encoding='utf-8'))
    for path, (anchors, links, duplicates) in parsed.items():
        relative = path.relative_to(root).as_posix()
        for anchor in duplicates:
            errors.append(f'{relative}: duplicate explicit anchor #{anchor}')
        if relative not in BILINGUAL_SINGLE_FILES:
            counterpart = (path.with_name(path.name[:-6] + '.md') if path.name.endswith('.en.md')
                           else path.with_name(path.stem + '.en.md'))
            if counterpart not in parsed:
                errors.append(f'{relative}: missing bilingual counterpart {counterpart.name}')
        for link in links:
            try:
                url = urlsplit(html.unescape(link))
            except ValueError as error:
                errors.append(f'{relative}: malformed link URL: {link} ({error})')
                continue
            if url.scheme or url.netloc:
                continue  # External URLs are deliberately not fetched or judged.
            destination = unquote(url.path)
            target = (root / destination.lstrip('/') if destination.startswith('/')
                      else path.parent / destination).resolve() if destination else path
            try:
                target.relative_to(root)
            except ValueError:
                errors.append(f'{relative}: local link escapes repository: {link}')
                continue
            if not target.exists():
                errors.append(f'{relative}: missing local target: {link}')
            elif url.fragment and target.suffix == '.md':
                if target not in parsed or unquote(url.fragment) not in parsed[target][0]:
                    errors.append(f'{relative}: missing Markdown anchor: {link}')
    return errors, len(parsed)


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    errors, count = check(root)
    for error in errors:
        print(error, file=sys.stderr)
    if not count:
        print('No Markdown documents found; refusing an empty check.', file=sys.stderr)
        return 1
    if errors:
        return 1
    print(f'PASS: {count} Markdown files; local links/anchors and bilingual file presence. '
          'External URLs, translation accuracy, and agent performance not assessed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
