# -*- coding: utf-8 -*-
"""
    Sphinx test suite utilities
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2014 by shimizukawa@gmail.com.
    :license: BSD, see LICENSE for details.
"""

import os
import shutil
from functools import wraps

from six import StringIO
from sphinx import application


__all__ = [
    'test_root', 'TestApp', 'with_app',
]


test_root = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'doc')


class ListOutput(object):
    """
    File-like object that collects written text in a list.
    """
    def __init__(self, name):
        self.name = name
        self.content = []

    def reset(self):
        del self.content[:]

    def write(self, text):
        self.content.append(text)


class TestApp(application.Sphinx):
    """
    A subclass of :class:`Sphinx` that runs on the test root, with some
    better default values for the initialization parameters.
    """

    def __init__(self, srcdir=None, confdir=None, outdir=None, doctreedir=None,
                 buildername='html', confoverrides=None,
                 status=None, warning=None, freshenv=None,
                 warningiserror=None, tags=None,
                 confname='conf.py', cleanenv=False):

        application.CONFIG_FILENAME = confname

        self.cleanup_trees = [os.path.join(test_root, 'generated')]

        if srcdir is None:
            srcdir = test_root
        self.builddir = os.path.join(srcdir, '_build')
        if confdir is None:
            confdir = srcdir
        if outdir is None:
            outdir = os.path.join(srcdir, self.builddir, buildername)
            if not os.path.exists(outdir):
                os.makedirs(outdir)
            self.cleanup_trees.insert(0, outdir)
        if doctreedir is None:
            doctreedir = os.path.join(srcdir, srcdir, self.builddir, 'doctrees')
            if not os.path.exists(doctreedir):
                os.makedirs(doctreedir)
            if cleanenv:
                self.cleanup_trees.insert(0, doctreedir)
        if confoverrides is None:
            confoverrides = {}
        if status is None:
            status = StringIO()
        if warning is None:
            warning = ListOutput('stderr')
        if freshenv is None:
            freshenv = False
        if warningiserror is None:
            warningiserror = False

        application.Sphinx.__init__(self, srcdir, confdir, outdir, doctreedir,
                                    buildername, confoverrides, status, warning,
                                    freshenv, warningiserror, tags)

    def cleanup(self, doctrees=False):
        for tree in self.cleanup_trees:
            shutil.rmtree(tree, True)


def with_app(*args, **kwargs):
    """
    Make a TestApp with args and kwargs, pass it to the test and clean up
    properly.
    """
    def generator(func):
        @wraps(func)
        def deco(*args2, **kwargs2):
            app = TestApp(*args, **kwargs)
            func(app, *args2, **kwargs2)
            # don't execute cleanup if test failed
            app.cleanup()
        return deco
    return generator
