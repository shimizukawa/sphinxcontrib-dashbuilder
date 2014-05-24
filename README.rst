`sphinxcontrib_dashbuilder` generate a 'Documentation Set' intended to be used with the `dash API browser` from a Sphinx documentation.

You can read the 'Documentation Set' style document by using `dash API browser`.

* For Mac OS X users: dash_
* For Windows or Linux users: Zeal_

This extension has been inspired by doc2dash_

.. _dash: http://kapeli.com/dash
.. _Zeal: http://zealdocs.org/
.. _doc2dash: https://pypi.python.org/pypi/doc2dash

Features
==========

Implemented:

* Generate a 'Documentation Set' for dash API browser.


Not Implemented yet:

* Keyword indexing with Sphinx i18n translated documentation.
* Disable sidebar
* Table of contents support http://kapeli.com/docsets#tableofcontents


Install
========

::

   $ pip install sphinxcontrib-dashbuilder


If you wanto to use unrelease version, you can install from repository::

   $ pip install -e hg+https://bitbucket.org/shimizukawa/sphinxcontrib-dashbuilder


Run
======

conf.py::

   extensions = ['sphinxcontrib.dashbuilder']

::

   $ sphinx-build -b dash [source] [outdir]

