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


class PaperCatalogTests(unittest.TestCase):
    CATALOG = '''<a id="personal-evaluation"></a>
## Evaluation
<a id="benchmark-one"></a>
### B1. Benchmark
[paper](https://example.org/paper(v1)) [data](https://example.org/data)
<a id="memory-methods"></a>
## Methods
### M1. Method
[paper](https://example.org/method)
<a id="human-studies"></a>
## Human studies
### H1. Human study
[paper](https://example.org/human)
<a id="sources-and-rights"></a>
## Sources
[not part of H1](https://example.org/rights)
'''

    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix='paper-checker-selftest-')
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        (self.root / 'docs').mkdir()
        self.write(self.CATALOG, self.CATALOG)

    def write(self, zh, en):
        for filename, text in [('PAPERS.md', zh), ('PAPERS.en.md', en)]:
            (self.root / 'docs' / filename).write_text(text, encoding='utf-8')

    def errors(self):
        return check_docs.check_papers(self.root)

    def test_valid_pair_and_general_checker_integration(self):
        self.assertEqual(self.errors(), [])
        self.assertEqual(check_docs.check(self.root)[0], [])

    def test_reading_guide_subheading_is_not_a_paper_entry(self):
        text = '<a id="reading-paths"></a>\n## Guide\n### User profiles: four questions\n' + self.CATALOG
        self.write(text, text)
        self.assertEqual(self.errors(), [])

    def test_missing_resource_link(self):
        self.write(self.CATALOG, self.CATALOG.replace('[data](https://example.org/data)', 'data above'))
        self.assertTrue(any('B1 bilingual external URL mismatch' in e for e in self.errors()))
        self.assertTrue(any('external URL mismatch' in e for e in check_docs.check(self.root)[0]))

    def test_entry_heading_url_is_included(self):
        text = self.CATALOG.replace('### B1. Benchmark', '### B1. [Benchmark](https://example.org/heading)')
        self.write(text, self.CATALOG)
        self.assertTrue(any('B1 bilingual external URL mismatch' in e for e in self.errors()))

    def test_duplicate_id(self):
        self.write(self.CATALOG, self.CATALOG.replace('### B1. Benchmark', '### B1. First\n### B1. Benchmark'))
        self.assertTrue(any('duplicate paper ID B1' in e for e in self.errors()))

    def test_missing_interior_id(self):
        text = self.CATALOG.replace('### B1. Benchmark', '### B3. Benchmark')
        self.write(text, text)
        self.assertTrue(any('non-contiguous B IDs' in e for e in self.errors()))

    def test_huge_sparse_id_does_not_allocate_a_range(self):
        text = self.CATALOG.replace('### B1. Benchmark', '### B1000000000. Benchmark')
        self.write(text, text)
        self.assertTrue(any('non-contiguous B IDs' in e for e in self.errors()))

    def test_ids_can_be_out_of_numerical_order(self):
        text = self.CATALOG.replace('### B1. Benchmark', '### B2. Later ID\n### B1. Benchmark')
        self.write(text, text)
        self.assertEqual(self.errors(), [])

    def test_bilingual_order_mismatch(self):
        zh = self.CATALOG.replace('### B1. Benchmark', '### B1. First\n### B2. Second')
        en = self.CATALOG.replace('### B1. Benchmark', '### B2. Second\n### B1. First')
        self.write(zh, en)
        self.assertTrue(any('ID/order mismatch' in e for e in self.errors()))

    def test_stray_human_heading_breaks_method_interval(self):
        text = self.CATALOG.replace('### M1. Method', '## New group: Human studies, not benchmarks\n### M1. Method')
        self.write(self.CATALOG, text)
        self.assertTrue(any('M1 outside its M section' in e for e in self.errors()))

    def test_real_human_section_rejects_method(self):
        text = self.CATALOG.replace('### H1. Human study', '### M2. Method\n### H1. Human study')
        self.write(text, text)
        self.assertTrue(any('M2 outside its M section' in e for e in self.errors()))

    def test_review_labels_both_languages(self):
        for label in ('**待审：** ', '**English review:** '):
            with self.subTest(label=label):
                self.write(self.CATALOG, self.CATALOG.replace('[paper]', label+'[paper]', 1))
                self.assertTrue(any('forbidden review label' in e for e in self.errors()))

    def test_examples_comments_and_prose_do_not_trigger_review_label(self):
        text = self.CATALOG + '\n<!-- **待审：** -->\n```md\n**English review:**\n### B999. Example\n```\nA discussion of English review is fine.\n'
        self.write(text, text)
        self.assertEqual(self.errors(), [])

    def test_resource_order_labels_and_repetition_do_not_matter(self):
        text = self.CATALOG.replace('[paper](https://example.org/paper(v1)) [data](https://example.org/data)',
                                    '[数据](https://example.org/data) [论文](https://example.org/paper(v1)) [again](https://example.org/data)')
        self.write(self.CATALOG, text)
        self.assertEqual(self.errors(), [])

    def test_following_section_links_not_assigned_to_last_entry(self):
        self.write(self.CATALOG, self.CATALOG.replace('https://example.org/rights', 'https://example.org/en-rights'))
        self.assertEqual(self.errors(), [])

    def test_missing_pair_and_empty_catalog_fail(self):
        (self.root / 'docs/PAPERS.en.md').unlink()
        self.assertTrue(self.errors())
        self.write('', '')
        self.assertTrue(any('missing B entries' in e for e in self.errors()))

    def test_malformed_heading(self):
        text = self.CATALOG.replace('### B1. Benchmark', '### B0. Benchmark')
        self.write(text, text)
        self.assertTrue(any('malformed paper entry heading' in e for e in self.errors()))

    def test_bilingual_section_difference(self):
        text = self.CATALOG.replace('id="personal-evaluation"', 'id="safety-evaluation"')
        self.write(self.CATALOG, text)
        self.assertTrue(any('B1 bilingual section mismatch' in e for e in self.errors()))


    def test_thematic_method_sections_and_legacy_aliases(self):
        for section in ('user-understanding-methods', 'memory-methods',
                        'planning-action-methods', 'proactive-clarification-methods',
                        'privacy-safety-methods'):
            with self.subTest(section=section):
                text = self.CATALOG.replace('<a id="memory-methods"></a>',
                    '<a id="legacy-methods-heading"></a>\n'
                    f'<a id="{section}"></a>')
                self.write(text, text)
                self.assertEqual(self.errors(), [])

    def test_method_theme_bilingual_mismatch(self):
        zh = self.CATALOG.replace('id="memory-methods"', 'id="planning-action-methods"')
        en = self.CATALOG.replace('id="memory-methods"', 'id="privacy-safety-methods"')
        self.write(zh, en)
        self.assertTrue(any('M1 bilingual section mismatch' in e for e in self.errors()))

    def test_human_entry_rejected_in_new_method_theme(self):
        text = self.CATALOG.replace('id="human-studies"', 'id="privacy-safety-methods"')
        self.write(text, text)
        self.assertTrue(any('H1 outside its H section' in e for e in self.errors()))

    def test_method_themes_do_not_require_numerical_order(self):
        text = self.CATALOG.replace('### M1. Method',
            '### M2. Later ID\n<a id="proactive-clarification-methods"></a>\n'
            '## Clarification\n### M1. Method')
        self.write(text, text)
        self.assertEqual(self.errors(), [])

if __name__ == '__main__':
    unittest.main()
