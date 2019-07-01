#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import setuptools
from distutils.version import StrictVersion
from setuptools import setup


def check_setuptools_version():
    actual_ver = StrictVersion(setuptools.__version__)
    requires_min_ver = StrictVersion('40.1.0')

    if actual_ver < requires_min_ver:
        msg = \
            'Expected version of setuptools is greater than or equals to {0}, but actural is {1}.'.format(requires_min_ver, actual_ver) + os.linesep + \
            'Upgrade setuptools by: ' + os.linesep + \
            '\tpip install -U setuptools'
        print(msg, file=sys.stderr)
        sys.exit(1)


check_setuptools_version()

setup()
