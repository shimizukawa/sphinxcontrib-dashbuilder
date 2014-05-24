# -*- coding: utf-8 -*-
"""
    sphinxcontrib-dashbuilder
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Sphinx Dash builder.

    :copyright: Copyright 2014 by shimizukawa@gmail.com.
    :license: BSD, see LICENSE for details.
"""
from sphinx.writers.html import HTMLTranslator


class DashTranslator(HTMLTranslator):

    def depart_title(self, node):
        if node.parent.hasattr('ids') and node.parent['ids']:
            anchor = node.parent['ids'][0]
            #self.body.append('<a name="%s">' % APPLE_REF(entry=entry))

        HTMLTranslator.depart_title(self, node)

    def depart_desc_signature(self, node):
        if node['ids']:
            pass
            #self.body.append('<a name="%s">' % APPLE_REF(entry=entry))

        HTMLTranslator.depart_desc_signature(self, node)
