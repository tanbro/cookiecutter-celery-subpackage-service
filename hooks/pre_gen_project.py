#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import re
import sys

print('INFO: pre-hook ...')

REGEX = re.compile(r'^[_a-zA-Z][_a-zA-Z0-9]*$')

subpackage = '{{cookiecutter.subpackage}}'
namespace = '{{cookiecutter.namespace}}'
package = '.'.join((namespace, subpackage))

for s in package.split('.'):
    if not re.match(REGEX, s):
        print(
            'ERROR: {!r} is not a valid Python module name!'.format(s),
            file=sys.stderr
        )
        sys.exit(1)

print('INFO: pre-hook complete.')
