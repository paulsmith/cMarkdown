#include <Python.h>
#include "markdown.h"
#include "xhtml.h"

static PyObject *
markdown_render(PyObject *self, PyObject *args, PyObject *kwds)
{
    struct buf *ib, *ob;
    struct mkd_renderer renderer;
    const char *s;
    int size;
    /* flags - renderer and markdown extensions */
    int skip_html = 0, skip_style = 0, skip_images = 0, skip_links = 0,
        smartypants = 0, safelink = 0, toc = 0, hard_wrap = 0, lax_emphasis = 0,
        tables = 0, fenced_code = 0, autolink = 0, strikethrough = 0,
        lax_html_blocks = 0;
    unsigned int render_flags = XHTML_EXPAND_TABS, extensions = 0;
    PyObject *result;

    static char *kwlist[] = {"text", "skip_html", "skip_style", "skip_images",
                             "skip_links", "smartypants", "safelink",
                             "toc", "hard_wrap", "lax_emphasis", "tables",
                             "fenced_code", "autolink", "strikethrough",
                             "lax_html_blocks", NULL};

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "s#|iiiiiiiiiiiiii", kwlist, &s, &size,
            &skip_html, &skip_style, &skip_images, &skip_links, &smartypants,
            &safelink, &toc, &hard_wrap, &lax_emphasis, &tables,
            &fenced_code, &autolink, &strikethrough, &lax_html_blocks))
        return NULL;

    /* Set render flags */
    if (skip_html)
        render_flags |= XHTML_SKIP_HTML;

    if (skip_style)
        render_flags |= XHTML_SKIP_STYLE;

    if (skip_images)
        render_flags |= XHTML_SKIP_IMAGES;

    if (skip_links)
        render_flags |= XHTML_SKIP_LINKS;

    if (smartypants)
        render_flags |= XHTML_SMARTYPANTS;

    if (safelink)
        render_flags |= XHTML_SAFELINK;

    if (toc)
        render_flags |= XHTML_TOC;

    if (hard_wrap)
        render_flags |= XHTML_HARD_WRAP;

    /* Set extension flags */
    if (lax_emphasis)
        extensions |= MKDEXT_LAX_EMPHASIS;

    if (tables)
        extensions |= MKDEXT_TABLES;

    if (fenced_code)
        extensions |= MKDEXT_FENCED_CODE;

    if (autolink)
        extensions |= MKDEXT_AUTOLINK;

    if (strikethrough)
        extensions |= MKDEXT_STRIKETHROUGH;

    if (lax_html_blocks)
        extensions |= MKDEXT_LAX_HTML_BLOCKS;

    ib = bufnew(size);
    bufgrow(ib, size);
    ib->data = (char *)s;
    ib->size = size;

    ob = bufnew(128);
    bufgrow(ob, size * 1.2);

    ups_xhtml_renderer(&renderer, render_flags);

    ups_markdown(ob, ib, &renderer, extensions);

    result = Py_BuildValue("s#", ob->data, ob->size);

    ups_free_renderer(&renderer);
    bufrelease(ob);

    return result;
}

static PyMethodDef MarkdownMethods[] = {
    {"markdown", (PyCFunction)markdown_render, METH_VARARGS | METH_KEYWORDS, PyDoc_STR("Render Markdown to HTML.")},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
initcMarkdown(void)
{
    (void)Py_InitModule("cMarkdown", MarkdownMethods);
}
