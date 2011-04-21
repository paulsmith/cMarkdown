from distutils.core import setup, Extension

setup(
    name='cMarkdown',
    version='0.1.1',
    description='Markdown for Python, accelerated by C.',
    author='Paul Smith',
    author_email='paulsmith@pobox.com',
    ext_modules=[Extension(
        'cMarkdown', 
        sources=['src/_markdown.c', 'src/markdown.c', 'src/array.c', 'src/buffer.c', 'src/xhtml.c']
    )],
    scripts=['bin/markdown'],
    url='https://github.com/paulsmith/cMarkdown',
    download_url='https://github.com/paulsmith/cMarkdown/archives/master',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Topic :: Communications :: Email :: Filters',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Software Development :: Documentation',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML',
    ]
)
