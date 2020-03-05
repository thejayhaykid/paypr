# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='paypr',
    version='0.1.0',
    description='Make a wallpaper from an undersized image.',
    long_description=readme,
    author='Jake Hayes',
    author_email='jakejhayes@gmail.com',
    url='https://github.com/thejayhaykid/paypr',
    license=license,
    packages=find_packages(exclude='test'),
    entry_points = {
        'console_scripts': [
            'paypr = paypr.cli:main'
        ]
    },
    install_requires=['click']
)
