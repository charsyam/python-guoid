#!/usr/bin/env python

from setuptools import setup

setup(name='guoid',
      version='0.1',
      description='Python SnowFlake Clone - Global Unique Object ID',
      author='DaeMyung Kang',
      author_email='charsyam@gmail.com',
      url='https://github.com/charsyam/python-quoid',
      platforms='any',
      install_requires=['bottle'],
      packages=['guoid'],
      scripts=['guoid/guoid.py']
      )
