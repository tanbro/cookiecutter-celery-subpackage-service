import io
import os
import shutil
import sys
from functools import partial
from urllib.error import HTTPError
from urllib.request import urlopen

PYTHON_GITIGNORE_URL = 'https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore'

print('INFO: post-hook ...')

subpackage = '{{cookiecutter.subpackage}}'
namespace = '{{cookiecutter.namespace}}'
package = '.'.join((namespace, subpackage))

src_dir = os.path.join('src', package)
dst_namespace_dir = os.path.join('src', *namespace.split('.'))

print('INFO: mkdir {!r}'.format(dst_namespace_dir))
os.makedirs(dst_namespace_dir)

print('INFO: move {!r} to {!r}'.format(src_dir, dst_namespace_dir))
dst = shutil.move(src_dir, dst_namespace_dir)

new_dst = os.path.join(dst_namespace_dir, subpackage)

print('INFO: rename {!r} to {!r}'.format(dst, new_dst))
os.rename(dst, new_dst)

print('INFO: download Python gitignore')
with open('.gitignore', 'wb') as fp:
    try:
        response = urlopen(PYTHON_GITIGNORE_URL)
        for chunk in iter(partial(response.read, io.DEFAULT_BUFFER_SIZE), b''):
            fp.write(chunk)
    except (OSError, HTTPError) as err:
        print('WARNING: download Python gitignore failed: %s', err)
