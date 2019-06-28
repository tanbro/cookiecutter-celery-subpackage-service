import re
import sys

print('INFO: pre-hook ...')

REGEX = re.compile(r'^[_a-zA-Z][_a-zA-Z0-9]+$')

subpackage = '{{ cookiecutter.subpackage }}'
namespace = '{{ cookiecutter.namespace }}'
package = '.'.join((namespace, subpackage))

if not re.match(REGEX, subpackage):
    print('ERROR: {} is not a valid Python sub-package name!'.format(subpackage), file=sys.stderr)
    sys.exit(1)

for s in package.split('.'):
    if not re.match(REGEX, s):
        print(
            'ERROR: {} is not a valid Python module name!'.format(s),
            file=sys.stderr
        )
        sys.exit(1)
