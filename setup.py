#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os
import glob

thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
install_requires = []
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

config = {
    'name': 'bitmapfont2otb',
    'author': 'Fredrick R. Brennan',
    'url': 'https://github.com/ctrlcctrlv/bitmapfont2otb',
    'description': 'Convert UFO .glif files to SVG',
    'long_description': open('README.md', 'r').read(),
    'license': 'MIT',
    'version': '2.4.0',
    'install_requires': install_requires,
    'classifiers': [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta"

    ],
    'package_dir': {'bitmapfont2otb': '.'},
    'packages': find_packages(),
    'scripts': ["bitmapfont2otb"],
    'zip_safe': False
}

if __name__ == '__main__':
    setup(**config)
