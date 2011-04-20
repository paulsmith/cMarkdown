import glob
import os
import re
import unittest
import cMarkdown

class TestMarkdown(unittest.TestCase):
    pass

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
        fn_name = 'test_' + re.sub('[^a-z0-9_]+', '', re.sub('\s+', '_', name.lower()))
        testcase = make_testcase(textfile)
        testcase.__name__ = fn_name
        testcase.__doc__ = 'Markdown test: {0}'.format(name)
        setattr(cls, fn_name, testcase)

gen_tests(TestMarkdown)

if __name__ == '__main__':
    unittest.main()
        
