#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_namespace_packages, setup


INSTALL_REQUIRES = ['Celery<5.0,>=4.3']
SETUP_REQUIRES = []
TEST_REQUIRES = []


setup(
    name='{{cookiecutter.project_slug}}',

    package_dir={'': 'src'},
    namespace_packages=[{%- for item in cookiecutter.namespace.split('.') -%} "{{item}}" {%- if not loop.last -%}, {% endif %} {% endfor %}],
    packages=find_namespace_packages('src'),

    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.author_email}}',
    description='{{cookiecutter.description}}',
    long_description=open('README.md', encoding='utf8').read(),
    long_description_content_type='text/markdown',

    install_requires=INSTALL_REQUIRES
    setup_requires=SETUP_REQUIRES
    test_requires=TEST_REQUIRES
)
