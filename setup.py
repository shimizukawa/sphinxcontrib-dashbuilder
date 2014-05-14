# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst', 'rt') as f:
    long_desc = f.read()

requires = ['Sphinx>=1.2']

setup(
    name='sphinxcontrib-dashbuilder',
    version='0.1.0',
    #url='http://bitbucket.org/birkenfeld/sphinx-contrib',
    url='http://bitbucket.org/shimizukawa/sphinxcontrib_dashbuilder',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-dashbuilder',
    license='BSD',
    author='shimizukawa',
    author_email='shimizukawa@gmail.com',
    description="Sphinx builder extension to generate a 'Documentation Set' for `dash API browser`.",
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
