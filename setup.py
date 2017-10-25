# coding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals


from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


setup(
    name='aptly-uploader',
    version='0.1',
    description='Upload deb files to aptly',
    url='https://github.com/craigds/aptly-uploader',
    author='Craig de Stigter',
    author_email='craig.ds@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=[],
    install_requires=['requests'],
    scripts=['bin/aptly-upload'],
)
