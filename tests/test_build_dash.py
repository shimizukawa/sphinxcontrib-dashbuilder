# -*- coding: utf-8 -*-
"""
    test_build_dash
    ~~~~~~~~~~~~~~~~

    test dash builder

    :copyright: Copyright 2014 by shimizukawa@gmail.com.
    :license: BSD, see LICENSE for details.
"""

import os
import shutil

from util import with_app, test_root


def teardown_module():
    shutil.rmtree(os.path.join(test_root, '_build'), True)


@with_app(buildername='dash')
def test_dash(app):
    app.builder.build_all()
