# -*- coding: utf-8 -*-
"""
    sphinxcontrib-dashbuilder
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Sphinx Dash builder.

    :copyright: Copyright 2014 by shimizukawa@gmail.com.
    :license: BSD, see LICENSE for details.
"""
from __future__ import absolute_import

from .builder import DashBuilder


def setup(app):
    app.add_builder(DashBuilder)

    # :dash_name: name docset explicitly
    app.add_config_value('dash_name', None, 'env')

    # :dash_icon_file: add PNG icon to docset
    app.add_config_value('dash_icon_file', None, 'env')

    # :dash_add_to_docsets: create docset in dashbuilder's default
    # directory and add resulting docset to dash
    app.add_config_value('dash_add_to_docsets', False, 'env')

    # :dash_translator_class: A string with the fully-qualified name of a
    # Dash Translator class, that is, a subclass of Sphinx' DashTranslator,
    # that is used to translate document trees to HTML for Dash.
    # Default is None (use the builtin translator).
    app.add_config_value('dash_translator_class', None, 'env')
