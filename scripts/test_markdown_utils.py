"""Ordinary example forms at diagnostic parsing boundaries."""

import unittest

from markdown_utils import visible_lines, without_inline_code


class MarkdownVisibilityTest(unittest.TestCase):
    def test_quote_container_exit_does_not_hide_following_source(self):
        self.assertEqual(list(visible_lines('> ```md\n> example\n# Actual owner\n')), ['# Actual owner'])

    def test_long_fence_and_matching_inline_spans(self):
        self.assertEqual(list(visible_lines('````\n```\n# hidden\n````\n# shown')), ['# shown'])
        self.assertEqual(without_inline_code('before ``one ` two`` after'), 'before  after')
        self.assertEqual(without_inline_code('unmatched ` then ``code`` after'), 'unmatched ` then  after')


if __name__ == "__main__":
    unittest.main()
