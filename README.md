cMarkdown
=========

[Markdown][1] for Python, accelerated by C.

Installation
------------

    $ pip install cMarkdown

Usage
-----

    >>> import cMarkdown as markdown
    >>> markdown.markdown('# Hello, world!')
    '<h1>Hello, world!</h1>\n'

Rendering flags
---------------

These are keyword arguments to pass to `markdown()`. They all default to
`False`.

 * `skip_html=True`: Any HTML in the input will be escaped on output.
 * `skip_style=True`: Any `<style>` elements in the input will be escaped on output.
 * `skip_images=True`: Any `<img>` elements in the input will be escaped on output.
 * `skip_links=True`: Any `<a>` elements in the input will be escaped on output.
 * `smartypants=True`: Applies [smart punctuation][2] transformations.
 * `toc=True`: Inserts anchors before `<h1>`, `<h2>`, _et al._ for linking in-document from a table of contents.
 * `hard_wrap=True`: Inserts `<br/>` tags before newlines in paragraphs.

Markdown extension flags
------------------------

These keyword arguments to `markdown()`, which default to `False`, enable
various extensions to the Markdown language.

 * `tables=True`: Enables a tabular format that renders to `<table>` in HTML.
 * `fenced_code=True`: Enables the use of three <code>```</code> to delimit
   the beginning and end of a literal code block.
 * `autolink=True`: Enables the conversion of bare URLs to links in HTML.
 * `strikethrough=True`: Enables the use of two <code>~~</code> before
   and after text to wrap it in the `<del>` tag in HTML.

Credits
-------

Inspired by [redcarpet][3] for Ruby. Like with redcarpet, all the hard
work is done by the (unfortunately named) [upskirt][3] C library. cMarkdown
just makes this Markdown parsing and rendering library available to Python.

 [1]: http://daringfireball.net/projects/markdown/
 [2]: http://daringfireball.net/projects/smartypants/
 [3]: https://github.com/tanoku/redcarpet
 [4]: https://github.com/tanoku/upskirt
