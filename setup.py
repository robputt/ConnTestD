# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages
import os

base_name='ConnTestD'

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name=base_name,
    version='1.0',
    author=u'Robert Putt',
    author_email='robputt796@github',
    include_package_data = True,
    packages=find_packages(), # include all packages under this directory
    description='to update',
    long_description="",
    zip_safe=False,

    entry_points = {'console_scripts': [
        'command-name = conntestd.app:main',],},

    package_data={'/conntestd/templates':['*'],
                  '/conntestd/static/js':['*'],
                  '/conntestd/static/css':['*'],},

    # Adds dependencies
    install_requires = ['flask',
                        'sqlalchemy',
                        'speedtest-cli',
                        'Flask-APScheduler',
                        'pygal'
                        ]
)
