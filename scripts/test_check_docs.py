# SPDX-License-Identifier: MIT
# This original test file only is MIT-licensed; see scripts/LICENSE.
"""Offline checker self-tests, not agent evaluations or translation review."""

from pathlib import Path
import tempfile
import subprocess
import sys
import unittest

import check_docs


class DocumentationTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix='docs-checker-selftest-')
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.write('README.md', '# 中文\n[English](README.en.md)\n')
        self.write('README.en.md', '# English\n[中文](README.md)\n')

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')

    def errors(self):
        return check_docs.check(self.root)[0]

    def test_valid_pair(self):
        self.assertEqual(self.errors(), [])

    def test_missing_translation(self):
        self.write('new.md', '# New')
        self.assertTrue(any('missing bilingual counterpart' in e for e in self.errors()))

    def test_missing_local_file(self):
        self.write('README.md', '[missing](absent.txt)')
        self.assertTrue(any('missing local target' in e for e in self.errors()))

    def test_explicit_and_heading_anchors(self):
        self.write('README.md', '[one](README.en.md#stable) [two](README.en.md#hello-world-1)')
        self.write('README.en.md', '<a id="stable"></a>\n# Hello world\n# Hello world\n')
        self.assertEqual(self.errors(), [])

    def test_missing_anchor(self):
        self.write('README.md', '[broken](README.en.md#absent)')
        self.assertTrue(any('missing Markdown anchor' in e for e in self.errors()))

    def test_url_decoding_and_asset(self):
        self.write('my file.txt', 'asset')
        self.write('README.md', '[asset](my%20file.txt) [heading](#%E4%B8%AD%E6%96%87)\n# 中文')
        self.assertEqual(self.errors(), [])

    def test_external_urls_ignored(self):
        self.write('README.md', '[url](https://invalid.example/missing#nope) '
                   '[email](mailto:test@example.invalid) [url](//invalid.example/path)')
        self.assertEqual(self.errors(), [])

    def test_code_and_comments_ignored(self):
        self.write('README.md', '<!-- [bad](no.txt) -->\n```md\n[bad](no.txt)\n```\n'
                   '`[bad](no.txt)`\n~~~\n[bad](no.txt)\n~~~\n')
        self.assertEqual(self.errors(), [])

    def test_html_reference_image_links(self):
        self.write('README.md', '<a href="one.txt">one</a>\n[x][ref]\n[ref]: two.txt\n![x](three.png)')
        self.assertEqual(sum('missing local target' in e for e in self.errors()), 3)

    def test_parent_traversal_is_rejected(self):
        self.write('README.md', '[outside](../outside.txt)')
        self.assertTrue(any('escapes repository' in e for e in self.errors()))

    def test_duplicate_explicit_anchor(self):
        self.write('README.md', '<a id="same"></a><a id="same"></a>')
        self.assertTrue(any('duplicate explicit anchor' in e for e in self.errors()))

    def test_existing_bilingual_single_file(self):
        self.write('docs/LICENSE.md', '# 中文 / English')
        self.assertEqual(self.errors(), [])

    def test_nested_parenthesis_asset(self):
        self.write('file(1).txt', 'asset')
        self.write('README.md', '[asset](file(1).txt)')
        self.assertEqual(check_docs.parse('[asset](file(1).txt)')[1], ['file(1).txt'])
        self.assertEqual(self.errors(), [])

    def test_missing_chinese_counterpart(self):
        self.write('new.en.md', '# New')
        self.assertTrue(any('missing bilingual counterpart new.md' in e for e in self.errors()))

    def test_fenced_heading_is_not_an_anchor(self):
        self.write('README.md', '[bad](#hidden)\n```md\n# Hidden\n```')
        self.assertTrue(any('missing Markdown anchor' in e for e in self.errors()))

    def test_repository_absolute_links(self):
        self.write('README.md', '[English](/README.en.md#english)')
        self.assertEqual(self.errors(), [])


    def test_escaped_literal_bracket_is_not_link(self):
        self.write('README.md', r'\[not a link](missing.txt)')
        self.assertEqual(self.errors(), [])

    def test_even_backslashes_do_not_escape_bracket(self):
        self.write('README.md', r'\\[real link](missing.txt)')
        self.assertTrue(any('missing local target' in e for e in self.errors()))

    def test_fence_with_trailing_text_does_not_close_block(self):
        for fence in ('```', '~~~'):
            with self.subTest(fence=fence):
                self.write('README.md', f'{fence}md\n{fence}not-a-close\n'
                           f'[not a link](missing.txt)\n{fence}\n')
                self.assertEqual(self.errors(), [])

    def test_longer_fence_and_trailing_whitespace_close_block(self):
        self.write('README.md', '```md\nignored\n````  \t\n[bad](missing.txt)')
        self.assertTrue(any('missing local target' in e for e in self.errors()))

    def test_malformed_url_reports_error_without_crashing(self):
        self.write('README.md', '[bad](http://[broken)')
        self.assertTrue(any('malformed link URL' in e for e in self.errors()))

    def test_unclosed_link_does_not_cause_catastrophic_backtracking(self):
        # A child process bounds regression runtime even if the regex hangs.
        result = subprocess.run(
            [sys.executable, '-c',
             "import check_docs; assert check_docs.parse('[x](' + 'a' * 10000)[1] == []"],
            cwd=Path(check_docs.__file__).resolve().parent,
            capture_output=True, text=True, timeout=3, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == '__main__':
    unittest.main()
