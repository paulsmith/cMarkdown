#include <Python.h>
#include "markdown.h"
#include "xhtml.h"

static PyObject *
markdown_render(PyObject *self, PyObject *args)
{
    struct buf *ib, *ob;
    struct mkd_renderer renderer;
    const char *s;
    int size;
    PyObject *result;

    if (!PyArg_ParseTuple(args, "s#", &s, &size))
        return NULL;

    ib = bufnew(size);
    bufgrow(ib, size+1);
    ib->data = s;
    ib->size = size+1;

    ob = bufnew(128);
    bufgrow(ob, size * 1.2);

    ups_xhtml_renderer(&renderer, 0);

    ups_markdown(ob, ib, &renderer, 0xFF);

    result = Py_BuildValue("s", ob->data);

    ups_free_renderer(&renderer);
    bufrelease(ob);

    return result;
}

static PyMethodDef MarkdownMethods[] = {
    {"markdown", (PyCFunction)markdown_render, METH_VARARGS, PyDoc_STR("Render Markdown to HTML.")},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
initcMarkdown(void)
{
    (void)Py_InitModule("cMarkdown", MarkdownMethods);
}
