#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import io
import os

from setuptools import find_packages, setup


NAME = 'dcat'
DESCRIPTION = 'Simple dockerization of catkin workspaces'
EMAIL = 'emircem.gezer@gmail.com'
AUTHOR = 'Emir Cem Gezer'
VERSION = None

here = os.path.abspath( os.path.dirname(__file__))


with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

with open('LICENSE') as f:
    license = f.read()


about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)

else:
    about['__version__'] = VERSION

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    packages=find_packages(exclude=('tests',)),
    license=license
)
