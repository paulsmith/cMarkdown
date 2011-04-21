import glob
import os
import re
import unittest
import cMarkdown

md = cMarkdown.markdown

class TestMarkdown(unittest.TestCase):
    def test_basic_html_rendering(self):
        self.assertEqual(md('# Hello, world!\n\nNow is the time for all good men to come to the aid of their party.'),
                         '<h1>Hello, world!</h1>\n\n<p>Now is the time for all good men to come to the aid of their party.</p>\n')

    def test_skip_html_flag(self):
        self.assertEqual(md('<b>Foo</b> <a href="http://example.com">Bar</a>', skip_html=True),
                         '<p>&lt;b&gt;Foo&lt;/b&gt; &lt;a href=&quot;http://example.com&quot;&gt;Bar&lt;/a&gt;</p>\n')

    def test_skip_style_flag(self):
        self.assertEqual(md('<b>Foo</b> <style>b{display:none;}</style> <a href="http://example.com">Bar</a>', skip_style=True),
                         '<p><b>Foo</b> &lt;style&gt;b{display:none;}&lt;/style&gt; <a href="http://example.com">Bar</a></p>\n')

    def test_skip_images_flag(self):
        self.assertEqual(md('<b>Foo</b> <img src="http://example.com/quux.gif"/> <a href="http://example.com">Bar</a>', skip_images=True),
                         '<p><b>Foo</b> &lt;img src=&quot;http://example.com/quux.gif&quot;/&gt; <a href="http://example.com">Bar</a></p>\n')

    def test_skip_links_flag(self):
        self.assertEqual(md('<b>Foo</b> <a href="http://example.com">Bar</a>', skip_links=True),
                         '<p><b>Foo</b> &lt;a href=&quot;http://example.com&quot;&gt;Bar&lt;/a&gt;</p>\n')

    def test_smartypants_flag(self):
        self.assertEqual(md('''"Hello, let's eat."'''),
                         "<p>&quot;Hello, let's eat.&quot;</p>\n")
        self.assertEqual(md('''"Hello, let's eat."''', smartypants=True),
                         '<p>&ldquo;Hello, let&rsquo;s eat.&rdquo;</p>\n')

    def test_safelink_flag(self):
        self.assertEqual(md('[Test](badscheme://danger)'), '<p><a href="badscheme://danger">Test</a></p>\n')
        self.assertEqual(md('[Test](badscheme://danger)', safelink=True), '<p>[Test](badscheme://danger)</p>\n')

    def test_toc_flag(self):
        self.assertEqual(md('# Foo\n\n## Bar', toc=True), '<a name="toc_0"></a><h1>Foo</h1>\n\n<a name="toc_1"></a><h2>Bar</h2>\n')

    def test_hard_wrap_flag(self):
        self.assertEqual(md('A\nB\nC'), '<p>A\nB\nC</p>\n')
        self.assertEqual(md('A\nB\nC', hard_wrap=True), '<p>A<br/>\nB<br/>\nC</p>\n')

    def test_tables(self):
        self.assertEqual(md('''\
a | b
--|--
1 | 2''', tables=True), '<table><thead>\n<tr>\n<td>a</td>\n<td>b</td>\n</tr>\n</thead><tbody>\n<tr>\n<td>1</td>\n<td>2</td>\n</tr>\n</tbody></table>')

    def test_fenced_code(self):
        self.assertEqual(md('''\
```
def foo():
    pass
```''', fenced_code=True), '<pre><code>def foo():\n    pass\n</code></pre>\n')

    def test_fenced_code_with_lang(self):
        self.assertEqual(md('''\
``` python
def foo():
    pass
```''', fenced_code=True), '<pre lang="python"><code>def foo():\n    pass\n</code></pre>\n')

    def test_autolink(self):
        self.assertEqual(md('Visit http://example.com/ today', autolink=True),
                         '<p>Visit <a href="http://example.com/">http://example.com/</a> today</p>\n')

    def test_strikethrough(self):
        self.assertEqual(md('~~Strike~~', strikethrough=True), '<p><del>Strike</del></p>\n')

def make_testcase(textfile):
    def testcase(self):
        expected_html = open(textfile.replace('.text', '.html')).read().strip()
        actual_html = cMarkdown.markdown(open(textfile).read()).strip()
        self.assertEqual(expected_html, actual_html)
    return testcase

def gen_tests(cls):
    testsdir = os.path.join(os.path.dirname(__file__), 'MarkdownTest_1.0.3', 'Tests')
    for textfile in glob.glob(os.path.join(testsdir, '*')):
        name = os.path.splitext(os.path.basename(textfile))[0]
        fn_name = 'test_mdtestsuite_' + re.sub('[^a-z0-9_]+', '', re.sub('\s+', '_', name.lower()))
        testcase = make_testcase(textfile)
        testcase.__name__ = fn_name
        testcase.__doc__ = 'Markdown test suite: {0}'.format(name)
        setattr(cls, fn_name, testcase)

# 7 tests from the Markdown test suite fail currently because of slight discrepancies, mostly with escaping HTML entities
gen_tests(TestMarkdown)

if __name__ == '__main__':
    unittest.main()

