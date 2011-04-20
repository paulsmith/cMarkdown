from distutils.core import setup, Extension

setup(name='cpymarkdown',
      version='0.1',
      description='Markdown for Python',
      ext_modules=[Extension(
        'markdown', 
        sources=['src/_markdown.c', 'src/markdown.c', 'src/array.c', 'src/buffer.c', 'src/xhtml.c']
      )]
)
