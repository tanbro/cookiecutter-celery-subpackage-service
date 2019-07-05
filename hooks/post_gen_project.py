#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import io
import os
import shutil
import sys
from functools import partial

PY3K = sys.version_info[0] > 2

if PY3K:
    from urllib.error import HTTPError
    from urllib.request import urlopen
else:
    from urllib2 import urlopen, HTTPError

print('INFO: post-hook ...')

PYTHON_GITIGNORE_URL = 'https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore'

subpackage = '{{cookiecutter.subpackage}}'
namespace = '{{cookiecutter.namespace}}'
readme_format = '{{cookiecutter.readme_format}}'
src_dir = {{cookiecutter.src_dir}}
tests_dir = {{cookiecutter.tests_dir}}
download_python_git_ignore = {{cookiecutter.download_python_git_ignore}}

package = '.'.join((namespace, subpackage))

if not tests_dir:
    print('INFO: rmtree "./tests"')
    shutil.rmtree('tests')

if readme_format == 'Markdown':
    os.rename('README', 'README.md')
elif readme_format == 'reStructuredText':
    os.rename('README', 'README.rst')

dst_namespace_dir = os.path.join(
    'src' if src_dir else '', *namespace.split('.')
)

print('INFO: mkdir {!r}'.format(dst_namespace_dir))
os.makedirs(dst_namespace_dir)

print('INFO: move {!r} to {!r}'.format(package, dst_namespace_dir))
dst = shutil.move(package, dst_namespace_dir)
if not PY3K:
    dst = os.path.join(dst_namespace_dir, package)

new_dst = os.path.join(dst_namespace_dir, subpackage)

print('INFO: rename {!r} to {!r}'.format(dst, new_dst))
os.rename(dst, new_dst)

if download_python_git_ignore:
    print('INFO: download Python gitignore')
    with open('.gitignore', 'wb') as fp:
        try:
            response = urlopen(PYTHON_GITIGNORE_URL)
            for chunk in iter(partial(response.read, io.DEFAULT_BUFFER_SIZE), b''):
                fp.write(chunk)
        except (OSError, HTTPError) as err:
            print('WARNING: download Python gitignore failed: %s', err)

print('INFO: post-hook complete.')
