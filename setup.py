from setuptools import setup, Extension

setup(
    name='cMarkdown',
    version='0.1',
    description='Markdown for Python, accelerated by C.',
    author='Paul Smith',
    author_email='paulsmith@pobox.com',
    ext_modules=[Extension(
        'cMarkdown', 
        sources=['src/_markdown.c', 'src/markdown.c', 'src/array.c', 'src/buffer.c', 'src/xhtml.c']
    )]
)
