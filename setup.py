#!/usr/bin/env python
from setuptools import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

packages = [
    'pymultipart'
]

requires = []

setup(
    name='pymultipart',
    version='0.1',
    description='HTTP Multipart Body Parser',
    long_description=readme,
    author='Adam Venturella',
    author_email='aventurella@gmail.com',
    url='http://github.com/aventurella/pymultipart',
    license=license,
    packages=packages,
    package_data={'': ['LICENSE']},
    include_package_data=True,
    install_requires=requires,
    package_dir={'pymultipart': 'pymultipart'},
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Internet :: WWW/HTTP'
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
    ),

)
