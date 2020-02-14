# Copyright (c) v87.us Development Team.

import os
import sys
from distutils.core import setup
from setuptools import find_packages
import json

os.chdir(os.path.dirname(sys.argv[0]) or ".")
here = os.path.abspath(os.path.dirname(__file__))

ns = dict()
with open("{}/package.json".format(here)) as v:
    ns["__version__"] = json.loads(v.read())["version"]

setup_args = dict(
    name='qq_server',
    version=ns['__version__'],
    description='Some descriptions',
    author='chenhao',
    license='WTF',
    url='https://git.v87.us/chenhao/qq-server',
    packages=find_packages(),
    include_package_data=True,
)

if 'setuptools' in sys.modules:
    setup_args['zip_safe'] = False
    setup_args['install_requires'] = install_requires = []

    with open('requirements.txt') as f:
        for line in f.readlines():
            req = line.strip()
            if not req or req.startswith('#') or '://' in req:
                continue
            install_requires.append(req)


def main():
    setup(**setup_args)


if __name__ == '__main__':
    main()
