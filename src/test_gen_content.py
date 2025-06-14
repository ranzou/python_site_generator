import unittest
from gen_content import extract_title


def test_extract_title(self):
    md = """
**Blah**
# This is a heading
"""
    output = extract_title(md)
    self.assertEqual(output, "This is a heading")
