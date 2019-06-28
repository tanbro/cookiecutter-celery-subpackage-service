import os
import shutil
import sys
from urllib.request import urlopen
from urllib.error import HTTPError

PYTHON_GITIGNORE_URL = 'https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore'

print('INFO: run post-hook ...')

subpackage = '{{cookiecutter.subpackage}}'
namespace = '{{cookiecutter.namespace}}'
package = '.'.join((namespace, subpackage))

src_dir = os.path.join('src', package)
dst_namespace_dir = os.path.join('src', *namespace.split('.'))

print('INFO: mkdir {}'.format(dst_namespace_dir))
os.makedirs(dst_namespace_dir)

print('INFO: move {} to {}'.format(src_dir, dst_namespace_dir))
dst = shutil.move(src_dir, dst_namespace_dir)

new_dst = os.path.join(dst_namespace_dir, subpackage)

print('INFO: rename {} to {}'.format(dst, new_dst))
os.rename(dst, new_dst)

print('INFO: download Python gitignore')
with open('.gitignore', 'wb') as fp:
    try:
        res = urlopen(PYTHON_GITIGNORE_URL)
        for data in res.read():
            fp.write(data)
    except (OSError, HTTPError) as err:
        print('WARNING: download Python gitignore failed: %s', err)
