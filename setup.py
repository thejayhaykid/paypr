# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='babysitter',
    version='0.1.0',
    description='Simulate a babysitter working and getting paid for one night.',
    long_description=readme,
    author='Jake Hayes',
    author_email='jakejhayes@gmail.com',
    url='https://github.com/thejayhaykid/babysitter-kata',
    license=license,
    packages=find_packages(exclude='test'),
    entry_points = {
        'console_scripts': [
            'babysitter = babysitter.cli:main'
        ]
    },
    install_requires=['click']
)
