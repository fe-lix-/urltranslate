from url_translate import URLTranslator
import unittest
from BeautifulSoup import BeautifulSoup

class TestURLTranslator(unittest.TestCase):
    
    def setUp(self):
        self.html = """<div>
        http://a.b/c
        <a href="http://a.b/c">foo</a>
        <a href="http://a.c/b">bar</a>
    </div>
    """

        self.html_relative = """<div>
        http://a.b/c
        <a href="../c">foo</a>
        <a href="http://a.c/b">bar</a>
    </div>
    """
        self.location = "http://a.b/d/e"

        self.result = unicode(BeautifulSoup("""<div>
        http://a.b/c
        <a href="http://foo">foo</a>
        <a href="http://bar">bar</a>
    </div>
    """))

        self.dictionary = {
            "http://a.b/c": "http://foo",
            "http://a.c/b": "http://bar"
        }

    def test_simple_translation(self):
        a = URLTranslator()
        a.dictionary = self.dictionary
        output = a.translate(self.html)

        self.assertEqual(output, self.result)

    def test_relative_link(self):
        a = URLTranslator()
        a.dictionary = self.dictionary
        a.location = self.location
        output = a.translate(self.html_relative)

        self.assertEqual(output, self.result)

if __name__ == '__main__':
    unittest.main()

